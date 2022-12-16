# Here, a new istance of whatsgram bot.
# First of all should start the setup of whatsapp.
# When finished, should start listening for messages in specified groups.
# Information about telegram group should be passed in creation.
# Information about whatsapp group are gathered during the setup.

import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('telegramToken')
	parser.add_argument('telegramChatID')
	args = parser.parse_args()
	
	
