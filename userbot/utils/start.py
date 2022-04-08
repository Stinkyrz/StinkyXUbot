from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/30e0e9b8bff25972b723b.jpg",
                caption="⚡ **StinkyXUbot Berhasil Diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@StinkyXUbot\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @Stinkyrz ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/StinkySupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
