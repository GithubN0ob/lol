import os
from random import randrange
from string import ascii_lowercase

print("running.")

def tap(x, y):
	os.system("adb shell input tap {x} {y}")

def type(text):
	os.system('adb shell input text "{text}"')

def word_generator(x):
	text = ""
	for i in range(x):
		text+=ascii_lowercase[randrange(26)]
	return text

# tap(100, 2100) #home
# tap(250, 2100) #chat
# tap(500, 500)

for i in range(5):
	type(word_generator(14))
	tap(1000, 1280)

"""
cd documents\desktop
"""

#for the command line


# if __name__ == "__main__":
# 	break_ = True
# 	while break_:
# 		x = input("say something bruv\n")
# 		if x=="55501555015":
# 			break
# 		type(x)
# 		tap(1000, 1280)
