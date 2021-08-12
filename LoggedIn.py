from User import User
from slixmpp import ClientXMPP
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')


class LoggedIn(ClientXMPP):
    def __init__(self, user: User, mode=None) -> None:
        ClientXMPP.__init__(self, user.jid, user.password)

        # Add event handlers
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.message)
        self.add_event_handler('presence_subscribed', self.subscribed)

        self.add_event_handler('disconnected', self.disconnected)

        self.add_event_handler('error', self.error)
        self.add_event_handler('failed_auth', self.failed_auth)
        self.add_event_handler('connected', self.connected)
        self.add_event_handler('got_online', self.notify_lone_online)
        self.add_event_handler('got_offline', self.notify_lone_offline)
        self.add_event_handler('groupchat_message', self.groupchat_message)
        self.add_event_handler('groupchat_presence', self.groupchat_presence)

        self.delete = mode == 'delete'

    def connected(self):
        print('You have been connected to the network.')

    def disconnected(self):
        print('You have been disconnected to the network.')

    def groupchat_message(self, message):
        pfrom = message['from']
        body = message['body']
        print(f'NEW GROUPCHAT MESSAGE\n\t- {pfrom}: {body}')

    def groupchat_presence(self, data):
        show = data['show']
        status = data['status']
        pfrom = data['from']
        print(f'GC: [{show} - {status}] {pfrom} is now online!')

    def notify_lone_online(self, data):
        show = data['show']
        status = data['status']
        pfrom = data['from']
        print(f'[{show} - {status}] {pfrom} is now online!')

    def notify_lone_offline(self, data):
        show = data['show']
        status = data['status']
        pfrom = data['from']
        print(f'[{show} - {status}] {pfrom} is now offline.')

    async def change_presence(self, new_presence='away', status_message='', nickname=''):
        if not nickname:
            nickname = self.boundjid.user
        self.send_presence(pshow=new_presence,
                           pstatus=status_message, pnick=nickname)

    async def start(self, event):
        print('Session started. Attempting to send presence.')
        self.send_presence()
        await self.get_roster()
        print('Presence sent. Roster gotten.')

        if self.delete:
            print('Deleting...')
            await self.delete_account()
        else:
            print('You can now try all the event-based features!')

    def send_new_message(self, receiver, str_message):
        self.send_message(mto=receiver, mbody=str_message, mtype='chat')

    def message(self, msg):
        print('New message received!')
        name_and_host, _ = str(msg['from']).split('/')
        name, host = name_and_host.split('@')
        if msg['type'] in ('chat', 'normal'):
            print(f"(To you) {name}: {msg['body']}")
        elif msg['type'] in ('groupchat', 'normal'):
            print(f"({host}) {name}: {msg['body']}")

        if input('Would you like to reply?') in ['y', 'Y']:
            self.send_new_message(msg['from'], input('Your message: '))

    def subscribed(self, presence):
        print('User subscribed: ' + presence['from'])

    def subscribe(self, show, status):
        self.send_presence(pstatus=status, pshow=show)

    def send_subscription(self, jid):
        self.send_presence_subscription(
            pto=jid, pfrom=self.boundjid.bare, ptype='subscribe')
        self.get_roster()

    def error(self):
        logging.error('There has been an error. Program will close')
        self.disconnect()

    def failed_auth(self):
        pass

    async def show_single_user(self, jid):
        user = self.client_roster[jid]
        name = user['name']
        subscription = user['subscription']
        print(f'{name}\t{jid}\t{subscription}\n')

    async def get_all_users(self):
        print('Members')
        for roster in self.boundjid.bare:
            print(roster)
        print('Groups')
        groups = self.client_roster.groups()
        for group in groups:
            print(f'{group}\n')
            for user in groups[group]:
                st = self.client_roster[user]['subscription']
                name = self.client_roster[user]['name']
                if name:
                    print(f'{name}\t{user}\t{st}\n')
                else:
                    print(f'{user}\t{st}\n')
                connections = self.client_roster.presence(user)
                for i, j in connections.items():
                    stat = j['show'] or 'available'
                    print(f'{i}\t{stat}\t{j["status"]}\n')
