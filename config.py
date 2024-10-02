import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "20478011")
    API_HASH  = os.environ.get("API_HASH", "0e4dcf39643e83c3c174a0d2370e5b4a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7077374297:AAGgxSqJOrJ5GR8E3iiphrAzpL1FT1RW3Fk") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","baji")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://suryagupta1928:6thfnQ3AxzK6VJUA@cluster0.6ppqasw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/01J.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2061656269').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', '0').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002306621324"))
    PORT = int(os.environ.get("PORT", "8078"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot
    
➻ Using This Bot You Can Auto Rename Of Your Files
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption
    
➻ Use /tutorial Command To Know How To Use Me

<b>Bot Is Made By @MuGiWaRaNoLuFFY23</b>

<b><a href='https://t.me/Anime_Sparta'>Sparta</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @Anime_Sparta </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Anime_Sparta'>Anime Sparta</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/MuGiWaRaNoLuFFY23'>Son Goku</a>
    
<b>♻️ Bot Made By :</b> @MuGiWaRaNoLuFFY23"""
    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @Anime_Sparta" -metadata author="@Anime_Sparta" -metadata:s:s title="Subtitled By :- @Anime_Sparta" -metadata:s:a title="By :- @Anime_Sparta" -metadata:s:v title="By:- @Anime_Sparta" </code>"""


    
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
┣⪼ 😶‍🌫️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ: @Anime_Sparta
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 1 Rs Upto Your Choice.
    
<b>Dm - @MuGiWaRaNoLuFFY23</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
 https://t.me/MuGiWaRaNoLuFFY23"""





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @PandaWep
# Developer @AshutoshGoswami24
