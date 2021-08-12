import re


class User:
    def __init__(self, username, password):
        self._jid = username
        self._password = password

    @property
    def jid(self):
        return self._jid or None

    @jid.setter
    def jid(self, username: str):
        if not username:
            raise ValueError("Username cannot be empty")
        if len(username) > 20:
            raise ValueError("Username cannot be longer than 20 characters")
        if not username.isalnum():
            raise ValueError("Username can only contain letters and numbers")
        if username[0] == ' ' or re.match(username, '^[0-9]') is not None:
            raise ValueError("Username cannot start with a space or a number")
        if '@' not in username:
            username += '@alumchat.xyz'
        if username[-1] == '@':
            username += 'alumchat.xyz'
        self._jid = username
        return self._jid

    @property
    def password(self):
        return self._password or None

    @password.setter
    def password(self, password: str):
        if not password:
            raise ValueError("Password cannot be empty")
        if len(password) > 20:
            raise ValueError("Password cannot be longer than 20 characters")
        if not password.isalnum():
            raise ValueError("Password can only contain letters and numbers")
        if password[0] == ' ' or re.match(password, '^[0-9]') is not None:
            raise ValueError("Password cannot start with a space or a number")
        self._password = password
        return self._password

    @property
    def auth(self):
        return (self._jid, self._password)

    @auth.setter
    def auth(self):
        pass
