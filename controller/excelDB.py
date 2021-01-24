import numpy as np
import pandas as pd
# ------------------------------------------------
# WELCOME TO THE EXCEL DB!!!!
# ------------------------------------------------

# ------------------------------------------------

def allUsersDB():
    #Find all users in DB
    '''List all current users in DB (home)'''
    path=r'C:\Users\Kye Manning-Lees\Desktop\vs\discordDB.xlsx'

    writer = pd.ExcelWriter(path, engine = 'openpyxl', index='False')

    df_home = pd.read_excel(path, sheet_name='home')
    df_list = pd.read_excel(path, sheet_name='userListData')
    
    all_users=list(df_home.keys())
    return all_users

def addNewUser(userID, wallet):
    '''Adding new user to DB'''
    path=r'C:\Users\Kye Manning-Lees\Desktop\vs\discordDB.xlsx'

    writer = pd.ExcelWriter(path, engine = 'openpyxl', index='False')

    df_home = pd.read_excel(path, sheet_name='home')
    df_list = pd.read_excel(path, sheet_name='userListData')

    #Adding to home:
    df_home[userID]=[wallet]
    #Adding to List:
    df_list[userID]=np.nan

    df_home.to_excel(writer, sheet_name='home', index=False)
    df_list.to_excel(writer, sheet_name='userListData', index=False)
    writer.save()
    writer.close()


# ------------------------------------------------
# Read DB
# ------------------------------------------------
def readDB(userID, query):
    path=r'C:\Users\Kye Manning-Lees\Desktop\vs\discordDB.xlsx'

    df_home = pd.read_excel(path, sheet_name='home', index='False')
    df_list = pd.read_excel(path, sheet_name='userListData', index='False')

    if query == 'find_list':
        rawList = list(df_list[userID])
        result = [x for x in rawList if str(x) != 'nan']
    elif query == 'find_wallet':
        your_wallet = df_home[userID]
        result = float(your_wallet)

    return result
# ------------------------------------------------


# ------------------------------------------------
# Write DB
# ------------------------------------------------
def writeDB(userID, data, query):

    path=r'C:\Users\Kye Manning-Lees\Desktop\vs\discordDB.xlsx'

    writer = pd.ExcelWriter(path, engine = 'openpyxl', index='False')

    df_home = pd.read_excel(path, sheet_name='home')
    df_list = pd.read_excel(path, sheet_name='userListData')

    #options include:
    # 1. Update wallet
    if query == 'writeWallet':
        wallet=data
        df_home[userID]=[wallet]
    # 3. Add to list
    elif query == 'writeListAdd':
        new_list = list(df_list[userID].values)
        new_list.append(data)
        # new_list = ["BB", "CL", "BFF"]

        #This can be reduced to function
        new_list_df = pd.DataFrame({userID:new_list})
        #check which column is larger:
        if len(df_list)>len(new_list_df):
            #delete row from DB
            df_list = df_list.drop(columns=[userID])
            #add db to larger df
            df_list = df_list.join(new_list_df)
        else:
            #delete row from DB
            df_list = df_list.drop(columns=[userID])
            #add db to larger df
            df_list = new_list_df.join(df_list)
    # 3. Del from list
    elif query == 'writeListDel':
        new_list = list(df_list[userID].values)
        new_list.remove(data)
        # new_list = ["BB", "CL", "BFF"]

        #This can be reduced to function
        new_list_df = pd.DataFrame({userID:new_list})
        #check which column is larger:
        if len(df_list)>len(new_list_df):
            #delete row from DB
            df_list = df_list.drop(columns=[userID])
            #add db to larger df
            df_list = df_list.join(new_list_df)
        else:
            #delete row from DB
            df_list = df_list.drop(columns=[userID])
            #add db to larger df
            df_list = new_list_df.join(df_list)

    df_home.to_excel(writer, sheet_name='home', index=False)
    df_list.to_excel(writer, sheet_name='userListData', index=False)
    writer.save()
    writer.close()
# ------------------------------------------------

# for improvement, remove cols which only have NaNs