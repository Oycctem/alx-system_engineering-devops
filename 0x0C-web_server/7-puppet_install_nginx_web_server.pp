# puppet commands
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/etc/nginx/sites-available/redirect_me':
  ensure  => present,
  content => "server {
                listen 80;
                server_name _;
                location /redirect_me {
                    return 301 http://example.com/new_page;
                }
            }",
}

file { '/etc/nginx/sites-enabled/redirect_me':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect_me',
  require => File['/etc/nginx/sites-available/redirect_me'],
}
