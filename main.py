import json
import discord

with open("private.json","r") as file:
    data = json.load(file)
    TOKEN = data["TOKEN"]
    PREFIX = data["PREFIX"]

client = discord.Client()

dictTI = {"/j":"joking","/hj":"half-joking", "/s":"sarcastic", "/gen":"genuine", "/g":"genuine","/srs":"serious","/nsrs":"non-serious","/pos":"positive connotation","/pc":"positive connotation","/neu":"neutral connotation","/neg":"negative connotation","/nc":"negative connotation","/p":"platonic","/r":"romantic","/c":"copypasta","/l":"lyrics","/ly":"lyrics",'/lh':"light-hearted","/nm":"not mad","/lu":"a little upset","/nbh":"for when you're vagueposting or venting, but it's directed at **nobody here**","/sx":"sexual intent","/x":"sexual intent","/nsx":"non-sexual intent","/nx":"non-sexual intent","/rh":"rhetorical question","/rt":"rhetorical question","/t":"teasing","/ij":"inside joke","/m":"metaphorically","/li":"literally","/hyp":"hpyerbole","/f":"fake","/th":"threat","/cb":"clickbait"}

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
            embed.add_field(name="Usage (example):", value="!tb \srs", inline=True)
            embed.set_footer(text="Returns not nound if Tone Indicator is not present or if there is no slash in front")
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

