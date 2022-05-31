from mailjet_rest import Client
import os

api_key = "13c93d7db00375555358e49376a10ce9"

api_secret = "792caf443ea60728fb8273ba06ccd0f9"

mailjet = Client(auth=(api_key, api_secret), version='v3.1')

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

          "Name": "You"

        }

      ],

      "Subject": "My first Mailjet Email!",

      "TextPart": "Greetings from Mailjet!",

      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"

    }

  ]

}

print (mailjet.send.create(data=data)).status_code
print (mailjet.send.create(data=data)).json()



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