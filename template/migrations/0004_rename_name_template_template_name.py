# Generated by Django 4.1 on 2022-08-09 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0003_template_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='name',
            new_name='template_name',
        ),
    ]
