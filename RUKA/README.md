## Bot Rank System
* ```WHITELIST_USERS``` - People who will be immune to all bans and mutes by bots, will be able to see the bot's stats and system info
* ```SUPPORT_USERS``` - All powers of ```WHITELIST_USERS``` and with gban power
* ```SUDO_USERS``` - People who will have self promoting right and all powers as ```SUPPORT_USER```
* ```DEV_USERS``` - Developers of the bot, have almost every right
* ```OWNER``` - Have all rights and access to the bots command

## File System
RUKA
    ```__init__.py```
    ```__main__.py```
    ```config.py```
    ```media.py```
    **modules**
    **tools**
    database
        ```mongodb.py```
        sql


RUKA
| Folder/File | Description |
| :---: | --- |
| src | Root folder |
| └── auth | Folder for authentication |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py | Initialization file |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── models.py | Models file |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── views.py | Views file |
| └── chat | Folder for chat |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py | Initialization file |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── models.py | Models file |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── views.py | Views file |
| └── utils | Folder for utility functions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py | Initialization file |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── email.py | Email utility file |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── logger.py | Logger utility file |
