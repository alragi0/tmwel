import os
import asyncio
from asyncio.subprocess import PIPE

from mody.Redis import db
from mody.get_info import sudo_info
from mody.mod import Bot

async def run_session(session):
    cmd = f"screen -d -m -S {session[:50]} python3 users.py {session}"
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=PIPE,
        stderr=PIPE,
        shell=True
    )
    await proc.communicate()

async def auto_run():
    while True:
        for session in db.smembers(f'{Bot.me.id}:{sudo_info.id}:sessions'):
            proc = await asyncio.create_subprocess_exec(
                "screen",
                "-ls",
                stdout=PIPE,
                stderr=PIPE,
            )
            stdout, stderr = await proc.communicate()
            res = stdout.decode()
            if session[:50] not in res:
                asyncio.create_task(run_session(session))
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(auto_run())
