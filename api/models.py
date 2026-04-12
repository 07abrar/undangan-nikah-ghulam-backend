from django.db import models


class Couple(models.Model):
    # Short name
    groom_name = models.CharField(max_length=20)
    bride_name = models.CharField(max_length=20)

    # Full name
    groom_full_name = models.CharField(max_length=200)
    bride_full_name = models.CharField(max_length=200)

    # Parent's name
    groom_father_name = models.CharField(max_length=200)
    groom_mother_name = models.CharField(max_length=200)
    bride_father_name = models.CharField(max_length=200)
    bride_mother_name = models.CharField(max_length=200)

    # Media social
    groom_linkedin = models.URLField(blank=True)

    # Quote
    opening_quote = models.TextField(blank=True)
    opening_quote_source = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.groom_name} & {self.bride_name}"

    class Meta:
        verbose_name_plural = "Couple"


class Event(models.Model):
    couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name="events")
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    location_name = models.CharField(max_length=200)
    location_address = models.TextField(blank=True)
    maps_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.location_name} - {self.date}"


class Story(models.Model):

    couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name="stories")
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.title} - {self.date}"


class RSVP(models.Model):
    class AttendanceStatus(models.TextChoices):
        ATTENDING = "hadir", "Hadir"
        NOT_ATTENDING = "tidak_hadir", "Tidak Hadir"

    couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name="rsvps")
    name = models.CharField(max_length=200)
    attendance = models.CharField(max_length=20, choices=AttendanceStatus.choices)

    # Number of guests
    guests = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.attendance}"

    class Meta:
        verbose_name = "RSVP"


class Wish(models.Model):
    couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name="wishes")
    name = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.message[:30]}..."
