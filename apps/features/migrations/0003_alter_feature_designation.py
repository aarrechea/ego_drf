# Generated by Django 5.1.4 on 2025-01-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_features', '0002_feature_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='designation',
            field=models.CharField(blank=True, default='None', max_length=20, null=True),
        ),
    ]
