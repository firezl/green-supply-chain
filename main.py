import asyncio
from fastapi_poe.types import ProtocolMessage
from fastapi_poe.client import get_bot_response
import json


# Create an asynchronous function to encapsulate the async for loop
async def get_responses(api_key):
    message = ProtocolMessage(role="user", content="你好，你是谁")
    async for partial in get_bot_response(
        messages=[message], bot_name="Web-Search", api_key=api_key
    ):
        data = partial.raw_response
        data = json.loads(data["text"])
        print(data["text"], end="")


# Replace <api_key> with your actual API key, ensuring it is a string.
api_key = ""

# Run the event loop
# For Python 3.7 and newer
asyncio.run(get_responses(api_key))

# For Python 3.6 and older, you would typically do the following:
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_responses(api_key))
# loop.close()
