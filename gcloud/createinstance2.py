#!/usr/bin/python                                                          #This tells us to run a python shell in the /usr/bin directory.

from oauth2client.client import GoogleCredentials                          #this imports our credentials from the gcloud.
from googleapiclient import discovery                                      #this imports all of our files and directories from the server. 
import pprint                                                              #this imports pretty print to make our files look nicer.
import json                                                                #this imports json, a javascript language that helps store data.
import create_ldap                                                         #this imports the file create_ldap, ldap is a directory of files.
from create_ldap import create_instance                                    #Basically the last line and this says to import the file/directory
                                                                           #create_instance from the #file/directory create_ldap.

credentials = GoogleCredentials.get_application_default()                  #this makes sure that our credentials,(username and pwd) are 
                                                                           #migrated and saved as a default to the instance so that we
                                                                           #don't have to keep logging in but are already there by default.
compute = discovery.build('compute', 'v1', credentials=credentials)        #this builds an instance with our user credentials.

project = 'instructor-nti-300-2018'                                        #names my instance instructor-nti-300-2018 
zone = 'us-east1-b'                                                        #sets my time zone

# what kind of machine is being requested and what should it's name be?   #a python server
# based on the machine type, we can derrive a name                        #yes

name = 'test3'                                                             #name's our new instance test3

def list_instances(compute, project, zone):                                #it creates a dictionary called list_instances with the 
                                                                           #variables compute, project and zone.
    result = compute.instances().list(project=project, zone=zone).execute()#basically sets up a search formula result for when someone 
                                                                           #references the instances list and along with the next line
    return result['items']                                                 #here, if someone were to search for the term 'project or zone',
                                                                           #then it would return the answer of items. But i'm not sure, the 
                                                                           #math really got the better of me, I know wer'e creating a parameter
                                                                           #for a search, with the printed answer coming up of items, but I am
                                                                           #not entirely sure what the equation involved is.

newinstance = create_instance(compute, project, zone, name)                #basically this adds the key's compute, project, zone and name,
instances = list_instances(compute, project, zone)                         #to the new instance definition and will return a list of compute
                                                                           #project, and zone of from above into our list called
pprint.pprint(newinstance)                                                 #new_instance I think. It then prints out in pretty format the
pprint.pprint(instances)                                                   #project, zone, compute key variable from above, and the name that
                                                                           #we defined earlier. I'm not sure, this is the most confusing thing 
                                                                           #to me in python that I struggled with was the terminology. It was a lot
                                                                           #to take in during a short period of time. I even struggled in the 
                                                                           #codeacademy section. Please help me learn what is wrong.
