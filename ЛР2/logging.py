import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send(log):
    # Аутлук кинул мне перманетный бан после отправки 4 сообщений, так что создай новый аккаунт где-нибудь 
    addr_from = "kafisbot@outlook.com"
    addr_to = "kafisbot@outlook.com"
    password = "KafIS2020"    

    html = f"""\
    <html>
    <head></head>
    <body>
        <p>
        Слава Украине
        </p>
        {log}
    </body>
    </html>"""

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = 'Тема сообщения'

    msg.attach(MIMEText(html, 'html', 'UTF-8'))

    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.set_debuglevel(True)
    server.starttls()
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()
