#!/usr/bin/python3
'''Defines tasks used for web_static deployment

   do_pack(:obj): a function creating .tgz archive of files to deploy.
'''
from fabric.api import hide, local, settings


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
