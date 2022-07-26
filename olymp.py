from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5399754914:AAGibcVpZenT-4FKKkMvz_2QWq7sY-XHV7Y").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling( )
