from User import User
import logging
from slixmpp import ClientXMPP

import slixmpp


class Server(ClientXMPP):
    def __init__(self, user: User) -> None:

        ClientXMPP.__init__(self, user.jid, user.password)
        self.add_event_handler("session_start", self.start)
        self.logging = logging

    async def start(self, event):
        self.send_presence()
        await self.get_roster()

    def login(self, User: User) -> bool:
        resp = self.Iq()

    def __repr__(self) -> str:
        return f'Server with values {self.ip}:{self.port}'
