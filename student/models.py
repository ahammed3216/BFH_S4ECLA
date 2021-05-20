from django.db import models
from django.conf import settings
from phone_field import PhoneField
from django.urls import reverse

class EventModel(models.Model):
    created_person=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=30)
    event_description=models.TextField()
    event_time=models.TimeField()
    event_date = models.DateField(null=True)
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    event_venue=models.CharField(max_length=15)
    event_head=models.CharField(max_length=30,blank=True,null=True)
    contact_email=models.EmailField(blank=True,null=True)
    contact_number=PhoneField(blank=True,null=True)
    event_hosted_by=models.CharField(max_length=30,blank=True,null=True)
    event_image=models.ImageField()

  

    def get_event_model_url(self):
        return reverse("model-define", kwargs={"id": self.id})

    def get_add_to_cart_url(self):
        return reverse("add-to-cart",kwargs={"id":self.id})

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart",kwargs={"id":self.id})


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

class EventRegistartion(models.Model):
    title=models.CharField(max_length=30)
    created_person=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    event_time=models.TimeField()
    event_date = models.DateField(null=True)
    event_venue=models.CharField(max_length=15)
    contact_number=PhoneField(blank=True,null=True)
    contact_email=models.EmailField(blank=True,null=True)
    event_image=models.ImageField(blank=True,null=True)
    event_head=models.CharField(max_length=30,blank=True,null=True)
    event_hosted_by=models.CharField(max_length=30,blank=True,null=True)
    total_seats=models.IntegerField()
    event_description=models.TextField(default="this is")
