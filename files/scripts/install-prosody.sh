#!/bin/sh

sudo apt install prosody lua-dbi-sqlite3 lua-unbound
sudo certbot -d cloud99p.org --nginx
sudo certbot -d xmpp.cloud99p.org --nginx
sudo certbot -d share.cloud99p.org --nginx
sudo prosodyctl --root cert import /etc/letsencrypt/live
sudo prosodyctl adduser reza@cloud99p.org
sudo systemctl restart prosody

