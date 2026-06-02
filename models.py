from django.db import models

# Create your models here.
class Resignation(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    reason = models.CharField(max_length=200)
    project = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    people_lead = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.employee_name} - {self.employee_id}"
