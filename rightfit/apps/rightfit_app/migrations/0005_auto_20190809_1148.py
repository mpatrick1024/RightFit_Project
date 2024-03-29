# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-09 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rightfit_app', '0004_auto_20190807_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('test_score', models.IntegerField()),
                ('school_int', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activities', models.ManyToManyField(related_name='students', to='rightfit_app.Activity')),
                ('majors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='rightfit_app.Major')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='rightfit_app.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.RemoveField(
            model_name='school',
            name='sports',
        ),
        migrations.AddField(
            model_name='school',
            name='activities',
            field=models.ManyToManyField(related_name='schools', to='rightfit_app.Activity'),
        ),
        migrations.AddField(
            model_name='school',
            name='majors',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='rightfit_app.Major'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='students',
            field=models.ManyToManyField(related_name='schools', to='rightfit_app.Student'),
        ),
    ]
