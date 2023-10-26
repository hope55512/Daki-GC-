from telethon import TelegramClient, events
from bs4 import BeautifulSoup
import requests
from Exon import telethn as client 

@client.on(events.NewMessage(pattern='/grs|/reverse|/pp|/p|/P'))
async def reverse(event):
    if not event.is_reply:
        await event.respond("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴀ sᴛɪᴄᴋᴇʀ.")
    elif event.reply_to_msg.media:
        msg = await event.respond("sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ɪᴍᴀɢᴇ.....")
        file = await event.reply_to_msg.download_media(file='image.jpg')
        result = reverse_image_search(file)
        if result:
            await event.respond(f"[{result['title']}]({result['link']})", link_preview=False, parse_mode='markdown')
        else:
            await event.respond("No results found.")
        await msg.delete()
    else:
        await event.respond("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴀ sᴛɪᴄᴋᴇʀ.")

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


