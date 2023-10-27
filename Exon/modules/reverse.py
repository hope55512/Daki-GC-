from pyrogram import Client, filters
import requests
from Exon import Abishnoi as app

async def reverse_image_search(image_url):
    saucenao_url = "https://saucenao.com/search.php"
    params = {
        "db": 999,  # 999 is the "All" database in SauceNao
        "output_type": 2,  # JSON output
        "testmode": 1,  # Test mode (remove this for production use)
        "url": image_url,
    }
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
            return "No results found."
    else:
        return "Error: Unable to perform reverse image search."

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
        if isinstance(results, str):
            await message.reply(results)
        else:
            for detail in results:
                await message.reply(detail)
        await msg.delete()

    elif message.reply_to_message.sticker:
        msg = await message.reply("sᴇᴀʀᴄʜɪɴɢ ғᴏʀ sᴛɪᴄᴋᴇʀ.....")
        sticker = message.reply_to_message.sticker
        image_url = sticker.file_id
        results = await reverse_image_search(image_url)
        if isinstance(results, str):
            await message.reply(results)
        else:
            for detail in results:
                await message.reply(detail)
        await msg.delete()


