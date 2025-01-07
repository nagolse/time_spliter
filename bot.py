import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import os 
from handlers import time_split, save_user
from dotenv import load_dotenv
from db import init_db  
from fastapi import FastAPI
import threading
load_dotenv()
app = FastAPI()

    
logging.basicConfig(level=logging.INFO)


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

async def main():
    asyncio.run(main())

def run_uvicorn():
    uvicorn.run(app, host="0.0.0.0", port=6000)


async def run_tasks():
    # Start the database initialization and main task concurrently
    await asyncio.gather(init_db()

                         
@dp.message()
async def cmd_start(message: types.Message):
    await save_user(message)
    result = await time_split(message.text)
    result_str = "\n".join(result)

    await message.answer(result_str)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Run the Uvicorn server in a separate thread
    uvicorn_thread = threading.Thread(target=run_uvicorn)
    uvicorn_thread.start()

    # Run your asynchronous tasks concurrently
    asyncio.run(run_tasks())
