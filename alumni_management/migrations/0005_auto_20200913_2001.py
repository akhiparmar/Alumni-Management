# Generated by Django 3.0.8 on 2020-09-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni_Management', '0004_feedback_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email_to_alumni',
            name='Image',
        ),
        migrations.AlterField(
            model_name='email_to_alumni',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to='Email/files'),
        ),
    ]
