from telegram.ext import Application, CommandHandler, MessageHandler, filters
from downloader.tiktok import download_tiktok
from downloader.xhs import download_xhs

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Application.builder().token(BOT_TOKEN).build()

async def start(update, context):
    await update.message.reply_text("Selamat datang di Douyin Downloader Pro!\nKirim link TikTok atau Xiaohongshu.")

async def handle_message(update, context):
    url = update.message.text

    if "tiktok.com" in url:
        result = await download_tiktok(url)
    elif "xhslink.com" in url or "xiaohongshu.com" in url:
        result = await download_xhs(url)
    else:
        result = "❌ Link tidak dikenali. Kirim link TikTok atau Xiaohongshu."

    await update.message.reply_text(result)

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
