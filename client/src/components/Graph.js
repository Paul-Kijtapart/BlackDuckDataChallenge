import React from 'react';
import GraphView from 'react-digraph'
import GraphConfig from './graph-config.js';
const styles = {
  graph: {
    height: '100%',
    width: '100%'
  }
};

const NODE_KEY = "id" // Key used to identify nodes

// These keys are arbitrary (but must match the config)
// However, GraphView renders text differently for empty types
// so this has to be passed in if that behavior is desired.
const EMPTY_TYPE = "empty"; // Empty node type
const SPECIAL_TYPE = "special";
const SPECIAL_CHILD_SUBTYPE = "specialChild";
const EMPTY_EDGE_TYPE = "LicenseEdgeType"; // emptyEdge
const SPECIAL_EDGE_TYPE = "VersionEdgeType"; // specialEdge

// NOTE: Edges must have 'source' & 'target' attributes
// In a more realistic use case, the graph would probably originate 
// elsewhere in the App or be generated from some other state upstream of this component.
// import sample from "sample.json";
const sample = {
  "nodes": [{
    "id": 1,
    "title": "Node A",
    "x": 0.0,
    "y": 0.0,
    "type": SPECIAL_TYPE
  }, {
    "id": 2,
    "title": "Node B",
    "x": 0.0,
    "y": 0.0,
    "type": EMPTY_TYPE,
    "subtype": SPECIAL_CHILD_SUBTYPE
  }, {
    "id": 3,
    "title": "Node C",
    "x": 0.0,
    "y": 0.0,
    "type": EMPTY_TYPE
  }, {
    "id": 4,
    "title": "Node C",
    "x": 0.0,
    "y": 0.0,
    "type": EMPTY_TYPE
  }],
  "edges": [{
    "source": 1,
    "target": 2,
    "type": SPECIAL_EDGE_TYPE
  }, {
    "source": 2,
    "target": 4,
    "type": EMPTY_EDGE_TYPE
  }]
}

import {
  ProjectNode,
  VersionNode,
  LicenseNode
} from "./GraphNode.js";

var getMapValueList = function(map) {
  let mapIterator = map.values();
  let res = [];
  while (true) {
    let current = mapIterator.next();
    if (current.done) {
      break;
    }
    res.push(current.value);
  }
  return res;
};

var getEdgeList = function(special_node_list) {
  var res = [];
  for (let node of special_node_list) {
    res = res.concat(node.get_edges_list());
  }
  return res;
};

var buildGraph = function(projects_querySet) {
  var projectNodes = [];
  var versionMap = new Map(); // {version_name : [p1, ... , pn]}
  var licenseMap = new Map();

  for (let project of projects_querySet) {
    let project_id = project.pk;
    let version_name = project.fields.version;
    let dns_list = project.fields.dns;
    let dws_list = project.fields.dws;
    let so_list = project.fields.so;
    let license_list = project.fields.license;

    var newProjectNode = new ProjectNode(
      project_id,
      dns_list, dws_list, so_list,
      version_name, license_list);

    // Sync newProject with Version
    let current_version_node = versionMap.get(version_name);
    if (current_version_node) {
      current_version_node.add_project(newProjectNode);
    } else {
      let vn = new VersionNode(version_name);
      vn.add_project(newProjectNode);
      versionMap.set(version_name, vn);
    }

    // Sync newProject with License 
    for (let id of license_list) {
      let current_license_node = licenseMap.get(id);
      if (current_license_node) {
        current_license_node.add_project(newProjectNode);
      } else {
        let ln = new LicenseNode(id);
        ln.add_project(newProjectNode);
        licenseMap.set(id, ln);
      }
    }
    projectNodes.push(newProjectNode);
  }

  let version_node_list = getMapValueList(versionMap);
  let version_edge_list = getEdgeList(version_node_list);

  let license_node_list = getMapValueList(licenseMap);
  let license_edge_list = getEdgeList(license_node_list);

  let edges = version_edge_list.concat(license_edge_list);
  let nodes = projectNodes.concat(version_node_list, license_node_list);
  let res = new GraphData(nodes, edges);
  res.log();
  return res;
};

var GraphData = function(
  nodes,
  edges) {

  this.nodes = nodes;
  this.edges = edges;
};

GraphData.prototype.log = function() {
  console.log("Edges: ");
  console.log(this.edges);
  console.log("Nodes: ");
  console.log(this.nodes);
};

class Graph extends React.Component {

  constructor(props) {
    super(props);

    let projects = this.props.projects;

    this.state = {
      graph: buildGraph(projects),
      selected: {}
    }

    this.getViewNode = this.getViewNode.bind(this);
    this.onSelectNode = this.onSelectNode.bind(this);
    this.onCreateNode = this.onCreateNode.bind(this);
    this.onUpdateNode = this.onUpdateNode.bind(this);
    this.onDeleteNode = this.onDeleteNode.bind(this);
    this.onSelectEdge = this.onSelectEdge.bind(this);
    this.onCreateEdge = this.onCreateEdge.bind(this);
    this.onSwapEdge = this.onSwapEdge.bind(this);
    this.onDeleteEdge = this.onDeleteEdge.bind(this);
  }

