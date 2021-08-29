##################### Extra Hard Starting Project ######################

import pandas
import datetime as dt
import smtplib
import random
from private_info import *


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

birthday_data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
this_month = now.month
this_day = now.day

match_data = birthday_data[birthday_data.month ==
                           this_month][birthday_data.day == this_day].to_dict(orient="records")

# another way to address csv data
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (
#     index, data_row) in birthday_data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

for person in match_data:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        mail_to_send = file.read().replace(
            "[NAME]", person["name"]).replace("Angela", "Arsene")

# 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday\n\n{mail_to_send}"
        )
