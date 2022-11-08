class script(object):
    START_TXT = """ Hey {} I Am Ｔｅｓｓａ ＡＦ !\nI Am Bot With Open Source Project \nCheck Source Button To Get Source Link\n
 ✰ I Am A Advanced AutoFilter Bot Made with Python By #ʀᴇǫᴜᴇsᴛʙᴏx1\nEnjoy By Adding To Your Group """
    HELP_TXT = """Hey {}\nʜᴀᴘᴘʏ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✩ ＥＮＪＯＹ ✩
  𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂"""
    ABOUT_TXT = """
✩ ᴄʀᴇᴀᴛᴏʀ <a href=https://t.me/know_sarthak16>✮ ꜱᴀʀᴛʜᴀᴋ ✮</a>
✧ ʟɪʙʀᴀʀʏ : ᴜᴋɴᴏᴡɴ ⚠︎
✩ ᴘʏᴛʜᴏɴ : 3.6+
✧ ᴅᴀᴛᴀʙᴀsᴇ : ‌🇵‌‌🇷‌‌🇮‌‌🇻‌‌🇦‌‌🇹‌‌🇪‌
✩ sᴇʀᴠᴇʀ : ☁︎︎✈︎ [𝙵𝙻𝙸𝙶𝙷𝚃𝙼𝙾𝙳𝙴]
✧ ᴠᴇʀsɪᴏɴ : ☃︎𝙑 8.0.5
✰ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇ : <a href=https://t.me/know_sarthak16>✪ ꜱᴀʀᴛʜᴀᴋ ✪</a>
✰ sᴏᴜʀᴄᴇ : <a href=https://github.com/sarthakxd16/Tessa-AF>✪ Ｔｅｓｓａ ＡＦ✪</a>
"""
    SOURCE_TXT = """<b>NOTE:</b>
- ＴｅｓｓａＡＦ is a open source project
- Maintained By #ʀᴇǫᴜᴇsᴛʙᴏx1

<b>DEVS:</b>
☞   <a href=https://t.me/sarthakkale16> ➪ Ｄｅｖ １ ✫</a> \n
☞   <a href=https://t.me/dev_brahmastra> ➪ Ｄｅｖ ２ ✫</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ＴＥＳＳＡ ＡＦwill respond whenever a keyword is found the message

<b>NOTE:</b>
1. Ｔｅｓｓａ ＡＦhould have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- TessaAF Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Ｔｅｓｓａ ＡＦsupports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/rb1official)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Ｔｅｓｓａ ＡＦ

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★  : <code>{}</code>
★  : <code>{}</code>
★  : <code>{}</code>
★  : <code>{}</code> 
★  : <code>{}</code> 
★Powered By Ｔｅｓｓａ ＡＦ !"""
    LOG_TEXT_G = """#NewGroup Of Ｔｅｓｓａ ＡＦ
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser Of Ｔｅｓｓａ ＡＦ
ID - <code>{}</code>
Name - {}
"""
