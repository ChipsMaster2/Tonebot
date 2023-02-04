import json
import discord

try:
    with open("config.json","r") as file:
        data = json.load(file)
        PREFIX = data["PREFIX"]
        TOKEN = data["TOKEN"]
except:
    tkn = input("Enter token: ")
    prfx = input("Enter prefix: ")
    dictionary = {
        "TOKEN":tkn,
        "PREFIX":prfx
    }

    json_object = json.dumps(dictionary, indent=4)
    with open("config.json","w") as file:
        file.write(json_object)

intents = discord.Intents(guild_messages=True,message_content=True,messages=True)

client = discord.Client(intents=intents)

dictTI = {"/j":"joking","/hj":"half-joking", "/s":"sarcastic", "/gen":"genuine", "/g":"genuine","/srs":"serious","/nsrs":"non-serious","/pos":"positive connotation","/pc":"positive connotation","/neu":"neutral connotation","/neg":"negative connotation","/nc":"negative connotation","/p":"platonic","/r":"romantic","/c":"copypasta","/l":"lyrics","/ly":"lyrics",'/lh':"light-hearted","/nm":"not mad","/lu":"a little upset","/nbh":"for when you're vagueposting or venting, but it's directed at **nobody here**","/sx":"sexual intent","/x":"sexual intent","/nsx":"non-sexual intent","/nx":"non-sexual intent","/rh":"rhetorical question","/rt":"rhetorical question","/t":"teasing","/ij":"inside joke","/m":"metaphorically","/li":"literally","/hyp":"hyperbole","/f":"fake","/th":"threat","/cb":"clickbait","/h":"humor"}

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(PREFIX):
        if message.content[len(PREFIX):].lower().strip() in ["", "-h","--h","h","help", " ","-help"]:
            print(message.content[len(PREFIX):].lower().strip())
            print(message.content[len(PREFIX):].lower().strip() in [""])
            embed=discord.Embed(title="Tone Bot Help", description="Dictionary Bot For Tone Indicators", color=0x9141ac)
            embed.add_field(name="Prefix: ", value="!tb", inline=True)
            embed.add_field(name="Usage (example):", value="!tb /srs", inline=True)
            embed.set_footer(text="Returns not found if tone indicator is not present or if there is no slash in front")
            await message.reply(embed=embed,mention_author=False)
            # help embed
        elif message.content[len(PREFIX):].lower().strip() in list(dictTI.keys()):
            TI = message.content[len(PREFIX):].lower().strip()
            embed=discord.Embed(color=0x9141ac)
            embed.add_field(name=TI, value=dictTI[TI], inline=False)
            embed.set_footer(text="Sourced from: https://toneindicators.carrd.co/")
            await message.reply(embed=embed,mention_author=False)
        else:
            embed=discord.Embed(color=0x9141ac)
            embed.add_field(name="NOT FOUND", value="Provided Indicator is not in list", inline=False)
            await message.reply(embed=embed,mention_author=False)


client.run(TOKEN)

