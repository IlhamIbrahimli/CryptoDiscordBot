import discord
from discord.ext import commands, tasks
import credits
import urllib.request
import json
import time
token = credits.token
intents = discord.Intents().all()


bot = commands.Bot(command_prefix='crypto!',help_command=None,intents=intents)
people = {}
@bot.command(name = "start")

async def start(ctx):
    await ctx.send("Hi. This bot will help you keep track of major crypto currencies and you can play a game of should i take out my stocks? Type crypto!help for more commands")
@bot.command(name = "check")
async def check(ctx, crypto):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids="+crypto
    print(type(urllib.request.urlopen(url).read()))
    urlresults = str(urllib.request.urlopen(url).read())
    n=2
    urlresults = urlresults[n:]
    size = len(urlresults)
    urlresults = urlresults[:size-1]
    urlresults = urlresults.strip('][').split(', ')
    urlresults = json.loads(urlresults[0])
    print(urlresults)
    print(type(urlresults))
    if urlresults == "":
        await ctx.send("No Cryptocurrency found with the name "+crypto)
    else:
        
        embed=discord.Embed(
        title= urlresults["name"],
        description="Here is current info on " + urlresults["name"] ,
        color=discord.Color.orange())
        embed.set_author(name="Coin Gecko", url="coingecko.com")
        embed.add_field(name="Current price", value="$"+str(urlresults["current_price"]), inline=False)
        embed.add_field(name="Price Change over the last 24 hours", value=urlresults["price_change_24h"], inline=False)
        embed.add_field(name="Lowest price over the last 24 hours", value=urlresults["low_24h"], inline=False)
        embed.add_field(name="Highest price over the last 24 hours", value=urlresults["high_24h"], inline=False)
        await ctx.send(embed=embed)
@bot.command(name = "startgame")
async def startgame(ctx):
    people[ctx.author.name] = [100000,0,0,0,0,0]
    await ctx.send("You have been registered with the game.To invest in the cryptocurrencies type crypto!invest (bitcoin, ethereum,binancecoin, tether or solana) (price) . You have a starting amount of $100000")
@bot.command(name = "invest")
async def invest(ctx, *args):
    if ctx.author.name in people.keys():
        cur = args[0]
        cur = cur.lower()
        if cur == "bitcoin":
            if people[ctx.author.name][0] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][1] += float(args[1])/urlresults["current_price"]
                people[ctx.author.name][0] -= float(args[1])
                msg = "You just invested $"+ args[1]+" in "+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough money. Try buying some of your cryptocurrency")
        if cur == "ethereum":
            if people[ctx.author.name][0] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][2] += float(args[1])/urlresults["current_price"]
                people[ctx.author.name][0] -= float(args[1])
                msg = "You just invested $"+ args[1]+" in "+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough money. Try buying some of your cryptocurrency")
        if cur == "binancecoin":
            if people[ctx.author.name][0] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=binancecoin"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][3] += float(args[1])/urlresults["current_price"]
                people[ctx.author.name][0] -= float(args[1])
                msg = "You just invested $"+ args[1]+" in "+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough money. Try buying some of your cryptocurrency")
        if cur == "tether":
            if people[ctx.author.name][0] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=tether"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][4] += float(args[1])/urlresults["current_price"]
                people[ctx.author.name][0] -= float(args[1])
                msg = "You just invested $"+ args[1]+" in "+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough money. Try buying some of your cryptocurrency")
        if cur == "solana":
            if people[ctx.author.name][0] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=solana"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][5] += float(args[1])/urlresults["current_price"]
                people[ctx.author.name][0] -= float(args[1])
                msg = "You just invested $"+ args[1]+" in "+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough money. Try buying some of your cryptocurrency")
@bot.command(name = "checkmy")
async def checkmy(ctx):
    embed=discord.Embed(
        title= ctx.author.name,
        description="Here is current info on your stats" ,
        color=discord.Color.orange())
    embed.set_author(name="Crypto bot")
    embed.add_field(name="USD", value=people[ctx.author.name][0], inline=False)
    embed.add_field(name="Bitcoin", value=people[ctx.author.name][1], inline=False)
    embed.add_field(name="Ethereum", value=people[ctx.author.name][2], inline=False)
    embed.add_field(name="Binance Coin", value=people[ctx.author.name][3], inline=False)
    embed.add_field(name="Tether", value=people[ctx.author.name][4], inline=False)
    embed.add_field(name="Solana", value=people[ctx.author.name][4], inline=False)  
    await ctx.send(embed=embed)
