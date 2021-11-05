#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) SL_Jana_Team

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Clinton
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


HELP_BOTTONS=InlineKeyboardMarkup([
        [InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about')],
        [InlineKeyboardButton("⚡ Telegram Sup 🗯", url="https://t.me/SL_Jana_Team")],
        [InlineKeyboardButton("🗂️ Report Bugs 🚨", url="https://t.me/SL_Jana_Team")],
         ])

ABOUT_BUTTONS=InlineKeyboardMarkup([
        [InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help')],
        [InlineKeyboardButton("📌️ Telegram Channel 🔎", url="https://t.me/SL_Jana_Team")],
        [InlineKeyboardButton("📌️ Telegram Group 🔎", url="https://t.me/joinchat/YiGR_JLyIG84ZmY1")],
        [InlineKeyboardButton("Developer 👨‍⚖️", url="https://t.me/SL_Jana_Team")],
     ])

START_BUTTONS=InlineKeyboardMarkup([
         [InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
          InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about')],
         [InlineKeyboardButton("📌️ Telegram Channel 🔎", url="https://t.me/SL_Jana_Team")],
         [InlineKeyboardButton("📌️ Telegram Group 🔎", url="https://t.me/joinchat/YiGR_JLyIG84ZmY1")],
         [InlineKeyboardButton("Developer 👨‍⚖️", url="https://t.me/SL_Jana_Team")],
                    ])

    @Clinton.on_callback_query(filters.private & filters.command([]))
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=Translation.HELP_USER,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Translation.ABOUT_USER,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
        
        
        


@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
      reply_markup=HELP_BOTTONS,
        reply_to_message_id=update.message_id
    )
    
    
@Clinton.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=Translation.ABOUT_USER.format(update.from_user.mention),
        disable_web_page_preview=True,
      reply_markup=ABOUT_BUTTONS,
        reply_to_message_id=update.message_id
    )

@Clinton.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
               reply_to_message_id=update.message_id
    )
    
    
    
    

    
   
                
            
        
    
