# ssh config
include stdlib

file_line { 'Turns off password authentication':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  ensure  => present,
}

file_line { 'Declares identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  ensure  => present,
}

