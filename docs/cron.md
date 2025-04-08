# Cron

cron is a time-based job scheduler in Unix-like operating systems. It allows users to schedule tasks (referred to as "cron jobs") to run periodically at fixed times, dates, or intervals.

---

## Table of contents

- [Installation](#installation)
- [Components](#components)
- [Crontab Format](#crontab-format)
- [Common Commands](#common-commands)
- [Special Strings](#special-strings)
- [AT Command](#at-command)

---

## Installation

There are many cron implementations:

- `cronie`: Daemon that runs specified programs at scheduled times and related tools. [github](https://github.com/cronie-crond/cronie) `BSD` `C`
  - arch: `cronie`

1. Install the package
2. Enable Service

    ```sh
    systemctl enable cronie
    systemctl start cronie
    ```

---

## Components

1. Cron Daemon: The background service that runs and checks cron jobs based on the schedule.

2. Crontab: A file that contains the list of jobs and their schedules for a specific user.

3. Cronjob: A single task that is scheduled in the crontab file.

---

## Crontab Format

Each line in the crontab file represents a cron job with the following format:

```txt
* * * * * command_to_run
- - - - -
| | | | |
| | | | +---- Day of the week (0 - 6) (Sunday=0)
| | | +------ Month (1 - 12)
| | +-------- Day of the month (1 - 31)
| +---------- Hour (0 - 23)
+------------ Minute (0 - 59)
```

- Asterisk `*`: Asterisks (also known as wildcard) represents "all". For example, using `* * * * *` will run every minute. Using `* * * * 1` will run every minute only on Monday.

- Comma `,`: Commas are used to separate items of a list. For example, using `MON,WED,FRI` in the 5th field (day of week) means Mondays, Wednesdays and Fridays.

- Hyphen `-`: Hyphen defines ranges. For example, `2000-2010` indicates every year between 2000 and 2010, inclusive.

- Slash `/`: slashes can be combined with ranges to specify step values. For example, `*/5` in the minutes field indicates every 5 minutes

### Example Cron Syntax

- `0 5 * * * /path/to/script.sh`: Runs script.sh every day at 5:00 AM.

- `*/10 * * * * /path/to/command`: Runs every 10 minutes.

- `*0,*5 9-16 * 1-5,9-12 1-5 /home/user/bin/i_love_cron.sh`: will execute the script i_love_cron.sh at five minute intervals from 9 AM to 5 PM (excluding 5 PM itself) every weekday (Mon-Fri) of every month except during the summer (June, July, and August).

---

## Common Commands

- Edit crontab file for the current user:
Special Strings

    ```sh
    crontab -e
    ```

- List crontab file for the current user:

    ```sh
    crontab -l
    ```

- Remove the current user's crontab:

    ```sh
    crontab -r
    ```

- Backup crontab:

    ```sh
    crontab -l > crontab_backup.txt
    ```

- Restore crontab:

    ```sh
    crontab crontab_backup.txt
    ```

---

## Special Strings

Cron also supports the following special strings as shorthand for specific schedules:

- `@reboot`: Run at startup

- `@hourly`: Run every hour

- `@daily`: Run once per day at midnight

- `@weekly`: Run once per week at midnight on Sunday

- `@monthly`: Run once per month at midnight on the first of the month

- `@yearly`: Run once per year at midnight on January 1st

### Example

```sh
@daily /path/to/daily_task.sh
```

---

## AT Command

The at command is used to schedule one-time tasks to run at a specific time in the future. Unlike cron, which runs recurring jobs, at is useful for tasks that should be executed only once.

### Syntax

```sh
echo "COMMAND" | at [OPTION] TIME
```

- TIME can be a specific time, such as HH:MM, or a relative time like now + 1 hour.
- After running at, you can enter the commands to be executed when the scheduled time arrives.

### Common Use

1. Schedule a Job To schedule a job at a specific time:

    ```sh
    at 15:30
    ```

2. Schedule a Job with Date You can also schedule jobs for specific dates:

    ```sh
    at 5:00 PM 2025-12-25
    ```

3. Schedule a Job Relative to Now For a job to run in the future relative to the current time:

    ```sh
    at now + 1 hour
    ```

### Managing Jobs

1. List Scheduled Jobs:

    ```sh
    atq
    ```

2. Remove a Scheduled Job:

    ```sh
    atrm JOB_NUMBER
    ```

---
