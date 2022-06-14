import smtplib
import ssl
import sys

from arguments_parser import USAGE
from arguments_manager import ArgumentsManager


def send_mail(login, password, mail_to, topic, content):
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(login, password)
        content = 'Subject:{}\n\n{}'.format(topic, content)
        server.sendmail(login, mail_to, content)


if __name__ == '__main__':
    args = sys.argv[1:]

    if not args:
        raise SystemExit(USAGE)

    cmd_manager = ArgumentsManager(args)
    result = cmd_manager.handle_args()
    print(result)
    if result is not None:
        send_mail(result['login'], result['password'], result['mail_to'], result['topic'], result['content'])
