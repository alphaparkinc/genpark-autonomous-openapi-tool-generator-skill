"""
MCP Server for Autonomous OpenAPI Tool Generator Skill
"""

import json
import sys
from client import OpenAPIToolGenerator

gen = OpenAPIToolGenerator()

def handle_call(name: str, args: dict) -> dict:
    if name == "import_spec":
        spec = args.get("spec", {})
        c = gen.parse_spec(spec)
        return {"tools_loaded": c, "tool_names": list(gen.tools.keys())}
    elif name == "invoke_tool":
        tname = args.get("tool_name", "")
        params = args.get("params", {})
        return gen.execute_tool_call(tname, **params)
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
