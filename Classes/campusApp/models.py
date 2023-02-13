from django.db import models

# creates University Campus model
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # creates model manager
    object = models.Manager()

    # displays object output values as a string
    def __str__(self):
        display_campus = '{0.campus_name}: {0.state}'
        return display_campus.format(self)

    # removes added 's' that django adds to the model name in the broswer display
    class Meta:
        verbose_name_plural = "University Campus"