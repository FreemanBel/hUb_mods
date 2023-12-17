# Copyright 2020-2023 nunopenim @github
# Copyright 2020-2023 prototype74 @github
# Copyright 2023 freemanbel @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

# from userbot.sysutils.configuration import getConfig
from importlib import import_module
from logging import getLogger
from sys import _getframe
from userbot.include.language_processor import (getBotLangCode,
                                                getLangString,
                                                getBotLang)

log = getLogger(__name__)

# Language selector logic


__botlangcode__ = getBotLangCode()
__botlangname__ = "Unknown"

try:
    lang = import_module("userbot.modules_user." + __botlangcode__)
except ModuleNotFoundError:  # Language file not found
    if not __botlangcode__ == "en":
        log.warning(f"'{__botlangcode__}' module language file not found. Make sure "
                    "it exists! Should have the same name as the UBOT_LANG "
                    "config in your config file. Attempting to load default "
                    "language...")
        try:
            lang = import_module("userbot.modules_user.en")
        except ModuleNotFoundError:
            log.error("Default module language file not found, bot quitting!")
            quit(1)
        except Exception:
            log.error("Unable to load default module language file, bot quitting!",
                      exc_info=True)
            quit(1)
    else:
        log.error("Default module language file not found, bot quitting!")
        quit(1)
except Exception:  # Unhandled exception in language file
    if not __botlangcode__ == "en":
        log.warning(f"There was a problem loading the '{__botlangcode__}' "
                    "module language file. Attempting to load default "
                    "language...", exc_info=True)
        try:
            lang = import_module("userbot.translations.en")
        except ModuleNotFoundError:
            log.error("Default language file not found, bot quitting!")
            quit(1)
        except Exception:
            log.error("Unable to load module default language file, bot quitting!",
                      exc_info=True)
            quit(1)
    else:
        log.error("Unable to load default module language file, bot quitting!",
                  exc_info=True)
        quit(1)

if hasattr(lang, "NAME"):
    __botlangname__ = lang.NAME
log.info(f"Loading {__botlangname__} module language")

try:
    if lang.__name__ == "userbot.modules_user.en":
        dlang = lang
    else:
        dlang = import_module("userbot.modules_user.en")
except ModuleNotFoundError:
    log.error("Default module language file not found, bot quitting!")
    quit(1)
except Exception:
    log.error("Unable to load default module language file, bot quitting!",
              exc_info=True)
    quit(1)

# Language processor!


class AdminText(object):
    USERS_IN_CHAT = getLangString(
        lang, _getframe().f_code.co_name, "USERS_IN_CHAT")
    UNABLE_GET_USERS = getLangString(
        lang, _getframe().f_code.co_name, "UNABLE_GET_USERS")


class GeneralMessages(object):
    UNKNOWN = getLangString(
        lang, _getframe().f_code.co_name, "UNKNOWN")


class ModuleDescriptions(object):
    ADMINPLUS_DESC = getLangString(
        lang, _getframe().f_code.co_name, "ADMINPLUS_DESC")


class ModuleUsages(object):
    ADMINPLUS_USAGE = getLangString(
        lang, _getframe().f_code.co_name, "ADMINPLUS_USAGE")


del lang, dlang  # clean up
log.info("{} module language loaded successfully".format(
    getBotLang().replace(GeneralMessages.UNKNOWN, "Unknown")))
