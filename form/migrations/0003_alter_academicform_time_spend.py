# Generated by Django 4.0.3 on 2022-04-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_academicform_batch_academicform_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicform',
            name='time_spend',
            field=models.CharField(blank=True, choices=[('Two hours', 'Two hours'), ('Three hours', 'Three hours'), ('More tha three hours', 'More than three hours')], max_length=50, null=True),
        ),
    ]