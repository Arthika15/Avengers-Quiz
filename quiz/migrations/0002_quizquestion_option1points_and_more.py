# Generated by Django 4.2.1 on 2023-05-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='option1points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='option2points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='option3points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='option4points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
