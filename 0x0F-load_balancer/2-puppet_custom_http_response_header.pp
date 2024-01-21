# install and configure nginx
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure => installed,
}
-> file_line { 'header_served_by':
  path  => '/etc/nginx/nginx.conf',
  match => '^http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  multiple => false,
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
