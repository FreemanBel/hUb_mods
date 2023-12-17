# English Language file
#
# Copyright 2020-2023 nunopenim @github
# Copyright 2020-2023 prototype74 @github
# Copyright 2023 freemanbel @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

NAME = "English"  # default language


class AdminText(object):
    USERS_IN_CHAT = "Users in **{}**"
    UNABLE_GET_USERS = "`Unable to get users from this chat`"



class GeneralMessages(object):
    UNKNOWN = "Unknown"

# Save your eyes from what may become the ugliest part of this userbot.
class ModuleDescriptions(object):
    ADMINPLUS_DESC = ("A module to help you get first 100 users in groups. "
                      "Command: userlist\n\n"
                      "Note: commands may require admin "
                      "privileges to work properly.")


class ModuleUsages(object):
    # KEEP CORRECT DICT FORMAT!!
    # {"cmd": {"args": ARGUMENTS, "usage": USAGE}} edit ARGUMENTS and
    # USAGE only!
    ADMINPLUS_USAGE = {"userlist": {"args": "[optional: <link/id>]",
                                    "usage": ("lists first 100 users from a "
                                              "channel or group (remotely). "
                                              "May requires admin privileges in "
                                              "channels.")}}
