#!/usr/bin/python
import os

def django_setup():
  os.system('sudo yum install python-pip -y')
  os.system('sudo pip install virtualenv')
  os.system('sudo pip install --upgrade pip')
  os.system('sudo mkdir /opt/django')
  os.chdir('/opt/django')
  os.system('sudo useradd paulierev1775')
  os.system('sudo yum install epel-release -y')
  os.system('sudo yum install python34 python-pip -y')

def django_install():
  os.system('sudo virtualenv -p python3 django')
  os.chdir('/opt/django/django')
  os.system('source /opt/django/django/bin/activate && pip install django')
  os.system('source /opt/django/django/bin/activate && django-admin startproject project1')

  os.chdir('..')
  os.system('sudo chown -R paulierev1775 /opt/django/')
  os.system('yum install git -y')
  os.system('myip=$( curl ifconfig.co ) && sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS =  \[\'"$myip"\'\]/g" /opt/django/django/project1/project1/settings.py ')
 
# "This is my comment for the startupscript.sh file. I am commenting here to remind myself that although the line above does
#  Indeed add the allowed hosts to the file, every time I start up the instance, I have to go in and plug in the new I.P. address
#  In order to get it working properly. This is because my instance generates a new IP address every time."

def django_start():
  os.system('sudo -u paulierev1775 virtualenv -p python3 django')
  os.chdir('/opt/django/django')
  os.system('sudo -u paulierev1775 -E sh -c "source /opt/django/django/bin/activate && /opt/django/django/project1/manage.py runserver 0.0.0.0:8000&"')

django_setup()
django_install()
django_start()
