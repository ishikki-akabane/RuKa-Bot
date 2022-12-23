import html
import socket
import random
import sys
from time import time
import json
from datetime import datetime
from platform import python_version
from typing import List
from uuid import uuid4
from pyrogram import __version__ as pyrover
from pyrogram import filters, errors

import requests
from telegram import InlineQueryResultArticle, ParseMode, InlineQueryResultPhoto, InputTextMessageContent, Update, InlineKeyboardMarkup, \
    InlineKeyboardButton
from telegram import __version__
from telegram.error import BadRequest
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler,
                          Filters, MessageHandler)
from telegram.utils.helpers import mention_html
import SUMI.modules.sql.users_sql as sql
from SUMI import (
    OWNER_ID,
    DRAGONS,
    DEMONS,
    DEV_USERS,
    TIGERS,
    WOLVES,
    pgram,
    sw, LOGGER
)
from SUMI.modules.helper_funcs.misc import article
from SUMI.modules.helper_funcs.decorators import SUMIinline
from SUMI.modules.sudoers import bot_sys_stats as bss


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        text = text.replace(prefix, "", 1)
    return text

@SUMIinline()
def inlinequery(update: Update, _) -> None:
    """
    Main InlineQueryHandler callback.
    """
    query = update.inline_query.query
    user = update.effective_user

    results: List = []
    inline_help_dicts = [
        {
            "title": "Hentai",
            "description": "Get Hentai And Pornhwa Channel Link",
            "message_text": "Click the button below to get the links.",
            "thumb_urL": "https://telegra.ph/file/2466b0d2e524b8d47a73d.jpg",
            "keyboard": ".hentai",
        },
         {
            "title": "Anime Cruise",
            "description": "Get Anime Channel Link",
            "message_text": "Click the button below to get the links.",
            "thumb_urL": "https://telegra.ph/file/941e6d601c37c3ddf2925.jpg",
            "keyboard": ".anime",
        },
        {
            "title": "SUMI",
            "description": "SUMI Inline",
            "message_text": "Click the button below to get the SUMI Inline.",
            "thumb_urL": "https://telegra.ph/file/93b575c4c4da42d9fa4b2.jpg",
            "keyboard": ".SUMI",
        },
        {
            "title": "Kaizuryu",
            "description": "The Kaizuryu",
            "message_text": "Click the button below to get the Kaizuryu Network Info.",
            "thumb_urL": "https://telegra.ph/file/5daac1fcf88ca6f177ef4.jpg",
            "keyboard": ".kaizuryu",
        },
        {
            "title": "Account info on SUMI",
            "description": "Look up a Telegram account in SUMI database",
            "message_text": "Click the button below to look up a person in SUMI database using their Telegram ID",
            "thumb_urL": "https://telegra.ph/file/3c93a66c6751088a00fbd.jpg",
            "keyboard": ".info",
        },
        {
            "title": "Help",
            "description": "Help Inline Commands",
            "message_text": "Click the button below to get Help Of Inline Commands.",
            "thumb_urL": "https://telegra.ph/file/645e0b5ca6382d6d73ab5.jpg",
            "keyboard": ".help",
        },
        {
            "title": "Anilist",
            "description": "Search anime and manga on AniList.co",
            "message_text": "Click the button below to search anime and manga on AniList.co",
            "thumb_urL": "https://telegra.ph/file/ace91d9ae6af3881d3940.jpg",
            "keyboard": ".anilist",
        },
    ]

    inline_funcs = {
        ".info": inlineinfo,
        ".hentai": hentai,
        ".SUMI": SUMI,  
        ".anime": anime,
        ".kaizuryu": kaizuryu,
        ".anilist": media_query,
        ".help": help,
    }

    if (f := query.split(" ", 1)[0]) in inline_funcs:
        inline_funcs[f](remove_prefix(query, f).strip(), update, user)
    else:
        for ihelp in inline_help_dicts:
            results.append(
                article(
                    title=ihelp["title"],
                    description=ihelp["description"],
                    message_text=ihelp["message_text"],
                    thumb_url=ihelp["thumb_urL"],
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Click Here",
                                    switch_inline_query_current_chat=ihelp[
                                        "keyboard"
                                    ],
                                )
                            ]
                        ]
                    ),
                )
            )

        update.inline_query.answer(results, cache_time=5)


