# Generated by Django 3.1.5 on 2021-01-29 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, null=True)),
                ('birth_date', models.DateField()),
                ('years_of_experience', models.PositiveBigIntegerField(default=0, null=True)),
                ('department_ID', models.CharField(choices=[('IT', 'IT'), ('HR', 'HR'), ('FI', 'Finance')], default='IT', max_length=2, null=True)),
                ('resume_file', models.FileField(upload_to='resume/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]