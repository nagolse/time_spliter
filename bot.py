import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import os 
from handlers import time_split, save_user
from dotenv import load_dotenv
from db import init_db  
from fastapi import FastAPI

load_dotenv()
app = FastAPI()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6000)
logging.basicConfig(level=logging.INFO)


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()


@dp.message()
async def cmd_start(message: types.Message):
    await save_user(message)
    result = await time_split(message.text)
    result_str = "\n".join(result)

    await message.answer(result_str)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    init_db()
    asyncio.run(main())
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6000)
    
