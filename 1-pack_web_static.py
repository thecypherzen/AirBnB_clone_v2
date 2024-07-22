from fabric.api import hide, local, settings


def do_pack():
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
