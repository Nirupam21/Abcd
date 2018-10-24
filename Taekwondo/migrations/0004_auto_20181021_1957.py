# Generated by Django 2.1 on 2018-10-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taekwondo', '0003_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='agegroup',
            field=models.CharField(choices=[('pee-wee', 'PEE-WEE'), ('sub junior', 'SUB JUNIOR'), ('junior', 'JUNIOR'), ('senior', 'SENIOR'), ('senior black belt', 'SENIOR BLACK BELT')], default='senior', max_length=20),
        ),
        migrations.AddField(
            model_name='results',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='male', max_length=6),
        ),
        migrations.AddField(
            model_name='results',
            name='weightcategory',
            field=models.CharField(choices=[('fin', 'FIN'), ('fly', 'FLY'), ('bantam', 'BANTAM'), ('feather', 'FEATHER'), ('light', 'LIGHT'), ('welter', 'WELTER'), ('light Middle', 'LIGHT MIDDLE'), ('middle', 'MIDDLE'), ('light Heavy', 'LIGHT HEAVY'), ('heavy', 'HEAVY')], default='fin', max_length=12),
        ),
    ]