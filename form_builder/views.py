from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from .models import survey, field


def index(request):
    template_name = 'origin.html'
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('add/')
    else:
        form = SurveyForm()
    return render(request, template_name, {'form': SurveyForm })


def add(request):
    template_name = 'create.html'
    if request.method == 'POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('submit/')
    else:
        form = FieldForm()
    return render(request, template_name, {'form': form})

def submit(request):
    template_name = 'submit.html'
    if request.method == 'POST':
        return HttpResponseRedirect('display/')
    return render(request, template_name)

def test(request):
    template_name = 'test.html'
    querySurvey = survey.objects.all()
    queryField = field.objects.values()
    return render(request, template_name, {'survey': querySurvey, 'field': queryField })

