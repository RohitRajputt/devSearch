# Generated by Django 4.1.1 on 2023-06-13 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_options_review_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_total', '-vote_ratio', 'title']},
        ),
    ]