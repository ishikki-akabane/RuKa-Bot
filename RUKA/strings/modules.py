ADMIN_STR = """
 ❍ /admins*:* list of admins in the chat

*Admins only:*
 ❍ /pin*:* silently pins the message replied to - add `'loud'` or `'notify'` to give notifs to users
 ❍ /unpin*:* unpins the currently pinned message
 ❍ /invitelink*:* gets invitelink
 ❍ /fullpromote*:* promotes the user with all rights
 ❍ /promote*:* promotes the user with basic rights
 ❍ /demote*:* demotes the user
 ❍ /title <title here>*:* sets a custom title for an admin that the bot promoted
 ❍ /setgtitle <newtitle>*:* Sets new chat title in your group.
 ❍ /setgpic*:* As a reply to file or photo to set group profile pic!
 ❍ /delgpic*:* Same as above but to remove group profile pic.
 ❍ /setsticker*:* As a reply to some sticker to set it as group sticker set!
 ❍ /setdescription <description>*:* Sets new chat description in group.
 ❍ /admincache*:* force refresh the admins list
 ❍ /del*:* deletes the message you replied to
 ❍ /purge*:* deletes all messages between this and the replied to message.
 ❍ /purge <integer X>*:* deletes the replied message, and X messages following it if replied to a message.
 """

ANIME_STR = """
Get information about anime, manga or characters from [AniList](anilist.co).
*Available commands:*
 ❍ `/anime <anime>`*:* returns information about the anime.
 ❍ `/character <character>`*:* returns information about the character.
 ❍ `/manga <manga>`*:* returns information about the manga.
 ❍ `/user <user>`*:* returns information about a MyAnimeList user.
 ❍ `/upcoming`*:* returns a list of new anime in the upcoming seasons.
 ❍ `/kaizoku <anime>`*:* search an anime on animekaizoku.com
 ❍ `/kayo <anime>`*:* search an anime on animekayo.com
 ❍ `/airing <anime>`*:* returns anime airing info.
 ❍ /whatanime - reply to gif or video
"""

ANTIFLOOD = """
*Antiflood* allows you to take action on users that send more than x messages in a row. Exceeding the set flood \
will result in restricting that user.
 This will mute users if they send more than 10 messages in a row, bots are ignored.
 ❍ /flood*:* Get the current flood control setting
*Admins only:*
 ❍ /setflood <int/'no'/'off'>*:* enables or disables flood control
 *Example:* `/setflood 10`
 ❍ /setfloodmode <ban/kick/mute/tban/tmute> <value>*:* Action to perform when user have exceeded flood limit. ban/kick/mute/tmute/tban
*Note:*
 ❍ Value must be filled for tban and tmute!!
 It can be:
 `5m` = 5 minutes
 `6h` = 6 hours
 `3d` = 3 days
 `1w` = 1 week
"""