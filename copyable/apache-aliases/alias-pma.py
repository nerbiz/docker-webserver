#!/usr/bin/python3

contents = """Alias /phpmyadmin "/etc/phpmyadmin"

<Directory "/etc/phpmyadmin">
    Options FollowSymlinks
    AllowOverride None
    Require all granted
</Directory>

"""

with open('/etc/apache2/conf-available/aliases.conf', 'a') as f:
    f.write(contents)
