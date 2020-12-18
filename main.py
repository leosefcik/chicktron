import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

chicktron_hate_crimes = ["chicktron gay", "ban chicktron", "fuck chicktron", "chicktron ban", "chicktron je zly", "chicktron je nahovno"]
starter_comebacks = ["No u", "ok bomer", "kden"]
emojis = [":orangutan:", ":sunglasses:", ":control_knobs:", ":flushed:", ":partying_face:", ":dancer:",":eye::lips::eye:", ":mechanical_leg:", ":bamboo:", ":hamburger:",":m:",":money_with_wings:",":b:",":crab:",":moyai:",":cheese:",":rat:",":hot_face:",":lungs:",":sauropod:",":lobster:",":fish_cake:",":avocado:",":trackball:",":nazar_amulet:",":no_bicycles:",":clock330:",":sponge:",":spoon:"]
no_u_list = ["no u","No u","NO u","No U","NO U","nO u","nO U","no U","nou","Nou","NOu","NOU","nOu","nOU","noU","NoU"]
no_i_list = ["no i","No i","NO i","No I","NO I","nO i","nO I","no I","noi","Noi","NOi","NOI","nOi","nOI","noI","NoI"]
funaz_1_list= ["c!funaz1","c!fuňáz1","c!joke1","c!funaz","c!fuňáz","c!joke","c!funaz 1","c!fuňáz 1","c!joke 1"]
funaz_2_list= ["c!funaz2","c!fuňáz2","c!joke2","c!funaz 2","c!fuňáz 2","c!joke 2"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = '*"'+json_data[0]["q"] + '"*\n -' + json_data[0]["a"]
  return(quote)

def get_funaz1():
  response = requests.get("https://official-joke-api.appspot.com/random_joke")
  json_data = json.loads(response.text)
  funaz = "**"+json_data["setup"]+"**\n"+json_data["punchline"]
  return(funaz)

def get_funaz2():
  response = requests.get("https://sv443.net/jokeapi/v2/joke/Any")
  json_data = json.loads(response.text)
  if json_data["type"] == "single":
    funaz = json_data["joke"]
  else:
    funaz = "**" + json_data["setup"] + "**\n" + json_data["delivery"]
  return(funaz)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="c!help"))
  print("{0.user} is online! And working, hopefully...".format(client))

@client.event
async def on_message(message):
  msg = ""
  if message.author == client.user:
    return
  
  if message.content.startswith("c!help"):
    if message.content.startswith("c!help useful"):
      await message.channel.send('```yaml\n--== Chicktron Useful Commands Page ==--\n\n\nCommands are prefixed with: c!\n\n- info: Info about Chicktron\n- rand: Takes 2 numbers, generates a random one between the 2 (example: "c!rand 1 10" would return a random number between 1-10)```')
    elif message.content.startswith("c!help fun"):
      await message.channel.send("```yaml\n--== Chicktron Fun Commands Page ==--\n\n\nCommands are prefixed with: c!\n\n- funaz/joke: Random joke (fuňáz)\n- funaz/joke2: Random joke from 2nd database, may contain inappropriate jokes\n- quote: Random inspirational quote\n- emoji: Gives you an emoji from a list of them\n\n- Prefixed Reply Commands: chicktron, idk, dozadgaming, h, s, vajca\n- Unprefixed Reply Commands: %appdata%, 2+2, get real, death, banánstvo, lolic, ňrat\n\nCan you find the secret commands? There could be only one, or there could be a bunch of them...```")
    elif message.content.startswith("c!help features"):
      await message.channel.send("```yaml\n--== Chicktron Features Page ==--\n\n\n- no u: no u\n- no i: yes u\n\nEvery message, there's a 1 in 10000 chance for Chicktron to say something very rare O_O```")
    else:
      await message.channel.send("```yaml\n--== Chicktron Help Commands Page ==--\n\n\nCommands are prefixed with: c!\n\n- help: This help\n- help useful: Useful commands\n- help fun: Fun commands\n- help features: Passive chicktron actions```")

  if message.content.startswith("c!chicktron"):
    await message.channel.send("cock-a-doodle-doo")

  if message.content.startswith("c!idk"):
    await message.channel.send("idk")

  if message.content.startswith("%appdata%"):
    await message.channel.send(".minecraft")
    
  if message.content.startswith("c!secret"):
    await message.channel.send("https://Chicktron.leosefcik.repl.co")
  
  if message.content.startswith("c!info"):
    await message.channel.send("```yaml\n- == Chicktron == -\n\nProgrammed by: leosefcik#3401\n\nA random bot created way back in 2017 for leosefcik's Discord server (which at the time of writing has 4 members, 2 of which are bots (yeah, it didn't take off)) Blue Ball Machine Topia. Back then, it didn't do anything, it was December of 2020 that it actually started doing bot stuff. It's written in Python and proves that even the biggest dummies (like leosefcik) can do a bot that at least does very useless stuff. It's not that big of a point, but whatever. Cock-a-doodle-doo! Visit c!help to see commands. Recommended Chicktron name color - #c3f794```")

  if message.content.startswith("c!quote"):
    quote=get_quote()
    await message.channel.send(quote)

  if any(word in message.content for word in funaz_2_list):
    funaz=get_funaz2()
    await message.channel.send(funaz)
  elif any(word in message.content for word in funaz_1_list):
    funaz=get_funaz1()
    await message.channel.send(funaz)
  
  
  if message.content.startswith("2+2"):
    emoji = random.randint(0,len(emojis))
    msg = "4 "+emojis[emoji]
    await message.channel.send(msg)
  
  if message.content.startswith('c!rand'):
    if message.content.startswith("c!rand "):
      nums = message.content.split(" ")
      NumberX = int(nums[1])
      NumberY = int(nums[2])
      msg = "`" + str(random.randint(NumberX,NumberY)) + "`"
      await message.channel.send(msg)
    else:
      await message.channel.send("```yaml\nUsage:\n\n- rand [1st number] [2nd number]```")
  
