from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    uid = models.IntegerField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    emilid = models.EmailField()
    usercontact = models.IntegerField(max_length=10)

    class Meta:
        db_table = "userdetails"
