import os
from dotenv import load_dotenv
load_dotenv()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


api_key = os.getenv("API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Этот бот пока что в глубоком бетатесте и пока только умеет писать хело ворлд. НО бекенд пилится. \n https://github.com/Zilibobka-S/zyd-bot \n https://youtu.be/YLhpPghyIQw?")




#if __name__ == '__bot__':
app = ApplicationBuilder().token(api_key).build()


app.add_handler(CommandHandler("start", start))



print( "Бот запущен!")
app.run_polling()

