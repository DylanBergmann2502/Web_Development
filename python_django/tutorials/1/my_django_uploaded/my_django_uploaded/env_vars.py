import os

dj_user= os.environ.get('django_user')
dj_password= os.environ.get('django_password')

print (dj_user, dj_password)