from datetime import datetime
from django.utils.timezone import make_aware
from authentication.models import UserActivity


class UserActivityMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.user.is_anonymous:
            activity = UserActivity.objects.filter(user=request.user).first()
            if activity:
                activity.last_request = make_aware(datetime.now())
                activity.save()
            else:
                new_activity = UserActivity(user=request.user, last_request=datetime.now())
                new_activity.save()
        return response
