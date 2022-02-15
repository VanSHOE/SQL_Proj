# Dead By Daylight


<img width="1116" alt="dbd" src="https://user-images.githubusercontent.com/71231079/141134632-a8531fc7-8dbd-4288-a0f0-c0675d5d366f.png">

## Installation
Download the zip file which consists of the `dbd.py`. This will allow you to run the CLI. The database should be setup on your sql system.

## Setup
To change the port and connect it to your sql database, check this line at line 178 in `dbd.py`. Here change the port to whichever port your sql is running on. And change your username accordingly in user

```python
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="root",
                              password=passwordi,
                              db='dna',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)
```

modified code:


```python
        con = pymysql.connect(host='localhost',
                              port= <YOUR_PORT>,
                              user= <YOUR_USERNAME>
                              password=passwordi,
                              db='dna',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

```
The username and password will be asked during the execution of the CLI too and access will be granted accordingly to ensure security.

##

<img width="1193" alt="main" src="https://user-images.githubusercontent.com/71231079/141135031-052ccace-2589-425b-8197-1f82ab6b0b82.png">
<img width="516" alt="login" src="https://user-images.githubusercontent.com/71231079/141134253-56784f81-dd36-49f6-8def-b0a20b6fc88c.png">

## CLI

We have a built a very user-friendly CLI, asking the user for Username and Password to help login to their sql database. The user is given a menu listing all the options available to them. The user can enter their choice, thus executing the corresponding functions. A success command will be printed on the CLI on successful completion of the command.

The user will then be continuously taken back to the menu until they decide to logout using the '0' option. 

The CLI is designed, incorporating various designs for the titles (DBD and Menu) as well as colors, reinforcing the choice that has been made. Errors re highlighted in red while success messages are highlighted in Green.

Furthermore, we have implemented a cool acronym for the database, with a benzene like symbol, characterising the essence of our CLI. We have implemented a shell-like user interface in our CLI for the ease of the user. 

##

<img width="669" alt="cli2" src="https://user-images.githubusercontent.com/71231079/141134319-be08f443-02f4-4a1d-853c-6d8b1a633a18.png">



## Menu Options 

<br>
<img width="884" alt="cli1" src="https://user-images.githubusercontent.com/71231079/141134339-e49b1c20-e018-4c50-8386-4ae40242f724.png">

### Insert a character
With this option we are inserting either a new killer or survivor. The data is added into the character table alongside with the killer or survivor table depending on the role given.
A success command will be printed on the CLI on successful completion of the command.

### Insert into leaderboards
With this option, a leaderboard record comprising of statistical data of a players are inserted into the leaderboard table. A success command will be printed on the CLI on successful completion of the command.  

### Show all players with rank greater than a particular rank (taken as input)
With this option, we show all players with ranks greater than the user-inputted rank. A success command will be printed on the CLI on successful completion of the command.  

### Insert into a generator
With this option, we insert a generator record into the generator table. Progress of all generators always start with 0. A success command will be printed on the CLI on successful completion of the command.
                  
### Insert into a Perk
With this option, we insert a Perk record into the Perks table. A success command will be printed on the CLI on successful completion of the command.  

### Deleting a record from Killer with a particular Killer ID
Executing this function will ask the user for an input of a Killer ID and the corresponding record will be deleted from both the Killer Table as well as the Character Table. The two tables are linked together by a foreign key constraint. 
A success command will be printed on the CLI on successful completion of the command.

### Deleting a record from Survivor with a particular Survivor ID
Executing this function will ask the user for an input of a Survivor ID and the corresponding record will be deleted from both the Survivor Table as well as the Character Table. The two tables are linked together by a foreign key constraint. 
A success command will be printed on the CLI on successful completion of the command.

### Deleting a record from totems if it is a Hex-based totem
Executing this function will remove all Hex-based totems (represented by 1 under Is_Hex in the Table Totems) from the Table, it will not take any input from the User.
A success command will be printed on the CLI on successful completion of the command.

### Updating abilities from Killers with a particular Killer ID
Executing this function will ask the user for an input of a Killer ID and the corresponding record will be updated with the correct ability which is also asked via input. 
A success command will be printed on the CLI on successful completion of the command.

### Updating abilities from Perks with a particular PerkName
This option will let you take PerkName as input and then update the ability corresponding to this PerkName in the database. A success command will be printed on the CLI on successful completion of the command.

# Updating score in Leaderboards
This option will let you take user_id as input and then update the score corresponding to this user_id in the database. A success command will be printed on the CLI on successful completion of the command.

### Updating size from Maps with a particular Map ID
This option will let you take MapID as input and then update the size corresponding to this Map in the database. A success command will be printed on the CLI on successful completion of the command.

### Retrieve datasets from Perks
This option will allow us to retrieve complete data tuples of records from Perks belonging to a particular Tier. Each perk has a tier signifying the strength. Through this option the user will be able to filter out the perk based on the input tier as requested by user. A success command will be printed on the CLI on successful completion of the command.

### Retrieve names of all players with rank ≤ input
This option will allow us to retrieve names of players whose rank is below a particular value as inputted by user. Through this option the user will be able to filter out the players whose rank is below the inputted rank. A success command will be printed on the CLI on successful completion of the command.

### Retrieve Maximum score from Leaderboard
This option will allow us to retrieve the maximum score from LeaderBoards which is basically the winning score. It will also print out the players who have the maximum score who are basically the winners of the game.A success command will be printed on the CLI on successful completion of the command.
             
### Search Killer Name
This option will let us partial search among the killers. Therefore for example if we have Killer Names such as: 'Wraith','WrathBringer','Doctor'. A partial search of 'Wra' using this option would output 'Wraith' and 'WrathBringer'. The names along with a success command will be printed on the CLI on successful completion of the command.
                    
### Analysing win rate of survivors
This option will let us analyse the win rate of Survivors which is basically the percentage of survivors that escaped. This will let us know whether whether the survivor or killer was at a disadvantage during the course of the game. The output will be the win percentage of the survivors. Also a success command will be printed on the CLI on successful completion of the command.
