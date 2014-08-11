__author__ = 'aclement'

from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoTango.settings')
path = os.path.join(settings.BASE_DIR, "static")
file_name = os.path.join(path, "CompletedCourses.csv")

file = open(file_name)

#for line in file:
    #print line

i = 0 if False else 1
print i