# Generated by Django 4.2 on 2025-01-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applight', '0003_alter_features_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='block',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='faq',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='features',
            name='icon',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='features',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='watchnow',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
