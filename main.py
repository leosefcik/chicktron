import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from replit import db

client = discord.Client()

db["funaz_times_used"] = db["funaz_times_used"]
db["quote_times_used"] = db["quote_times_used"]
db["rand_times_used"] = db["rand_times_used"]
db["emoji_times_used"] = db["emoji_times_used"]
db["no_u_replies"] = db["no_u_replies"]
db["fun_reply_times_used"] = db["fun_reply_times_used"]
db["rare_message_appearances"] = db["rare_message_appearances"]

chicktron_hate_crimes = ["chicktron gay", "ban chicktron", "fuck chicktron", "chicktron ban", "chicktron je zly", "chicktron je nahovno"]
starter_comebacks = ["No u", "ok bomer", "kden"]
emojis = [":orangutan:", ":sunglasses:", ":control_knobs:", ":flushed:", ":partying_face:", ":dancer:",":eye::lips::eye:", ":mechanical_leg:", ":bamboo:", ":hamburger:",":m:",":money_with_wings:",":b:",":crab:",":moyai:",":cheese:",":rat:",":hot_face:",":lungs:",":sauropod:",":lobster:",":fish_cake:",":avocado:",":trackball:",":nazar_amulet:",":no_bicycles:",":clock330:",":sponge:",":spoon:"]
no_u = ["no u"]
cries = ["https://tenor.com/view/crying-cat-memes-meme-gif-19632395", "https://tenor.com/view/cry-about-it-gif-19162157", "https://tenor.com/view/sad-cry-crying-tears-broken-gif-15062040", "https://media.discordapp.net/attachments/671340986223296574/784521503412584509/image0-3.gif", "https://media.discordapp.net/attachments/296056831514509312/788619064884985927/image0.gif", "https://tenor.com/view/free-smiley-faces-de-emoji-sad-crying-cry-gif-16168301"]

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
  reply=""
  secret_key=random.randint(1,100000)
  msg=message.content.lower()
  if message.author == client.user:
    return
  print(message.content)

  ### PRIORITY COMMANDS ###
  if msg=="h" or msg=="c!h":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789529752854986772/h.gif")

  elif msg=="s" or msg=="c!s":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789529764926849045/s.gif")

  elif msg=="hs" or msg=="c!hs":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789529752854986772/h.gif\nhttps://cdn.discordapp.com/attachments/743569092061036644/789529764926849045/s.gif")

  elif msg=="sh" or msg=="c!sh":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789529764926849045/s.gif\nhttps://cdn.discordapp.com/attachments/743569092061036644/789529752854986772/h.gif")

  elif msg=="c!":
    await message.channel.send("`Hint: Type c!help for Chicktron commands`")

  ### HELP COMMANDS ###
  elif msg.startswith("c!help"):
    if msg.startswith("c!help useful"):
      await message.channel.send('```yaml\n--== Chicktron Useful Commands Page ==--\n\n\nCommands are prefixed with: c!\n\n- info: Info about Chicktron\n- rand: Takes 2 numbers, generates a random one between the 2 (example: "c!rand 1 10" would return a random number between 1-10)\n- stats: Chicktron statistics```')

    elif msg.startswith("c!help fun"):
      await message.channel.send("```yaml\n--== Chicktron Fun Commands Page ==--\n\n\nCommands are prefixed with: c!\n\n- funaz/joke: Random joke (fuňáz)\n- funaz/joke2: Random joke from 2nd database, may contain inappropriate and programming jokes\n- quote: Random inspirational quote\n- say: Make Chicktron say something\n- emoji: Gives you an emoji from a list of them\n\n- Prefixed Reply Commands: chicktron, idk, fish lip thicc thick nibba gif, h, s, hs, sh, vajca, %appdata%, 2+2, get real, death, banánstvo, lolic, nrat, ban, and, gg ez, balock, poland, cviklomat, la creatura, cry about it/cry\n\nCan you find the secret commands? There could be only one, or there could be a bunch of them...```")

    elif msg.startswith("c!help features"):
      await message.channel.send("```yaml\n--== Chicktron Features Page ==--\n\n\n- no u: no u\n- no i: yes u\n\nEvery message, there's a 1 in 10000 chance for Chicktron to say something very rare O_O```")

    else:
      await message.channel.send("```yaml\n--== Chicktron Help Commands Page ==--\n\n\nCommands are prefixed with: c!\n\n- help: This help\n- help useful: Useful commands\n- help fun: Fun commands\n- help features: Passive chicktron actions```")

  ### USEFUL COMMANDS ###
  elif msg.startswith("c!info"):
    await message.channel.send("```yaml\n- == Chicktron == -\n\nProgrammed by: leosefcik#3401\n\nA random bot created way back in 2017 for leosefcik's Discord server (which at the time of writing has 4 members, 2 of which are bots (yeah, it didn't take off)) Blue Ball Machine Topia. Back then, it didn't do anything, it was December of 2020 that it actually started doing bot stuff. It's written in Python and proves that even the biggest dummies (like leosefcik) can do a bot that at least does very useless stuff. It's not that big of a point, but whatever. Cock-a-doodle-doo! Visit c!help to see commands. Recommended Chicktron name color - #c3f794```")

  elif msg.startswith('c!rand'):
    if msg.startswith("c!rand "):
      nums = msg.split(" ")
      NumberX = int(nums[1])
      NumberY = int(nums[2])
      reply = "`" + str(random.randint(NumberX,NumberY)) + "`"
      db["rand_times_used"]=db["rand_times_used"]+1
      await message.channel.send(reply)
    else:
      await message.channel.send("```yaml\nUsage:\n\n- rand [1st number] [2nd number]```")

  elif msg.startswith("c!stats"):
    await message.channel.send("```yaml\n--== Chicktron Statistics ==--\n\n\n- Times funaz used: "+str(db["funaz_times_used"])+"\n- Times quote used: "+str(db["quote_times_used"])+"\n- Times rand used: "+str(db["rand_times_used"])+"\n- Emoji times used: "+str(db["emoji_times_used"])+"\n- No u replies: "+str(db["no_u_replies"])+"\n- Fun replies: "+str(db["fun_reply_times_used"])+"\n\n- Rare message appearances (0,01%): "+str(db["rare_message_appearances"])+"\n```")

  ### FUN COMMANDS ###
  elif msg.startswith("c!funaz 2") or msg.startswith("c!joke 2") or msg.startswith("c!funaz2") or msg.startswith("c!joke2"):
    reply=get_funaz2()
    db["funaz_times_used"]=db["funaz_times_used"]+1
    await message.channel.send(reply)

  elif msg.startswith("c!funaz") or msg.startswith("c!joke") or msg.startswith("c!funaz 1") or msg.startswith("c!joke 1") or msg.startswith("c!funaz1") or msg.startswith("c!joke1"):
    reply=get_funaz1()
    db["funaz_times_used"]=db["funaz_times_used"]+1
    await message.channel.send(reply)

  elif msg.startswith("c!quote"):
    reply=get_quote()
    db["quote_times_used"]=db["quote_times_used"]+1
    await message.channel.send(reply)

  elif msg.startswith("c!say"):
    if msg.startswith("c!say "):
      msg = message.content.split(" ")
      for x in range(1,len(msg)):
        reply = reply + " " + msg[x]
      await message.channel.send(reply)
    else:
      await message.channel.send("```yaml\nUsage:\n\n- say [message]```")

  elif msg.startswith("c!emoji"):
    db["emoji_times_used"]=db["emoji_times_used"]+1
    await message.channel.send(random.choice(emojis))

  ## REPLY COMMANDS ##
  elif msg=="chicktron" or msg=="c!chicktron":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("Cock-a-Doodle-Doo!")

  elif msg=="idk" or msg=="c!idk":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("idk either")

  elif msg=="%appdata%" or msg=="c!%appdata%":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send(".minecraft")

  elif msg.startswith("c!secret"):
    await message.channel.send("https://Chicktron.leosefcik.repl.co")

  elif msg=="2+2" or msg=="c!2+2":
    reply = "4 "+random.choice(emojis)
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send(reply)

  elif msg=="get real" or msg=="c!get real":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://tenor.com/view/get-real-chinese-egg-man-chinese-guy-eats-raw-eggs-raw-eggs-raw-eggs-chug-gif-19458097")

  elif msg=="death" or msg=="c!death":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://tenor.com/view/walter-white-falling-fast-gif-18043850")

  elif msg=="banánstvo" or msg=="c!banánstvo":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send(":banana:")

  elif msg.startswith("fish lip thicc thick nibba") or msg.startswith("c!fish lip thicc thick nibba"):
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://tenor.com/view/fish-lip-thicc-thick-nibba-gif-13850958")

  elif msg=="lolic" or msg=="c!lolic":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://cdn.discordapp.com/attachments/693552113254662256/760953024247496774/image0.gif")

  elif msg=="nrat" or msg=="c!nrat":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789532988458795021/nrat.mp4")

  elif msg=="vajca" or msg=="c!vajca":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/789534999929815090/vajca.mp4")

  elif msg=="ban" or msg=="c!ban":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://tenor.com/view/when-your-team-too-good-ban-salt-bae-gif-7580925")

  elif msg=="and" or msg=="c!and":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://cdn.discordapp.com/attachments/295982317959380993/789938286139408394/and.gif")

  elif msg.startswith("gg ez") or msg.startswith("c!gg ez") or msg.startswith("c!ez") or msg.startswith("c!ggez") or msg.startswith("ggez"):
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://tenor.com/view/gg-ez-gg-ez-gg-noobs-gg-noob-gif-17962280")

  elif msg=="balock" or msg=="balok" or msg=="c!balock" or msg=="c!balok":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://cdn.discordapp.com/attachments/743569092061036644/790251735347101696/balock.jpg")

  elif msg=="poland" or msg=="c!poland":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://media.discordapp.net/attachments/699302569700229121/788188949017002024/4e42a22e33409d1d19c4ec0947a970b29ee77647b8c125e40a41a80a7a374c08_1.gif.gif")

  elif msg=="cviklomat" or msg=="c!cviklomat":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("drop da beets\nhttps://tenor.com/view/drop-beats-joke-pun-audio-gif-3829021")

  elif msg=="la creatura" or msg=="c!la creatura":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send("https://tenor.com/view/la-creatura-dog-angry-mad-gif-16725854")

  elif msg=="cry about it" or msg=="cry" or msg=="c!cry" or msg=="c!cry about it":
    db["fun_reply_times_used"]=db["fun_reply_times_used"]+1
    await message.channel.send(random.choice(cries))


  ### PASSIVE FEATURES ###
  
  elif any(word in message.content for word in no_u):
    if msg.startswith("no u") or msg.startswith("no u "):
      db["no_u_replies"]=db["no_u_replies"]+1
      if random.randint(1,100)==69:
        reply=message.conent.replace("no u", "u no")
        await message.channel.send(reply)
      await message.channel.send(message.content)
    else:
      db["no_u_replies"]=db["no_u_replies"]+1
      reply = message.content.replace("*", "")
      reply = reply.replace("no u", "**no u**")
      reply = reply.replace("****", "")
      await message.channel.send(reply)

  elif msg=="no i":
    db["no_u_replies"]=db["no_u_replies"]+1
    await message.channel.send("yes u")

  elif secret_key==69:
    db["rare_message_appearances"]=db["rare_message_appearances"]+1
    reply="This message has a 1 in 100000 chance of showing up! "+random.choice(emojis)
    await message.channel.send(reply)

keep_alive()
client.run(os.getenv("TOKEN"))

#if any(word in message.content for word in list):

#banan

#  elif msg.startswith("no u"):
#    if msg=="no u":
#      db["no_u_replies"]=db["no_u_replies"]+1
#      await message.channel.send(message.content)
#    elif msg.startswith("no u "):
#      db["no_u_replies"]=db["no_u_replies"]+1
#      await message.channel.send(message.content)
