import random
import smtplib
import pandas as pd
from datetime import datetime


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "www.alkmustafa05@gmail.com"
GMAIL_PASSWORD = "YOUR-PASSWORD"

def send_email(to_address, subject, message):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(GMAIL_USER, to_address, email_message)

        print(f"Successfully sent email to {to_address}")

    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

def check_and_send_quote():
    today = datetime.today()
    print(f"Today is: {today.strftime('%A')}")
    if today.weekday() == 0:
        quotes = pd.read_csv("Quotes.csv")


        email = pd.read_csv("GmailBot.csv")
        quote = random.choice(quotes["Quote"])

        for index, row in email.iterrows():
            name = row["name"]
            email = row["email"]
            subject = "Motivation Monday"
            message = f"Assalam Alaikum {name},\nMere Methe Methe Musalman Bhai Yeh Apki Motivation ke lye.. \n{quote}"
            send_email(email, subject, message)
    else:
        print("Today is not Monday So No Quote")


if __name__ == "__main__":
    check_and_send_quote()
