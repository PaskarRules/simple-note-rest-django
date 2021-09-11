from django.db.models import Count
from django.db.models.functions import TruncDay

from django.http import HttpResponse

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from user_todo.models import Like
from user_todo.serializers import LikeSerializer


class LikeInfo(RetrieveAPIView):
    serializer_class = LikeSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        start = request.GET.get("date_from")
        finish = request.GET.get("date_to")

        like_count = list(Like.objects. \
                          filter(date_created__range=[start, finish]). \
                          annotate(day=TruncDay('date_created')). \
                          values("day"). \
                          annotate(amount=Count("id")). \
                          values("day", "amount"))

        return HttpResponse(like_count)
