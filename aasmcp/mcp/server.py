import logging
import sys

from aasmcp.tool import BaseTool, tool_list

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stderr)])
import argparse
from mcp.server.fastmcp import FastMCP



def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="OpenManus MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="stdio",
        help="Communication method: stdio or http (default: stdio)",
    )
    return parser.parse_args()

# Initialize the server instance as soon as possible to allow the usage of the MCP Inspector (debugger)
app = FastMCP("AAS MCP Bridge")
for tool in tool_list:
    if type(tool["type"]) == BaseTool:
        app._mcp_server.tools[tool["name"]] = tool["func"]
    else:
        app.tool()(tool["func"])

if __name__ == "__main__":
    args = parse_args()
    app.run(transport="sse")
