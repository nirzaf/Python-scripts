import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login()
b'quadrate.lk@gmail.com authenticated (Success)'
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search('SINCE 20-Aug-2019')
rawMessage = conn.fetch(UIDs, ['BODY[]', 'FLAGS'])

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[1][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.text_part
message.html_part
message.text_part.get_payload().decode('utf-8')
message.html_part.get_payload().decode('utf-8')



