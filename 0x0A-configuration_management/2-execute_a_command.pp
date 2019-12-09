# Excecute the command pkill
exec { 'killmenow':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
}