@bot.command(name = "buy")
async def buy(ctx, *args):
     if ctx.author.name in people.keys():
        cur = args[0]
        cur = cur.lower()
        if cur == "bitcoin":
            if people[ctx.author.name][1] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][0] += urlresults["current_price"]*float(args[1])
                people[ctx.author.name][1] -= float(args[1])
                msg = "You just bought "+ args[1]+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough currency. Try selling some of your currency")
        if cur == "ethereum":
            if people[ctx.author.name][2] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][0] += urlresults["current_price"]*float(args[1])
                people[ctx.author.name][2] -= float(args[1])
                msg = "You just invested $"+ args[1]+" in "+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough currency. Try selling some of your currency")
        if cur == "binancecoin":
            if people[ctx.author.name][3] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=binancecoin"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][0] += urlresults["current_price"]*float(args[1])
                people[ctx.author.name][3] -= float(args[1])
                msg = "You just invested $"+ args[1]+" in "+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough currency. Try selling some of your currency")
        if cur == "tether":
            if people[ctx.author.name][4] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=tether"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][0] += urlresults["current_price"]*float(args[1])
                people[ctx.author.name][4] -= float(args[1])
                msg = "You just invested $"+ args[1]+" in "+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough currency. Try selling some of your currency")
        if cur == "solana":
            if people[ctx.author.name][5] - float(args[1]) >= 0:
                url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=solana"
                urlresults = str(urllib.request.urlopen(url).read())
                n=3
                urlresults = urlresults[n:]
                
                size = len(urlresults)
                urlresults = urlresults[:size-2]
                urlresults = json.loads(urlresults)
                people[ctx.author.name][0] += urlresults["current_price"]*float(args[1])
                people[ctx.author.name][5] -= float(args[1])
                msg = "You just invested $"+ args[1]+" in "+cur
                await ctx.send(msg)
            else:
                await ctx.send("Not enough currency. Try selling some of your currency")
            

@bot.command(name="help")
async def help(ctx):
    embed=discord.Embed(
    title= "Help",
    color=discord.Color.red())
    embed.set_author(name="CryptoBot")
    embed.add_field(name="Check stats on cryptocurrencies.", value="crypto!check (currency)", inline=False)
    embed.add_field(name="Start the game", value="crypto!startgame", inline=False)
    embed.add_field(name="Invest in the game", value="crypto!invest (bitcoin,ethereum,binancecoin,tether,solana) (amount)", inline=False)
    embed.add_field(name="Buy out your cryptocurrencies", value="crypto!buy (bitcoin,ethereum,binancecoin,tether,solana) (amount)", inline=False)
    embed.add_field(name="Check your game stats", value="crypto!checkmy", inline=False)
    channel = bot.get_channel(926828331184316436)
    await ctx.send(embed = embed)
    


    
@tasks.loop(hours = 24)
async def called_once_a_day():
    i=0
    for crypto in ["bitcoin","ethereum","binancecoin","tether","solana"]:
        print(crypto)
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids="+crypto
        #print(urllib.request.urlopen(url).read())
        urlresults = str(urllib.request.urlopen(url).read())
        n=3
        urlresults = urlresults[n:]
        size = len(urlresults)
        urlresults = urlresults[:size-2]
       
        #print(urlresults)
        
        urlresults = json.loads(urlresults)
        
        
        
        embed=discord.Embed(
        title= urlresults["name"],
        url="https://realdrewdata.medium.com/",
        description="Here is current info on " + urlresults["name"] ,
        color=discord.Color.orange())
        embed.set_author(name="Coin Gecko", url="https://twitter.com/RealDrewData")
        embed.add_field(name="Current price", value="$"+str(urlresults["current_price"]), inline=False)
        embed.add_field(name="Price Change over the last 24 hours", value=urlresults["price_change_24h"], inline=False)
        embed.add_field(name="Lowest price over the last 24 hours", value=urlresults["low_24h"], inline=False)
        embed.add_field(name="Highest price over the last 24 hours", value=urlresults["high_24h"], inline=False)
        channel = bot.get_channel(926828331184316436)
        await channel.send(embed = embed)
        i+=1
@bot.event

async def on_ready():
    called_once_a_day.start()
        
bot.run(token)