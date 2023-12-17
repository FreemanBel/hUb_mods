# Copyright 2020-2023 nunopenim @github
# Copyright 2020-2023 prototype74 @github
# Copyright 2023 freemanbel @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

from userbot.include.language_processor import AdminText as msgRep
from userbot.modules_user.include.user_language_processor import (AdminText as msgRepPlus,
                                                ModuleDescriptions as descRepPlus,
                                                ModuleUsages as usageRepPlus)
from userbot.sysutils.configuration import getConfig
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import (register_cmd_usage,
                                           register_module_desc,
                                           register_module_info)
from userbot.version import VERSION
from telethon.errors import (UserAdminInvalidError, ChatAdminRequiredError,
                             AdminsTooMuchError, AdminRankEmojiNotAllowedError)
from telethon.tl.types import (ChatAdminRights, ChatBannedRights,
                               ChannelParticipantsAdmins, User, Channel,
                               PeerUser, PeerChannel)
from logging import getLogger

log = getLogger(__name__)
ehandler = EventHandler(log)
LOGGING = getConfig("LOGGING")


@ehandler.on(command="userlist", hasArgs=True, outgoing=True)
async def userlist(event):
    arg = event.pattern_match.group(1)
    if arg:
        try:
            arg = int(arg)
        except ValueError:
            pass

        try:
            chat = await event.client.get_entity(arg)
        except Exception as e:
            log.warning(e)
            await event.edit(msgRep.FAIL_CHAT)
            return
    else:
        chat = await event.get_chat()

    if not isinstance(chat, Channel):
        await event.edit(msgRep.NO_GROUP_CHAN_ARGS)
        return

    try:
        text = msgRepPlus.USERS_IN_CHAT.format(chat.title) + ":\n\n"
        num = 1
        async for member in (event.client.iter_participants(chat.id)):
            if member.deleted:
                text += f"{num}. {msgRep.DELETED_ACCOUNT}"
            elif member.username:
                text += f"{num}. @{member.username}"
            else:
                if member.last_name is not None:
                    text += (f"{num}. [{member.first_name} {member.last_name}]"
                             f"(tg://user?id={member.id})")
                else:
                    text += (f"{num}. [{member.first_name}]"
                             f"(tg://user?id={member.id})")
            text += f"\n id: {member.id}"
            if member.phone:
                text += f"\n phone: +{member.phone}"
            text += "\n"
            num += 1
            if num == 100:
                break
        await event.edit(text)
    except ChatAdminRequiredError:
        await event.edit(msgRep.NO_ADMIN)
    except Exception as e:
        log.warning(e)
        await event.edit(msgRepPlus.UNABLE_GET_USERS)
    return


for cmd in (["userlist"]):
    register_cmd_usage(
        cmd,
        usageRepPlus.ADMINPLUS_USAGE.get(cmd, {}).get("args"),
        usageRepPlus.ADMINPLUS_USAGE.get(cmd, {}).get("usage")
    )

register_module_desc(descRepPlus.ADMINPLUS_DESC)
register_module_info(
    name="Administration Plus",
    authors="nunopenim, prototype74, freemanbel",
    version=VERSION
)
