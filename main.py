import asyncio
from fastapi_poe.types import ProtocolMessage
from fastapi_poe.client import get_bot_response
import json


# Create an asynchronous function to encapsulate the async for loop
async def get_responses(api_key, messages):
    response = ""
    async for partial in get_bot_response(
        messages=messages, bot_name="ChatGPT", api_key=api_key
    ):
        data = partial.text
        print(data, end="")
        response += data
    print("")
    return response


# Replace <api_key> with your actual API key, ensuring it is a string.
api_key = "tR4M-mL3mr_dNsH6ik19iF7AbMt4YcupQTk3JhsowVU"
messages = []
# Run the event loop
# For Python 3.7 and newer
message = ProtocolMessage(role="user", content="你好")
messages.append(message)
response = asyncio.run(get_responses(api_key, messages))
response = ProtocolMessage(role="bot", content=response)
messages.append(response)
message = ProtocolMessage(role="user", content="你可以帮我翻译一下下面的句子吗？")
messages.append(message)
response = asyncio.run(get_responses(api_key, messages))
response = ProtocolMessage(role="bot", content=response)
messages.append(response)
message = ProtocolMessage(
    role="user", content="碳是生物体（动物植物的组成物质）和矿物燃料（天然气，石油和煤）的主要组成部分。"
)
messages.append(message)
asyncio.run(get_responses(api_key, messages))
