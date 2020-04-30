from email.mime.text import MIMEText
import smtplib

def send_email(email, bday, age):
    from_email = "ranjankk01@gmail.com"
    from_password = "ranjankk00"
    to_email = email

    subject = "Your accurate age!"
    message = "Hey there, you birthday is <strong>%s</strong>. You are %s days old" %(bday, age)

    msg = MIMEText(message,"html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)