from pyrogram import Client, filters
from bs4 import BeautifulSoup
import requests
from Exon import Abishnoi as app

@app.on_message(filters.command(['grs', 'reverse', 'pp', 'p', 'P']))
async def reverse_image_search(client, message):
    if not message.reply_to_message:
        await message.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴀ sᴛɪᴄᴋᴇʀ.")
        return

    if message.reply_to_message.photo:
        msg = await message.reply("sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ɪᴍᴀɢᴇ.....")
        photo = message.reply_to_message.photo[-1]
        file_id = photo.file_id
        file_path = await client.download_media(file_id)
        result = reverse_image_search(file_path)
        if result:
            caption = f"[{result['title']}]({result['link']})"
            await client.send_photo(chat_id=message.chat.id, photo=file_path, caption=caption, parse_mode='markdown')
        else:
            await message.reply("No results found.")
        await msg.delete()

    elif message.reply_to_message.sticker:
        msg = await message.reply("sᴇᴀʀᴄʜɪɴɢ ғᴏʀ sᴛɪᴄᴋᴇʀ.....")
        sticker = message.reply_to_message.sticker
        file_id = sticker.file_id
        file_path = await client.download_media(file_id)
        result = reverse_image_search(file_path)
        if result:
            caption = f"[{result['title']}]({result['link']})"
            await client.send_sticker(chat_id=message.chat.id, sticker=file_path, caption=caption, parse_mode='markdown')
        else:
            await message.reply("No results found.")
        await msg.delete()

def reverse_image_search(image_path):
    search_url = "https://www.google.com/searchbyimage"
    files = {'encoded_image': open(image_path, 'rb')}
    params = {'image_url': ''}
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.post(search_url, params=params, headers=headers, files=files)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        anchor = soup.find('a', {'class': 'iKjWAf'})
        if anchor:
            title = anchor.text
            link = anchor['href']
            return {'title': title, 'link': link}
    return None

