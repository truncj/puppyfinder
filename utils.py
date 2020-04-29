import json
import smtplib

import requests


def read_json(name, message=''):
    file = open(f'config/{name}.json', mode='r')
    data = json.load(file)
    file.close()
    print(f'reading {name} {message}')
    return data


def rebrandly_maker(long_url):
    creds = read_json('creds', 'rebrandly')

    payload = {
        "destination": long_url,
        "domain": {"fullName": "rebrand.ly"}
    }

    headers = {
        "Content-type": "application/json",
        "apikey": creds['rebrandly_token'],
        "workspace": creds['rebrandly_workspace']
    }

    r = requests.post("https://api.rebrandly.com/v1/links",
                      data=json.dumps(payload),
                      headers=headers)

    if r.status_code == requests.codes.ok:
        link = r.json()
        short_url = link["shortUrl"]
        return short_url


def send_message(subject, message):
    conf = read_json('config', 'email')
    sender_user = conf['sender_user']
    sender_pass = conf['sender_pass']
    recipients = conf['recipients']

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    for recipient in recipients:
        FROM = sender_user
        TO = recipient
        SUBJECT = f'[New Puppy Alert] {subject}'
        TEXT = message
        MESSAGE = f'From: {FROM}\nTo: {TO}\nSubject: {SUBJECT}\n\n{TEXT}'

        server.login(sender_user, sender_pass)
        server.sendmail(FROM, TO, MESSAGE)
