from aiogram import Bot, Router
from aiogram.types import Message

router = Router()

@router.message()
async def send_echo_message(message: Message) -> None:
    await message.answer(text="Я не знаю, как ответить на ваше сообщение:(")