from __future__ import unicode_literals

from django.db import models

class Complaint(models.Model):
    ctype = [('H', 'HCC'),
            ('S', 'Security'),
            ('L', 'LAN'),
            ('P', 'Sports'),
            ('E', 'Eateries'),
            ('I', 'Independent Bodies'),
            ('A', 'Academics'),
            ('M', 'Miscellaneous'),
            ]
    date = models.DateTimeField(auto_now_add=True)
    
