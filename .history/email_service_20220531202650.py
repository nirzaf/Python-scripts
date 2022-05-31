import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('quadrate.lk@gmail.com', '4Chy6Q^)G.SUy49')
conn.sendmail(from_addr, to_addrs, msg)