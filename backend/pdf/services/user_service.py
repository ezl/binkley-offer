from types import SimpleNamespace

from ..models import PersistentUserChoice
from ..serializers import UserPreferencesSerializer

from django.contrib.auth.models import User
from rest_framework.exceptions import ParseError

def create_user_persistent_choices(choices_request, user: User):    
    persistent_user_choices, created = PersistentUserChoice.objects.get_or_create(user=user)

    for key, value in choices_request.items():
        if value:
            setattr(persistent_user_choices, key, value)

    persistent_user_choices.save()
    
