#!/usr/bin/env bash
# sets up web server for for deployment of web_static

create_current(){
    if test -L "$1"; then
	sudo unlink "$1"
    fi
    sudo ln -s "$2" "$1"
}


# install nginx if not installed
if ! command -v nginx > /dev/null; then
    sudo apt update -y
    sudo apt install nginx -y
    if command -v ufw > /dev/null; then
	sudo ufw allow 'nginx HTTP'
	sudo ufw allow 80/tcp
	sudo ufw allow 22/tcp
    fi
    sudo service nginx start
fi

# create folder heirarchy
sudo mkdir -p /data/web_static/{releases,shared}/test
test_dir="/data/web_static/releases/test/"


# create fake html file
echo "I am ready" | sudo tee  "$test_dir/index.html" > /dev/null

# create symlink afresh
current_link='/data/web_static/current'
create_current "$current_link" '/data/web_static/releases/test/'

# set permissions
sudo chown -R ubuntu:ubuntu '/data/'

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
	    alias $current_link;
	}
}
"
echo "$config" | sudo tee '/etc/nginx/sites-available/default' > /dev/null
sudo service nginx restart
