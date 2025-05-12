# docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev
from email.message import EmailMessage  # пакет email модуль message
import smtplib  # модуль
# с помощью smtplib мы будет отправлять имэйл сконструированный классом EmailMessage

my_email = EmailMessage()  # новый экземпляр класса
# с помощью EmailMessage мы будем конструировать имэйл

my_email['from'] = 'Vika'
my_email['to'] = 'test@gmail.com'
my_email['subject'] = 'Hello from Python'
my_email.set_content('Hey! How are you doing?')

# порт указываем тот на котором у нас открыт докер
with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()  # ehlo - метод который устранавливает связь с smtp сервером
    # smtp_server.starttls()  # передача данных в зашифрованном виде
    # smtp_server.login('username', 'password')  # для авторизации
    smtp_server.send_message(my_email)
    print('email was sent!')
