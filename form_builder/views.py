from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import survey, field
from django.views.generic import UpdateView, CreateView, View
from django.urls import reverse_lazy


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
    widget = TypeForm()
    return render(request, template_name, {'survey': querySurvey, 'field': queryField, 'widget': widget })

class EditSurvey(UpdateView):
    model = survey
    fields = '__all__'
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'survey_id'
    context_object_name = 'survey'
    success_url = reverse_lazy('test')

class EditField(UpdateView):
    model = field
    fields = '__all__'
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'field_id'
    context_object_name = 'field'
    success_url = reverse_lazy('test')
