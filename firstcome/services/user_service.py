from typing import Optional

from data.user import User


def get_users():
    return User.objects().order_by('-created_date').only('name', 'email').all()


def get_users_count():
    return User.objects().count()


def find_user_by_email(email: str) -> Optional[User]:
    return User.objects().filter(email=email).first()


def create_user(name: str, email: str) -> Optional[User]:
    if find_user_by_email(email):
        return None

    user = User()

    user.name = name
    user.email = email

    user.save()

    return user