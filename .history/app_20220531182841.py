#! python3

import re, pyperclip

#TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345 

# area code (optional)
# first separator
# first 3 digits
# separator
# last 4 digits

''', re.VERBOSE)

#TODO: Create a regex for email addresses


#TODO: Get the text off the clipboard


#TODO: Extract the email/phone from this text


#TODO: Copy the extracted email/phone to the clipboard 



