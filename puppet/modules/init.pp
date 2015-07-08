include main

class phpldapadmin inherits php {
	package { $name:
		name => 'phpldapadmin',
		ensure => 'installed'
	}
	service { 

	}
	




}
class phpldapadmin::config inhertis php {
	if $key_enable {
		$directory = dirname($keys_file)
		file {$directory:
			ensure => directory, 
			owner => root,
			group => root,
			mode => '0755',
			recurse => 'true'
		}
	}
	
	file {$config:
		
	}


}