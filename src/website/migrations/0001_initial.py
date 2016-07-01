# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-01 17:57
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('details', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pinned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('article_pic', models.ImageField(blank=True, null=True, upload_to='article_pics/%Y-%m-%d/')),
                ('content', django_markdown.models.MarkdownField()),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prof_pic', models.ImageField(blank=True, null=True, upload_to='author_profile_pics/%Y-%m-%d/')),
                ('blurb', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('convenor', models.CharField(max_length=100)),
                ('strength', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=300)),
                ('details', models.CharField(max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ctype', models.CharField(choices=[('H', 'HCC'), ('S', 'Security'), ('L', 'LAN'), ('P', 'Sports'), ('E', 'Eateries'), ('I', 'Independent Bodies'), ('A', 'Academics'), ('M', 'Miscellaneous')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CoreMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prof_pic', models.ImageField(blank=True, upload_to='member_pic_thumbnail/%Y-%m-%d/')),
                ('designation', models.CharField(choices=[('PR', 'President'), ('IC', 'Incident Convenor'), ('EC', 'Engineer Convenor'), ('GS', 'General Secretary'), ('JS', 'Joint Secretary'), ('GR', "Girls' Representative"), ('PG', "PG Girls' Representative"), ('PP', 'PG Representative'), ('IT', 'Incident Treasurer'), ('ET', 'Engineer Treasurer')], max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', django_markdown.models.MarkdownField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('contact', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('organizer', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='website.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressee', models.CharField(choices=[('DR', 'Director'), ('SW', 'Dean SW'), ('FW', 'Dean FW'), ('PD', 'Dean P&D'), ('HS', 'Hostel Office'), ('MC', 'Miscellaneous')], max_length=2)),
                ('subject', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('date_of_letter', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(choices=[('CH', 'Chemical Engineering'), ('CO', 'Computer Engineering'), ('CV', 'Civil Engineering'), ('EC', 'Electronics and Communications Engineering'), ('EE', 'Elelctrical and Electronics Engineering'), ('IT', 'Information Technology'), ('ME', 'Mechanical Engineering'), ('MN', 'Mining Engineering'), ('MT', 'Materials and Metallurgical Engineering')], max_length=2)),
                ('prof_pic', models.ImageField(blank=True, upload_to='member_pic_thumbnail/%Y-%m-%d/')),
                ('year', models.IntegerField(choices=[(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Final Year')])),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='MessageFromPresident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='presi_image/')),
                ('year', models.DateField()),
                ('message', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.CreateModel(
            name='Minute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('date_of_meeting', models.DateField()),
                ('title', models.CharField(default='Minutes of the Meeting', max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('date_of_signing', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('news_pic', models.ImageField(blank=True, null=True, upload_to='article_pics/%Y-%m-%d/')),
                ('thumbnail', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='news_thumbnail/%Y-%m-%d/')),
                ('details', django_markdown.models.MarkdownField()),
                ('category', models.CharField(choices=[('C', 'Campus News'), ('N', 'In the News'), ('S', 'Spotlight')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pinned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchGrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('date_of_grant', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SenateReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('date_of_report', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.ResourceCategory'),
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Author'),
        ),
    ]
