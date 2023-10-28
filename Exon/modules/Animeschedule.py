from pyrogram import filters, types
import requests
from Exon import Abishnoi as app

# Define a global variable to store the schedule text
schedule_text = ""

@app.on_message(filters.command('latest'))
def schedule(_, message):
    global schedule_text
    if not schedule_text:
        schedule_text = get_schedule_text()
    inline_keyboard = types.InlineKeyboardMarkup(
        [
            [types.InlineKeyboardButton("Refresh", callback_data="refresh_schedule")]
        ]
    )
    message.reply_text(
        f"**Today's Schedule:**\nTime-Zone: India (IST, GMT +5:30)\n\n{schedule_text}",
        reply_markup=inline_keyboard,
    )

@app.on_callback_query(filters.regex("refresh_schedule"))
def refresh_schedule(_, query):
    global schedule_text
    schedule_text = get_schedule_text()
    query.answer("Schedule refreshed!")

def get_schedule_text():
    results = requests.get('https://subsplease.org/api/?f=schedule&h=true&tz=Asia/Kolkata').json()
    text = []
    for result in results['schedule']:
        title = result['title']
        time_india = result['time']
        aired = bool(result['aired'])

        # Determine if it's AM or PM
        hour_parts = time_india.split(':')[0]
        period = 'AM' if int(hour_parts) < 12 else 'PM'
        time_parts = time_india.split(':')
        hours = int(time_parts[0]) if int(time_parts[0]) <= 12 else int(time_parts[0]) - 12

        title = f"**[{title}](https://subsplease.org/shows/{result['page']})**" if not aired else f"**~~[{title}](https://subsplease.org/shows/{result['page']})~~**"
        data = f"{title} - **{hours:02}:{time_parts[1]} {period} IST**"
        text.append(data)

    return "\n".join(text)

__mod_name__ = "Sᴄʜᴇᴅᴜʟᴇ 📑"

__help__ = """
 ❍ `/latest`: to see the latest anime episode
"""
