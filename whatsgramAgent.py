# Here, a new istance of whatsgram bot.
# First of all should start the setup of whatsapp.
# When finished, should start listening for messages in specified groups.
# Information about telegram group should be passed in creation.
# Information about whatsapp group are gathered during the setup.

import argparse
from telegram.ext import ApplicationBuilder
from whatsapp import WhatsappBOT
import wx
from queue import Queue
from threading import Thread
import asyncio

def sendToTelegram(message):
	global tgram
	global args
	global tloop
	asyncio.run_coroutine_threadsafe(
    tgram.bot.send_message(
      chat_id=args.telegramChatID,
      text=message
    )
	, tloop)
	print(tgram, args, message)

def onMessage(message):	# From whatsapp.
	global tgram
	split = message.GetString().split(':', 1)
	topic = split[0]
	message = split[1]
	sendToTelegram(topic)

def connectToTelegram():
	global tloop
	tloop = asyncio.new_event_loop()
	asyncio.set_event_loop(tloop)
	global tgram
	global args
	tgram = ApplicationBuilder().token(args.telegramToken).build()
	tgram.run_polling()

def connectToWhatsapp():
	asyncio.set_event_loop(asyncio.new_event_loop())
	global wsapp
	app = wx.App()
	wsapp = WhatsappBOT()
	wsapp.bindTopic(onMessage)
	wsapp.loadWhatsapp()
	wsapp.Show() # GUI
	app.MainLoop()

def main():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument('telegramToken')
	parser.add_argument('telegramChatID')
	args = parser.parse_args()
	
	# Telegram.
	Thread(target=connectToTelegram).start()
	
	# Whatsapp.
	w = Thread(target=connectToWhatsapp)
	w.start()
	w.join()

if __name__ == "__main__":
	main()