import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = '7142268864:AAFffBRRonLJg-ye6qyUNoWPoNZoOPv'


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Kirim link TikTok atau Xiaohongshu!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if "tiktok.com" in text:
        await update.message.reply_text("⏳ Sedang mendownload video dari TikTok...")
        await download_tiktok(update, text)
    elif "xhslink.com" in text or "xiaohongshu.com" in text:
        await update.message.reply_text("⏳ Sedang mencoba download dari Xiaohongshu...")
        await download_xiaohongshu(update, text)
    else:
        await update.message.reply_text("❌ Link tidak dikenali. Kirim link TikTok atau Xiaohongshu.")

async def download_tiktok(update: Update, url: str):
    try:
        api = f"https://tikwm.com/api/?url={url}"
        r = requests.get(api).json()
        if r.get("data") and r["data"].get("play"):
            video_url = r["data"]["play"]
            await update.message.reply_video(video=video_url)
        else:
            await update.message.reply_text("❌ Gagal download dari TikTok.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error TikTok: {e}")

async def download_xiaohongshu(update: Update, url: str):
    try:
        api = f"https://www.xhsdownload.com/api/download?url={url}"
        r = requests.get(api).json()
        if r.get("data") and r["data"].get("video_url"):
            video_url = r["data"]["video_url"]
            await update.message.reply_video(video=video_url)
        else:
            await update.message.reply_text("❌ Gagal download dari Xiaohongshu.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error Xiaohongshu: {e}")

if __name__ == '__main__':
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

