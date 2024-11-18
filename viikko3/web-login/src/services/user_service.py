from entities.user import User
import string
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        chars = string.ascii_lowercase
        
        username_ok = True
        password_ok = True
        password_chars_ok = False
        password_other_ok = False
        
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if len(username) < 3:
            raise UserInputError("Username is too short")
        
        if len(password) < 8:
            raise UserInputError("Password is too short")
        
        for c in username:
            if c not in chars:
                username_ok = False
                break

        for c in password:
            if c in chars:
                password_chars_ok = True
            else:
                password_other_ok = True

        if not password_chars_ok or not password_other_ok:
            password_ok = False
        
        if not username_ok and password_ok:
            raise UserInputError("Username is invalid")
        
        if username_ok and not password_ok:
            raise UserInputError("Password is invalid")
        
        if username_ok and password_ok:
            if password != password_confirmation:
                raise UserInputError("Password and password confirmation don't match")

        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already exists")
        
        return
        
        
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


user_service = UserService()
