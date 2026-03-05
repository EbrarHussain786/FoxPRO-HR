from django.db import models


class Recruitment(models.Model):
    job_title = models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(max_length=40, default='open')
    posted_at = models.DateTimeField(auto_now_add=True)


class Candidate(models.Model):
    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    interview_date = models.DateField(null=True, blank=True)
    evaluation = models.TextField(blank=True)
    hiring_decision = models.CharField(max_length=30, blank=True)
