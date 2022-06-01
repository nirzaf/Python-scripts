import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('quadrate.lk@gmail.com', 'YahmikAllah@123')
b'quadrate.lk@gmail.com authenticated (Success)'
conn.select_folder('INBOX', readonly=True)
conn.search('SINCE 20-Aug')
UIDs = conn.search(['ALL'])
