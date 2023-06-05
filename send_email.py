import smtplib
email="suresh.n@cmr.edu.in"
password="8179203374"
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=email,password=password)
list1=["sureshrohitn@gmail.com","sureshktd92@gmail.com"]
connection.sendmail(from_addr=email,to_addrs=list1, msg="Welcome to the python mailling")
connection.close()
print("mail Sent")
