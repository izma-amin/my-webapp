from django.db import models

class EmailDetection(models.Model):
    email_content = models.TextField()
    is_phishing = models.BooleanField(default=False)
    confidence_score = models.FloatField()

    def __str__(self):
        return f"Detection {self.id}: {'Phishing' if self.is_phishing else 'Safe'}"

class AwarenessContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
