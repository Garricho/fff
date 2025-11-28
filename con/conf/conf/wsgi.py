from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetMessagesViewsRequest


# TelegramClient uchun kerakli ma'lumotlarni kiriting

api_id = 26760714
api_hash = "70af2b06b0b205ed699ae058dd18ce17"
phone_number = '+998991464563'  # Telefon raqamingiz
channel_username = '@Qorgontepaliklar_Bozori'  # Kanal username

# TelegramClient yaratish
client = TelegramClient('session_name', api_id, api_hash)

async def get_latest_post_views():
    async with client:
        channel = await client.get_entity(channel_username)
        messages = await client.get_messages(channel, limit=1)
        latest_message = messages[0]
        views = await client(GetMessagesViewsRequest(
            peer=channel,
            id=[latest_message.id],
            increment=False
        ))
        print(f"Oxirgi post ko'rishlar soni: {views.count}")

client.loop.run_until_complete(get_latest_post_views())