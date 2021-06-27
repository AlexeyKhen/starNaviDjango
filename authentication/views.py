from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import serializers
from .models import UserActivity
from .serializers import UserStatisticsSerializer, UserActivitySerializer
from .utils import get_and_authenticate_user, create_user_account

User = get_user_model()


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'register': serializers.UserRegisterSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        raise ImproperlyConfigured("There is no appropriate serializer")


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_user_statistics(request):
    serialized = UserStatisticsSerializer(data=request.GET)
    if serialized.is_valid():
        username = serialized.validated_data['email']
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({'message': 'No such user'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user_activity = UserActivity.objects.filter(user=user).first()
            return Response(UserActivitySerializer(user_activity).data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'This is not a valid email'}, status=status.HTTP_400_BAD_REQUEST)
