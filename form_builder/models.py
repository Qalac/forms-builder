from django.db import models

MC = 'MC'
SC = 'SC'
TX = 'TX'

CHOICES = (
    ('MC', 'Multiple Choice'),
    ('SC', 'Single Choice'),
    ('TX', 'Text')
)

TEXT = 'TEXT'
SELECT_LIST = 'SELECT_LIST'
CHECK_BOX = 'CHECK_BOX'
RADIO_BUTTON = 'RADIO_BUTTON'

WIDGETS = (
    ('TEXT', 'Text'),
    ('SELECT_LIST', 'Select_list'),
    ('CHECK_BOX', 'Check_box'),
    ('RADIO_BUTTON', 'Radio_button'),
)

# -------------------------------------------------------------------------------------------------------------

class survey(models.Model):
    survey_title = models.CharField(max_length=22, verbose_name='survey Title', null=False, default=None,
    blank=False, unique=True)
    objects = models.Manager

    class Meta:
        ordering = ['survey_title']

    def __str__(self):
        return self.survey_title

class field(models.Model):
    survey = models.ForeignKey(survey, on_delete=models.CASCADE, default=None)
    question_type = models.CharField(choices=CHOICES, max_length=23, default=None, blank=False)
    widget = models.CharField(choices=WIDGETS, max_length=23, default=None, blank=False)
    question_text = models.CharField(max_length=22)
    objects = models.Manager

    class Meta:
        ordering = ['question_text', 'survey']
    
    def __str__(self):
        return self.question_text



