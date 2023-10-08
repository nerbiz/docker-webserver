#!/usr/bin/python3

import os

# If the document root has a 'public' directory,
# Change the symlink to point to that instead
if os.path.isdir('/var/www/html/public'):
    os.remove('/var/www/html')
    os.symlink('/var/www/site/public', '/var/www/html')
