#!/usr/bin/env python3
"""Generate graphml GraphML views from a single-table CSV (nodes + edges).

The CSV must have these columns:
    kind,node_id,label,type,role,order,views,source,target,edge_label

Where:
    - kind=node rows define nodes using node_id,label,type,role,order,views
    - kind=edge rows define edges using source,target,edge_label,views
    - views is "all" or comma-separated list among:
            applicant,panel,host,secretariat,reviewers

Usage:
    python generate_graphml_views.py CVUT_StG_2026_process_source.csv

Outputs:
    *_applicant.graphml
    *_panel.graphml
    *_host.graphml
    *_secretariat.graphml
"""

import csv
import os
import sys
from typing import Dict, List, Set, Tuple


# Node type styling configuration
NODE_STYLES = {
        "decision": {"w": 120, "h": 70, "shape": "diamond", "fill": "#FFF7E6", "border": "#B26A00"},
        "milestone": {"w": 220, "h": 55, "shape": "roundrectangle", "fill": "#FCE8E6", "border": "#C5221F"},
        "task": {"w": 240, "h": 75, "shape": "roundrectangle", "fill": "#E8F0FE", "border": "#1A73E8"},
}
VIEWS = ("applicant", "panel", "host", "secretariat")


def escape_xml(s: str) -> str:
        """Escape XML special characters."""
        return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def parse_views(views_str: str) -> Set[str]:
        """Parse comma-separated views string into a set."""
        views_str = (views_str or "").strip().lower()
        return {v.strip() for v in views_str.split(",") if v.strip()} if views_str else set()


def compute_layout(nodes: List[Dict]) -> Tuple[Dict[str, int], Dict[str, int]]:
        """Compute x,y coordinates based on order and role."""
        roles = []
        for n in nodes:
                r = n.get("role", "")
                if r not in roles:
                        roles.append(r)
        
        role_y = {r: 60 + i * 150 for i, r in enumerate(roles)}
        nodes_sorted = sorted(nodes, key=lambda d: d.get("order", 0))
        x_map = {n["id"]: 60 + idx * 240 for idx, n in enumerate(nodes_sorted)}
        return x_map, role_y


def generate_node_xml(node: Dict, x_map: Dict, role_y: Dict) -> str:
        """Generate XML for a single node."""
        nid = node["id"]
        label = escape_xml(node.get("label", ""))
        role = node.get("role", "")
        ntype = node.get("type", "task")
        
        style = NODE_STYLES.get(ntype, NODE_STYLES["task"])
        x = x_map[nid]
        y = role_y.get(role, 60)
        
        return f"""    <node id=\"{escape_xml(nid)}\">
            <data key=\"d0\">
                <y:ShapeNode>
                    <y:Geometry x=\"{x}\" y=\"{y}\" width=\"{style['w']}\" height=\"{style['h']}\"/>
                    <y:Fill color=\"{style['fill']}\" transparent=\"false\"/>
                    <y:BorderStyle color=\"{style['border']}\" type=\"line\" width=\"1.0\"/>
                    <y:NodeLabel alignment=\"center\" autoSizePolicy=\"content\" fontFamily=\"Dialog\" fontSize=\"12\" textColor=\"#000000\" visible=\"true\">{label}</y:NodeLabel>
                    <y:Shape type=\"{style['shape']}\"/>
                </y:ShapeNode>
            </data>
        </node>"""


def generate_edge_xml(edge_id: int, source: str, target: str, label: str = "", dashed: bool = False) -> str:
        """Generate XML for a single edge."""
        label_xml = f'<y:EdgeLabel alignment="center" fontFamily="Dialog" fontSize="11" textColor="#000000" visible="true">{escape_xml(label)}</y:EdgeLabel>' if label else ""
        line_type = "dashed" if dashed else "line"
        
        return f"""    <edge id=\"e{edge_id}\" source=\"{escape_xml(source)}\" target=\"{escape_xml(target)}\">
            <data key=\"d1\">
                <y:PolyLineEdge>
                    <y:LineStyle color=\"#000000\" type=\"{line_type}\" width=\"1.0\"/>
                    <y:Arrows source=\"none\" target=\"standard\"/>
                    {label_xml}
                </y:PolyLineEdge>
            </data>
        </edge>"""


