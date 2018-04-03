from __future__ import absolute_import

from celery import shared_task

import paramiko, os, sys, sh

from django.core.files import File


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def create_backup(ip, port, username, password):

    backup_dir = "/backup_dir"

    git = sh.git.bake( _cwd = backup_dir )
    
    #try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    client.connect(ip, port, username, password)
    stdin, stdout, stderr = client.exec_command(':global idt [/system identity get name]; :put $idt;')
    identity = stdout.read()
    stdin, stdout, stderr = client.exec_command('/export')
    export = stdout.read()
    client.close()

    export = export.strip().decode("utf-8")
    
    mt, kdnr, boxnr = identity.decode("utf-8").split("-")

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    if not os.path.exists(backup_dir + "/" + kdnr):
        os.makedirs(backup_dir + "/" + kdnr)
        
    backup_file = backup_dir + "/" + kdnr + "/" + identity.strip().decode("utf-8") + ".rsc"
        
    if not os.path.exists(backup_file):
        git_add = True
    else:
        git_add = False
        
    with open( backup_file, 'w', newline="\n") as bf:
        file = File(bf)
        file.write(export)
            
    if git_add == True:
        git.add(backup_file)
        print("git add durchgeführt!")
                
    print(git_add)
    print("Done!")
    #except:
        #print("Grosse Scheisse!")
    return(None)
