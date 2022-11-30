# Telegram channel statistics project

# Project description
This project is a simple Telegram channel statistics project. 

# Purpose
The purpose of this project is to provide a simple way to get statistics about a Telegram channel.

# Features

- Get the number of posts
- Get the number of posts per day
- Get the number of posts per month
- Get the number of posts per weekday
- Get the number of posts per year
- Get the number of posts per week 

# Message data structure

```json

{
    "id": 1,
    "type": "message|service",
    "date": "YYYY-MM-DD HH:MM:SS",
    "date_unixtime": "UNIXTIME",
    "actor": "ACTOR",
    "actor_id": "ACTOR_ID",
    "action": "ACTION",
    "title": "TITLE",
    "text": "TEXT",
    "text_entities":[]
}

