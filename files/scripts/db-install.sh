#!/bin/sh

sudo apt install mariadb-server

sudo mysql_secure_installation

mariadb -u root -p < db-user.sql
