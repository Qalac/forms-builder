from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add/$', add, name='add'),
    url(r'^add/submit/$', submit, name='submit'),
    url(r'^add/submit/display/$', test, name='test'),
    url(r'^edit/survey/(?P<survey_id>\d+)/$', EditSurvey.as_view(), name='edit_survey'),
    url(r'^edit/field/(?P<field_id>\d+)/$', EditField.as_view(), name='edit_field')
]

