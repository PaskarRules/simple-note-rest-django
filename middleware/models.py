from django.db import models

from user_management.models import User


class IpAddress(models.Model):
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()
    method = models.CharField(max_length=50)
    url = models.URLField()

    class Meta:
        db_table = "ip_addresses"


class UserIps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.ForeignKey(IpAddress, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_ip_d"
