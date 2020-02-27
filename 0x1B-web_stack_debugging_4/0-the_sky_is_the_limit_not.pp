# Increase number of requests allowed to Ngnix
exec { 'fix--for-nginx':
  command => "sed -i 's/worker_processes 4;/worker_processes 30;/' /etc/nginx/nginx.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
