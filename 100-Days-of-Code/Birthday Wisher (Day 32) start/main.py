import smtplib
import datetime as dt
import random
from private_info import *

now = dt.datetime.now()
weekday = now.weekday()

# date_of_birth = dt.datetime(year=1995, month=12, day=15)

if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient_mail,
                msg=f"Subject:Hello\n\n{quote}"
            )
