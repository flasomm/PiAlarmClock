from __future__ import print_function
import httplib2
import os
import datetime

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


class Google:
    SCOPES = [
        'https://www.googleapis.com/auth/gmail.readonly',
        'https://www.googleapis.com/auth/calendar.readonly'
    ]
    CLIENT_SECRET_FILE = 'client_secret_322051245517-ceifrljp5nrq06ctdrh2toggucb3pknf.apps.googleusercontent.com.json'
    APPLICATION_NAME = 'RaspberryClock'

    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'google-raspberry-calendar.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(
                os.path.dirname(os.path.realpath(__file__)) + "/" + self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            credentials = tools.run_flow(flow, store)
        return credentials

    def mail_unread(self):
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)
        results = service.users().labels().get(userId='me', id='INBOX').execute()
        return "Vous avez %s emails non lus.".format(results['messagesUnread'])

    def calendar_events(self):
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        eventsResult = service.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])
        res = "Vos rendez-vous aujourd'hui."
        for event in events:
            print(event["Name"])
        print(events)
