# Using Asset Administration Shell as a MCP Server for LLM-Agent

The AAS MCP Server currently provides two tools for interacting with Asset Administration Shell (AAS) data.  
aas_explore gives an overview on existing AAS instances and their submodels on a given AAS server endpoint.  
aas_parser extracts all the submodel elements and their path from a given AAS id hosted on the AAS server endpoint and saves them in a dataframe csv for the further usage.

### 1. `aas_explore(endpoint)`

Fetches metadata about all available AAS instances from a specified AAS server.

- **Parameter:**
  - `endpoint` (*string*): The URL of the target AAS server.

---

### 2. `aas_parser(endpoint, id)`

Downloads the full AAS package in AASX format for a given AAS instance and extracts its property paths into a structured table.

- **Parameters:**
  - `endpoint` (*string*): The URL of the AAS server.
  - `id` (*string*): The unique identifier of the AAS instance.

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
## Our Work on AAS + LLM Integration

We explore how to conceptualize, develop, and deploy AAS Submodels with the support of Large Language Models (LLMs), particularly for enabling semantic search and interoperability in manufacturing systems.

### 1. Conceptualizing and Deploying AAS Submodels with LLM Support

This work demonstrates how to leverage LLMs for semantic search to support the creation and deployment of AAS Submodels, with a focus on quality control and zero-defect manufacturing.

**Citation:**

Dachuan Shi, Philipp Liedl, Thomas Bauernhansl  
*Interoperable information modelling leveraging Asset Administration Shell and Large Language Model for quality control toward zero defect manufacturing*  
**Journal of Manufacturing Systems**, Volume 77, 2024, Pages 678–696  
[https://doi.org/10.1016/j.jmsy.2024.10.011](https://doi.org/10.1016/j.jmsy.2024.10.011)

---

### 2. Mapping Data into AAS Entities (Semantic/Entity Matching)

This study presents a dual mapping approach using fine-tuned LLMs to align unstructured or semi-structured data with AAS entities, enabling interoperable knowledge representation.

**Citation:**

Dachuan Shi, Olga Meyer, Michael Oberle, Thomas Bauernhansl  
*Dual data mapping with fine-tuned large language models and Asset Administration Shells toward interoperable knowledge representation*  
**Robotics and Computer-Integrated Manufacturing**, Volume 91, 2025, Article 102837  
[https://doi.org/10.1016/j.rcim.2024.102837](https://doi.org/10.1016/j.rcim.2024.102837)

