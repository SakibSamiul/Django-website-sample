# Generated by Django 5.1.1 on 2024-09-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_doctors_description_remove_doctors_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DEPARTMENTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
