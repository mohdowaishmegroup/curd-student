from django.db import models
from django.utils import timezone

class TimeStamp(models.Model):
    """ Base class containg all models"""
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def soft_delete(self):
        self.is_deleted=True
        self.deleted_at=timezone.now()
        self.save()

    class Meta:
        " define model as abstract class"
        abstract=True

class Teacher(TimeStamp):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    Fathr_name=models.CharField(max_length=225)
    House_no=models.CharField(max_length=225)
    Qualification=models.CharField(max_length=225)
    skills=models.CharField(max_length=225)
    emailid=models.EmailField()
    salary=models.IntegerField()

    def save(self,**kwargs):
        super(Teacher, self).save()

    class Meta:
        db_table='teacher'





# Create your models here.