def generate_graphml(nodes: List[Dict], edges: List[Dict], title: str = "Process") -> str:
        """Generate complete GraphML document."""
        x_map, role_y = compute_layout(nodes)
        nodes_sorted = sorted(nodes, key=lambda d: d.get("order", 0))
        
        nodes_block = "\n".join(generate_node_xml(n, x_map, role_y) for n in nodes_sorted)
        edges_block = "\n".join(
                generate_edge_xml(i + 1, e["source"], e["target"], e.get("label", ""), dashed=(e.get("style") == "dashed"))
                for i, e in enumerate(edges)
        )
        
        return f"""<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>
<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\"
        xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"
        xmlns:y=\"http://www.yworks.com/xml/graphml\"
        xmlns:graphml=\"http://www.yworks.com/xml/graphml/3\"
        xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns
         http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd\">

    <key id=\"d0\" for=\"node\" yfiles.type=\"nodegraphics\"/>
    <key id=\"d1\" for=\"edge\" yfiles.type=\"edgegraphics\"/>
    <key id=\"d2\" for=\"graph\" attr.name=\"label\" attr.type=\"string\"/>

    <graph id=\"G\" edgedefault=\"directed\">
        <data key=\"d2\">{escape_xml(title)}</data>

{nodes_block}

{edges_block}

    </graph>
</graphml>"""


def load_source_table(path: str) -> Tuple[Dict, List]:
        """Load nodes and edges from CSV file."""
        nodes = {}
        edges = []
        
        with open(path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                        if row["kind"] == "node":
                                nodes[row["node_id"]] = {
                                        "id": row["node_id"],
                                        "label": row["label"],
                                        "type": row["type"],
                                        "role": row["role"],
                                        "order": int(row["order"]),
                                        "views": parse_views(row["views"]) or {"all"},
                                }
                        elif row["kind"] == "edge":
                                edges.append({
                                        "source": row["source"],
                                        "target": row["target"],
                                        "label": row.get("edge_label", ""),
                                        "views": parse_views(row["views"]) or {"all"},
                                })
        
        return nodes, edges


def build_view(nodes_dict: Dict, edges_list: List, view: str) -> Tuple[List, List]:
        """Filter nodes and edges for a specific view."""
        view = view.lower().strip()
        allowed_nodes = {nid for nid, n in nodes_dict.items() if "all" in n["views"] or view in n["views"]}
        
        allowed_edges = []
        for e in edges_list:
                if not ("all" in e["views"] or view in e["views"]):
                        continue
                if e["source"] in allowed_nodes and e["target"] in allowed_nodes:
                        is_parallel = e.get("label", "").strip().lower() == "parallel"
                        allowed_edges.append({
                                "source": e["source"],
                                "target": e["target"],
                                "label": e.get("label", ""),
                                "style": "dashed" if is_parallel else "solid",
                        })
        
        nodes = [nodes_dict[nid] for nid in allowed_nodes]
        nodes.sort(key=lambda d: d["order"])
        return nodes, allowed_edges


def main():
        if len(sys.argv) < 2:
                print("Usage: python generate_graphml_views.py <source.csv>")
                sys.exit(2)
        
        src = sys.argv[1]
        nodes_dict, edges_list = load_source_table(src)
        stem = os.path.splitext(os.path.basename(src))[0]
        
        for view in VIEWS:
                nodes, edges = build_view(nodes_dict, edges_list, view)
                out = f"{stem}_{view}.graphml"
                with open(out, "w", encoding="utf-8") as f:
                        f.write(generate_graphml(nodes, edges, title=f"{stem} – {view} view"))
                print(f"Wrote {out}")


if __name__ == "__main__":
        main()
