from mailjet_rest import Client

api_key = "037e5d87d179e6bfdf0ba7b5c8a979bc"

api_secret = "fe26f25639812684059fd12839a10d05"

mailJet = Client(auth=(api_key, api_secret), version='v3.1')

data = {
    'Messages': [
        {
            "From": {
                "Email": "quadrate.lk@gmail.com",
                "Name": "Quadrate Tech Solutions"
            },

            "To": [
                {
                    "Email": "mfmfazrin1986@gmail.com",
                    "Name": "Fazrin"
                }
            ],
            "CC": [
                
            ]
            "Subject": "My first Mailjet Email!",
            "TextPart": "Greetings from Mailjet!",
            "HTMLPart": "<h3>Dear Fazrin, welcome to <a href=\"quadrate.lk\">Mailjet</a>!</h3><br/><p style=\"color:red\"> May Allah's peace be with you!"
        }
    ]
}

res = mailJet.send.create(data=data)
print(res.status_code)
print(res.json())


# #try catch block

# try:

#     conn = smtplib.SMTP('in-v3.mailjet.com', 587)

#     conn.ehlo()

#     conn.starttls()

#     conn.login('quadrate.lk@gmail.com', '4Chy6Q^)G.SUy49')

#     conn.sendmail("quadrate.lk@gmail.com", "mfmfazrin1986@gmail.com", 'Subject: Test...... \n\n This is a sample email')

#     conn.quit()

#     print("Success: Email sent!")

# except:

#     print("Email failed to send.")
