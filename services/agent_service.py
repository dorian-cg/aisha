from typing import List
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from models.message import Message
from kernel.config import kernel, chat_completion, execution_settings


async def ask(messages: List[Message]) -> str:
    history = ChatHistory()

    history.add_system_message("You are a smart home agent/assistant")
    history.add_system_message("Your name is A.I.S.H.A")
    history.add_system_message("You can control devices in a smart home")
    history.add_system_message(
        "You can also provide information about the smart home devices"
    )
    history.add_system_message(
        "If the user asks something out of your capabilities, kindly tell them you can't help with that"
    )
    history.add_system_message("Keep your responses human-friendly and simple")

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
