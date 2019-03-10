import smtplib
from email.mime.text import MIMEText


def send_mail(email, data):
    from_email = "######################################"
    from_password = "####################################"
    to_email = email

    subject = "Webcrawl from ANONSE"

    message = "Dzień dobry!<br><br>Twoja dzienna porcja ogłoszeń z portalu anonse.com:<br><br>"\
              + data + "<br><br>Do zobaczenia :-)<br><br><br><br>" \
                       "UWAGA! Jeśli nie chcesz dłużej otrzymywać naszych powiadomień - odwiedź www.xxxxxxxxx i odwołaj subskrypcję."

    msg = MIMEText(message, 'html')

    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)