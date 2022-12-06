from whatsapp import WhatsappBOT
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def sendMessages(update, context, messages):
  for message_part in messages:
    await context.bot.send_message(
      chat_id=update.effective_chat.id,
      text=message_part
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  messages = [
    "HI!",
    "I'm Whatsgram!",
    "My job here is to merge groups between Telegram and Whatsapp.",
    "To start, make me join the group you want to merge with a Whatsapp group.",
    "Make sure to have another device ready to scan whatsapp QRcode.",
  ]
  await sendMessages(update, context, messages)

async def new_member(update, context):
  messages = [
    "HI!",
    "Be ready to scan QR code!!",
    "A Whatsgram agent is connecting... as soon as he has it, he'll send you the QR.",
    "If it expires, you'll need to kick and make me rejoin this group.",
    "I'll now leave you in the hands of my agent!",
    "Thanks for using whatsgram! :D"
  ]
  for member in update.message.new_chat_members:
    if member.username == 'whatsgram_bot':
      await sendMessages(messages)

  # Call for a whatsgram agent.

if __name__ == '__main__':
  file = open('token.txt',mode='r')
  application = ApplicationBuilder().token(file.read()).build()
  file.close()

  start_handler = CommandHandler('start', start)
  application.add_handler(start_handler)
  welcome_handler = MessageHandler(Filters.status_update.new_chat_members, new_member)
  application.add_handler(welcome_handler)
  
  print("Bot up and running :)")

  application.run_polling()