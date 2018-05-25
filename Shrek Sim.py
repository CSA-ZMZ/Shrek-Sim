#Zachary Zawaideh
#Computer Programming
#4/18/18
#Shrek Trivia questions, games, and role play!
#Shrek sim is a fun and interactive game in which the user can get to learn their shrek triva in a greate program.
#Utilizes files vvery well
#Lots of ascii art to make the game fun and interactive
#Because of the trivia there are a lot of if statements
#I was diverse in the code and used lists, tuples, globals, max and min, and many other diverse program methodes.
#I have one audio file of the Shrek song All Star by Smash mouth. Shrek gave smash mouth the opprotunity to become a great band through Dreamwork's masterpeice of a movie.
#Audio does not loop it stops at the end of the song.
#There are no errors!

"""
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time
points=0
import random
import pygame


def menu():#This is just the menu in a basic function-if statement style.
    score= open("score.txt","r")#This opens the file which has the points so it can be passed to the high_ function where the user can see the current player and high score.
    print("   ________.__                   __         _________.__         ")
    print(" /   _____/|  |_________   ____ |  | __    /   _____/|__| _____  ")
    print(" \_____  \ |  |  \_  __ \_/ __ \|  |/ /    \_____  \ |  |/     \ ")
    print(" /        \|   Y  \  | \/\  ___/|    <     /        \|  |  Y Y  \"")
    print("/_______  /|___|  /__|    \___  >__|_ \   /_______  /|__|__|_|  /")
    time.sleep(1)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load("real_allstar.mp3")
    pygame.mixer.music.play()
    time.sleep(5)
    print("Welcome to the Shrek Simulator!")#Introduces to the user.
    print("Do you already have an account?")
    print("1. Yes")
    print("2. No")
    print("3. Resume Progress")
    print("4. See High Score")
    x= input(": ")
    if x== "1":#There are four options and if statements. 
        old_login()#You can log in as a log in you have already made.

    elif x== "2":#You can sign up with a new login.
        sign_up()

    elif x== "3":#This allows you to resume at the function you left off at, although your points will reset. 
        pass_code()

    elif x== "4":#This will take the user to a function where he can see the user can see the high score and the player that has it. 
        high_(score)#Although this may seem simple the code for this function was hard to write.
    
    else:#If the user does not input properly they are told to and sent back to the top.
        print("Pick a number choice!")
        menu()#At the menu

def old_login():#This is a log in function
    global username#Uses a global for the username.
    username= input("What is your username?: ")#Asks for users username.
    password= input("What is your password?: ")#Asks for password.
    file= open("shrekpass.txt","r")#This opens a file of passwords with their usernames
    line=file.readline()#This reads that file.
    all_login=[]#I make an empty list to append the passwords and usernaems later.
    while line:#Uses a while loop to complete everything.
        this=line.split()
        all_login.append(this)
        line=file.readline()
    for data in all_login:
        dude= False
        if username== data[0] and password== data[1]:
            print("Yay you logged in!")
            dude= True
            file.close()
            start_game()
    if dude== False:
        print("Incorrect login, try again!")
        menu()
        file.close()

def sign_up():
    newuser= input("What is your new username?: ")
    newpass= input("What is your new password?: ")
    new_term= open("shrekpass.txt","r")
    the_line= new_term.readline()
    linelist= []
    while the_line:
        that= the_line.split()
        linelist.append(that)
        the_line= new_term.readline()
    for new_entry in linelist:
        if newpass == new_entry[1]:
            print("You must create a different password. That one is already in use!")
            sign_up()
    passfile= open("shrekpass.txt","a")
    passfile.write(newuser+" "+newpass+"\n")
    print("Sign up successful!")
    time.sleep(1.5)
    passfile.close()
    print("Now sign in!")
    old_login()

def pass_code():
    global username
    print("Welcome to the password menu!")
    time.sleep(2)
    print("In this menu you can enter a code given to you to leave off from where you last were!")
    time.sleep(2)
    print("First you have to sign in!")
    time.sleep(2)
    username= input("What is your username?: ")
    password= input("What is your password?: ")
    file= open("shrekpass.txt","r")
    line=file.readline()
    all_login=[]
    while line:
        this=line.split()
        all_login.append(this)
        line=file.readline()
    for data in all_login:
        dude= False
        if username== data[0] and password== data[1]:
            print("Yay you logged in!")
            dude= True
            file.close()
            pass_code2()
    if dude== False:
        print("Incorrect login, try again!")
        menu()
        file.close()

def pass_code2():
    print("In this menu you can enter a code given to you to leave off from where you last were!")
    code= input("What is your game code?: ")
    if code=="donkey1":
        continue_game5()

    if code=="knight":
        trivia3()

    if code=="actors":
        trivia6()

    if code=="throw":
        onions()

    else:
        print("That is not a correct game code!")
        menu()

def start_game():
    print("Welcome to Shrek Simulator!")
    time.sleep(1)
    print("You will need to play this game in full screen mode!")
    time.sleep(1)
    print("You start of as Donkey and must escape Shrek's swamp with out being caught!")
    time.sleep(3)
    print("Answer trivia, puzzles, and Shrek role play in order to collect Donkey points and get a high score!")
    begin()

def begin():
    global points
    points= 0
    print("Shrek has found you in his shack and is blocking the door!")
    print("What is the best way out of his shack?")
    print("A. Jump out the window")
    print("B. Break his ankles and out the door")
    print("C. Hide and wait for him to leave")
    option= input(":").lower()
    if option== "a":
        print("A donkey can't fit through a window!")
        time.sleep(1)
        print("You hit the window and fell, Shrek has cought you")
        end_game()

    elif option== "b":
        print("Shrek is very top heavy. Good choice!")
        points= points+1
        continue_game()

    elif option== "c":
        print("You can not hide from Shrek!")
        time.sleep(1)
        print("Shrek has caught you!")
        end_game()

    else:
        print("Pick a valid letter choice!")
        begin()
        
def continue_game():
    global points
    print("You must truge through Shrek's murky swamp water to escape!")
    time.sleep(2)
    print("Fill in the lines to continue!")
    time.sleep(1)
    line= input("What are you doing in my _____: ").lower()
    if line== "swamp":
        print("Correct!")
        print("You are almost at the end of the water!")
        points= points+1
        continue_game2()
    else:
        print("Incorrect, Shrek has caught you!")
        end_game()

def continue_game2():
    global points
    print("Almost there!")
    print("Fill in the lines to continue!")
    time.sleep(1)
    newline= input("I'm making _______!: ").lower()
    if newline== "waffles":
        print("Correct!")
        points= points+1
        continue_game3()
    else:
        print("Incorrect, Shrek has caught you!")
        end_game()

def continue_game3():
    print("After a long journey through the swamp you have reached a long trench.")
    time.sleep(1.5)
    print("You must hop over!")
    time.sleep(1.5)
    print("Make sure your game mode is in full screen!!!")
    time.sleep(1)
    print("                         /\          /\"")
    print("                        ( \\        // )")
    print("                         \ \\      // /")
    print("                          \_\\||||//_/")
    print("                           \/ _  _ \"")
    print("                          \/|(O)(O)|")
    print("                         \/ |      |")
    print("     ___________________\/  \      /")
    print("    //                //     |____|")
    print("   //                ||     /      \"")
    print("  //|                \|     \ 0  0 /")
    print(" // \       )         V    / \____/")
    print("//  /\     /        (     /")
    print("   /  \   /_________|  |_/")
    print("  /  /\   /     |  ||")
    print(" /  / /  /      \  ||")
    print(" | |  | |        | ||")
    print(" | |  | |        | ||")
    print(" |_|  |_|        |_||")
    print("_\_\ _\_\_________\_\\______________________________________________                                                   _____________________________________________________________")
    print("                                                                    1                                                 1 ")
    print("                                                                    1                                                 1")
    print("                                                                    1                                                 1")
    print("                                                                    1                                                 1 ")
    print("                                                                    1                                                 1")
    print("                                                                    1                                                 1") 
    continue_game4()

def continue_game4():
    import random
    print("Pick a number from zero to three")
    print("If your number matches Donokey's random jump power you can jump over the trench!")
    time.sleep(1.5)
    print("If not you will fall down the trench and die!!!")
    number= int(input("What is your number?: "))
    time.sleep(1)
    for x in range(1):
        RandomNumber = random.randrange(1, 3)
    if RandomNumber == number:
        print("Yay!")
        print("You have made it over the trench!")
        time.sleep(2.5)
        print("                                                                                                                                                         /\          /\"")
        print("                                                                                                                                                        ( \\        // )")
        print("                                                                                               YAY                                                       \ \\      // /")
        print("                                                                                                                                                          \_\\||||//_/")
        print("                                                                                                                                                           \/ _  _ \"")
        print("                                                                                                                                                          \/|(O)(O)|")
        print("                                                                                                                                                         \/ |      |")
        print("                                                                                                                                     ___________________\/  \      /")
        print("                                                                                                                                    //                //     |____|")
        print("                                                                                                                                   //                ||     /      \"")
        print("                                                                                                                                  //|                \|     \ 0  0 /")
        print("                                                                                                                                 // \       )         V    / \____/")
        print("                                                                                                                                //  /\     /        (     /")
        print("                                                                                                                                   /  \   /_________|  |_/")
        print("                                                                                                                                      /  /\   /     |  ||")
        print("                                                                                                                                     /  / /  /      \  ||")
        print("                                                                                                                                     | |  | |        | ||")
        print("                                                                                                                                     | |  | |        | ||")
        print("                                                                                                                                     |_|  |_|        |_||")
        print("____________________________________________________________________                                                   ______________\_\__\__\_______\_\_\_______________________________")
        print("                                                                    1                                                 1 ")
        print("                                                                    1                                                 1")
        print("                                                                    1                                                 1")
        print("                                                                    1                                                 1 ")
        print("                                                                    1                                                 1")
        print("                                                                    1                                                 1") 
        continue_game5()
    elif RandomNumber != number:
        print("Your number is not Donkey's jumping power!")
        time.sleep(2)
        end_game()

def continue_game5():
    time.sleep(2)
    print("You game code: donkey1")
    time.sleep(2)
    print("Shrek is catching up! He is on your tail!")
    time.sleep(2)
    print("He grabed your tail!")
    time.sleep(1.5)
    print("Pin the tail on the Donkey to continue!")
    time.sleep(2)
    print("""              
                    _/,/ /
                 _/` (/"/////,
                 (          '```--.___
                /'   _),       ,-     '-.
               /,   /   \                \,
               \_()/     \)   )' =_       |
                         |    |           )
                         (   ( \_        /
                          \  >_,\  (/)  /
                           | | | \ #\| /
                           |=| |=|\ ( (
                           (=> ( >( >),)
                           | | |=| \ ( (
                           / / / /  ) |/
                          /_( /_(   , ||""")
    time.sleep(2)
    print("You must create a ascii tail!")
    time.sleep(1)
    print("Create the tail below!")
    tail= input(": ")
    print("""              
                    _/,/ /
                 _/` (/"/////,
                 (          '```--.___
                /'   _),       ,-     '-.
               /,   /   \                \,
               \_()/     \)   )' =_"""+tail+"""
                         |    |           )
                         (   ( \_        /
                          \  >_,\  (/)  /
                           | | | \ #\| /
                           |=| |=|\ ( (
                           (=> ( >( >),)
                           | | |=| \ ( (
                           / / / /  ) |/
                          /_( /_(   , ||""")
    time.sleep(1.5)
    print("That is your new tail!")
    trivia()

def trivia():
    global points
    time.sleep(2)
    print("Time for some more trivia!")
    time.sleep(1.5)
    tr1= input("Blue flower, red ______: ").lower()
    if tr1=="thorns".lower():
        print("Great!")
        points= points+1
        trivia2()
    else:
        print("That is incorrect! Shrek will now eat you.")
        end_game()

def trivia2():
    global points
    time.sleep(1.5)
    tr2= input("Shrek: [going to save Donkey] Well, I Have to save my ___: ").lower()
    if tr2=="ass".lower():
        print("Good job, although Shrek wants you out of his swamp!")
        points= points+1
        trivia3()
    else:
        print("Wrong!")
        end_game()
        
def trivia3():
    global points
    time.sleep(2)
    print("Your new game code: knight")
    time.sleep(1.5)
    tr3= input("That'll do, ______. That'll do: ").lower()
    if tr3=="donkey":
        print("Keep going!")
        points= points+1
        trivia4()
    else:
        print("Wrong!")
        end_game()

def trivia4():
    global points
    time.sleep(1.5)
    tr4= input("Thats a nice _______: ").lower()
    if tr4=="boulder":
        print("Yes, yes it is. Jump over it and keep going!")
        points= points+1
        trivia5()
    else:
        print("No you are wrong. Shrek will now eat you!")
        end_game()

def trivia5():
    global points
    time.sleep(1.5)
    tr5= input("Ogres are like ______.: ").lower()
    if tr5=="onions":
        print("Yes, becaus they have layers!")
        points= points+1
        trivia6()
    else:
        print("No you are wrong. Shrek will now eat you!")
        end_game()

def trivia6():
    global points
    print("Your new game code: actors")
    time.sleep(1.5)
    tr6= input("Who voices for Shrek?: ").lower()
    if tr6=="mike myers":
        print("Yes, Mike Myers does play Shrek!")
        points= points+1
        trivia7()
    else:
        print("No. Shrek will now eat you!")
        end_game()
        
def trivia7():
    global points
    time.sleep(1.5)
    tr7= input("What is the first word said in the movie?: ").lower()
    if tr7=="once":
        print("Once upon a time there was a lovely princess.")
        points= points+1
        trivia8()
    else:
        print("That is not the correct answer, you do not know your shrek very well!")
        end_game()

def trivia8():
    global points
    time.sleep(1.5)
    tr8= input("What is the first song in the movie?(just the song not the band): ").lower()
    if tr8=="all star":
        print("Hey now! Thats correct!")
        points= points+1
        trivia9()
    else:
        print("No. Shrek will now eat you!")
        end_game()

def trivia9():
    global points
    time.sleep(1.5)
    print("How many shillings is Donkey almost sold for?")
    tr9= input("Enter a number, Ex: 20: ").lower()
    if tr9=="10":
        print("Correct!")
        points= points+1
        onions()
    else:
        print("No. Shrek will now eat you!")
        end_game()




def onions():
    
    global points
    time.sleep(1.5)
    print("Your new game code: throw")
    time.sleep(2)
    print("You have reached a field of onions!")
    time.sleep(1.5)
    print("You must throw the onions at Shrek!")
    time.sleep(2)
    print("""""                 ,-'     `._ 
                 ,'           `.        ,-. 
               ,'               \       ),.\ 
     ,.       /                  \     /(  \; 
    /'\_     ,o.        ,ooooo.   \  ,'  `-') 
    )) )`. d8P'Y8.    ,8P'''''Y8.  `'  .--'' 
   (`-'   `Y'  `Y8    dP       `'     / 
    `----.(   __ `    ,' ,---.       ( 
           ),--.`.   (  ;,---.        ) 
          / \O_,' )   \  \O_,'        | 
         ;  `-- ,'       `---'        | 
         |    -'         `.           | 
        _;    ,            )          : 
     _.'|     `.:._   ,.::' `..       | 
  --'   |   .'     '''         `      |`. 
        |  :;      :   :     _.       |`.`.-'--. 
        |  ' .     :   :__.,'|/       |  \ 
        `     \--.__.-'|_|_|-/        /   ) 
         \     \_   `--^"__,'        ,    | 
         ;  `    `--^---'          ,'     | 
          \  `                    /      / 
           \   `    _ _          / 
            \           `       / 
             \           '    ,' 
              `.       ,   _,' 
                `-.___.---' 
                
                              """"")
    time.sleep(1.5)
    print("Throw your onions at Shrek!")
    time.sleep(2)
    print("In order to successfully throw the onions at Shrek you must answer this question!")
    time.sleep(2)
    print("When Shrek and Donkey get to Duloc, it's set up like Disney World. There's a sign that tells how long the wait is from a certain point. How long is the wait?")
    time.sleep(3)
    when= input("Enter a number in minuets --Ex: 50--!: ")
    if when=="45":
        print("Thats correct!")
        time.sleep(1.5)
        print("Although there are only two people in the line!")
        time.sleep(1.5)
        print("Great job you hit Shrek in the eye and mouth with the onions!")
        print("""""                 ,-'     `._ 
                 ,'           `.        ,-. 
               ,'               \       ),.\ 
     ,.       /                  \     /(  \; 
    /'\_     ,o.        ,ooooo.   \  ,'  `-') 
    )) )`. d8P'Y8.    ,8P'''''Y8.  `'  .--'' 
   (`-'   `Y'  `Y8    dP       `'     / 
    `----.(   __ `    ,'#########     ( 
           ),--.`.   (  ;,**#####**    ) 
          / \O_,' )   **######****    | 
         ;  `-- ,'  **********#####   | 
         |    -'    ########*****     | 
        _;    ,            )          : 
     _.'|     `.:._   ,.::' `..       | 
  --'   |   .'     '''         `      |`. 
        |  :;      :   :     _.       |`.`.-'--. 
        |  ' .     :   :__#####       |  \ 
        `     \--.########_|-/        /   ) 
         \     \_#########       ,    | 
         ;  `    `-########    ,'     | 
          \  `                    /      / 
           \   `    _ _          / 
            \           `       / 
             \           '    ,' 
              `.       ,   _,' 
                `-.___.---' 
                
                              """"")
        still_going()
    else:
        print("You missed Shrek!")
        time.sleep(1.5)
        print("He grabed you by the torso!")
        print("The game is now over")
        end_game()

def still_going():
    time.sleep(2.5)
    print("Good job you have significantly slowed shrek!")
    time.sleep(2.5)
    print("You have fallen through a portal that opened in the ground!")
    time.sleep(2.5)
    print("There is a feild of donkies!")
    time.sleep(2)
    print("They are all almost identical to you!")
    time.sleep(2.5)
    print("You are looking at your self in/with a feild of other Donkies!")
    time.sleep(2.5)
    print("You must find yourself in thrid person!")
    time.sleep(2.5)
    print("This is what you look like from third person:")
    print("    *_")
    print("   _+O|")
    print("  / /")
    time.sleep(2)
    print("You must find yourself in the feild in third person!")
    print("Which one is different?")
    print("answer like this ex: A1, B3, or F5")
    time.sleep(4)
    print("    A     B     C     D     E     F     G     H     I ")
    print("1   *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    print("2   *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    print("3   *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    print("4   *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    print("5   *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    print("6   *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    print("7   *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    print("8   *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    print("9   *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O| __+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    print("10  *_    *_    *_    *_    *_    *_    *_    *_    *_")
    print("   _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|  _+O|")
    print("  / /   / /   / /   / /   / /   / /   / /   / /   / /")
    which= input("Which donkey is different?: ").lower()
    if which== "h9":
        print("Thats correct!")
        time.sleep(1.5)
        print("You have fell through the portal again and are traveling back to your world!")
        real_world()

    else:
        print("That is not correct.")
        time.sleep(1.5)
        print("You will forever remain looking at yourself in third person and die in Donkey land!")
        time.sleep(2)
        end_game()

def real_world():
    global points
    time.sleep(2)
    print("In order to sucessfuly make it back you must answer more trivia!")
    time.sleep(2)
    print("Time for some multiple choice trivia!")
    time.sleep(2)
    print("How many gumdrop buttons does the gingerbread man have?")
    print("A. 1")
    print("B. 2")
    print("C. 3")
    print("D. 4")
    one= input(": ").lower()
    if one== "b":
        print("Thats correct!")
        points= points+1
        go1()

    else:
        print("The correct answer was two.")
        time.sleep(2)
        print("The game is now over for you!")
        end_game()

def go1():
    global points
    time.sleep(2)
    print("Which princess is not one of Lord Farquaad's potential brides?")
    print("A. Cinderella")
    print("B. Rapunzel")
    print("C. Snow White")
    print("D. Princess Fiona")
    princess= input(": ").lower()
    if princess== "b":
        time.sleep(2)
        print("Great job, she was not on Farquaad's list!")
        points= points+1
        go2()

    else:
        print("NO, she was on Farquaad's list!")
        end_game()

def go2():
    global points
    time.sleep(2)
    print("What does Fiona give Shrek as a thank you for saving her?")
    print("A. Flowers")
    print("B. A pair of socks")
    print("C. A handkerchief")
    print("D. A kiss")
    gift= input(": ").lower()
    if gift== "c":
        print("Correct!")
        points= points+1
        go3()

    else:
        print("Incorrect!")
        end_game()

def go3():
    global points
    print("Okay! Time for some fill in the blank!")
    time.sleep(2)
    fly= input("You might have seen a housefly, maybe even a superfly, but I bet you ain't never seen a donkey ___.: ").lower()
    if fly== "fly":
        print("Ha, ha Donkey! Thats correct!")
        points= points+1
        go4()

    else:
        print("That was the wrong answer.")
        time.sleep(2)
        print("Perish.")
        end_game()

def go4():
    global points
    castle= input("*Shrek looking at Farquaad's castle* Do you think he's maybe ____________ for something?: ").lower()
    if castle== "compensating":
        print("Thats correct!")
        time.sleep(2)
        print("Because he is short!")
        points= points+1
        go5()

    else:
        print("No! You are incorrect!")
        end_game()

def go5():
    global points
    sacrifice= input("Some of you may die, but that is a _________ I am willing to make.: ").lower()
    if sacrifice== "sacrifice":
        print("Yes! Farquaad said this when he was preparing to send his soldiers on a mission.")
        points= points+1
        go6()

    else:
        print("No! It was a sacrifice he was willing to make.")
        end_game()

def go6():
    global points
    allstar= input("Somebody once told me, the world was gonna ____ me.: ").lower()
    if allstar== "roll":
        print("I aint the sharpest tool in the shed!")
        time.sleep(2)
        print("Correct!")
        points= points+1
        go7()

    else:
        print("The answer was roll me. The world was gonna roll me.")
        time.sleep(2)
        print("Perish.")
        end_game()

def go7():
    time.sleep(1.5)
    print("Great job, you have sucessfully made it back to the real world!")
    time.sleep(2)
    print("You have lost Shrek and are safe.")
    time.sleep(2)
    print("But you have not made it home yet, just back to your reality!")
    time.sleep(2)
    print("As you are walking home you see a sign.")
    time.sleep(2)
    print("What's this!")
    time.sleep(2)
    print("A wanted sign!")
    time.sleep(2.5)
    print("  _____________________________________________________________________________")
    print(" |             __      __                __             .___                  |")
    print(" |            /  \    /  \_____    _____/  |_  ____   __| _/                  |")
    print(" |            \   \/\/   /\__  \  /    \   __\/ __ \ / __ |                   |")
    print(" |             \        /  / __ \|   |  \  | \  ___// /_/ |                   |")
    print(" |              \__/\__/  (______/___|  /__|  \___  /____ |                   |")
    print(" |                        _             _                                     |")
    print(" |                       | |           | |                                    |")
    print(" |                     __| | ___  _ __ | | _____ _   _                        |")
    print(" |                    / _` |/ _ \| '_ \| |/ / _ \ | | |                       |")
    print(" |                   | (_| | (_) | | | |   <  __/ |_| |                       |")
    print(" |                    \__,_|\___/|_| |_|_|\_\___|\__, |                       |")
    print(" |                                                __/ |                       |")
    print(" |                                                |___/                       |")
    print(" |                          |\               /|                               |")
    print(" |                          |\\             //|                               |")
    print(" |                          | \\           // |                               |")
    print(" |                          |_=\\         //=_|                               |")
    print(" |                          | _=||       ||=_ |                               |")
    print(" |                          \ _=||       ||=_ /                               |")
    print(" |                           \_ =\',:;:,'/= _/                                |")
    print(" |                             \__| `:` |__/                                  |")
    print(" |                                )     (                                     |")
    print(" |                               /       \                                    |")
    print(" |                              |         |                                   |")
    print(" |                              |_       _|                                   |")
    print(" |                              (0\     /0)                                   |")
    print(" |                              |         |                                   |")
    print(" |                              `.       .'                                   |")
    print(" |                               |       |                                    |")
    print(" |                               |       |                                    |")
    print(" |                               ;       |                                    |")    
    print(" |                               :|     |;                                    |")
    print(" |                               '/     \'                                    |")
    print(" |                               (()   ())                                    |")
    print(" |                                \     /                                     |")
    print(" |                                 `---'                                      |")
    print(" |                                                                            |")
    print(" |Reward: 45 Shillings                                                        |")
    print(" |If found call: 800-Shrek                                                    |")   
    print(" |____________________________________________________________________________|")
    time.sleep(3)
    print("It is a wanted sign!")
    time.sleep(2)
    print("As you look up you relize you are in Dulock!")
    time.sleep(2)
    print("You also relize that everyone is looking at you!")
    time.sleep(2)
    print("Run!")
    time.sleep(1)
    print("A mob is chasing you!")
    time.sleep(1.5)
    print("Every correct answer makes you go faster. If you get one wrong the mob catches you.")
    mob()

def mob():
    global points
    time.sleep(2)
    print("What does Fiona call Donkey after rescuing her?")
    print("A. A brave one")
    print("B. A good'en")
    print("C. A pig!")
    print("D. A noble steed")
    steed= input(": ").lower()
    if steed== "d":
        print("Thats correct.")
        time.sleep(2)
        print("Fiona sees Shrek as a knight and Donkey as her steed.")
        points= points+1
        mob2()

    else:
        print("That was wrong!")
        time.sleep(1.5)
        print("The mob has caught you!")
        caught()

def mob2():
    global points
    time.sleep(2)
    print("What does Fiona call Shrek and Donkey when she's mad at them?")
    print("A. A pig and a piglet!")
    print("B. An oversized ogre and his pathetic pet!")
    print("C. An ogre and his pet!")
    print("D. An ogre and his pig!")
    pet= input(": ").lower()
    if pet== "c":
        print("Great, keep going.")
        points= points+1
        mob3()

    else:
        print("That was wrong!")
        time.sleep(1.5)
        print("The mob has caught you!")
        caught()

def mob3():
    global points
    time.sleep(2)
    print("What does Shrek, Fiona and Donkey run into in the forest?")
    print("A. Red Riding Hood")
    print("B. Mowgli")
    print("C. Robin Hood")
    print("D. Balou")
    hood= input(": ").lower()
    if hood== "c":
        print("Thats correct!")
        time.sleep(2)
        print("Keep running!")
        time.sleep(1)
        print("Oh no!")
        time.sleep(1)
        print("You have fallen and can't get up!")
        time.sleep(2)
        print("The mob has caught you!")
        caught()

    else:
        print("That was wrong!")
        time.sleep(1.5)
        print("The mob is chasing you!")
        time.sleep(2)
        print("  ☻/   ☻/  ☻/   ☻/  ☻/   ☻/   ☻/  ☻/   ☻/  ☻/  ☻/   ☻/  ☻/  ☻/   ☻/  ☻/   ☻/   ☻/")
        print(" /▌   /▌  /▌   /▌  /▌   /▌   /▌  /▌   /▌  /▌  /▌   /▌  /▌  /▌   /▌  /▌   /▌   /▌")
        print(" /\   /\  /\   /\  /\   /\   /\  /\   /\  /\  /\   /\  /\  /\   /\  /\   /\   /\"")  
        time.sleep(2)
        print("The mob has caught you!")
        caught()

def caught():
    time.sleep(2)
    print(":(")
    time.sleep(1)
    print("The mob is draging you through the streets!")
    time.sleep(2)
    print("  ☻/   ☻/  ☻/   ☻/  ☻/   ☻/   ☻/  ☻/   ☻/  ☻/  ☻/   ☻/  ☻/  ☻/   ☻/  ☻/   ☻/   ☻/")
    print(" /▌   /▌  /▌   /▌  /▌   /▌   /▌  /▌   /▌  /▌  /▌   /▌  /▌  /▌   /▌  /▌   /▌   /▌")
    print(" /\   /\  /\   /\  /\   /\   /\  /\   /\  /\  /\   /\  /\  /\   /\  /\   /\   /\"")
    time.sleep(3)
    print("They threw you in a carrige!")
    time.sleep(2)
    print("They are taking you to Shrek!")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("They are at Shrek's house!")
    time.sleep(2)
    print("You here the doors open! But you can't see anything, they put a bag over your head.")
    time.sleep(2.5)
    print("You are in Shreks house.")
    time.sleep(2)
    print("You can smell it.")
    time.sleep(2)
    print("Shrek took off the mask!")
    time.sleep(2)
    print("*Shrek calmly sits in front of Donkey.")
    time.sleep(2)
    print("Shrek: What were you doing in my swamp?")
    time.sleep(2)
    caught2()

def caught2():
    global points
    print("A. Stealing things.")
    print("B. Hiding from Farquaad")
    print("C. Making waffles")
    what_= input(": ").lower()
    if what_== "a":
        print("Shrek: Donkey...")
        time.sleep(2)
        print("Shrek: That was the wrong answer.")
        time.sleep(2)
        print("*Shrek proceeds to cook and eat Donkey for dinner that night*")
        end_game()

    if what_== "b":
        points= points+1
        print("Shrek: Thats no excuse to be in my swamp!")
        time.sleep(2)
        print("Shrek: All fairy tale creatures are hiding from him!")
        time.sleep(2)
        print("Shrek: I'll let you stay in my swamp...")
        time.sleep(2)
        print("Shrek: As long as you don't let any other creatures come!")
        time.sleep(2)
        print("Shrek: I didn't mean to scare you.")
        time.sleep(2)
        print("Shrek: Well I did but I was'nt gonna hurt you Donkey.")
        time.sleep(2)
        print("*Shrek proceeds to untie Donkey from his restraints*")
        time.sleep(2)
        print("Shrek and Donkey live Shrekily ever after!")
        end_game()

    if what_== "c":
        points= points+1
        print("Shrek: Well you did not have to act so guilty!")
        time.sleep(2)
        print("Shrek: You can stay, as long as you don't let any other creatures come!")
        time.sleep(2)
        print("*Shrek proceeds to untie Donkey from his restraints*")
        time.sleep(2)
        print("*Donkey imediatly begins making waffles for himself and his new BFF Shrek.")
        time.sleep(2)
        print("Shrek and Donkey live Shrekily ever after!")
        end_game()

    else:
        print("Pick a letter!")
        print("Ex: A, B, or C")
        caught2()
          
def end_game():
    global points
    global username
    print("Your score was "+ str(points)+ " Donkey points.")
    points= str(points)
    score= open("score.txt","a")
    score.write(username+"'s score: "+points+"\n")
    score.close()
    time.sleep(2)
    quit()

def high_(score):
    print("Here is the current high score!")
    all_pass= []
    score_total= score.readline()
    while score_total:
        value= score_total.split()
        list_= all_pass.append(score_total)
        score_total= score.readline()
    score.close()
    all_num= []
    for this in all_pass:
        wrds= this.split(": ")
        wrds[1] = wrds[1].strip("\n")
        num= int(wrds[1])
        new_num= all_num.append(num)
    max= 0
    for i in range(len(all_num)):
        if all_num[i] > max:
            max= all_num[i]
            max_index = i
    print(all_pass[max_index])
    print("1. Yes")
    print("2. No")
    goback= input("Would you like to go back to the menu?: ")
    if goback== "1":
        menu()

    elif goback== "2":
        print("The program will now end.")
        time.sleep(2)
        quit()

    else:
        print("Pick 1 or 2!")
        print("You will now go back to the menu!")
        time.sleep(1)
        menu()




menu()
