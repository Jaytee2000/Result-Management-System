# Generated by Django 4.2.10 on 2024-03-15 17:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("student_classes", "0002_alter_studentclass_section"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentclass",
            old_name="section",
            new_name="department",
        ),
    ]