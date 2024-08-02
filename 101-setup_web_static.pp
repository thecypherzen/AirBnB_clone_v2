# sets up a new machine for deploy backup
exec {'update packages':
  command => 'apt update',
  user    => 'root',
  path    => '/usr/bin'
}

-> package {'install nginx':
  ensure   => installed,
  name     => 'nginx',
  provider => 'apt',
}

-> exec {'open ufw ports':
  command => 'ufw allow 80/tcp && ufw allow 22/tcp',
  path    => '/usr/sbin',
  user    => 'root',
}

-> exec {'create directories':
  command => 'mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"',
  path    => '/usr/bin',
  user    => 'root',
}

-> exec {'update test content':
  command => 'echo "I am ready" | tee /data/web_static/releases/test/index.html > /dev/null',
  path    => '/usr/bin',
  user    => 'root',
}

-> exec { 'create symlink':
  command => 'ln -s /data/web_static/releases/test/ /data/web_static/current',
  path    => 'usr/bin',
  user    => 'root',
}

-> exec { 'change ownership':
  command => 'chown -R ubuntu:ubuntu /data/',
  user    => 'root',
  path    => '/usr/bin',
}

$server_config = @("CONFIG"/L)
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
        alias /data/web_static/current;
    }
}
CONFIG

-> file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $server_config,
}

-> exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/sbin',
  user    => 'root',
}