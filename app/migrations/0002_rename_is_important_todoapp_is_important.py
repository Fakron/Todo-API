# Generated by Django 4.1.2 on 2022-10-22 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todoapp", old_name="Is_important", new_name="is_important",
        ),
    ]
