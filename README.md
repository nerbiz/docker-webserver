# Docker webserver

Docker files for running PHP and MySQL servers.

## Installation

Download or clone this repo somewhere.

In `docker-compose.yml`, the values are 'C:\docker-webserver' (Windows) and '~/docker-webserver' (Linux/macOS), so if you use a different directory, change `docker-compose.yml` accordingly.

Set the right context values in `docker-compose.yml`, according to your operating system.

### Windows

```sh
cd C:\
git clone https://github.com/nerbiz/docker-webserver
```

### Linux / macOS
```sh
cd ~
git clone https://github.com/nerbiz/docker-webserver
```

## Naming

The compose file creates these things:

* Images
    * dbserver
    * phpserver
* Volumes
    * dbdata
* Networks
    * webdev

If your project directory is 'tester', the volume will be 'tester_dbdata' and network will be 'tester_webdev'.

## Using

Copy the `docker-compose.yml` file to your project directory and run it:

```sh
# The -d makes it run in the background
docker compose up -d
```

**Please note:** The first time 'up' takes a while, because the images need to be built first. After that, it's much faster.

To stop/remove the containers:

```sh
# This removes the containers and the network,
# not the volume
docker compose down
```

After running it, http://localhost should be working (also https://localhost).

## What's included

* A MariaDB database server at port 3306
* An Apache + PHP server
    * Apache mods: rewrite, headers, expires
    * Both http://localhost and https://localhost available
    * Container is mapped to /var/www/site
    * Document root is /var/www/html, which is a symlink to /var/www/site
    * Gettext for translating strings
    * PHP extensions: zip mysqli, pdo, pdo_mysql, gd, mbstring, fileinfo, bcmath, exif, intl
    * Extra PHP extensions: imagick, memcached
    * Backend tools: Mailpit, Adminer, phpMyAdmin, Composer, WordPress CLI
    * Frontend tools: Node.js, NPM, Yarn
    * Git
    * Nano
    * Aliases:
        * ls: ls --color=auto -lAhF
        * mailpit: starts the Mailpit service
    * Ports:
        * 80: HTTP connection
        * 443: HTTPS connection
        * 3000: Node.js port
        * 5173: Vite dev server
        * 8000: Laravel port
        * 8025: Mailpit web UI
