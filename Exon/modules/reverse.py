from pyrogram import Client, filters
import requests
from Exon import Abishnoi as app
from bs4 import BeautifulSoup

# Replace 'YOUR_SAUCENAO_API_KEY' with the provided SauceNao API key
SAUCENAO_API_KEY = '077f16b38a2452401790540f41246c7d951330c0'

async def reverse_image_search(image_url):
    saucenao_url = "https://saucenao.com/search.php"
    params = {
        "db": 999,  # 999 is the "All" database in SauceNao
        "output_type": 2,  # JSON output
        "testmode": 0,  # Production mode
        "numres": 16,  # Maximum number of results
        "url": image_url,
        "api_key": SAUCENAO_API_KEY,
    }
    
    try:
        response = requests.get(saucenao_url, params=params)

        if response.status_code == 200:
            result = response.json()
            if 'results' in result:
                results = result['results']
                details = []
                for res in results:
                    data = res['data']
                    if 'characters' in data and 'material' in data:
                        characters = data['characters']
                        material = data['material']
                        character_names = ", ".join(characters)
                        anime_name = material[0]['title']
                        details.append(f"Character(s): {character_names}\nAnime: {anime_name}")
                return details
            else:
                return ["No results found."]
        else:
            return [f"Error: SauceNao API returned status code {response.status_code}."]
    except Exception as e:
        return [f"Error: {str(e)}"]

@app.on_message(filters.command(['grs', 'reverse', 'pp', 'p', 'P']))
async def reverse_image_search_command(client, message):
    if not message.reply_to_message:
        await message.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴀ sᴛɪᴄᴋᴇʀ.")
        return

    if message.reply_to_message.photo:
        msg = await message.reply("sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ɪᴍᴀɢᴇ.....")
        photo = message.reply_to_message.photo
        image_url = photo.file_id
        results = await reverse_image_search(image_url)
        for detail in results:
            await message.reply(detail)
        await msg.delete()

    elif message.reply_to_message.sticker:
        msg = await message.reply("sᴇᴀʀᴄʜɪɴɢ ғᴏʀ sᴛɪᴄᴋᴇʀ.....")
        sticker = message.reply_to_message.sticker
        image_url = sticker.file_id
        results = await reverse_image_search(image_url)
        for detail in results:
            await message.reply(detail)
        await msg.delete()


