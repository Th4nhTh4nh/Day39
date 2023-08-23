import smtplib

MY_EMAIL = "phamdatthanh213@gmail.com"
MY_PASSWORD = "iaojfqjfdmylcdtn"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_email(self, massage):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Low price alert!\n\n{massage}".encode("utf-8"),
            )
