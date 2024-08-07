# sets up a new machine for deploy backup
exec { 'update packages':
  command => 'apt update',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}

package { 'install nginx':
  ensure   => installed,
  name     => nginx,
  provider => apt,
}

exec { 'open ufw ports':
  command => 'ufw allow 80/tcp && ufw allow 22/tcp',
  path    => ['/usr/sbin', '/usr/bin']
}

exec { 'create directories':
  command => 'mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"',
  path    => ['/usr/bin', '/usr/sbin']
}

exec { 'update test content':
  command => 'echo "I am ready" | tee /data/web_static/releases/test/index.html > /dev/null',
  path    => ['/usr/bin', '/usr/sbin'],
}

file {'/data/web_static/current':
  ensure  => absent,
}

exec { 'create symlink':
  command => 'ln -s /data/web_static/releases/test/ /data/web_static/current',
  path    => ['/usr/bin', '/usr/sbin'],
}

exec { 'change ownership':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => ['/usr/bin', '/usr/sbin'],
}

$nginx_config = @(CONFIG/$)
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
 | - CONFIG


file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => $nginx_config,
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/usr/sbin'],
}
