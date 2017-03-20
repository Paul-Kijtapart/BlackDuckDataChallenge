import React from 'react';

const EmptyShape = (
	<symbol viewBox="0 0 100 100" id="empty" key="0">
    <circle cx="50" cy="50" r="45"></circle>
  </symbol>
)

const SpecialShape = (
	<symbol viewBox="0 0 100 100" id="special" key="1">
    <rect transform="translate(50) rotate(45)" width="70" height="70"></rect>
  </symbol>
)

const SpecialChildShape = (
	<symbol viewBox="0 0 100 100" id="specialChild" key="0">
    <rect x="2.5" y="0" width="95" height="97.5" fill="rgba(30, 144, 255, 0.12)"></rect>
  </symbol>
)

const LicenseEdgeTypeShape = (
	<symbol viewBox="0 0 50 50" id="LicenseEdgeType" key="0">
    <circle cx="25" cy="25" r="8" fill="currentColor"> </circle>
  </symbol>
)

const VersionEdgeTypeShape = (
	<symbol viewBox="0 0 50 50" id="VersionEdgeType" key="1">
    <rect transform="rotate(45)"  x="25" y="-4.5" width="15" height="15" fill="currentColor"></rect>
  </symbol>
)

export default {
	NodeTypes: {
		empty: {
			typeText: "None",
			shapeId: "#empty",
			shape: EmptyShape
		},
		special: {
			typeText: "Special",
			shapeId: "#special",
			shape: SpecialShape
		}
	},
	NodeSubtypes: {
		specialChild: {
			shapeId: "#specialChild",
			shape: SpecialChildShape
		}
	},
	EdgeTypes: {
		LicenseEdgeType: {
			shapeId: "#LicenseEdgeType",
			shape: LicenseEdgeTypeShape
		},
		VersionEdgeType: {
			shapeId: "#VersionEdgeType",
			shape: VersionEdgeTypeShape
		}
	}
}