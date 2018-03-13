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
    
    #Lines 11-12 select the style and size of the instance.

    config = {
        'name': name,
        'machineType': machine_type,

    # lines 16-18 basically name the machine, lines 23-26 specify the boot disk and selects the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],
        
        # Lines 33-36 pecifiy a network interface with NAT to access the public internet.
 
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Lines 41-45 allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

       # Lines 50-58 enable https/http for select instances
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

        # Lines 64-68 take metadata that is readable from the instance and allows you to 
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

        #Finally, Lines 75-78 basically allow us final run permissions on the instance when started, and the project folder
        #etc. and makes sure that our arguments ring true for compute.instances using the keys project, zone, and config
        #and executing it.
