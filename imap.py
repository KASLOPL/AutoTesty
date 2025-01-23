from imap_tools import MailBox
from Data import data

with MailBox('imap.fastmail.com').login(data("email"), data("imap_password"), "Inbox") as mb:
    for msg in mb.fetch(limit=1, reverse=True, mark_seen=True):
        mail = msg.html
        print(mail[10683:10689])
