from __future__ import absolute_import

from celery import shared_task

import paramiko, os, sys, sh

from django.core.files import File


backup_dir = "/Users/cosmic/backup_dir"


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def backup_test(dev_hostname, dev_mgt_ip, dev_username, dev_password):
    print(dev_hostname)
    print(dev_mgt_ip)
    print(dev_username)
    print(dev_password)
    return 1

@shared_task
def test_print(x):
    return print("Das ist test_print: ", x)


@shared_task
def git_add_and_commit():
    git = sh.git.bake(_cwd=backup_dir)

    if git.status('--porcelain') == "":
        print("Nothing to commit")
        print("git.status ausgeführt")
    else:
        git.add('-A')
        print("git.add ausgeführt")
        git.commit(m='Backup Commit')
        print("git.commit ausgeführt")

    print("Done")
    return()


@shared_task
def create_backup(kdnr, hostname, ip, port, username, password):
    # try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(ip, port, username, password)
    #stdin, stdout, stderr = client.exec_command(':global idt [/system identity get name]; :put $idt;')
    #identity = stdout.read()
    stdin, stdout, stderr = client.exec_command('/export')
    export = stdout.read()
    client.close()

    export = export.strip().decode("utf-8")

    #mt, kdnr, boxnr = identity.decode("utf-8").split("-")

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    if not os.path.exists(backup_dir + "/" + kdnr):
        os.makedirs(backup_dir + "/" + kdnr)

    backup_file = backup_dir + "/" + kdnr + "/" + hostname + ".rsc"

    with open(backup_file, 'w', newline="\n") as bf:
        file = File(bf)
        file.write(export)

    print("Done!")
    # except:
    # print("Grosse Scheisse!")

    return()