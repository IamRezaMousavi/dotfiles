#!/bin/sh

sudo named-checkconf
sudo named-checkzone cloud99p.org /etc/bind/zones/db.cloud99p.org

sudo systemctl restart bind9
sudo ufw allow Bind9

