import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://telegra.ph/file/6d1572e7ec3179ae5452f.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ 𝗞𝗜𝗡𝗚 𝗫 𝗧𝗘𝗔𝗠 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **ᴋɪɴɢ x ᴛᴀ ᴠᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/ll_VIP_SUPPORT_ll"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/II_VIP_CHATTING_ZONE_II")], [Button.url("• ʀᴇᴘᴏ •", "https://github.com/WCGKING/KINGSPAM")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴋɪɴɢ x ᴛᴇᴀᴍ ʙʀᴀɴᴅᴇᴅ-ꜱᴘᴀᴍʙᴏᴛ!**") 