def inlineinfo(query: str, update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    bot = context.bot
    query = update.inline_query.query
    LOGGER.info(query)
    user_id = update.effective_user.id

    try:
        search = query.split(" ", 1)[1]
    except IndexError:
        search = user_id

    try:
        user = bot.get_chat(int(search))
    except (BadRequest, ValueError):
        user = bot.get_chat(user_id)

    chat = update.effective_chat
    sql.update_user(user.id, user.username)

    text = (
        f"<b>Information:</b>\n"
        f"• ID: <code>{user.id}</code>\n"
        f"• First Name: {html.escape(user.first_name)}"
    )

    if user.last_name:
        text += f"\n• Last Name: {html.escape(user.last_name)}"

    if user.username:
        text += f"\n• Username: @{html.escape(user.username)}"

    text += f"\n• Permanent user link: {mention_html(user.id, 'link')}"

    nation_level_present = False

    if user.id == OWNER_ID:
        text += f"\n\nThis person is my Owner"
        nation_level_present = True
    elif user.id in DEV_USERS:
        text += f"\n\nThis Person is a part Developer of SUMI"
        nation_level_present = True
    elif user.id in DRAGONS:
        text += f"\n\nThe Nation level of this person is Royal"
        nation_level_present = True
    elif user.id in DEMONS:
        text += f"\n\nThe Nation level of this person is Demon"
        nation_level_present = True
    elif user.id in TIGERS:
        text += f"\n\nThe Nation level of this person is Tiger Level Disaster"
        nation_level_present = True
    elif user.id in WOLVES:
        text += f"\n\nThe Nation level of this person is Wolf Level Disaster"
        nation_level_present = True

    if nation_level_present:
        text += ' [<a href="https://t.me/{}?start=nations">?</a>]'.format(bot.username)

    try:
        spamwtc = sw.get_ban(int(user.id))
        if spamwtc:
            text += "<b>\n\n• SpamWatched:\n</b> Yes"
            text += f"\n• Reason: <pre>{spamwtc.reason}</pre>"
            text += "\n• Appeal at @SpamWatchSupport"
        else:
            text += "<b>\n\n• SpamWatched:</b> No"
    except:
        pass  # don't crash if api is down somehow...

    num_chats = sql.get_user_num_chats(user.id)
    text += f"\n• <b>Chat count</b>: <code>{num_chats}</code>"




    kb = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Report Error",
                    url=f"https://t.me/SUMISupport",
                ),
                InlineKeyboardButton(
                    text="Search again",
                    switch_inline_query_current_chat=".info ",
                ),

            ],
        ]
        )

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            thumb_url="https://telegra.ph/file/0b5e88c90238c357641a7.jpg",
            title=f"User info of {html.escape(user.first_name)}",
            input_message_content=InputTextMessageContent(text, parse_mode=ParseMode.HTML,
                                                          disable_web_page_preview=True),
            reply_markup=kb
        ),
    ]

    update.inline_query.answer(results, cache_time=5)


def hentai(query: str, update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    user_id = update.effective_user.id
    user = context.bot.get_chat(user_id)
    sql.update_user(user.id, user.username)
    about_text = f"""
    • [Hentai Forever](https://t.me/+S6Kq1YC5bxkwZjgx) \n• [Pornhwa Heaven](https://t.me/+jKF-knaR0LE5MzYx) \n• [Hentai Chat Group](https://t.me/+TOAvpiqpUeoxMzdh)
    """
    results: list = []
    kb = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Hentai",
                    url=f"https://t.me/+S6Kq1YC5bxkwZjgx",
                ),

            ],
            [
                InlineKeyboardButton(
                    text="Pornhwa",
                    url=f"https://t.me/+jKF-knaR0LE5MzYx",
                ),

            ],
        ])

    results.append(
        InlineQueryResultPhoto(
            id=str(uuid4()),
            title="Hentai",
            description="Get Hentai Channel Link",
            thumb_url="https://telegra.ph/file/2466b0d2e524b8d47a73d.jpg",
            photo_url="https://telegra.ph/file/2466b0d2e524b8d47a73d.jpg",
            caption=about_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb,
        )
    )
    update.inline_query.answer(results)
    
