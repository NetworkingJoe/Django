#!/bin/bash                       #this basically says we are working in bash language and gets the code started at a user level.
echo "yaaaaah hoooooooooooo"      #adds the comment "yaaaaah hoooooooooooo" too the top of the page              

yum -y install httpd              #gives a yes command to installing a basic version of apache.
systemctl enable httpd            #this enables apache to run in our environment.
systemctl start httpd             #this starts apache when the server is powered on.
