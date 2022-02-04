# Generated by Django 3.2.5 on 2022-02-01 23:41

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0011_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('image', models.ImageField(default='', upload_to='image')),
            ],
        ),
    ]