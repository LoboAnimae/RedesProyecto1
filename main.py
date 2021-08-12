import asyncio
from argparse import ArgumentParser
from os import system, name
from sys import argv
from LoggedIn import LoggedIn
from Message import Message
from xml.etree.ElementTree import parse
from Server import Server
from User import User
from Register import Register
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

system('cls') if name == 'nt' else system('clear')
argNum = len(argv)
parser = ArgumentParser()
parser.add_argument('-r', '--register', action='store_true',
                    help='Register a new user')
parser.add_argument('-jid', '--jid', help='Username', dest='jid')
parser.add_argument('-p', '--password', help='Password', dest='password')
parser.add_argument('-d', '--delete', help='Deletes a user',
                    action='store_true')
parsed_arguments = parser.parse_args()

if not parsed_arguments.jid:
    parsed_arguments.jid = input('Enter your JID: ')

if not parsed_arguments.password:
    parsed_arguments.password = input('Enter your password: ')

# Works >> Depends on server


def register(user: User):
    server = Register(user)
    server['xep_0077'].force_registration = True
    server.connect()
    server.process(forever=True)


def login(user: User):
    server = LoggedIn(user)
    server['feature_mechanisms'].unencrypted_plain = True
    server.register_plugin('xep_0030')  # Service Discovery
    server.register_plugin('xep_0004')  # Data Forms
    server.register_plugin('xep_0060')  # PubSub
    server.register_plugin('xep_0199')  # XMPP Ping
    server.register_plugin('xep_0078')
    server.connect()
    print('Trying to achieve connection to server...')
    server.process()
    server.disconnect()


def delete(user: User):
    server = LoggedIn(user, mode='delete')
    server['feature_mechanisms'].unencrypted_plain = True
    server.register_plugin('xep_0030')  # Service Discovery
    server.register_plugin('xep_0004')  # Data Forms
    server.register_plugin('xep_0060')  # PubSub
    server.register_plugin('xep_0199')  # XMPP Ping
    server.register_plugin('xep_0078')
    server.connect()
    server.process()
    server.disconnect()


if __name__ == '__main__':
    print('Hello! Welcome to the Chat Projects')
    user = User(parsed_arguments.jid, parsed_arguments.password)
    if parsed_arguments.register:
        register(user)
    elif parsed_arguments.delete:
        delete(user)
    else:
        login(user)
