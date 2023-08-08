#!/usr/bin/python3
alpha = ""
for character in range(97, 123):
    if character != 101 and character != 113:
        alpha += "{}".format(chr(character))
print(alpha, end='')
