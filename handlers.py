
from aiogram import types   
from db import log 
from datetime import datetime   

async def time_split(time_ranges: str):
    periods = time_ranges.split(',')
    results = []

    for period in periods:
        start_time_str, end_time_str = period.split('-')
        start_time = datetime.strptime(start_time_str.strip(), "%H:%M")
        end_time = datetime.strptime(end_time_str.strip(), "%H:%M")
        time_diff = end_time - start_time

        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        results.append(f"{hours} H {minutes} M")

    return results

async def save_user(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name  
    request_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log(user_id, first_name, request_time)