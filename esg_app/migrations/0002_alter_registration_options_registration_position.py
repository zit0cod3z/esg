# Generated by Django 4.2.2 on 2024-09-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esg_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ('-submitted_at',)},
        ),
        migrations.AddField(
            model_name='registration',
            name='position',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
