from django.db.models import F
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserRegistrationSerializer
from .serializers import UserLoginSerializer

from .models import User
from middleware.models import UserIps


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User registered  successfully',
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


class UserActivityView(RetrieveAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (IsAdminUser,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request, *args, **kwargs):
        result = UserIps.objects.\
            filter(user_id=kwargs['pk']).\
            prefetch_related('ip_addresses'). \
            annotate(request_last_date=F('ip__pub_date'), last_login=F('user__last_login')).\
            values("request_last_date", "last_login").\
            latest("request_last_date")

        return Response(result)
