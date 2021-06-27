from datetime import datetime

from django.contrib.auth import authenticate, get_user_model
from django.utils.timezone import make_aware
from rest_framework import serializers

from authentication.models import UserActivity


def set_user_enter(user):
    activity = UserActivity.objects.filter(user=user).first()
    if activity:
        activity.last_login = make_aware(datetime.now())
        activity.save()
    else:
        new_activity = UserActivity(user=user, last_login=make_aware(datetime.now()))
        new_activity.save()


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    set_user_enter(user)
    return user


def create_user_account(email, password, first_name="",
                        last_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        username=email, email=email, password=password, first_name=first_name,
        last_name=last_name, **extra_fields)
    authenticate(username=email, password=password)
    set_user_enter(user)
    return user
