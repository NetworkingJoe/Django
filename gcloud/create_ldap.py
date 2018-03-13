def create_instance(compute, project, zone, name):
    startup_script = open('startup-script.sh', 'r').read()
    image_response = compute.images().getFromFamily(
      project='centos-cloud', family='centos-7').execute()

   #The top part basically creates a defined library with the contents compute, project, zone, and name.
   #It imports a recursive startup_script file to open and read at startup so we can run our instance 
   #With the centos-7 type of processor and the image from a library called compute so that it can start up.
   #I.E. the first part is our instance startup as if we were doing it directly from gcloud itself.

    source_disk_image = image_response['selfLink']
    machine_type = "zones/%s/machineTypes/f1-micro" % zone
    
    #This section selects the style and size of the instance.

    config = {
        'name': name,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],
        
        #Basically this starts our disk when the instance is powered on from the source_disk_image library of files which 
        #is needed to have no blank screen of doom or an error message.

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

       # Enable https/http for select instances
       "labels": {
       "http-server": "",
      "https-server": ""
       },

       "tags": {
       "items": [
       "http-server",
       "https-server"
       ]
       },

        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            }]
        }
    }


    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()

