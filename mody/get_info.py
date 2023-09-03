from asyncio import get_event_loop
from pyrogram import Client

async def getBot_token():
    token = "6109895485:AAE43imQ2y0W_yDx5B_Fsdod_SWt7MyrKQg"
    sudo_username = "YYNNXXXX"
    sudo_id = "6699312679"
    user_bot = "EEObot"
    
    try: 
        from info import token
        bot = Client('MainBot', 23650675, '748bb442baf8fdb359be739d58ae9b07',
                     no_updates=True, in_memory=True, bot_token=token)
        await bot.start()
    except:
        from info import token
        bot = Client('MainBot', 23650675, '748bb442baf8fdb359be739d58ae9b07',
                     no_updates=True, in_memory=True, bot_token=token)
        await bot.start()            
   
    try:
        from info import sudo_username
        get_sudo = await bot.get_chat(sudo_username)
    except:
        pass
    
    try:
        from info import user_bot
        get_bot_tmwel = await bot.get_chat(user_bot)
    except:
        pass
    
    try:
        from info import user_id
    except:
        pass
    
    get_bot = await bot.get_me()
    await bot.stop()
    return token, get_sudo, get_bot, get_bot_tmwel

loop = get_event_loop()
token, sudo_info, get_bot, get_bot_tmwel = loop.run_until_complete(getBot_token())
