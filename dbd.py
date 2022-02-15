import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate
from termcolor import cprint
import sys


def intro():
    dbd = '''   
                                                                                                                                                
                                                                                                                                                
                         )`·.                                                                                           )`·.                    
         (`·.        .·´     )                              (`·.                )\                      (`·.        .·´     )                   
           ) :).·´(_\::. .::`·. )`·.      )\   ’'             )  `·.   .·´( .·´  (     /(                 ) :).·´(_\::. .::`·. )`·.      )\   ’'
.·´(    .·´::..::::::;;  --  ' '\ .::(_.·´::(   ’'     .·´( .·´:..::(,(::--  ' ’\::.`·._) `·.   .·´(    .·´::..::::::;;  --  ' '\ .::(_.·´::(   ’'
)  .:`·.);;.--  ' '               \ ..        `·.      );; :--  ' '               \::....:::::)´()  .:`·.);;.--  ' '               \ ..        `·. 
 `·:::../\                 ,      ` ·:::.....:::)  .·´/\                 ____ ¯¯ ` · ::::/' `·:::../\                 ,      ` ·:::.....:::)
    )/::::\...:´/       /::::,,      `·:::::·´     )/:::'\...:´/       /::::::::::/\      \(   '    )/::::\...:´/       /::::,,      `·:::::·´   
     \::::/::::/       /:::::::`·.      I/’'         \:::/::::/       /;;:::::-··´´      /           \::::/::::/       /:::::::`·.      I/’'      
       \/;::-'/       /:::::·::/      /        '    '\/;::-'/               __,...::::/      '         \/;::-'/       /::::;:::::/      /        '
            /       / :::::··::/      /                    /        ,,           ` -:::/                    /        /:::::·:: /      /          
          '/       /.·´:::::·/      /’             .·´( '/       /:::::·-..,          \        '          '/       /.·::;::  /      /’           
  .·´(.·´/        /);; --  ' ´      '/             _) ::/       /::::::://             /   "  .·´(.·´     /       /);; --  ' ´      '/             
  ) .::/                     .·::´/              `·:::/        /''::- ··  ´´       /              ) .::/                     .·::´/              
  `·:/:`·.______ .·::´/:::::/'                  )/::; - '          ..-:::::'/::::/            `·:/:`·.______ .·::´/:::::/'::.·             
   /:::::/:::::::::::/:::'/:::·´'               ::::::¯/::`*..¸..-::::::::::::/:::·´              /:::::/:::::::::::/:::'/:::·´'                 
    `·:/::::::::::::/::::·´''                   :::::: :::::::/::::::::::-·· ´´                     `·:/::::::::::::/::::·´''                     
       ¯¯¯¯¯¯¯¯¯’'                             `*-::;/::::-·· '"´´                                      ¯¯¯¯¯¯¯¯¯’'                         
                         
    '''

    cprint(dbd, "blue", attrs=['bold'])
    cprint("****************************************************************************************************************************************", "blue")
    cprint("                                                                Dead By Daylight")
    cprint("                                                     Welcome to Dead By Daylight Database!")
    cprint("****************************************************************************************************************************************", "blue")
    print("\n")


def printTable(myDict, colList=None):
    if not colList:
        colList = list(myDict[0].keys() if myDict else [])
    myList = [colList]  # 1st row = header
    for item in myDict:
        myList.append([str(item[col] if item[col] is not None else '')
                      for col in colList])
    colSize = [max(map(len, col)) for col in zip(*myList)]
    formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
    myList.insert(1, ['-' * i for i in colSize])  # Seperating line
    for item in myList:
        print(formatStr.format(*item))


