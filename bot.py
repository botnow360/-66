import os
import time
import logging
from telegram import Bot
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL_ID")

bot = Bot(token=TOKEN)
logging.basicConfig(level=logging.INFO)

def send_test():
    bot.send_message(chat_id=CHANNEL, text="✅ Бот успешно запущен!")
    logging.info("Test message sent")
    scheduler.shutdown()  # остановим после отправки

if __name__ == "__main__":
    logging.info("Starting bot…")
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_test, 'interval', seconds=10, max_instances=1)
    scheduler.start()
    while True:
        time.sleep(1)
