import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv 

import controller
from controller import excelDB 

import secret_stuff

client = commands.Bot(command_prefix=">")



@client.event
async def on_ready():
    # general_channel = client.get_channel(799408860292710443)
    print("Bot is ready")
    print(f"logged in as {client.user}")

@client.command()
async def hello(ctx):
    await ctx.send("hi")



# ------------------------------------------------
# HELP I DUNNO COMMANDS!
# ------------------------------------------------
available_commands = ["Hi and Welcome to Kye's CrackBot!\n\nCurrent Available Bot commands:\n- hello\n- choose\n- mylist\n- stonks\n- NOT AVAILABLE buy stonkname amount\n- NOT AVAILABLE sell stonkname amount\n\n -- all commands use prefix '>' -- "]
@client.command()
async def info(ctx, *args, **kwargs):
    '''Available commands'''
    await ctx.send(available_commands[0])
# ------------------------------------------------


# ------------------------------------------------
# Let bot decide for you
# ------------------------------------------------
@client.command()
async def choose(ctx, *args, **kwargs):
    """Randomly pick an option."""
    options = locals().values()
    options = list(list(options)[1])
    decision = random.choice(options)
    await ctx.send(decision)
# ------------------------------------------------


# --------------------------------
# Excel DB
# --------------------------------
@client.command()
async def myID(ctx):
    await ctx.send(ctx.message.author.id)

@client.command()
async def myWallet(ctx):
    #get user ID
    myID = str(ctx.message.author.id) 
    your_wallet = excelDB.readDB(myID, 'find_wallet')
    await ctx.send(your_wallet)

@client.command()
async def myList(ctx, *args, **kwargs):
    #get user ID
    myID = str(ctx.message.author.id)
    
    #get user params
    local_values = locals().values()
    params = list(list(local_values)[1])

    if len(params)>0:
        if params[0] == 'add':
            try:
                excelDB.writeDB(myID, params[1], query='writeListAdd')
            except:
                await ctx.send("error adding "+str(params[1])+" to your list")
        elif params[0] == 'del':
            try:
                excelDB.writeDB(myID, params[1], query='writeListDel')
            except:
                await ctx.send(str(params[1])+" cannot be found in your list")

    your_list = excelDB.readDB(myID, 'find_list')
    await ctx.send(your_list)
#remove NaN from returned list
    
@client.command()
async def signUp(ctx):
    '''Add new user to the database'''
    myID = str(ctx.message.author.id)
    
    all_users=excelDB.allUsersDB()
    if myID not in all_users:
        excelDB.addNewUser(myID, wallet=200)
        await ctx.send("User "+myID+" has successfully been added to Kye's scuffed DB")
    else:
        await ctx.send("User "+myID+" already exists in Kye's scuffed DB")
# --------------------------------




# ------------------------------------------------
# STONKS
# ------------------------------------------------
current_stonks = ['Budget Burials (Ticker Symbol: BB)', 'Crack Limited (Ticker Symbol: CL)', 'Burger Fat Friends (Ticker Symbol: BFF)']
stonk_tickers = ['BB', 'CL', 'FBF']
@client.command()
async def stonks(ctx):
    """Stonk Market"""
    await ctx.send('Welcome to the Stonk Market!\nStonks publically listed include:')
    for stonk in current_stonks:
        await ctx.send('- '+stonk)
# ------------------------------------------------



# ------------------------------------------------
# EXCHANGE
# ------------------------------------------------

available_stonks = ['CSL']
stonkPrices = {'CSL':100}

# user makes an order (buy)
@client.command()
async def buy(ctx):
    #get user ID
    myID = str(ctx.message.author.id) 
    
    #get user params
    local_values = locals().values()
    params = list(list(local_values)[1])

    #money available
    # your_wallet = excelDB.readDB(myID, 'find_wallet')
    wallet_test = 100

    #check stock to buy is available
    if len(params)>0:
        if params[0] in available_stonks:
            #reduce wallet by (stock price * number of stocks purchased)
            if (wallet_test - (stonkPrices[params[0]]*params[1])) > 0:
                wallet_test-=(stonkPrices[params[0]]*params[1])

                # once confirmed for execution:
                # order is compared to current listings

                    # if volume is not completely removed by current listings then it is listed

                    # listed until volume is depleted by price matches

                await ctx.send('purchased',params[0],'for',stonkPrices[params[0]])
            else:
                await ctx.send('insufficient funds')
                return 
             
    # await ctx.send('purchased',stonkName,'for',stonkPrice)
# ------------------------------------------------

client.run(secret_stuff.clientID)