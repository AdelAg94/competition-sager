# Generated by Django 3.2.4 on 2021-06-12 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_competition'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='description',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=265)),
                ('competition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.competition')),
            ],
        ),
    ]