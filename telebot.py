# will not work like chat gpt because we need to do recharge for a api in open api 
#https://platform.openai.com/settings/organization/api-keys



from dotenv import load_dotenv
import os
from aiogram import Bot,Dispatcher,types,executor
import openai
import sys

class Refrences:

    """ a class to store previously response for the chat gpt api 
    """

    def __init__(self):
        self.response=""


    
load_dotenv()
openai.api_key=os.getenv("OpenAI_API_KEY")
    
reference= Refrences()

TOKEN=os.getenv("Token")

# model name 

MODEL_NAME="gpt-3.5-turbo"

bot = Bot(token=TOKEN)
dispatcher=Dispatcher(bot)  

def clear_past():
    "function o clear the pre vious coversation and context"
    reference.response=""   # means replacing with empty 



@dispatcher.message_handler(commands=["start"])
async def welcome(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.reply("hi\nI am telebot!\n created by meraj . how can i assist u ")


# to clear past outputs 


@dispatcher.message_handler(commands=["clear"])
async def clear(message:types.message):

    """a handler to clear the previous conversation and context """

    clear_past()    # calling above stated clear function 
    await message.reply(" i have cleared the past conversation ")


# creating hep function 


@dispatcher.message_handler(commands=["help"])
async def helper(message:types.message):

    """an handler to display the help menu """

    help_command="""
hi there i am chatGPT telegram bot created by meraj ! please follow these commands-
/start - to start the coversation 
/clear - to clear the past conversation 
/help - to get this help menu """

    await message.reply(help_command)



# a handler to procees the user input and generate a response using the chat gpt api




"""
    A handler to process the user's input and generate a response using the chatGPT API.
    """



@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    
    print(f">>> USER: \n\t{message.text}")               # user give message this will print in a terminal 
    response = openai.ChatCompletion.create(            # openai because we r performing chatbot operation  chatcompletion because it is this default see on open ai documentation of chatbots 
        model = MODEL_NAME,                            # this will use api of gpt3.5 turbo we r not downloading model in pc because it is too huge this gives acces to the llm model 
        messages = [
            {"role": "assistant", "content": reference.response}, # bot role is assistant and it gives ouptput or response 
            {"role": "user", "content": message.text} #our query 
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)



    
if __name__== "__main__":
    executor.start_polling(dispatcher,skip_updates=True)   # if we set ski updates = false means if server is down and live again then it will answer previous question first 






