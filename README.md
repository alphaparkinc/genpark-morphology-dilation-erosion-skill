# genpark-morphology-dilation-erosion-skill

> Binary and grayscale mathematical morphology operators: dilation, erosion, opening, and closing.

Part of the **GenPark AI Agent Skills Matrix**. Production-ready, zero external dependencies, native Python 3.9+ standard library.

## Architecture

```mermaid
flowchart TD
    A[Image Input Matrix] --> B[Spatial Processing Kernel]
    B --> C[Feature & Geometry Extraction]
    C --> D[Structured Output / Segments]
    D --> E[MCP Protocol Endpoint]
```

## Features
- **Zero Third-Party Dependencies**: Pure Python standard library (`math`, `collections`).
- **Precision Computer Vision**: Optimized spatial convolution and disjoint-set Union-Find.
- **Native MCP Protocol Support**: Integrated JSON-RPC 2.0 stdio server ready for Claude Desktop, Cursor, and Windsurf.

## Installation

```bash
pip install genpark-morphology-dilation-erosion-skill
```

Or clone directly:

```bash
git clone https://github.com/alphaparkinc/genpark-morphology-dilation-erosion-skill.git
cd genpark-morphology-dilation-erosion-skill
python example_usage.py
```

## Quick Start

```python
from client import *
# Refer to example_usage.py for end-to-end execution
```

## Model Context Protocol (MCP) Setup

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-morphology-dilation-erosion-skill": {
      "command": "python",
      "args": ["-m", "genpark-morphology-dilation-erosion-skill.mcp_server"]
    }
  }
}
```

## License
MIT License. Copyright (c) 2026 AlphaPark Inc. & Alpha-Park.
