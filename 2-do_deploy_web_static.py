#!/usr/bin/python3
'''Defines tasks used for web_static deployment

   do_pack(:obj:func): creates .tgz archive of files to deploy.
   do_deploy(:obj:func): distributes an archive to multiple web servers
'''
from fabric.api import env, hosts, hide, local, put, run, settings


env.hosts = ["34.239.254.5", "18.204.14.172"]


def do_pack():
    '''A function that creates a .tgz archive from web_static folder
    - 1. Creates the versions directory if not exists
    - 2. Creates archive with name in the format
         `web_static_<year><month><day><hour><minute><second>.tgz`
         saved in versions directory
    Returns
        path to archive on success or None otherwise.
    '''
    folder = "versions"

    with settings(warn_only=True):
        with hide("everything"):
            # create folder if not exists
            res = local(f"test -d {folder}", capture=True)
            if res.failed:
                local(f"mkdir {folder}")

            # set archive name
            res = local("date +'%Y%m%d%H%M%S'", capture=True)
            tar_fname = f"{folder}/web_static_{res.stdout}.tgz"
            if res.failed:
                return

        # create archive
        print(f"Packing web_static to {tar_fname}")
        res = local(f"tar -cvz web_static -f {tar_fname}", capture=True)
        if res.succeeded:
            print(res.stdout)
            return tar_fname


def do_deploy(archive_path):
    """ Deploys files to multiple servers """
    with hide("everything"):
        if local(f"test -f {archive_path}").failed:
            return False
    dirname = archive_path.split('/')[1].split('.')[0]
    remote_arch = put(archive_path, "/tmp")[0]
    dest = f"/data/web_static/releases/{dirname}"
    curr_link = "/data/web_static/current"
    if run(f"mkdir -p {dest}").failed:
        return False
    if run(f"tar -xf {remote_arch} -C {dest}").failed:
        return False
    if run(f"rm -f {remote_arch}").failed:
        return False
    if run(f"cp -rf {dest}/web_static/* {dest}").failed:
        return False
    if run(f"rm -rf {dest}/web_static").failed:
        return False
    if run(f"unlink {curr_link}").failed:
        return False
    if run(f"ln -s {dest} {curr_link}").failed:
        return False
    print("New version deployed!")
    return True