def SUMI(query: str, update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    user_id = update.effective_user.id
    user = context.bot.get_chat(user_id)
    sql.update_user(user.id, user.username)
    about_text = f"""
    ──── • SUMI Langley Soryu • ────
    """
    results: list = []
    kb = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="SUMI Robot",
                    url=f"https://t.me/SUMI",
                ),

            ],
            [
                InlineKeyboardButton(
                    text="Support",
                    url=f"https://t.me/SUMISupport",
                ),
                 InlineKeyboardButton(
                    text="Updates",
                    url=f"https://t.me/SUMIUpdates",
                ),

            ],
            [
                InlineKeyboardButton(
                    text="Try Inline",
                    switch_inline_query_current_chat="",
                ),

            ],
        ])

    results.append(
        InlineQueryResultPhoto(
            id=str(uuid4()),
            title="SUMI",
            description="Get SUMI Inline",
            thumb_url="https://telegra.ph/file/62ad4ddfcb9ec5189a590.jpg",
            photo_url="https://telegra.ph/file/f6be5a2866ae719a17fb0.jpg",
            caption=about_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb,
        )
    )
    update.inline_query.answer(results)

MEDIA_QUERY = '''query ($search: String) {
  Page (perPage: 10) {
    media (search: $search) {
      id
      title {
        romaji
        english
        native
      }
      type
      format
      status
      description
      episodes
      bannerImage
      duration
      chapters
      volumes
      genres
      synonyms
      averageScore
      airingSchedule(notYetAired: true) {
        nodes {
          airingAt
          timeUntilAiring
          episode
        }
      }
      siteUrl
    }
  }
}'''


def media_query(query: str, update: Update, context: CallbackContext) -> None:
    """
    Handle anime inline query.
    """
    results: List = []

    try:
        results: List = []
        r = requests.post('https://graphql.anilist.co',
                          data=json.dumps({'query': MEDIA_QUERY, 'variables': {'search': query}}),
                          headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        res = r.json()
        data = res['data']['Page']['media']
        res = data
        for data in res:
            title_en = data["title"].get("english") or "N/A"
            title_ja = data["title"].get("romaji") or "N/A"
            format = data.get("format") or "N/A"
            type = data.get("type") or "N/A"
            bannerimg = data.get("bannerImage") or "https://telegra.ph/file/cc83a0b7102ad1d7b1cb3.jpg"
            try:
                des = data.get("description").replace("<br>", "").replace("</br>", "")
                description = des.replace("<i>", "").replace("</i>", "") or "N/A"
            except AttributeError:
                description = data.get("description")

            try:
                description = html.escape(description)
            except AttributeError:
                description = description or "N/A"

            if len((str(description))) > 700:
                description = description [0:700] + "....."

            avgsc = data.get("averageScore") or "N/A"
            status = data.get("status") or "N/A"
            genres = data.get("genres") or "N/A"
            genres = ", ".join(genres)
            img = f"https://img.anili.st/media/{data['id']}" or "https://telegra.ph/file/cc83a0b7102ad1d7b1cb3.jpg"
            aurl = data.get("siteUrl")


            kb = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Read More",
                            url=aurl,
                        ),
                        InlineKeyboardButton(
                            text="Search again",
                            switch_inline_query_current_chat=".anilist ",
                        ),

                    ],
                ])

            txt = f"<b>{title_en} | {title_ja}</b>\n"
            txt += f"<b>Format</b>: <code>{format}</code>\n"
            txt += f"<b>Type</b>: <code>{type}</code>\n"
            txt += f"<b>Average Score</b>: <code>{avgsc}</code>\n"
            txt += f"<b>Status</b>: <code>{status}</code>\n"
            txt += f"<b>Genres</b>: <code>{genres}</code>\n"
            txt += f"<b>Description</b>: <code>{description}</code>\n"
            txt += f"<a href='{img}'>&#xad</a>"

            results.append(
                InlineQueryResultArticle
                    (
                    id=str(uuid4()),
                    title=f"{title_en} | {title_ja} | {format}",
                    thumb_url=img,
                    description=f"{description}",
                    input_message_content=InputTextMessageContent(txt, parse_mode=ParseMode.HTML,
                                                                  disable_web_page_preview=False),
                    reply_markup=kb
                )
            )
    except Exception as e:

        kb = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Report error",
                        url="https://t.me/SUMISupport",
                    ),
                    InlineKeyboardButton(
                        text="Search again",
                        switch_inline_query_current_chat=".anilist ",
                    ),

                ],
            ])

        results.append(

            InlineQueryResultArticle
                (
                id=str(uuid4()),
                title=f"Media {query} not found",
                input_message_content=InputTextMessageContent(f"Media {query} not found due to {e}", parse_mode=ParseMode.MARKDOWN,
                                                              disable_web_page_preview=True),
                reply_markup=kb
            )

        )

    update.inline_query.answer(results, cache_time=5)

