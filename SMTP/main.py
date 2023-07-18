import datetime as dt
import random
import smtplib

EMAIL = "pruebascodigo0@gmail.com"
PWD = "gobkowgsovaehans"
now = dt.datetime.now()
weekday = now.weekday()

try:
    with open("quotes.txt") as f:
        motivations = f.readlines()
        to_send_motivation = random.choice(motivations).strip()
except FileNotFoundError:
    print("File does not exist")

else:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PWD)
        if weekday == 2:
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="pruebaspython@yahoo.com",
                msg=f"Subject:Monday motivation \n\n {to_send_motivation}"
            )
            print("Sent message successfully")

        else:
            print("Nothing was sent")
