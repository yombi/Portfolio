# Generated by Django 3.2.9 on 2021-12-16 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_alter_medicine_medicine_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medicine_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
