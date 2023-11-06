from django.db import models

# Create your models here.


class Enquiry(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    phone = models.BigIntegerField(null=True)
    message = models.TextField(max_length=3000,null=True)
    options = (
        ("Attended", "Attended"),
        ("Not Attended", "Not Attended"),

    )
    status = models.CharField(max_length=120, choices=options, default="Not Attended")

    def __str__(self):
        return self.name