from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Добрый день. Вас приветствует бот, которой позволяет вам произвести скачивание понравившегося Вам видео с любого доступного видеохостинга. Для этого Вам необходимо отправить ссылку на понравившееся видео, и в ответном сообщении Вам будет оправлена ссылка на его скачивание")
