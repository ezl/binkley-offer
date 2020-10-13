from types import SimpleNamespace

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from ..exceptions.custom_exceptions import DuplicateEntityException
from ..models import UserProfile

from rest_framework.exceptions import NotFound
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from rest_framework import exceptions

from cryptography.fernet import Fernet
import uuid

key = b'1hRIU-349FvJ742AUvdbbuVq2KPuEMTVtfOrVGeBKSM='  # TODO put in local.env
cipher_suite = Fernet(key)


def create_user(user_request):
    user_request = SimpleNamespace(**user_request)

    duplicate_user = UserProfile.objects.filter(email=user_request.email).first()

    if duplicate_user:
        raise DuplicateEntityException(class_name=UserProfile.__name__)

    user_uid = str(uuid.uuid4())
    password = encrypt_password(user_request.password)
    User.objects.create(username=user_request.email, password=password)
    user = User.objects.filter(username=user_request.email).first()
    UserProfile.objects.create(
        user=user,
        username=user_request.username,
        password=password,
        email=user_request.email,
        user_uid=user_uid)

    user_profile = UserProfile.objects.filter(user_uid=user_uid).first()
    return {
        'user_uid': user_profile.user_uid,
        'username': user_profile.username,
        'email': user_profile.email,
        'data_joined': user_profile.data_joined,
        'is_confirmed': user_profile.is_confirmed
    }


def login_user(user_request):
    user_request = SimpleNamespace(**user_request)

    user_profile = UserProfile.objects.filter(email=user_request.email).first()
    user = User.objects.filter(username=user_request.email, password=user_profile.password).first()

    if not user_profile and not user and decrypt_password(user_profile.password) != user_request.password:
        raise NotFound(detail='User not found')

    token_list = Token.objects.filter(user=user)
    if token_list:
        new_key = token_list[0].generate_key()
        token_list.update(key=new_key)
    else:
        Token.objects.create(user=user)
    return {
        'user_uid': user_profile.user_uid,
        'username': user_profile.username,
        'email': user_profile.email,
        'data_joined': user_profile.data_joined,
        'is_confirmed': user_profile.is_confirmed,
        'token': Token.objects.filter(user=user).first().key
    }


def encrypt_password(password):
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    return encrypted_password.decode('utf-8')


def decrypt_password(encrypted_password):
    password = cipher_suite.decrypt(encrypted_password.encode('utf-8'))
    return password.decode('utf-8')
