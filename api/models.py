from django.db import models

class Couple(models.Model):
    groom_name = models.CharField(max_length=100)
    bride_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.groom_name} & {self.bride_name}"

    class Meta:
        verbose_name_plural = "Couple"


class Event(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"{self.date}"
