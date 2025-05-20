import base64
import json

from aasmcp.aas_utils.basyx_client import BasyxApiClient
from aasmcp.tool.base import BaseTool, ToolResult


class AASExplore(BaseTool):
    name: str = "aas_explore"
    description: str = (
        "Given an endpoint of an AAS server, fetch the metainformation of AAS instances "
        "and their submodels hosted on the AAS server."
    )
    parameters: dict = {
        "type": "object",
        "properties": {
            "endpoint": {
                "type": "string",
                "description": "The base URL of the AAS server, e.g., http://localhost:8081",
            }
        },
        "required": ["endpoint"],
    }

    async def execute(self, endpoint: str, **kwargs) -> ToolResult:
        try:
            client = BasyxApiClient(endpoint)
            shells = await client.get_shells()

            if not isinstance(shells, list):
                return ToolResult(error="Shells response is not a list.")

            results = []
            for shell in shells:
                aas_id = shell.get("id")
                id_short = shell.get("idShort")
                if not aas_id:
                    continue

                b64_id = base64.urlsafe_b64encode(aas_id.encode()).decode()

                # Get submodel references (returns list of ModelReference)
                submodel_refs = await client.get(f"/shells/{b64_id}/submodel-refs")
                submodel_refs = submodel_refs.get('result', [])
                submodel_infos = []
                for ref in submodel_refs:
                    try:
                        submodel_id = ref["keys"][0]["value"]  # Full URL
                        submodel_name = submodel_id.strip("/").split("/")[-1]  # "TechnicalData"
                        b64_submodel_id = base64.urlsafe_b64encode(submodel_id.encode()).decode()
                        submodel_infos.append(
                            {
                                "name": submodel_name,
                                "id": submodel_id,
                                # "base64_id": b64_submodel_id,
                            }
                        )
                    except Exception as e:
                        continue

                results.append(
                    {
                        "aas_id": aas_id,
                        "aas_idShort": id_short,
                        # "aas_base64_id": b64_id,
                        "submodels": submodel_infos,
                    }
                )

            return ToolResult(output=json.dumps(results, indent=2))

        except Exception as e:
            return ToolResult(error=f"AASExplore failed: {str(e)}")
