# Generated by Django 5.1.4 on 2024-12-22 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_note_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='notes',
            new_name='content',
        ),
    ]
