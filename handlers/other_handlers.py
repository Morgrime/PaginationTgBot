from aiogram.types import Message
from lexicon.lexicon import LEXICON
from aiogram import Router

router = Router()

@router.message()
async def send_echo(message: Message):
    await message.answer(f"Данный бот работает как книга, пожалуйста используйте команду /help, если хотите что-то сделать, но не знаете что")
        