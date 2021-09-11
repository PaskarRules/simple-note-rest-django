from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import IpAddress
from .serializers import IpAddressesSerializer


class UserRequestsView(ListAPIView):
    queryset = IpAddress.objects.all()
    serializer_class = IpAddressesSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        allowed_ips = IpAddress.objects.all().values_list('ip_address', flat=True)

        user_ip = request.META['REMOTE_ADDR']
        if user_ip in allowed_ips:
            user_requests = IpAddress.objects.\
                filter(ip_address=user_ip).\
                values('ip_address', 'pub_date'). \
                order_by('-pub_date')

            return Response(user_requests)

