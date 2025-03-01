import smtplib
import os
import random
import datetime as dt

from dotenv import load_dotenv
load_dotenv()

my_email = "parinnagda@gmail.com"
password = os.getenv("SMTP_PASSWORD")

today = dt.datetime.now().weekday()
if today == 5:
    with open("quotes.txt") as data_file:
        all_quotes = data_file.readlines()
        quote = random.choice(all_quotes)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="parinnagda.pn@gmail.com",
                msg=f"Subject:Hello\n\n {quote}"
            )






