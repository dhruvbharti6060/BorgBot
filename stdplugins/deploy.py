"""Emoji

Available Commands:

.deploy"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "deploy":

        await event.edit(input_str)

        animation_chars = [
        
            "**Heroku Connecting To Latest Github Build (BorgBot)**",
            "**Build started by user** @prabal007",
            "**Deploy** `696969` **by user** @prabal007",
            "**Restarting Heroku Server...**",
            "**Status changed from up to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 143`",
            "**Starting process with command** `python3 -m stdborg`",
            "**Status changed from starting to up**",
            "__INFO:UniBorg:Logged in as  713761864__",
            "__INFO:UniBorg:Successfully loaded all plugins__",
            "**Build Succeeded**"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