#  if message.content.startswith("c!say"):
#    if message.content.startswith("c!say "):
#      saz = message.content.split(" ")
#      msg = str("")
#      for x in range(1,len(saz)):
#        msg = msg + " " + saz[x]
#      await message.channel.send(msg)
#    else:
#      await message.channel.send("```yaml\nUsage:\n\n- say [message]```")
  
  if message.content.startswith("c!math "):
    methplus = message.content.split("+")
    calc = 0
    for x in range(1,len(methplus)):
      calc = calc + int(methplus[x])
    await message.channel.send(calc)

  if message.content.startswith("c!emoji"):
    await message.channel.send(random.choice(emojis))

  if message.content.startswith("get real"):
    await message.channel.send("https://tenor.com/view/get-real-chinese-egg-man-chinese-guy-eats-raw-eggs-raw-eggs-raw-eggs-chug-gif-19458097")

  if message.content.startswith("death"):
    await message.channel.send("https://tenor.com/view/walter-white-falling-fast-gif-18043850")

  if message.content.startswith("banánstvo"):
    await message.channel.send(":banana:")

  if message.content.startswith("c!dozadgaming"):
    await message.channel.send("https://tenor.com/view/fish-lip-thicc-thick-nibba-gif-13850958")

  if message.content.startswith("c!h"):
    if message.content.startswith("c!help"):
      print("nothing")
    else:
      await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789529752854986772/h.gif")

  if message.content.startswith("c!s"):
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789529764926849045/s.gif")

  if message.content.startswith("lolic"):
    await message.channel.send("https://cdn.discordapp.com/attachments/693552113254662256/760953024247496774/image0.gif")
  
  if message.content.startswith("ňrat"):
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789532988458795021/nrat.mp4")

  if message.content.startswith("c!vajca"):
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789534999929815090/vajca.mp4")

  if any(word in message.content for word in no_u_list):
    await message.channel.send(message.content)

  if any(word in message.content for word in no_i_list):
    await message.channel.send("yes u")


  secret=random.randint(1,100000)
  if secret==69:
    await message.channel.send("This message has a 1 in 100000 chance of showing up!")

#  if client.user.mentioned_in(message):
#    await message.channel.send("https://media.discordapp.net/attachments/710878721615200368/781576144210100234/image0-1.gif")

keep_alive()
client.run(os.getenv("TOKEN"))

# Setting `Playing ` status
#await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
#await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

#banan
