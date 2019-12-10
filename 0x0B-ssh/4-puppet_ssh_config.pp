#This file is to create a file
file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  ensure  => 'present',
  line    => '    PasswordAuthentication no'
}
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  ensure  => 'present',
  line    => '    IdentityFile ~/.ssh/holberton'
}
