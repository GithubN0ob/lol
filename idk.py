import os
from random import randrange
from string import ascii_lowercase

print("running.")

def tap(x, y):
	os.system(f"adb shell input tap {x} {y}")

def type(text):
	os.system(f'adb shell input text "{text}"')

def word_generator(x):
	text = ""
	for i in range(x):
		text+=ascii_lowercase[randrange(26)]
	return text

# tap(100, 2100) #home
# tap(250, 2100) #chat
# tap(500, 500)

for i in range(0):
	type(word_generator(14))
	tap(1050, 1420)

"""
cd documents\desktop
"""

#for the command line


if __name__ == "__main__":
	message_count = int(input("How many messages do you want to send? (Integer) "))
	send_custom_message = bool(input("Send custom message? (y/n) ").lower() == "y")
	if send_custom_message:
		message = input("message: ")
		for i in range(message_count):
			type(message)
			tap(1050, 1420)
	else:
		message_length = int(input("Length of [randomly generated] message? (Integer) "))
		for i in range(message_count):
			type(word_generator(message_length))
			tap(1050, 1420)