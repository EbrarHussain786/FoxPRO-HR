from django.db import models


class ReportLog(models.Model):
    report_name = models.CharField(max_length=120)
    generated_by = models.CharField(max_length=120)
    generated_at = models.DateTimeField(auto_now_add=True)
    filters_json = models.JSONField(default=dict, blank=True)
