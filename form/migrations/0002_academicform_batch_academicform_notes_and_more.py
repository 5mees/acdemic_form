# Generated by Django 4.0.3 on 2022-04-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicform',
            name='batch',
            field=models.CharField(blank=True, choices=[('018', '018'), ('017', '017'), ('016', '016'), ('015', '015')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='academicform',
            name='notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='academicform',
            name='specialty',
            field=models.CharField(blank=True, choices=[('GIS/RM', 'GIS/RM'), ('Geodisy', 'Geodisy'), ('Photogrammetry', 'Photogrammetry')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='academicform',
            name='time_spend',
            field=models.CharField(blank=True, choices=[('GIS/RM', 'GIS/RM'), ('Geodisy', 'Geodisy'), ('Photogrammetry', 'Photogrammetry')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='academicform',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
