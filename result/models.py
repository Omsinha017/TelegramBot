from django.db import models

# Create your models here.

class Total_result(models.Model):
    stupid = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    dumb = models.IntegerField(default=0)


class Individual_result(models.Model):
    user_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    stupid = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    dumb = models.IntegerField(default=0)

    def __str__(self):
        return self.name


