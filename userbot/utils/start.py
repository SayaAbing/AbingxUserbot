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
                "https://telegra.ph/file/be26ac5cf24ca73e0548e.jpg",
                caption="⚡ **Dx-Userbot Berhasil Diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@Dx-Userbot\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @ZeannProject ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/ZeanSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
