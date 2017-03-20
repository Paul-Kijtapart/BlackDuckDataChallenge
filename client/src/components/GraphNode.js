import {
  Edge
} from "./Edge.js";

var Node = function(
  id,
  title,
  x, y,
  type) {

  this.id = id;
  this.title = title;
  this.x = x;
  this.y = y;
  this.type = type;
};

Node.prototype.toString = function() {
  return "id : " + this.id; + "\n";
};

var xcounter = 0,
  ycounter = 0,
  idcounter = 1;

var ProjectNode = function(id,
  dns_list, dws_list, so_list,
  version, license_id_list) {

  Node.call(this, id, id, xcounter += 100, ycounter += 100, "empty");
  this.id = id;
  this.dns_list = dns_list;
  this.dws_list = dws_list;
  this.so_list = so_list;
  this.version = version;
  this.license_id_list = license_id_list;
};

ProjectNode.prototype = new Node();
ProjectNode.prototype.constructor = ProjectNode;

ProjectNode.prototype.toString = function() {
  var res = "id : " + this.id + "\n";
  res += "version : " + this.version + "\n";
  return res;
};

var VersionNode = function(
  id) {

  Node.call(this, id, id, xcounter += 100, ycounter += 100, "empty");

  this.id = id;
  this.edgeType = "VersionEdgeType";
  this.project_map = new Map();
  this.type = "empty";
};

VersionNode.prototype = new Node();
VersionNode.prototype.constructor = VersionNode;

VersionNode.prototype.add_project = function(project) {
  if (!this.project_map.get(project.id)) {
    this.project_map.set(project.id, project);
  }
};

VersionNode.prototype.get_edges_list = function() {
  var res = [];
  var mapIter = this.project_map.keys();
  while (true) {
    let current = mapIter.next();
    if (current.done) {
      break;
    }
    let project_id = current.value;

    var newEdge = new Edge(
      this.id,
      project_id,
      this.edgeType
    );

    res.push(newEdge);
  }
  return res;
};

var LicenseNode = function(
  id) {

  Node.call(this, id, id.toString(), xcounter += 100, ycounter += 100, "empty");
  this.id = id;
  this.edgeType = "LicenseEdgeType";
  this.project_map = new Map();
  this.type = "empty";
};

LicenseNode.prototype = new Node();
LicenseNode.prototype.constructor = LicenseNode;

LicenseNode.prototype.add_project = function(project) {
  if (!this.project_map.get(project.id)) { // TODO: refactor this
    this.project_map.set(project.id, project);
  }
};

LicenseNode.prototype.get_edges_list = function() {
  var res = [];
  var mapIter = this.project_map.keys();
  while (true) {
    let current = mapIter.next();
    if (current.done) {
      break;
    }
    let project_id = current.value;

    var newEdge = new Edge(
      this.id,
      project_id,
      this.edgeType
    );

    res.push(newEdge);
  }
  return res;
};

export {
  ProjectNode,
  VersionNode,
  LicenseNode
};