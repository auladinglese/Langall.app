# Generated by Django 2.2.6 on 2019-12-09 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_teachers', '0010_timecell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecell',
            name='day',
            field=models.CharField(blank=True, choices=[('H', 'Hétfő'), ('K', 'Kedd'), ('Sze', 'Szerda'), ('Cs', 'Csütörtök'), ('P', 'Péntek'), ('Szo', 'Szombat'), ('V', 'Vasárnap')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timecell',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_cell', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, max_length=600)),
                ('rated_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_one_rev', to=settings.AUTH_USER_MODEL)),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rater_rev', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]