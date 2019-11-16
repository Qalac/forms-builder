from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add/$', add, name='add'),
    url(r'^add/submit/$', submit, name='submit'),
    url(r'^add/submit/display/$', test, name='test')
]