def insertLeaderboard():
    """
    insert into leaderboards

    """
    try:
        row = {}
        print("Enter new character's details: ")
        # name = (input("Name (Fname Minit Lname): ")).split(' ')
        # row["Minit"] = name[1]
        # row["Lname"] = name[2]
        row["SteamName"] = input("Steam Name: ")
        row["Ranks"] = int(input("Ranks: "))
        row["user_id"] = int(input("User ID: "))
        row["status"] = input("Status: ")
        row["score"] = float(input("Score: "))
        row["numberofkills"] = int(input("Number of kills: "))
        row["chaseswon"] = int(input("Chases won: "))
        row["escapes"] = int(input("Escapes: "))
        row["generators"] = int(input("Generators: "))
        row["experience"] = float(input("Experience: "))
        row["level"] = int(input("Level: "))
        row["mapid"] = int(input("Map ID: "))
        row["PerksUsed"] = input("Perks Used: ")
        row["AddonsUsed"] = input("Addons Used: ")

        query = "INSERT INTO LeaderBoards VALUES('%s', '%d', '%d', '%s', '%f', '%d', '%d', '%d', '%d', '%f', '%d', '%d', '%s', '%s')" % (
            row["SteamName"], row["Ranks"], row["user_id"], row["status"], row["score"], row["numberofkills"], row["chaseswon"], row["escapes"], row["generators"], row["experience"], row["level"], row["mapid"], row["PerksUsed"], row["AddonsUsed"])

        cur.execute(query)
        con.commit()

        cprint("\n⌬ DBD", "blue", end='')
        print("< Inserted Into Database ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Inserted Into Database ~>", end='')
        cprint("Failed to insert into database", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


insertLeaderboard.counter = 0


def showRankG():
    """
    Show all players with rank greater than a particular rank (taken as input)

    """
    try:

        level = int(input("Enter limiting rank: "))
        query = "SELECT * FROM LeaderBoards WHERE Ranks > %d" % (level)
        cur.execute(query)
        result = cur.fetchall()

        table = []
        headers = ["SteamName", "Ranks", "user_id", "status", "score", "numberofkills", "chaseswon",
                   "escapes", "generators", "experience", "level", "MapID", "PerksUsed", "AddonsUsed"]
        for row in result:
            table_row = list(row.values())
            table.append(table_row)

        print(tabulate(table, headers=headers, tablefmt="grid"))

        cprint("\n⌬ DBD", "blue", end='')
        print("< Command Execution ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command Execution ~>", end='')
        cprint("Failed to execute command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


def insertGenerator():
    """
    Insert generator

    """
    try:
        row = {}
        print("Enter new generator details: ")
        row["sid"] = int(input("User ID: "))
        row["location"] = input("Location: ")
        row["progress"] = 0

        query = "INSERT INTO Generators VALUES('%d', '%s', '%f')" % (
            row["sid"], row["location"], row["progress"])

        cur.execute(query)
        con.commit()

        cprint("\n⌬ DBD", "blue", end='')
        print("< Inserted Into Database ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Inserted Into Database ~>", end='')
        cprint("Failed to insert into database", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


def insertCharacter():
    """
    Inserts details of "Characters" and places them into "Survivor" and "Killers" accordingly

    """
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new character's details: ")
        # name = (input("Name (Fname Minit Lname): ")).split(' ')
        # row["Fname"] = name[0]
        # row["Minit"] = name[1]
        # row["Lname"] = name[2]
        row["Name"] = input("Name: ")
        row["user_id"] = int(input("User id: "))
        role = input("Role (Survivor/Killer): ")
        row["Role"] = role
        row["movement_speed"] = float(input("Movement speed: "))
        row["specific_map"] = int(input("Map ID: "))
        row["ability"] = input("Ability: ")
        row["TeachablePerks"] = input("Teachable Perks: ")
        row["generatorLocation"] = input("Generator Location: ")

        query1 = "INSERT INTO Characters(user_id, Role , Name) VALUES('%d', '%s', '%s')" % (
            row["user_id"], row["Role"], row["Name"])

        if role == 'Survivor':
            query2 = "INSERT INTO Survivor VALUES('%d', '%d', '%s', '%f', '%s')" % (
                row["user_id"], row["specific_map"], row["ability"], row["movement_speed"], row["generatorLocation"])
        else:
            query2 = "INSERT INTO Killer VALUES('%d', '%d', '%s', '%f', '%s')" % (
                row["user_id"], row["specific_map"], row["ability"], row["movement_speed"], row["TeachablePerks"])

        cur.execute(query1)
        con.commit()

        cur.execute(query2)
        con.commit()

        query = "select * from Characters"
        cur.execute(query)
        result = cur.fetchall()
        for row in result:
            print(row)
            print("\n")

        cprint("\n⌬ DBD", "blue", end='')
        print("< Inserted Into Database ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Inserted Into Database ~>", end='')
        cprint("Failed to insert into database", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


def insertPerk():
    """
    Insert Perk

    """
    try:
        row = {}
        print("Enter new Perk details: ")
        row["id"] = int(input("User ID: "))
        row["Name"] = input("Name: ")
        row["tier"] = int(input("Tier: "))

        query = "INSERT INTO Perks VALUES('%s', '%s', '%f')" % (
            row["Name"], row["id"], row["tier"])

        cur.execute(query)
        con.commit()

        cprint("\n⌬ DBD", "blue", end='')
        print("< Inserted Into Database ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Inserted Into Database ~>", end='')
        cprint("Failed to insert into database", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


def delKillerName():

    try:
        name = input("Enter name of the Killer: ")

        query1 = "Select user_id from Characters where Name = '%s'" % (name)
        cur.execute(query1)
        result = cur.fetchall()

    # print(result)
        con.commit()

        for x in result:
            query = "Delete from Killer where user_id = '%d'" % (x["user_id"])
            query0 = "Delete from LeaderBoards where user_id = '%d'" % (
                x["user_id"])
            query1 = "Delete from Characters where user_id = '%s'" % (
                x["user_id"])

            cur.execute(query)
            con.commit()

            cur.execute(query0)
            con.commit()

            cur.execute(query1)
            con.commit()

        cprint("\n⌬ DBD", "blue", end='')
        print("< Deleted Database ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Deleted Database ~>", end='')
        cprint("Failed to delete database", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


def Rdataset():
    '''
    Retrieve names of all players with rank ≤ input

    '''
    try:
        Rank = int(input("Enter Rank: "))
        query = "SELECT * FROM LeaderBoards WHERE Rank = %d" % (Rank)
        cur.execute(query)
        result = cur.fetchall()

        table = []
        headers = ["User_ID", "Name", "Rank"]
        for row in result:
            table_row = list(row.values())
            table.append(table_row)

        print(tabulate(table, headers=headers, tablefmt="grid"))

        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


def Rdataset():
    '''
    Retrieve complete data tuples of records from Perks belonging to a particular tier 
    '''
    try:
        tier = int(input("Enter Tier: "))
        query = "SELECT * FROM Perks WHERE Tier = %d" % (tier)

        cur.execute(query)
        result = cur.fetchall()

        table = []
        headers = ["Name", "ID", "Tier"]
        for row in result:
            table_row = list(row.values())
            table.append(table_row)

        print(tabulate(table, headers=headers, tablefmt="grid"))

        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")


def delSurvID():

    try:
        ID = int(input("Enter ID of the Survivor: "))

        query2 = "Delete from Survivor where user_id = '%d'" % (ID)
        query1 = "Delete from Characters where user_id = '%d'" % (ID)
        query = "Delete from Generators where sid = '%d'" % (ID)
        query0 = "Delete from LeaderBoards where user_id = '%d'" % (ID)

        cur.execute(query)
        con.commit()

        cur.execute(query0)
        con.commit()

        cur.execute(query2)
        con.commit()

        cur.execute(query1)
        con.commit()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Deleted Database ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Deleted Database ~>", end='')
        cprint("Failed to delete database", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


def delHex():
    try:
        query = "Delete from Totems where Is_Hex = 1"
        cur.execute(query)
        con.commit()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Deleted Database ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Deleted Database ~>", end='')
        cprint("Failed to delete database", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


def RRanks():
    '''
    Retrieve names of all players with rank <= input

    '''
    try:
        Rank = int(input("Enter Rank: "))
        query = "SELECT Characters.user_id, Characters.Name, Characters.Role, LeaderBoards.SteamName, LeaderBoards.score, LeaderBoards.Ranks FROM LeaderBoards INNER JOIN Characters WHERE LeaderBoards.user_id = Characters.user_id AND LeaderBoards.Ranks <= %d" % (
            Rank)

        cur.execute(query)
        result = cur.fetchall()

        table = []
        headers = ["User_ID", "Name", "Role", "SteamName", "Score", "Ranks"]
        for row in result:
            table_row = list(row.values())
            table.append(table_row)

        print(tabulate(table, headers=headers, tablefmt="grid"))

        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")


def updateKiller():
    try:
        name = input("Enter name of the Killer: ")
        ab = input("Killer Ability:")
        query1 = "Select user_id from Characters where Name = '%s'" % (name)
        cur.execute(query1)
        result = cur.fetchall()

        con.commit()
        for x in result:
            query = "UPDATE Killer SET Ability = '%s' where user_id = '%d'" % (
                ab, x["user_id"])
            cur.execute(query)
            con.commit()
            cprint("\n⌬ DBD", "blue", end='')
            print("< Command ~>", end='')
            cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")


def updatePerk():
    try:
        name = input("Perk name:")
        ab = int(input("Perk Tier:"))
        query = "Update Perks SET Tier=%d where name = '%s'" % (ab, name)

        cur.execute(query)
        con.commit()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")


def updateLdr():
    try:
        id = int(input("Player ID:"))
        score = int(input("Score:"))
        query = "Update LeaderBoards SET score=%d where user_id = %d" % (
            score, id)

        cur.execute(query)
        con.commit()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")


def updateMap():
    try:
        id = int(input("Map ID:"))
        size = int(input("Size:"))
        query = "Update Maps SET size=%d where id = %d" % (size, id)

        cur.execute(query)
        con.commit()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")


def maxScore():
    """
    Show all players with rank greater than a particular rank (taken as input)

    """
    try:

        print("The Maximum Score is: ")
        query = "SELECT MAX(score) FROM LeaderBoards"
        cur.execute(query)
        result = cur.fetchall()
        maxscore = float(result[0]['MAX(score)'])
        print(maxscore)

        query = "SELECT * FROM LeaderBoards WHERE score = %f" % (maxscore)
        cur.execute(query)
        result = cur.fetchall()

        print("\n")
        print("The details of the players who secured maximum score are:")
        print("\n")

        table = []
        headers = ["SteamName", "Ranks", "user_id", "status", "score", "numberofkills", "chaseswon",
                   "escapes", "generators", "experience", "level", "MapID", "PerksUsed", "AddonsUsed"]
        for row in result:
            table_row = list(row.values())
            table.append(table_row)

        print(tabulate(table, headers=headers, tablefmt="grid"))

        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")

    return


def SearchKiller():
    try:
        name = input("Name: ")
        query = "SELECT * FROM Characters WHERE Role='Killer'"
        cur.execute(query)
        table = []
        headers = ["Killer Name"]
        result = cur.fetchall()
        for x in result:
            if name in x["Name"]:
                table_row = []
                table_row.append((str(x["Name"])))
                table.append(table_row)

        con.commit()

        print(tabulate(table, headers=headers, tablefmt="grid"))
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")


def winRateSurvivors():
    try:

       # query0 = "SELECT Characters.user_id, Characters.Name, Characters.Role, LeaderBoards.SteamName, LeaderBoards.score, LeaderBoards.Ranks FROM LeaderBoards INNER JOIN Characters WHERE LeaderBoards.user_id = Characters.user_id AND LeaderBoards.Ranks <= %d" % (
        query = "SELECT status FROM LeaderBoards, Survivor WHERE LeaderBoards.user_id = Survivor.user_id"
        cur.execute(query)
        result = cur.fetchall()
        val = 0
        for x in result:
            if x["status"] == "Escaped":
                val += 1

        cprint("Win rate of Survivors (percentage of survivors that escaped): ", "blue")
        score = float(val)*100/(len(result))
        print(str(score) + "%")
        con.commit()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Success!", "green")

    except Exception as e:
        con.rollback()
        cprint("\n⌬ DBD", "blue", end='')
        print("< Command ~>", end='')
        cprint("Failed command", "magenta")
        print("Error: ", e)
        print("****************************************************************************************")


def dispatch(ch):
    """
    Function that maps helper functions to option entered

    """
    if(ch == 1):
        insertCharacter()
    elif(ch == 2):
        insertLeaderboard()
    elif(ch == 3):
        showRankG()
    elif(ch == 4):
        insertGenerator()
    elif(ch == 5):
        insertPerk()
    elif(ch == 6):
        delKillerName()
    elif(ch == 7):
        delSurvID()
    elif(ch == 8):
        delHex()
    elif(ch == 9):
        updateKiller()
    elif(ch == 10):
        updatePerk()
        # print("Hello")
    elif(ch == 11):
        updateLdr()
    elif(ch == 12):
        updateMap()
    elif(ch == 13):
        Rdataset()
    elif(ch == 14):
        RRanks()
    elif(ch == 15):
        maxScore()
    elif(ch == 16):
        SearchKiller()
    elif(ch == 17):
        winRateSurvivors()
    else:
        cprint("Error: Invalid Option", "magenta")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    intro()
    # Can be skipped if you want to hardcode username and password
    usernamei = input("Username: ")
    passwordi = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server port = 3306
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="root",
                              password=passwordi,
                              db='dna',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            cprint("\n⌬ DBD", "blue", end='')
            print("< Connected to Database ~>", end='')
            cprint(" Success!", "green")
            print("\n")
        else:
            cprint("\n⌬ DBD", "blue", end='')
            print("< Connected to Database ~>", end='')
            cprint("Failed to connect", "magenta")
            print("\n")

        sys.stdout.flush()

        print("\n")
        cprint("\n⌬ DBD", "blue", end='')
        tmp = input(" < Enter any key to CONTINUE :~> ")
        print("\n")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)

                menu = ''' 
                    __    __      
                    | \  / | ___ _ __  _   _  
                    | |\/| |/ _ \ '_ \| | | | 
                    | |  | |  __/ | | | |_| | 
                    |_|  |_|\___|_| |_|\__,_| 
                '''

                cprint(menu, "blue", attrs=['bold'])
                cprint(
                    "********************************************************************************", "blue")
                print("\n")

                # Insert a character
                print("1.  Insert a new character")

                # Insert into leaderboards
                print("2.  Insert into leaderboards")

                # Show all players with rank greater than a particular rank (taken as input)
                print(
                    "3.  Show all players with rank greater than a particular rank (taken as input) ")

                # Insert into a generator
                print("4.  Insert a new generator in generator")

                # Insert into a Perk
                print("5.  Insert a new perk in Perks")

                # Deleting a record from Killer with a particular Killer ID
                print("6.  Delete from Killer with a particular Killer Name")

                # Deleting a record from Survivor with a particular Survivor ID
                print("7.  Delete from Survivor with a particular Survivor ID")

                # Deleting a record from totems if it is a Hex-based totem
                print("8.  Delete from totems if it is Hex based totem")

                # Updating abilities from Killers with a particular Killer ID
                print("9.  Update abilities in Killer with a particular Killer Name")

                # Updating abilities from Perks with a particular PerkName
                print("10. Update tier in Perks with a particular Perk Name")

                # Updating score in Leaderboards
                print("11. Update score in Leaderboards")

                # Updating size from Maps with a particular Map ID
                print("12. Update size in Map with a particular Map ID")

                # Retrieve datasets from Perks
                print(
                    "13. Retrieve complete data tuples of records from Perks belonging to a particular Tier")

                # Retrieve names of all players with rank ≤ input
                print("14. Names of all players with rank ≤ input")

                # Retrieve Maximum score from Leaderboard
                print("15. Maximum score secured in the Leaderboard")

                # Retrieve Maximum score from Leaderboard
                print("16. Search Killer Name")

                # Analysis
                print("\n")
                cprint("Analysis", "blue")
                

                # Analysing win rate
                print("17. Win rate of Survivors (percentage of survivors that escaped) ")


                # Logout
                print("\n")
                cprint("    ** Press 0 to Logout **", "magenta")
                print("\n")
                cprint(
                    "********************************************************************************", "blue")

                print("\n")
                sys.stdout.flush()
                print("\n")
                cprint("\n⌬ DBD", "blue", end='')
                ch = int(input(" < Enter choice :~> "))
                print("\n")
                tmp = sp.call('clear', shell=True)
                if ch == 0:
                    exit()
                else:
                    dispatch(ch)
                    print("\n")
                    cprint("\n⌬ DBD", "blue", end='')
                    tmp = input(" < Enter any key to CONTINUE :~> ")
                    print("\n")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("\n")
        cprint("\n⌬ DBD", "blue", end='')
        tmp = input(" < Enter any key to CONTINUE :~> ")
        print("\n")
