from User import User
from slixmpp import ClientXMPP
import logging
import slixmpp.exceptions as exceptions


class Register(ClientXMPP):
    def __init__(self, user: User):
        ClientXMPP.__init__(self, user.jid, user.password)
        self.add_event_handler("register", self.register)
        self.add_event_handler('connected', self.connected)
        self.register_plugin('xep_0030')  # Service Discovery
        self.register_plugin('xep_0004')  # Data forms
        self.register_plugin('xep_0066')  # Out-of-band Data
        self.register_plugin('xep_0077')  # In-band Registration
        self.register_plugin('xep_0045')  # Groupchat
        self.register_plugin('xep_0199')  # XMPP Ping

    async def register(self, iq):
        print('Initializing registration...')
        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password

        try:
            await resp.send()
            print("Registered with server")
        except exceptions.IqError as e:
            print(f"Failed to register with server: {e}")
        except exceptions.IqTimeout:
            print("No response from server.")
        finally:
            self.disconnect()
            exit()

    def connected(self, data):
        print('Connected to server, attempting to register...')
