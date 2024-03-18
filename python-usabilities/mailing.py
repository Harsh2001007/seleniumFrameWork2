import smtplib
import mailtrap as mt

sender = "hs5686584@gmail.com"
receiver = ["hs5686584@gmail.com"]
message = "this is smtp message"

try:
    smtpObj = smtplib.SMTP("localhost")
    smtpObj.sendmail(sender, receiver, message)
    print("successfully sent")

except Exception:
    print("i am an exception")


# createing mail object
mail = mt.Mail(
    sender=mt.Address(email="mailtrap@example.com", name="dretrix"),
    to=[mt.Address(email="hs5686584@gmail.com")],
    subject="you are awesome",
    text="i am from mailtrap",
)

client = mt.MailtrapClient(token="b10acf5818aec6da039dfbe0deb03ebb")
client.send(mail)
