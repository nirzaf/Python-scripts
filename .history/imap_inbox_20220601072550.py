import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('quadrate.lk@gmail.com', 'YahmikAllah@123')
b'quadrate.lk@gmail.com authenticated (Success)'
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search('SINCE 20-Aug-2019')
rawMessage = conn.fetch(UIDs, ['BODY[]', 'FLAGS'])

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[1][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')


