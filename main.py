import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()
chicktron_hate_crimes = ["chicktron gay", "ban chicktron", "fuck chicktron", "chicktron ban", "chicktron je zly", "chicktron je nahovno"]
starter_comebacks = ["No u", "ok bomer", "kden"]
emojis = [":orangutan:", ":sunglasses:", ":control_knobs:", ":flushed:", ":partying_face:", ":dancer:",":eye::lips::eye:", ":mechanical_leg:", ":bamboo:", ":hamburger:"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = '*"'+json_data[0]["q"] + '"*\n -' + json_data[0]["a"]
  return(quote)

def get_funaz():
  response = requests.get("https://official-joke-api.appspot.com/random_joke")
  json_data = json.loads(response.text)
  funaz = "**"+json_data["setup"]+"**\n"+json_data["punchline"]
  return(funaz)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="c!help"))
  print("{0.user} is online! And working, hopefully...".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("c!help"):
    if message.content.startswith("c!help useful"):
      await message.channel.send('```yaml\n--== Chicktron Useful Commands Page ==--\n\n\nCommands are prefixed with: c!\n\n- info: Info about Chicktron\n- rand: Takes 2 numbers, generates a random one between the 2 (example: "c!rand 1 10" would return a random number between 1-10)```')
    elif message.content.startswith("c!help fun"):
      await message.channel.send("```yaml\n--== Chicktron Fun Commands Page ==--\n\n\nCommands are prefixed with: c!\n\n- funaz: Random joke (fuňáz)\n- quote: Random inspirational quote\n- say: Make Chicktron say something\n\n- Reply Commands: chicktron, idk\n\nCan you find the 3 secret commands?```")
    else:
      await message.channel.send("```yaml\n--== Chicktron Help Commands Page ==--\n\n\nCommands are prefixed with: c!\n\n- help: This help\n- help useful: Useful commands\n- help fun: Fun commands```")

  if message.content.startswith("c!chicktron"):
    await message.channel.send("cock-a-doodle-doo")

  if message.content.startswith("c!idk"):
    await message.channel.send("idk")

  if message.content.startswith("%appdata%"):
    await message.channel.send(".minecraft")
    
  if message.content.startswith("c!secret"):
    await message.channel.send("https://Chicktron.leosefcik.repl.co")
  
  if message.content.startswith("c!info"):
    await message.channel.send("```yaml\n- == Chicktron == -\n\nProgrammed by: leosefcik#3401\n\nA random bot created way back in 2017 for leosefcik's Discord server (which at the time of writing has 4 members, 2 of which are bots (yeah, it didn't take off)) Blue Ball Machine Topia. Back then, it didn't do anything, it was December of 2020 that it actually started doing bot stuff. It's written in Python and proves that even the biggest dummies (like leosefcik) can do a bot that at least does very useless stuff. It's not that big of a point, but whatever. Cock-a-doodle-doo! Visit c!help to see commands.```")

  if message.content.startswith("c!quote"):
    quote=get_quote()
    await message.channel.send(quote)

  if message.content.startswith("c!funaz"):
    funaz=get_funaz()
    await message.channel.send(funaz)

  if message.content.startswith("c!fuňáz"):
    funaz=get_funaz()
    await message.channel.send(funaz)
  
  if message.content.startswith('c!rand'):
    if message.content.startswith("c!rand "):
      nums = message.content.split(" ")
      NumberX = int(nums[1])
      NumberY = int(nums[2])
      msg = "`" + str(random.randint(NumberX,NumberY)) + "`"
      await message.channel.send(msg)
    else:
      await message.channel.send("```yaml\nUsage:\n\n- rand [1st number] [2nd number]```")
  
  if message.content.startswith("c!say"):
    if message.content.startswith("c!say "):
      saz = message.content.split(" ")
      msg = str("")
      for x in range(1,len(saz)):
        msg = msg + " " + saz[x]
      await message.channel.send(msg)
    else:
      await message.channel.send("```yaml\nUsage:\n\n- say [message]```")
  
  if message.content.startswith("c!math "):
    methplus = message.content.split("+")
    calc = 0
    for x in range(1,len(methplus)):
      calc = calc + int(methplus[x])
    await message.channel.send(calc)

keep_alive()
client.run(os.getenv("TOKEN"))

#banan
