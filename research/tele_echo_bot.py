# connectiong telegram bot with a python 

# using iogram3.1.1 because it is compatable with python 3.7 

# u can get these codes from iogram documentattion 
import logging
from aiogram import Bot,Dispatcher,types,executor
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN=os.getenv("TOKEN")

# configuration 
logging.basicConfig(level=logging.INFO)

# initialize bot  and dispatcher 

bot = Bot(token=API_TOKEN)
dp=Dispatcher(bot)              # these are to make connection 

# press control and right click on any function to see their detail 


@dp.message_handler(commands=["start","help"])
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.reply("hi\nI am bot!\n powered by iogram.")


@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return echo
    """

    await message.answer(message.text)


if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)

