import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv

# Загружаем .env переменные
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

# 👇 aiogram v3: регистрируем хендлер через filter отдельно
@dp.message(F.text == "/start")
async def start_handler(message: Message):
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(
            text="🎮 Играть",
            web_app=WebAppInfo(url=f"{WEBAPP_URL}/play?user_id={message.from_user.id}")
        )
    )
    builder.adjust(1)
    await message.answer("Добро пожаловать в GraphRace!", reply_markup=builder.as_markup(resize_keyboard=True))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
