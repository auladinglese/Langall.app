# Generated by Django 2.2.6 on 2019-10-25 16:09

import cuser.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email address already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('city', models.CharField(blank=True, max_length=40)),
                ('location', models.CharField(blank=True, max_length=150)),
                ('interest_lang_1', models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('GER', 'German'), ('FRA', 'French'), ('ITA', 'Italian'), ('RUS', 'Russian')], max_length=3)),
                ('interest_lang_2', models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('GER', 'German'), ('FRA', 'French'), ('ITA', 'Italian'), ('RUS', 'Russian')], max_length=3)),
                ('interest_lang_3', models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('GER', 'German'), ('FRA', 'French'), ('ITA', 'Italian'), ('RUS', 'Russian')], max_length=3)),
                ('form_fill_factor', models.FloatField(blank=True, default=1, max_length=4)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('is_premium', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', cuser.models.CUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(blank=True, max_length=600)),
                ('base_price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('teach_lang_1', models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('GER', 'German'), ('FRA', 'French'), ('ITA', 'Italian'), ('RUS', 'Russian')], max_length=3)),
                ('teach_lang_2', models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('GER', 'German'), ('FRA', 'French'), ('ITA', 'Italian'), ('RUS', 'Russian')], max_length=3)),
                ('teach_lang_3', models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('GER', 'German'), ('FRA', 'French'), ('ITA', 'Italian'), ('RUS', 'Russian')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacherprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