def help(query: str, update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    user_id = update.effective_user.id
    user = context.bot.get_chat(user_id)
    sql.update_user(user.id, user.username)
    help_text = f"""
     [SUMI Inline Help](https://t.me/SUMI)\n*Inline Help Commands:*\n*• .hentai:* `You Can Get Hentai Links`\n*• .kaizuryu* `To Check Out Kaizuryu Network`\n*• .anilist:* `To Search Animes And Mangas`\n*• .info:* `To Check Your Information`\n• Want your own inline on @SUMI? You can get it in low pricing by contacting @Xelcius
     """
    results: list = []
    kb = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Search Inline",
                    switch_inline_query_current_chat=".info ",
                ),

            ],
        ])

    results.append(
        InlineQueryResultPhoto(
            id=str(uuid4()),
            title="Help Commands",
            thumb_url="https://telegra.ph/file/0b5e88c90238c357641a7.jpg",
            photo_url="https://telegra.ph/file/f975d75dabca471894485.jpg",
            caption=help_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb,
        )
    )
    update.inline_query.answer(results)

@pgram.on_callback_query(filters.regex("pingCB"))
async def stats_callbacc(_, CallbackQuery):
    text = await bss()
    await pgram.answer_callback_query(CallbackQuery.id, text, show_alert=True)

def _netcat(host, port, update: Update, context: CallbackContext):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    content = update.inline_query.query.split(" ", 1)[1]
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096).decode("utf-8").strip("\n\x00")
        if not data:
            break
        return data
    s.close()
    
def kaizuryu(query: str, update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    user_id = update.effective_user.id
    user = context.bot.get_chat(user_id)
    sql.update_user(user.id, user.username)
    about_text = f"""
    ──── • The Kaizuryu Network • ────
    """
    results: list = []
    kb = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Kaizuryu Network",
                    url=f"https://t.me/TheKaizuryu",
                ),

            ],
            [
                InlineKeyboardButton(
                    text="Chat Group",
                    url=f"https://t.me/+RH-EofbQPhwyNGE1",
                ),

            ],
        ])

    results.append(
        InlineQueryResultPhoto(
            id=str(uuid4()),
            title="Kaizuryu",
            description="Get Kaizuryu Network Link",
            thumb_url="https://telegra.ph/file/5daac1fcf88ca6f177ef4.jpg",
            photo_url="https://telegra.ph/file/5daac1fcf88ca6f177ef4.jpg",
            caption=about_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb,
        )
    )
    update.inline_query.answer(results)
    
def anime(query: str, update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    user_id = update.effective_user.id
    user = context.bot.get_chat(user_id)
    sql.update_user(user.id, user.username)
    about_text = f"""
    ‣ Anime Cruise • Kaizuryu \n\n• Uploading All The Latest Animes \n• Best Quality, Low Size Encoded \n• One Tap Channel Access
    """
    results: list = []
    kb = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Join Now",
                    url=f"https://t.me/Anime_Cruise",
                ),

            ],
            [
                InlineKeyboardButton(
                    text="Index",
                    url=f"https://t.me/Cruise_Index",
                ),

            ],
        ])

    results.append(
        InlineQueryResultPhoto(
            id=str(uuid4()),
            title="Anime",
            description="Get Anime Cruise Link",
            thumb_url="https://telegra.ph/file/941e6d601c37c3ddf2925.jpg",
            photo_url="https://telegra.ph/file/941e6d601c37c3ddf2925.jpg",
            caption=about_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb,
        )
    )
    update.inline_query.answer(results)
