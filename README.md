# mcp_aas



## Install

```
uv venv --python 3.12
```
In a windows cmd 
``` 
.venv\Scripts\activate 
uv pip install -r requirements.txt
```

## run and inspect MCP server with AAS tools

using stodio or sse connection  
```
python run_mcp_server.py --transport stdio
```
If If using 'stdio', can directly start inspector by
```
npx @modelcontextprotocol/inspector python run_mcp_server.py --transport stdio
```
If using 'sse' transport mode, should start the MCP server at first. Then start MCP Inspector. The default MCP endport is at "http://localhost:8000/sse"
```
npx @modelcontextprotocol/inspector python run_mcp_server.py --transport sse
```
## AAS tools
Currently, two AAS tools are implemented.  
aas_explore gives an overview on existing AAS instances and their submodels on a given AAS server endpoint.  
aas_parser extracts all the submodel elements and their path from a given AAS id hosted on the AAS server endpoint and saves them in a dataframe csv for the further usage.