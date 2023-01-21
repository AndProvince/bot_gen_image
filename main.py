import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN, API_OPENAI

openai.api_key = API_OPENAI

bot = Bot(TOKEN)
dsp = Dispatcher(bot)

@dsp.message_handler()
async def send(message: types.Message):
    response = openai.Image.create(
        prompt=message.text,
        n=1,
        size="1024x1024"
    )
    
    await message.answer_photo(response['data'][0]['url'])

executor.start_polling(dsp, skip_updates=True)