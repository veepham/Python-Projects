from django.db import models


# Create your model for University Campus
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # Create model manager
    object = models.Manager()

    # display of object output as string
    def __str__(self):
        display_campus = '{0.campus_id}: {0.campus_name}'
        return display_campus.format(self)

    # class Meta to display model name without appended 's'
    class Meta:
        verbose_name_plural = 'University Campus'
