from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django_markdown.models import MarkdownField
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerImageField

class News(models.Model):
    CHOICE = [('C', 'Campus News'),
            ('N', 'In the News'),
            ('S', 'Spotlight'),
            ]
    title = models.CharField(max_length=300)
    news_pic = models.ImageField(upload_to='article_pics/%Y-%m-%d/',null=True,blank=True)
    thumbnail = ThumbnailerImageField(upload_to='news_thumbnail/%Y-%m-%d/', blank=True)
    details = MarkdownField()
    category = models.CharField(max_length=1, choices=CHOICE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Announcements(models.Model):
    title = models.CharField(max_length=300)
    thumbnail = ThumbnailerImageField(upload_to='announcement_thumbnail/%Y-%m-%d/', blank=True)
    details = MarkdownField()
    timestamp = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Club(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=300)
    convenor = models.CharField(max_length=100)
    strength = models.IntegerField()

    def __str__(self):
        return self.name

class CoreMember(models.Model):
    DESIGNATION = [('PR','President'),
                   ('IC','Incident Convenor'),
                   ('EC','Engineer Convenor'),
                   ('GS','Secretary'),
                   ('GR','Girls\' Representative'),
                   ('PG','PG Girls\' Representative'),
                   ('PP','PG Representative'),
                   ('IT','Incident Treasurer'),
                   ('ET','Engineer Treasurer'),
                  ]
    name = models.CharField(max_length=50)
    prof_pic = models.ImageField(upload_to='member_pic_thumbnail/%Y-%m-%d/', blank=True)
    designation = models.CharField(max_length=2, choices=DESIGNATION)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return u'%s %s' % (self.name,self.get_designation_display())

class Member(models.Model):
    BRANCH_LIST = [('CH', 'Chemical Engineering'),
                   ('CO', 'Computer Engineering'),
                   ('CV', 'Civil Engineering'),
                   ('EC', 'Electronics and Communications Engineering'),
                   ('EE', 'Elelctrical and Electronics Engineering'),
                   ('IT', 'Information Technology'),
                   ('ME', 'Mechanical Engineering'),
                   ('MN', 'Mining Engineering'),
                   ('MT', 'Materials and Metallurgical Engineering'),
                   ]
    YEAR_LIST = [(1,'First Year'),
                 (2,'Second Year'),
                 (3,'Third Year'),
                 (4,'Final Year'),
                ]
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=2, choices=BRANCH_LIST)
    prof_pic = models.ImageField(upload_to='member_pic_thumbnail/%Y-%m-%d/', blank=True)
    year = models.IntegerField(choices=YEAR_LIST)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return u'%s %s %s' % (self.name,self.branch,self.get_year_display())

class Events(models.Model):
    title = models.CharField(max_length=200)
    organizer = models.ForeignKey(Club, editable=False)
    details = MarkdownField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    prof_pic = models.ImageField(upload_to='author_profile_pics/%Y-%m-%d/',null=True,blank=True)
    blurb = MarkdownField()

    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    article_pic = models.ImageField(upload_to='article_pics/%Y-%m-%d/',null=True,blank=True)
    content = MarkdownField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Complaint(models.Model):
    choice = [('H', 'HCC'),
            ('S', 'Security'),
            ('L', 'LAN'),
            ('P', 'Sports'),
            ('E', 'Eateries'),
            ('I', 'Independent Bodies'),
            ('A', 'Academics'),
            ('M', 'Miscellaneous'),
            ]
    complaint = models.CharField(max_length=300)
    details = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    ctype = models.CharField(max_length=1, choices=choice)

    def __str__(self):
        return self.complaint

class Minute(models.Model):
    link = models.URLField()
    date_of_meeting = models.DateField()
    title = models.CharField(max_length=100, default="Minutes of the Meeting")
    description = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title + '-' + str(self.date_of_meeting)

class ResearchGrant(models.Model):
    link = models.URLField()
    date_of_grant = models.DateField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title

class MoU(models.Model):
    link = models.URLField()
    date_of_signing = models.DateField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title

class Resource(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class SenateReport(models.Model):
    link = models.URLField()
    date_of_report = models.DateField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title + '-' + str(self.date_of_report)
