# Docker webserver

Docker files for running PHP and MySQL servers.

This is intended for people who have used services like XAMPP, but have never worked with Docker before.

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
* Containers
    * [project-name]-db-1
    * [project-name]-php-1

If your project directory is 'tester', these will be the resulting names:

* Volume: tester_dbdata
* Network: tester_webdev
* Database container: tester-db-1
* Apache/PHP container: tester-php-1

## Using

Copy the `docker-compose.yml` file to your project directory and run it:

### Starting

```sh
# The -d makes it run in the background
docker compose up -d
```

**Please note:** The first time 'up' takes a while, because the images need to be built first. After that, it's much faster.

After running it, http://localhost should be working (also https://localhost).

**Important:** The database host is not 'localhost', but the name of the database container ('tester-db-1' in the above example).

If you need to run commands inside the PHP container, you can open a terminal with this command:

```sh
# Replace 'tester-php-1' with your container name
docker exec -it tester-php-1 bash
```

For example, if you use Laravel and you want to make the `public` directory the document root (so that https://localhost points to the `public` directory), you can replace the `html` symlink:

```sh
# Do this inside your container
cd /var/www
rm html
ln -s /var/www/site/public html
```

### Stopping / restarting / removing

To stop/start or remove the containers, go to Containers in Docker Desktop and click the right button under Actions.

## What's included

* A MariaDB database server at port 3306
* An Apache + PHP server
    * Apache mods: rewrite, headers, expires
    * Both http://localhost and https://localhost available
    * Container is mounted to /var/www/site
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
