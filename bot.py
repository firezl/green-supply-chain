from fastapi_poe import PoeBot, run
from fastapi_poe.types import PartialResponse, SettingsRequest, QueryRequest, SettingsResponse
from fastapi_poe.client import stream_request
from typing import AsyncIterable

class GPT35TurboBot(PoeBot):
    async def get_response(self, query: QueryRequest) -> AsyncIterable[PartialResponse]:
        async for msg in stream_request(query, "GPT-3.5-Turbo", api_key=""):
            yield msg

    async def get_settings(self, setting: SettingsRequest) -> SettingsResponse:
        return SettingsResponse(
            server_bot_dependencies={"GPT-3.5-Turbo": 1}
        )
if __name__ == "__main__":
    run(GPT35TurboBot(), access_key="")