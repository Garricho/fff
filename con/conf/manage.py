from telethon.sync import TelegramClient

# TelegramClient uchun kerakli ma'lumotlarni kiriting
api_id = 26760714
api_hash = "70af2b06b0b205ed699ae058dd18ce17"
phone_number = '+998991464563'  # Telefon raqamingiz
channel_username = '@Qorgontepaliklar_Bozori'  # Kanal username

# TelegramClient yaratish
client = TelegramClient('session_name', api_id, api_hash)

def send_last_post_to_user(user_id):
    with client:
        # Kanal username'iga asosan kanal ID sini olamiz
        channel = client.get_entity(channel_username)

        # Kanalning oxirgi postini olish
        message = client.get_messages(channel, limit=1)[0]

        # Foydalanuvchiga oxirgi postni yuborish
        client.send_message(user_id, message)

# Foydalanuvchini ID sini kiriting
user_id = '7788645685'

# Funktsiyani chaqirish
send_last_post_to_user(user_id)
