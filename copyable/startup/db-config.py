#!/usr/bin/python3

import sys, os

# Get the DB server name from an argument
db_server = sys.argv[1] if len(sys.argv) > 1 else 'mariadb'

# Change phpMyAdmin config
config_file = '/etc/phpmyadmin/config.inc.php'
blowfish_secret = os.urandom(16).hex()

with open(config_file, 'r') as file:
    contents = file.read()

contents = contents.replace(
    "$cfg['blowfish_secret'] = '';",
    f"$cfg['blowfish_secret'] = '{blowfish_secret}';"
)

contents = contents.replace(
    "$cfg['Servers'][$i]['host'] = 'localhost';",
    f"$cfg['Servers'][$i]['host'] = '{db_server}';"
)

with open(config_file, 'w') as file:
    file.write(contents)

# Change Adminer config
with open('/etc/adminer/servername.txt', 'w') as file:
    file.write(db_server)
