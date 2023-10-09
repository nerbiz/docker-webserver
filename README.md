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

The compose file creates these:
* Images
    * dbserver
    * phpserver
* Volumes
    * dbdata
* Networks
    * webdev

The volume has a fixed name ('dbdata'), because the database data is intended for reuse across projects. Names for containers and network are dynamic based on your project directory name. Change any of these names if needed.

## Using

Copy the `docker-compose.yml` file to your project directory and run it:

```sh
# The -d makes it run in the background
docker compose up -d
```

To stop/remove the containers:

```sh
# This removes the containers and the network,
# not the volume
docker compose down
```
