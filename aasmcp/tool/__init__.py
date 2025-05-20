from aasmcp.tool.base import BaseTool
from aasmcp.tool.aas_parser import AASParser
from aasmcp.tool.aas_explore import AASExplore


__all__ = [
    "BaseTool",
    "AASParser",
    "AASExplore"
]

tool_list = [
    {"name": AASExplore().name, "func": AASExplore, "type": BaseTool},
    {"name": AASParser().name, "func": AASParser, "type": BaseTool},
]