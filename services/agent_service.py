from typing import List
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from models.message import Message
from kernel.config import kernel, chat_completion, execution_settings


async def ask(messages: List[Message]) -> str:
    history = ChatHistory()

    history.add_system_message("You are a smart home agent/assistant")
    history.add_system_message("Your name is Aisha")
    history.add_system_message(
        "If the user asks something out of your capabilities, kindly tell them you can't help with that"
    )
    history.add_system_message(
        "Keep your responses human-friendly and SHORT unless the ask is for a detailed explanation"
    )
    history.add_system_message(
        "Do not make up information or answers, for example don't say there are 2 locks in the garage if there is only one"
    )
    history.add_system_message(
        "Get all the rooms and devices available for context before answering the user (keep it to yourself)"
    )
    history.add_system_message(
        "Every device has a 'kind' property which can be 'Light', 'Lock' or 'Thermo' (thermostat)"
    )
    history.add_system_message(
        "If the user says 'hi' introduce yourself with a VERY SHORT message, don't overwhelm them with information!"
    )
    history.add_system_message(
        "If the user asks to set the thermo to some temperature, turn the thermo on if it is off"
    )

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
