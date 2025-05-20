from aasmcp.tool.base import BaseTool, ToolResult
from aasmcp.aas_utils import aas_loader
import pandas as pd


class AASParser(BaseTool):
    name: str = "aas_parser"
    description: str = (
        "To parse AAS properties for more detailed information. "
        "Given the AAS id and server endpoint, this tool fetches the full AAS as AASX and extracts property paths into a structured table."
    )
    parameters: dict = {
        "type": "object",
        "properties": {
            "endpoint": {
                "type": "string",
                "description": "The base URL of the AAS server, e.g., http://localhost:8081",
            },
            "id": {
                "type": "string",
                "description": "The id of the AAS, such as https://dpp40.harting.com/shells/08968020001A0",
            },
        },
        "required": ["endpoint", "id"],
    }

    async def execute(self, endpoint: str, id: str, **kwargs) -> ToolResult:
        try:
            aasx_filepath = await aas_loader.get_aasx(endpoint=endpoint, aas_id=id, base_dir="temp")
            if not aasx_filepath:
                return ToolResult(error=f"AAS not found for ID: {id}")

            df_aas = aas_loader.aasx_parser(aasx_filepath)

            # Extract only needed columns and preview
            df_selected = df_aas[["idShort", "type", "semantic_path"]]
            core_types = ["AssetAdministrationShell", "Submodel", "SubmodelElementCollection"]
            core_rows = df_selected[df_selected["type"].isin(core_types)]

            # Optionally add a few more rows for diversity
            supplemental_rows = df_selected[~df_selected["type"].isin(core_types)].head(5)

            # Combine and drop duplicates
            preview_rows = pd.concat([core_rows, supplemental_rows]).drop_duplicates()

            # Format for output
            preview = preview_rows.to_string(index=False)
            csv_path = aasx_filepath.replace(".aasx", "_aas_df.csv")

            return ToolResult(output=f"Information included in AAS:\n{preview}. More details are saved as a dataframe table in {csv_path} locally.")

        except Exception as e:
            return ToolResult(error=f"AASParser failed: {str(e)}")




