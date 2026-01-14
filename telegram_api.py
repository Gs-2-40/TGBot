from constants import *
from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji
import asyncio


client = TelegramClient('my_session', api_id, api_hash)

@client.on(events.NewMessage(chats=DUSHA_tg_id))
async def init_reactor(event):
    if 'разряд' in event.message.text.lower():
        messages = await client.get_messages(DUSHA_tg_id, limit=5)
        for msg in messages:
            await client(SendReactionRequest(DUSHA_tg_id, msg.id, reaction=[ReactionEmoji(emoticon='⚡')]))
    elif 'океан' in event.message.text.lower():
        messages = await client.get_messages(DUSHA_tg_id, limit=5)
        for msg in messages:
            await client(SendReactionRequest(DUSHA_tg_id, msg.id, reaction=[ReactionEmoji(emoticon='🐳')]))
#    elif 'огонь' in event.message.text.lower():
#        messages = await client.get_messages(DUSHA_tg_id, limit=3)
#        for msg in messages:
#            await client(SendReactionRequest(DUSHA_tg_id, msg.id, reaction=[ReactionEmoji(emoticon='🔥')]))
    elif 'love' in event.message.text.lower() or ("люблю" in event.message.text.lower() and not "не люблю" in event.message.text.lower()):
        messages = await client.get_messages(DUSHA_tg_id, limit=5)
        for msg in messages:
            await client(SendReactionRequest(DUSHA_tg_id, msg.id, reaction=[ReactionEmoji(emoticon='❤️')]))
    elif 'clear' in event.message.text.lower():
        print('clr')
        messages = await client.get_messages(DUSHA_tg_id, limit=30)
        for msg in messages:
            if msg.reactions:
                await client(SendReactionRequest(DUSHA_tg_id, msg.id, reaction=[]))

async def main():
    await client.start(password=password)
    
    print("Авторизация успешна! Бот работает...")
    
    #await client.send_message('me', 'Я успешно зашел в аккаунт с 2FA!')
    
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())