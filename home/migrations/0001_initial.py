# Generated by Django 4.2.7 on 2023-11-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField(null=True)),
                ('message', models.TextField(max_length=3000, null=True)),
                ('status', models.CharField(choices=[('Attended', 'Attended'), ('Not Attended', 'Not Attended')], default='Not Attended', max_length=120)),
            ],
        ),
    ]
