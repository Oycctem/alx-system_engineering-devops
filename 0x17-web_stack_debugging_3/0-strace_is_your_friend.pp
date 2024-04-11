# A puppet script

$file_to_edit = '/var/www/html/wp-settings.php'

# changing line containing "phpp" to "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}