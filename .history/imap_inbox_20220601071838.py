import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('quadrate.lk@g