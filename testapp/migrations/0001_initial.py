# Generated by Django 4.1.2 on 2023-08-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('EmpID', models.CharField(max_length=50)),
                ('EmpPost', models.CharField(max_length=50)),
                ('Photo', models.ImageField(upload_to='upload')),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField(max_length=225)),
            ],
        ),
    ]