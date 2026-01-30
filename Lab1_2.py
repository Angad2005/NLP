import re

# Set of all alphabetical characters
p1=r'[a-zA-Z]+'

# Set of all lower case alphabetical characters ending with 'b'
p2=r'[a-z]*b$'

# Set of all string from the alphabet {a,b} such that each 'a' is precceded and followed by a 'b'
p3=r'(b+(b|ab)*b+)?'

# Set of all string with two consecutive words
p4=r'([a-zA-Z]+)\s+\1'

# All strings that start at the begining of a line with an integer and that end at the end of a line with a word.
p5=r'^[0-9]+[a-zA-Z]+$'

#All strings that have both the words 'grotto' and the word 'raven' in them.
p6=r'\bgrotto\b.*\braven\b|\braven\b.*\bgrotto\b'

# Write a pattern that places the first word of an english sentence in a register.
p7=r'^[^a-zA-Z]*([a-zA-Z]+)[^a-zA-Z]*\1'