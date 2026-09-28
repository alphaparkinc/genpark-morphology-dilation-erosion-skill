import sys
import json
from client import MorphologyDilationErosionEngine

def handle_rpc(line):
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-morphology-dilation-erosion-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "apply_morphology",
                    "description": "Apply mathematical morphology operations (dilate, erode, open, close) to a binary image matrix",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "image": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}},
                            "operation": {"type": "string", "enum": ["dilate", "erode", "open", "close"], "default": "dilate"}
                        },
                        "required": ["image"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "apply_morphology":
            morph = MorphologyDilationErosionEngine()
            img = args.get("image", [])
            op = args.get("operation", "dilate")
            if op == "dilate":
                res_img = morph.dilate(img)
            elif op == "erode":
                res_img = morph.erode(img)
            elif op == "open":
                res_img = morph.opening(img)
            else:
                res_img = morph.closing(img)
            res = {"content": [{"type": "text", "text": json.dumps({"output": res_img, "active_pixels": sum(row.count(255) for row in res_img)})}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
