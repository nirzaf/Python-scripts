import smtplib


#try catch block


conn = smtplib.SMTP('in-v3.mailjet.com', 587)
conn.ehlo()
conn.starttls()
conn.login('quadrate.lk@gmail.com', '4Chy6Q^)G.SUy49')
conn.sendmail("quadrate.lk@gmail.com", "mfmfazrin1986@gmail.com", 'Subject: Test...... \n\n This is a sample email')
conn.quit()