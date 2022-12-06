from whatsapp import WhatsappBOT
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message = [
    "HI!",
    "I'm Whatsgram!",
    "My job here is to merge groups between Telegram and Whatsapp.",
    "To start, make me join the Telegram group you want to merge.",
    "Make sure to have another device ready to scan whatsapp QRcode.",
  ]
  await context.bot.send_message(
    chat_id=update.effective_chat.id,
    text=message_part
  )

if __name__ == '__main__':
  file = open('token.txt',mode='r')
  application = ApplicationBuilder().token(file.read()).build()
  file.close()

  start_handler = CommandHandler('start', start)
  application.add_handler(start_handler)
  
  print("Bot up and running :)")

  application.run_polling()