from django.db import models
from django.conf import settings

class EventModel(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    date = models.DateTimeField(null=True)
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    venue=models.CharField(max_length=15)

    def __str__(self):
        return self.title

class OrderEvent(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    events=models.ForeignKey(EventModel,on_delete=models.CASCADE)
    booked=models.BooleanField(default=False)

    def __str__(self):
        return f" {self.user.username} in {self.events.title}"


class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    events=models.ManyToManyField(OrderEvent)
    start_date = models.DateTimeField(auto_now_add=True,null=True)
    ref_code=models.CharField(max_length=30)

class Profile(models.Model):
     user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)  
     event=models.ManyToManyField(OrderEvent)