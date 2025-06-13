from telethon.sync import TelegramClient
import os
import time

# API info
api_id = 123456
api_hash = ''
phone = '+'

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone)


target = input("typing @username").strip()

# image path
SAVE_DIR = 'downloads/photos_only'
os.makedirs(SAVE_DIR, exist_ok=True)

count = 0
delay = 0.5

print(f" 正在從 {target} 抓取圖片...")

# only image 
for message in client.iter_messages(target):
    if message.photo:
        try:
            path = client.download_media(message.photo, SAVE_DIR)
            print(f" 已下載：{path}")
            count += 1
            time.sleep(delay)
        except Exception as e:
            print(f" 錯誤：{e}")

print(f"\n🎉 完成，共下載 {count} 張圖片。")
client.disconnect()
