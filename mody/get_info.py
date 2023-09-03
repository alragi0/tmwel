from asyncio import get_event_loop
from pyrogram import Client

async def getBot_token():
    token = "6109895485:AAE43imQ2y0W_yDx5B_Fsdod_SWt7MyrKQg"
    sudo_username = "YYNNXXXX"
    sudo_id = "6699312679"
    user_bot = "EEObot"
    
    try: 
        from get_info import token
        bot = Client('MainBot', 27786450, '1fb7b1af2837205d7ce8d77cefc0acbd',
                     no_updates=True, in_memory=True, bot_token=token)
        await bot.start()
    except:
        from info import token
        bot = Client('MainBot', 27786450, '1fb7b1af2837205d7ce8d77cefc0acbd',
                     no_updates=True, in_memory=True, bot_token=token)
        await bot.start()            
   
    try:
        from get_info import sudo_username
        get_sudo = await bot.get_chat(sudo_username)
    except:
        pass
    
    try:
        from get_info import user_bot
        get_bot_tmwel = await bot.get_chat(user_bot)
    except:
        pass
    
    try:
        from get_info import user_id
    except:
        pass
    
    get_bot = await bot.get_me()
    await bot.stop()
    return token, get_sudo, get_bot, get_bot_tmwel

loop = get_event_loop()
token, sudo_info, get_bot, get_bot_tmwel = loop.run_until_complete(getBot_token())
