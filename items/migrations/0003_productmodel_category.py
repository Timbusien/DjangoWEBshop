# Generated by Django 4.2.5 on 2023-09-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_categorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='items.categorymodel'),
        ),
    ]
