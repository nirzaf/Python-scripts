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
# some.+_thing@(\d{2,5})).com
# name part
# @ symbol
# domain name part
''', re.VERBOSE)

#TODO: Get the text off the clipboard
text = pyperclip.paste()


#TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


#Copy the extracted email/phone to the clipboard 
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)



