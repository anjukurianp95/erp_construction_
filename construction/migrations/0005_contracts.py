# Generated by Django 3.0 on 2020-02-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0004_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='contracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('jtype', models.CharField(max_length=20)),
                ('contractor', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('fromdate', models.DateField()),
                ('todate', models.DateField()),
                ('noemp', models.IntegerField()),
                ('budget', models.IntegerField()),
            ],
        ),
    ]
