from pyrogram import Client, filters

#obtener los datos de https://my.telegram.org/auth
app = Client(
    "Tasky",
    api_id=14173078,
    api_hash="e5214b5d5e0e7eaf50cc9f9d17c16f3d",
    bot_token="2050139568:AAHrj-e20YYBZgHh-7SqYuy8PsMozPemW7s")

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text('Hello!')
    
print('Bot Online')
app.run()