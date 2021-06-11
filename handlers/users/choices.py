import logging

from aiogram.types import CallbackQuery

from keyboards.inline.new_download import new_url_callback
from loader import dp


@dp.callback_query_handler(new_url_callback.filter(answer="yes"))
async def selected_yes(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data['answer']}")

    await call.message.answer("Введите ссылку на понравившееся Вам видео.")
