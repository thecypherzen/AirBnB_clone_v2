#!/usr/bin/env bash
# sets up web server for for deployment of web_static

create_current(){
    if test -L "$1"; then
	unlink "$1"
    fi
    ln -s "$2" "$1"
}


# install nginx if not installed
if ! command -v nginx; then
    apt install nginx -y
    if command -v ufw; then
	ufw allow 'nginx HTTP'
	ufw allow 80/tcp
	ufw allow 22/tcp
    fi
    service nginx start
fi

# create folder heirarchy
mkdir -p /data/web_static/{releases,shared}/test
test_dir="/data/web_sttic/releases/test/"


# create fake html file
echo "I am ready" > "$test_dir/index.html"

# create symlink afresh
current_link='/data/web_static/current'
create_current "$current_link" '/data/web_static/releases/test/'

# set permissions
chown -R ubuntu:ubuntu '/data/'

# edit nginx config
config="
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;
        server_name _;

        add_header X-Served-By \$hostname always;


        location / {
           try_files \$uri \$uri/ =404;
        }

	location /hbnb_static {
	    alias $current_link
	}
}
"
echo "$config" | tee '/etc/nginx/sites-available/default' > /dev/null
service nginx restart
