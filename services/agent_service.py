from typing import List
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from models.message import Message
from kernel.config import kernel, chat_completion, execution_settings


async def ask(messages: List[Message]) -> str:
    history = ChatHistory()

    history.add_system_message("You are a smart home assistant")
    history.add_system_message("Your name is A.I.S.H.A")

    for msg in messages:
        match msg.sender:
            case "user":
                history.add_user_message(msg.content)
            case "assistant":
                history.add_assistant_message(msg.content)

    response: ChatMessageContent = await chat_completion.get_chat_message_content(
        history,
        settings=execution_settings,
        kernel=kernel,
    )

    return response.content
