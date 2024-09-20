import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21740783")
    API_HASH  = os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7541201119:AAGTK0XIH-fD9T-BdNl7A7BEaLkKx8GpG4E") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","baji")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://taki:taki@taki710.lk8s5t1.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/w6Y.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1501687881 6321064549').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', '0').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002080756028"))
    PORT = int(os.environ.get("PORT", "8089"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot
    
➻ Using This Bot You Can Auto Rename Of Your Files
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption
    
➻ Use /tutorial Command To Know How To Use Me

<b>Bot Is Made By @VOATcb</b>

<b><a href='https://t.me/Manga_Yugen'>Yugen</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @Anime_Wide </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Manga_Yugen'>Manga Yugen</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/VOATcb'>Vot</a>
    
<b>♻️ Bot Made By :</b> @VOATcb"""
    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @Manga_Yugen" -metadata author="@Manga_Yugen" -metadata:s:s title="Subtitled By :- @Manga_Yugen" -metadata:s:a title="By :- @Manga_Yugen" -metadata:s:v title="By:- @Manga_Yugen" </code>"""


    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 😶‍🌫️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ: @Manga_Yugen
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 1 Rs Upto Your Choice.
    
<b>Dm - @VOATcb</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
 https://t.me/Manga_Yugen_Group"""





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @PandaWep
# Developer @AshutoshGoswami24
