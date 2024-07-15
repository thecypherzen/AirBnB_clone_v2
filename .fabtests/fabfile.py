from fabric.api import local, settings, lcd, run, env, hosts


def set_env():
    '''    print(env.keys(), end="\n\n")
    env.hosts = ["ubuntu@web01:22"]
    env.key_filename = ["~/key_stack/.web01_ubuntu"]
    '''
    env.use_ssh_config = True

    '''    print("config_path: ",env.ssh_config_path)
    print("host: ",env.host)
    print("hosts: ",env.hosts)
    print("use_ssh_config: ", env.use_ssh_config)
    print("key_filename: ", env.key_filename)
    '''

set_env()

def greet(name=None):
    msg = "Hello"
    if not name:
        msg += " there"
    else:
        msg += f" {name}"
    msg += '!'
    print(msg)

def num(val):
    print(val, type(val))
    num_val = int(val)
    print(type(num_val))


def test():
    with settings(warn_only=True):
        res = local("ls ~/that_file.txt", capture=True)
        print(res.succeeded)

def usr_files():
    with lcd("~/"):
        cmd = local("ls -l .", capture=True)
        if cmd.succeeded:
            print(cmd.stdout)
        else:
            print(cmd.stderr)

@hosts("web01_ubuntu")
def get_name():
    res = run("hostname", quiet=True)
    if res.succeeded:
        print(res.stdout)
    else:
        print(res.stderr)
