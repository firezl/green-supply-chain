import asyncio
from fastapi_poe.types import ProtocolMessage
from fastapi_poe.client import get_bot_response
import json


class Conversation(object):
    def __init__(self, api_key, bot_name, system_message):
        self.api_key = api_key
        self.messages = []
        self.response = ""
        self.bot_name = bot_name
        if system_message == "":
            pass
        else:
            self.add_message(system_message, "system")

    def get_responses(self):
        async def get_responses(api_key, messages):
            response = ""
            async for partial in get_bot_response(
                messages=messages, bot_name="ChatGPT", api_key=api_key
            ):
                data = partial.text
                response += data
            print("")
            return response

        return get_responses(self.api_key, self.messages)

    def add_message(self, message, role):
        message = ProtocolMessage(role=role, content=message)
        self.messages.append(message)

    def chat(self, message):
        self.add_message(message, "user")
        self.response = asyncio.run(self.get_responses())
        self.add_message(self.response, "bot")
        return self.response


if __name__ == "__main__":
    conversation = Conversation("", "ChatGPT", "")
    while True:
        message = input("You: ")
        print(conversation.chat(message))
