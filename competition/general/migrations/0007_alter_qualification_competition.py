# Generated by Django 3.2.4 on 2021-06-12 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20210612_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='competition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualifications', to='general.competition'),
        ),
    ]
