# Here, a new istance of whatsgram bot.
# First of all should start the setup of whatsapp.
# When finished, should start listening for messages in specified groups.
# Information about telegram group should be passed in creation.
# Information about whatsapp group are gathered during the setup.

import argparse
from telegram.ext import ApplicationBuilder
import asyncio
from whatsapp import WhatsappBOT
import wx

def sendToTelegram(message):
	global tgram
	global args
	asyncio.get_event_loop().create_task(
        tgram.bot.send_message(
          chat_id=args.telegramChatID,
          text=message
        )
	)

def onMessage(message):
	global tgram
	split = message.GetString().split(':', 1)
	topic = split[0]
	message = split[1]
	print(topic+'\n'+message)
	sendToTelegram(topic)

async def connectToTelegram(args):
	global tgram
	tgram = ApplicationBuilder().token(args.telegramToken).build()
	#tgram.run_polling()

async def connectToWhatsapp():
	global wsapp
	app = wx.App()
	wsapp = WhatsappBOT()
	wsapp.bindTopic(onMessage)
	wsapp.loadWhatsapp()
	wsapp.Show() # GUI
	app.MainLoop()

async def main():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument('telegramToken')
	parser.add_argument('telegramChatID')
	args = parser.parse_args()
	
	# Telegram.
	await asyncio.get_event_loop().create_task(connectToTelegram(args))
	
	# Whatsapp.
	await asyncio.get_event_loop().create_task(connectToWhatsapp())

if __name__ == "__main__":
	asyncio.get_event_loop().run_until_complete(main())