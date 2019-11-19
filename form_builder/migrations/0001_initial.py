# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-19 11:58
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('MC', 'Multiple Choice'), ('SC', 'Single Choice'), ('TX', 'Text')], default=None, max_length=23)),
                ('option', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, default=None, max_length=23), size=None)),
                ('question_text', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_title', models.CharField(default=None, max_length=22, unique=True, verbose_name='survey Title')),
            ],
        ),
        migrations.AddField(
            model_name='field',
            name='survey',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='form_builder.survey'),
        ),
    ]
