import React from "react";

// Components
import Version from "./Version.js";
import Graph from './Graph.js';

// Mock data
import projects_json_str from "projects.json";


class App extends React.Component {
	render() {
		const projects = JSON.parse(projects_json_str);
		return (
			<div>
				<Graph projects={projects}/>
			</div>
		);
	}
};

export default App;