  // Helper to find the index of a given node
  getNodeIndex(searchNode) {
    return this.state.graph.nodes.findIndex((node) => {
      return node[NODE_KEY] === searchNode[NODE_KEY]
    })
  }

  // Helper to find the index of a given edge
  getEdgeIndex(searchEdge) {
    return this.state.graph.edges.findIndex((edge) => {
      return edge.source === searchEdge.source &&
        edge.target === searchEdge.target
    })
  }

  // Given a nodeKey, return the corresponding node
  getViewNode(nodeKey) {
    const searchNode = {};
    searchNode[NODE_KEY] = nodeKey;
    const i = this.getNodeIndex(searchNode);
    return this.state.graph.nodes[i]
  }

  /*
   * Handlers/Interaction
   */

  // Called by 'drag' handler, etc.. 
  // to sync updates from D3 with the graph
  onUpdateNode(viewNode) {
    const graph = this.state.graph;
    const i = this.getNodeIndex(viewNode);

    graph.nodes[i] = viewNode;
    this.setState({
      graph: graph
    });
  }

  // Node 'mouseUp' handler
  onSelectNode(viewNode) {
    // Deselect events will send Null viewNode
    if (!!viewNode) {
      this.setState({
        selected: viewNode
      });
    } else {
      this.setState({
        selected: {}
      });
    }
  }

  // Edge 'mouseUp' handler
  onSelectEdge(viewEdge) {
    this.setState({
      selected: viewEdge
    });
  }

  // Updates the graph with a new node
  onCreateNode(x, y) {
    const graph = this.state.graph;

    // This is just an example - any sort of logic 
    // could be used here to determine node type
    // There is also support for subtypes. (see 'sample' above)
    // The subtype geometry will underlay the 'type' geometry for a node
    const type = Math.random() < 0.25 ? SPECIAL_TYPE : EMPTY_TYPE;

    const viewNode = {
      id: this.state.graph.nodes.length + 1,
      title: '',
      type: type,
      x: x,
      y: y
    }

    graph.nodes.push(viewNode);
    this.setState({
      graph: graph
    });
  }

  // Deletes a node from the graph
  onDeleteNode(viewNode) {
    const graph = this.state.graph;
    const i = this.getNodeIndex(viewNode);
    graph.nodes.splice(i, 1);

    // Delete any connected edges
    const newEdges = graph.edges.filter((edge, i) => {
      return edge.source != viewNode[NODE_KEY] &&
        edge.target != viewNode[NODE_KEY]
    })

    graph.edges = newEdges;

    this.setState({
      graph: graph,
      selected: {}
    });
  }

  // Creates a new node between two edges
  onCreateEdge(sourceViewNode, targetViewNode) {
    const graph = this.state.graph;

    // This is just an example - any sort of logic 
    // could be used here to determine edge type
    const type = sourceViewNode.type === SPECIAL_TYPE ? SPECIAL_EDGE_TYPE : EMPTY_EDGE_TYPE;

    const viewEdge = {
      source: sourceViewNode[NODE_KEY],
      target: targetViewNode[NODE_KEY],
      type: type
    }
    graph.edges.push(viewEdge);
    this.setState({
      graph: graph
    });
  }

  // Called when an edge is reattached to a different target.
  onSwapEdge(sourceViewNode, targetViewNode, viewEdge) {
    const graph = this.state.graph;
    const i = this.getEdgeIndex(viewEdge);
    const edge = JSON.parse(JSON.stringify(graph.edges[i]));

    edge.source = sourceViewNode[NODE_KEY];
    edge.target = targetViewNode[NODE_KEY];
    graph.edges[i] = edge;

    this.setState({
      graph: graph
    });
  }

  // Called when an edge is deleted
  onDeleteEdge(viewEdge) {
    const graph = this.state.graph;
    const i = this.getEdgeIndex(viewEdge);
    graph.edges.splice(i, 1);
    this.setState({
      graph: graph,
      selected: {}
    });
  }

  /*
   * Render
   */

  render() {
    const nodes = this.state.graph.nodes;
    const edges = this.state.graph.edges;
    const selected = this.state.selected;

    const NodeTypes = GraphConfig.NodeTypes;
    const NodeSubtypes = GraphConfig.NodeSubtypes;
    const EdgeTypes = GraphConfig.EdgeTypes;

    return (
      <div id='graph' style={styles.graph}>
      
        <GraphView  ref='GraphView'
                    nodeKey={NODE_KEY}
                    emptyType={EMPTY_TYPE}
                    nodes={nodes}
                    edges={edges}
                    selected={selected}
                    nodeTypes={NodeTypes}
                    nodeSubtypes={NodeSubtypes}
                    edgeTypes={EdgeTypes}
                    getViewNode={this.getViewNode}
                    onSelectNode={this.onSelectNode}
                    onCreateNode={this.onCreateNode}
                    onUpdateNode={this.onUpdateNode}
                    onDeleteNode={this.onDeleteNode}
                    onSelectEdge={this.onSelectEdge}
                    onCreateEdge={this.onCreateEdge}
                    onSwapEdge={this.onSwapEdge}
                    onDeleteEdge={this.onDeleteEdge}/>
      </div>
    );
  }

}


export default Graph;