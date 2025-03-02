##################### Extra Hard Starting Project ######################
from calendar import month
from email.contentmanager import raw_data_manager

import pandas
import datetime as dt
import random
import smtplib
import os, dotenv

from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("SENDER_EMAIL")
my_password = os.getenv("SMTP_PASSWORD")
from pyexpat.errors import messages

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

data_val = data.to_dict(orient="records")
value = [item for item in data_val if item['month'] == current_month and item['day'] == current_day]
for item in value:
    letter_val = random.choice(range(1,3))
    with open(f"letter_templates/letter_{letter_val}.txt") as letter:
        message = letter.read()
        message = message.replace("[NAME]",item['name'])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{item['email']}",
                msg=f"Subject:Happy Birthday!\n\n {message}"
            )
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




