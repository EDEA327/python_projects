import smtplib

email = "pruebascodigo0@gmail.com"
password = "gobkowgsovaehans"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs="pruebaspython@yahoo.com",
                    msg="Subject:Este es un mensaje de prueba\n\n Soy un mensaje")

connection.close()
