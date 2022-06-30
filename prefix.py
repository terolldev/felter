import json

default = "f+"

def get_prefix(bot, message):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  return prefixes[str(message.guild.id)]