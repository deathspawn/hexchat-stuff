# Copyright (c) 2016 deathspawn
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#

from urllib.parse import urlencode
from urllib.request import urlopen
import hexchat

__module_name__ = 'Pirate Translator'
__module_author__ = 'deathspawn'
__module_version__ = '1'
__module_description__ = 'Translate text to pirate speak.'

def pirate(jargon):
    phrase = jargon
    phrase = phrase.lstrip("\'").rstrip("\'")
    query = urlencode({ 'typing' : phrase.replace('<','{`{') })
    url = "http://postlikeapirate.com/AJAXtranslate.php?" + query
    doc = urlopen(url)
    response = doc.read().decode('utf8', 'ignore')
    #response = response.replace('{`{','<').encode('utf8', 'ignore')
    return str(response)

def pirate_func(word, word_eol, userdata):
    try:
        try:
            subcommand = word[1].lower()
        except IndexError:
            subcommand = None
        if subcommand == None:
            hexchat.prnt("Error: Please include something to translate. Use -e to echo and -m for emote.")
        elif subcommand == "-e":
            try:
                pirate_jargon = word_eol[2]
                hexchat.prnt(pirate(pirate_jargon))
            except IndexError:
                hexchat.prnt("Error: Please include something to translate. Use -e to echo and -m for emote.")
        elif subcommand == "-m":
            try:
                pirate_jargon = word_eol[2]
                hexchat.command("ME "+pirate(pirate_jargon))
            except IndexError:
                hexchat.prnt("Error: Please include something to translate. Use -e to echo and -m for emote.")
        else:
            try:
                pirate_jargon = word_eol[1]
                hexchat.command("SAY "+pirate(pirate_jargon))
            except IndexError:
                hexchat.prnt("Error: Please include something to translate. Use -e to echo and -m for emote.")
        return hexchat.EAT_ALL
    except IndexError:
        pass
    return hexchat.EAT_NONE

def unload(userdata):
    hexchat.prnt(__module_name__+" "+__module_version__+" unloaded.")

hexchat.prnt(__module_name__+" "+__module_version__+" loaded. Use /pirate <text to translate> and /pirate -e <text to translate> for echo and -m for emote.")

hexchat.hook_unload(unload)
hexchat.hook_command("pirate", pirate_func)
