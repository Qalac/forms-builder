from django.db import models

class survey(models.Model):
    survey_title = models.CharField(max_length=22, verbose_name='survey Title', null=False, default=None,
    blank=False, unique=True)
    objects = models.Manager

    def __str__(self):
        return self.survey_title

class field(models.Model):
    survey = models.ForeignKey(survey, on_delete=models.CASCADE, default=None)
    question_text = models.CharField(max_length=22)
    objects = models.Manager
    
    def __str__(self):
        return self.question_text



