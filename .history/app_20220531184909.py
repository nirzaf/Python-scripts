#! python3

import re, pyperclip

#TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345 

    (((\d\d\d)|(\(\d\d\d)))?    # area code (optional)
   \s| # first separator
    # first 3 digits
    # separator
    # last 4 digits
    # extension (optional)

''', re.VERBOSE)

#TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5})).com
# name part
# @


#TODO: Get the text off the clipboard


#TODO: Extract the email/phone from this text


#TODO: Copy the extracted email/phone to the clipboard 



