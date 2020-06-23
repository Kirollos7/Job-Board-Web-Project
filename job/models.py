from django.db import models

# Create your models here.

'''
Django Models Fields

- html widget
- validation
- database Size

'''

# Table
class Job(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    JOB_TYPE = (
    ('P', 'Part Time'),
    ('F', 'Full Time'),
    ('I', 'Internship'),
    )
    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=70, help_text='Enter Job Name', null=True)
    # location
    description = models.TextField(max_length=1000,null=True,help_text='Enter Job Description')
    job_type = models.CharField(max_length=1, choices=JOB_TYPE,help_text='Choice Type of Job')
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1,null=True)
    salary = models.IntegerField(null=True,default=0)
    experience = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title
    
    
    
    
    
    
    
