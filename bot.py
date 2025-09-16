from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Aapka BotFather ka Token
TOKEN = "8358685036:AAE89_77Gn6Gabiqyc9C3C-CZieJtOgTrTw"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello bhai! Main aapka Telegram bot hoon.")

# Normal messages ka reply
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Aapne bola: {text}")

def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("✅ Bot chal raha hai... (Ctrl+C dabake band karna)")
    app.run_polling()

if __name__ == "__main__":
    main()
