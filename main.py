import os
from dotenv import load_dotenv
load_dotenv()
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import asyncio
import aiofiles
import yt_dlp
import os
api_key = os.getenv("API_KEY")




async def log(logtext2):
    async with aiofiles.open("log.txt", mode="a") as log:

        await log.write("\n" + str(logtext2.from_user.id) + "\n" + logtext2.text  + "\n next user:"   )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Этот бот пока что в глубоком бетатесте и пока только умеет писать хело ворлд. НО бекенд пилится. \n https://github.com/Zilibobka-S/zyd-bot \n https://youtu.be/YLhpPghyIQw?\n \n Используя любые функции бота (кроме /start) вы соглашаетесь на хранение вашего Id и отправленных сообщений на неопределённый срок. Ради моей же безопасности. Способ удаления появится чуть позже")

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Отправьте ссылку на видео!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)
    await log(update.message)

    url = update.message.text
    if os.path.exists((str(update.message.from_user.id)) + ".mp4"):
        os.remove(str(update.message.from_user.id) +".mp4")
    ydl_opts = {
    "outtmpl": str(update.message.from_user.id) + ".mp4",
    "format": "mp4"
}
    url = update.message.text
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
    #return await asyncio.to_thread(lambda: YoutubeDL(ydl_opts).download(str(update.message.text)))
    await update.message.reply_video(video=open(str(update.message.from_user.id) + ".mp4", "rb"))


if __name__ == '__main__':
    app = ApplicationBuilder().token(api_key).build()


    app.add_handler(CommandHandler("start", start))

    #app.add_handler(CommandHandler("command", URL))
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

   # echo_handler= MessageHandler(filters.TEXT & (~filters.COMMAND), echo_handler)

    app.add_handler(echo_handler)
    print( "Бот запущен!")
    app.run_polling()

