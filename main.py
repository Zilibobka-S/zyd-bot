from dotenv import load_dotenv
load_dotenv()
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import asyncio
import aiofiles
from yt_dlp import YoutubeDL
import aiofiles.os
import os
api_key = os.getenv("API_KEY")
#downloaddir =
import proxychecker
import random
proxies = {}
proxychecker.check()

proxies = proxychecker.get_proxies()
proxies_list = list(proxies.keys())
print(proxies_list)
print(proxies)
async def proxy_updater():
    startcount=len(proxychecker.get_proxies)

async def log(logtext2):
    async with aiofiles.open("log.txt", mode="a") as log:

        await log.write("\n" + str(logtext2.from_user.id) + "\n" + logtext2.text  + "\n next user:"   )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Этот бот пока что в глубоком бетатесте и пока только умеет писать хело ворлд. НО бекенд пилится. \n https://github.com/Zilibobka-S/zyd-bot \n https://youtu.be/YLhpPghyIQw?\n \n Используя любые функции бота (кроме /start) вы соглашаетесь на хранение вашего Id и отправленных сообщений на неопределённый срок. Ради моей же безопасности. Способ удаления появится чуть позже")

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Отправьте ссылку на видео!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    downloadname = str(update.message.from_user.id) +".mp4"

    await log(update.message)
    await update.message.reply_text("Got a link!")
    url = update.message.text
    if await aiofiles.os.path.exists(downloadname):
        await aiofiles.os.remove(downloadname)
    url = update.message.text
    async def das():
        ydl_opts = {
        "outtmpl":downloadname,
        "format": "mp4",
        "ratelimit": 10000000,
        "proxy": ("http://" + random.choice(proxies_list))
        }
        print(ydl_opts["proxy"])
        await asyncio.to_thread(lambda: YoutubeDL(ydl_opts).download(str(url)))
        downloaded = await asyncio.to_thread(lambda: open(downloadname, "rb"))
        await update.message.reply_video(video=downloaded)
        await update.message.reply_text ("Downloaded!")

    asyncio.create_task(das())
if __name__ == '__main__':
    app = ApplicationBuilder().token(api_key).build()

    app.add_handler(CommandHandler("start", start))

    #app.add_handler(CommandHandler("command", URL))
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

   # echo_handler= MessageHandler(filters.TEXT & (~filters.COMMAND), echo_handler)

    app.add_handler(echo_handler)
    print( "Бот запущен!")
    app.run_polling()


