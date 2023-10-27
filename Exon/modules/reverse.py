from pyrogram import Client, filters
from AIOSauceNao import AIOSauceNao
from Exon import Abishnoi as app

# Replace 'YOUR_SAUCENAO_API_KEY' with the provided API key
SAUCENAO_API_KEY = '077f16b38a2452401790540f41246c7d951330c0'

async def reverse_image_search(image_url):
    # Initialize AIOSauceNao with the API key
    async with AIOSauceNao(SAUCENAO_API_KEY) as aio:
        results = await aio.from_url(image_url)
        # Process and format the results as needed
        details = []
        for result in results:
            if result.characters and result.material:
                character_names = ", ".join(result.characters)
                anime_name = result.material[0].title
                details.append(f"Character(s): {character_names}\nAnime: {anime_name}")
        return details

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
