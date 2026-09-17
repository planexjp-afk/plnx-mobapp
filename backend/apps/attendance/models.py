from django.db import models
from django.contrib.auth.models import User

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances')
    clock_in = models.DateTimeField(auto_now_add=True)
    clock_out = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-clock_in']

    def __str__(self):
        return f"{self.employee.username} | {self.clock_in.strftime('%Y-%m-%d %H:%M')}"