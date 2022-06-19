#=================================================================================================
# Copyright (C) 2022 by szsupunma@Github, < https://github.com/szsupunma >.
# Released under the "GNU v3.0 License Agreement".
# All rights reserved.
#=================================================================================================
import os
import json
import asyncio
import requests

from pyrogram.errors import UserNotParticipant
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid

from database import (
    get_served_users,
    add_served_user,
    remove_served_user,
    get_served_chats,
    add_served_chat,
    remove_served_chat
)
app = Client(
    "hq_proxy_bot",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"],
)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
start_text = """
👋Hello!, I can create **free proxies** for you.

[+] For Http(S) click /http
[+] For Socks5 click /socks5
[+] For Socks4 click /socks4

Powered by @szteambots """

start_button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👥 Group", url="https://t.me/slbotzone"),
                    InlineKeyboardButton("🗣 Channel", url="https://t.me/szteambots")
                ]
            ]
)

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
🚧 **Access Denied** {message.from_user.mention}
You must,
🔹[join Our Telegram Channel](https://t.me/szteambots).
@szteambots
""")
       return
    name = message.from_user.id
    if message.chat.type != "private":
       await app.send_message(
        name,
        text = start_text,
        reply_markup = start_button)
       return await add_served_chat(message.chat.id) 
    else:
        await app.send_message(
         name,
         text = start_text,
         reply_markup = start_button)
        return await add_served_user(message.from_user.id) 
    


#********************************************************************************
API1='https://api.proxyscrape.com/v2/?request=proxyinfo&protocol='
API2='https://api.proxyscrape.com/v2/?request=getproxies&protocol'
#********************************************************************************

create = InlineKeyboardMarkup(
            [[InlineKeyboardButton("SZ team bots 🇱🇰", url="https://t.me/szteambots")]])

#********************************************************************************
@app.on_message(filters.command("socks4"))
async def proxy(_, message: Message):
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
🚧 **Access Denied** {message.from_user.mention}
You must,
🔹 : [join Our Telegram Channel](https://t.me/szteambots).

@szteambots
""")
       return
    name = message.from_user.id
    m =  await app.send_message(name,text=f"♻️ Creating Proxy....",reply_markup = create)
    req=requests.get(f'{API2}=socks4&timeout=10000&country=all').text
    with open(f"SOCKS4.txt", "w") as txt:
     txt.write(req)
     txt.close()
    info=json.loads(requests.get(f'{API1}socks4').text)
    last = info['last_updated'] 
    await app.send_document(name, f"SOCKS4.txt", caption=f"""
**✅ SUCCESSFULLY CREATED ✅**

※ Proxy count : `{str(len(req))}`
※ Lasted Updated : `{last}`

**Powered by** : @szteambots """,)
    await m.delete()
    os.remove(f"SOCKS4.txt")

#********************************************************************************
@app.on_message(filters.command("socks5"))
async def proxy(_, message: Message):
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
🚧 **Access Denied** {message.from_user.mention}
You must,
🔹 : [join Our Telegram Channel](https://t.me/szteambots).

@szteambots
""")
       return
    name = message.from_user.id
    m =  await app.send_message(name,text=f"♻️ Creating Proxy....",reply_markup = create)
    req=requests.get(f'{API2}=socks5&timeout=10000&country=all').text
    with open(f"SOCKS5.txt", "w") as txt:
     txt.write(req)
     txt.close()
    info=json.loads(requests.get(f'{API1}socks5').text)
    last = info['last_updated'] 
    await app.send_document(name, f"SOCKS5.txt", caption=f"""
**✅ SUCCESSFULLY CREATED ✅**

※ Proxy count : `{str(len(req))}`
※ Lasted Updated : `{last}`

**Powered by** : @szteambots """,)
    await m.delete()
    os.remove(f"SOCKS5.txt")

#********************************************************************************
@app.on_message(filters.command("http"))
async def proxy(_, message: Message):
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
🚧 **Access Denied** {message.from_user.mention}
You must,
🔹 : [join Our Telegram Channel](https://t.me/szteambots).

@szteambots
""")
       return
    name = message.from_user.id
    m =  await app.send_message(name,text=f"♻️ Creating Proxy....",reply_markup = create)
    req=requests.get(f'{API2}=http&timeout=10000&country=all').text
    with open(f"http.txt", "w") as txt:
     txt.write(req)
     txt.close()
    info=json.loads(requests.get(f'{API1}http').text)
    last = info['last_updated'] 
    await app.send_document(name, f"http.txt", caption=f"""
**✅ SUCCESSFULLY CREATED ✅**

※ Proxy count : `{str(len(req))}`
※ Lasted Updated : `{last}`

**Powered by** : @szteambots """,)
    await m.delete()
    os.remove(f"http.txt")

#============================================================================================
#Owner commands pannel here
#user_count, broadcast_tool

@app.on_message(filters.command("stats") & filters.user(1467358214))
async def stats(_, message: Message):
    name = message.from_user.id
    served_chats = len(await get_served_chats())
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    served_users = len(await get_served_users())
    served_users = []
    users = await get_served_users()
    for user in users:
        served_users.append(int(user["bot_users"]))

    await app.send_message(
        name,
        text=f"""
🍀 Chats Stats 🍀

🙋‍♂️ Users : `{len(served_users)}`
👥 Groups : `{len(served_chats)}`

🚧 Total users & groups : {int((len(served_chats) + len(served_users)))} """)

async def broadcast_messages(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await remove_served_user(user_id)
        return False, "Deleted"
    except UserIsBlocked:
        await remove_served_user(user_id)
        return False, "Blocked"
    except PeerIdInvalid:
        await remove_served_user(user_id)
        return False, "Error"
    except Exception as e:
        return False, "Error"

@app.on_message(filters.private & filters.command("bcast") & filters.user([1467358214,1483482076]) & filters.reply)
async def broadcast_message(_, message):
    b_msg = message.reply_to_message
    chats = await get_served_users() 
    m = await message.reply_text("Broadcast in progress")
    for chat in chats:
        try:
            await broadcast_messages(int(chat['bot_users']), b_msg)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass  
    await m.edit(f"""
Broadcast Completed:.""")    

@app.on_message(filters.command("ads"))
async def ads_message(_, message):
	await app.forward_messages(
		chat_id = message.chat.id, 
		from_chat = int(-1001325914694), 
		message_ids = 1050,
	)
	
app.run()
