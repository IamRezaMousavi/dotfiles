# UFW

Uncomplicated Firewall (UFW) is a program for managing a netfilter firewall designed to be easy to use. It uses a command-line interface consisting of a small number of simple commands, and uses iptables for configuration.

---

## Show rules

```sh
sudo ufw status verbose
```

## Reload ufw

```sh
sudo ufw reload
```

## Show apps

```sh
sudo ufw app list
```

## Delete rules

```sh
sudo ufw status numbered
sudo ufw delete <number|rule>
```

```sh
sudo ufw delete <allow app>
```

---
