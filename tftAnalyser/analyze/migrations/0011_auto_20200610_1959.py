# Generated by Django 2.2.12 on 2020-06-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0010_analyzetrait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchtrait',
            name='trait',
            field=models.CharField(max_length=32),
        ),
    ]
