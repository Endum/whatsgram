# Here, a new istance of whatsgram bot.
# First of all should start the setup of whatsapp.
# When finished, should start listening for messages in specified groups.
# Information about telegram group should be passed in creation.
# Information about whatsapp group are gathered during the setup.

import argparse
from telegram.ext import ApplicationBuilder

def connectToTelegram(args):
	application = ApplicationBuilder().token(args.telegramToken).build()
	application.bot.send_message(
      chat_id=args.telegramChatID,
      text='Test'
    )
	application.run_polling()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('telegramToken')
	parser.add_argument('telegramChatID')
	args = parser.parse_args()
	
	connectToTelegram(args)