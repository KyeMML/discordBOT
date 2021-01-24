# ------------------------------------------------
# BUYING STONKS
# ------------------------------------------------
# @client.command()
# async def buy(ctx):
#     """Buying Stonks"""
#     local_values = locals().values()
#     params = list(list(local_values)[1])
#     if len(params)>0:
#         if params[0] == 'buy':
#             try:
#                 # take money out
#                 wallet-=price
#                 #check stocker exists and add to owned stonks
#                 if params[1] in stonk_tickers:
#                     stocks_owned.append(params[1])
#                 else:
#                     await ctx.send(params[1]+" cannot be found on stonk market")
#             except:
#                 await ctx.send("Insufficient funds")
#     await ctx.send("your current holdings:"+stocks_owned)
# ------------------------------------------------


# ------------------------------------------------
# SELLING STONKS
# ------------------------------------------------
# @client.command()
# async def sell(ctx):
#     """Selling Stonks"""
#     local_values = locals().values()
#     params = list(list(local_values)[1])
#     if len(params)>0:
#         if params[0] == 'sell':
#             my_list.append(params[1])
#         elif params[0] == 'del':
#             try:
#                 my_list.remove(params[1])
#             except:
#                 await ctx.send(str(params[1])+"cannot be found in your list")
#     await ctx.send(my_list)
# ------------------------------------------------