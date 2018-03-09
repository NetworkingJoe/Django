#!/usr/bin/python                                                          #This tells us to run a python shell in the /usr/bin directory.

from oauth2client.client import GoogleCredentials                          #this imports our credentials from the server. I am not sure what credentials it needs? Does this connect our user to the new directory?
from googleapiclient import discovery                                      #this imports all of our directories from the server. I am not sure what this line does or if I got this correct. I think it creates a directory system but i'm not sure. 
import pprint                                                              #this imports pretty print to make our files look nicer.
import json                                                                #this imports json, a javascript language that helps store data.
import create_ldap                                                         #this imports the file create_ldap.
from create_ldap import create_instance                                    #this says to import the file/directory create_instance from the 
                                                                           #file/directory create_ldap.

credentials = GoogleCredentials.get_application_default()                  #this gives python our default credentials.
compute = discovery.build('compute', 'v1', credentials=credentials)        #this builds an instance with our default credentials of our user.

project = 'instructor-nti-300-2018'                                        #imports my repository instructor-nti-300-2018 into my instance 
zone = 'us-east1-b'                                                        #sets my time zone

# what kind of machine is being requested and what should it's name be?
# based on the machine type, we can derrive a name

name = 'test3'                                                             #name's our new instance test3

def list_instances(compute, project, zone):                                #
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']

newinstance = create_instance(compute, project, zone, name)
instances = list_instances(compute, project, zone)

pprint.pprint(newinstance)
pprint.pprint(instances)

