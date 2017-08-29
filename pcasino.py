



"""Word Scramble"""


def wordscramble():
    import random
    import re  #need this to import the regex function
    #makes several lists with each containing several different cities
    europe=["london","paris","rome","berlin","barcelona","vienna","zurich","moscow",
            "saint petersburg","budapest","warsaw","munich","prague","amsterdam",
            "brussels","dublin","madrid","stockholm","oslo","helsinki"]
    us=["boston","portland","new york city","philadelphia","los angeles","miami",
        "houston","dallas","albuquerque","denver","salt lake city","seattle",
        "nashville","cincinatti","cleveland","milwaukee","kansas city","saint louis",
        "omaha","detroit","baltimore","san francisco","phoenix","san antonio",
        "new orleans","charlotte","washington dc","chicago"]
    minnesota=["duluth","rochester","minneapolis","saint paul","stillwater","alexandria",
               "bloomington","saint cloud","moorhead","ely","mankato","winona","faribault"]
    asia=["tokyo","beijing","hong kong","bangkok","shanghai","taipei","osaka","seoul"]
    latin_america=["mexico city","buenos aires","rio de janeiro","sao paulo","lima","quito",
                   "havana","bogota","caracas"]

    all=["us","minnesota","latin_america","europe","asia"]  #Makes a list of all of the location lists
    print ("\n")
    selection=random.choice(all)  #selects a random list from the all list

    if selection=="europe":
        print ("Unscramble the word below.  The category is European cities.")
        newword=random.choice(europe)  #newword is the word that has been selected for the puzzle
    elif selection=="minnesota":
        print ("Unscramble the word below.  The category is Minneosta cities.")
        newword=random.choice(minnesota)
    elif selection=="us":
        print ("Unscramble the word below.  The category is major US cities.")
        newword=random.choice(us)
    elif selection=="asia":
        print ("Unscramble the word below.  The category is major Asian cities.")
        newword=random.choice(asia)
    elif selection=="latin_america":
        print ("Unscramble the word below.  The category is major Latin American cities.")
        newword=random.choice(latin_america)


    #print(newword)  this is printing the answer.  I will take it out for the final game
    underscorePhrase = re.sub('[0-9a-zA-Z]', "_", newword)  #the regex function replaces all chars in string with something else
    #in this case, this is what took me so long...to get a space between the space in the city names
    h="  ".join(underscorePhrase) #this will make an extra space between all chars in underscorePhrase string
    print ("\n")
    print (h) #these are the underscores actually printing
    word1=newword.replace(" ","")  #creates new variable, and word.replace method removed spaces
    wordlist2=(list(word1)) #puts the chars of the string, now without spaces, into a new list
    b=random.shuffle(wordlist2)  #picks a random order for the list, named b
    print ("\n")
    print ("   ".join(wordlist2))  #turns the newly scrambled list into a string, with three spaces between chars

    print ("\n")
    answer=input("What is your guess? ")
    newword1=newword.title()  #this variable makes it so an answer in uppercase letter first is OK
    newword2=newword.upper()

    if answer==newword or answer==newword1 or answer==newword2:  #this makes it so upper case or lower case are all ok
        print ("Right!")
    else:
        print ("That's incorrect")










"""Hangman"""


def hangmangame():
    def hangman(countwrongguesses):
            import turtle
            wn=turtle.Screen()        
            jo=turtle.Turtle()
            jo.hideturtle()
            jo.speed(10)
            jo.pensize(8)
            if countwrongguesses==1:
                head()
                wn.exitonclick()
            if countwrongguesses==2:
                head()
                body()
                wn.exitonclick()
            if countwrongguesses==3:
                head()
                body()
                rightleg()
                wn.exitonclick()
            if countwrongguesses==4:
                head()
                body()
                rightleg()
                leftleg()
                wn.exitonclick()

            if countwrongguesses==5:
                head()
                body()
                rightleg()
                leftleg()
                rightarm()
                wn.exitonclick()


            if countwrongguesses==6:
                head()
                body()
                rightleg()
                leftleg()
                rightarm()
                leftarm()
                wn.exitonclick()

            if countwrongguesses==7:
                head()
                body()
                rightleg()
                leftleg()
                rightarm()
                leftarm()
                rightfoot()
                wn.exitonclick()
            
            if countwrongguesses==8:
                head()
                body()
                rightleg()
                leftleg()
                rightarm()
                leftarm()
                rightfoot()
                leftfoot()
                turtle.write("You Lose!",align="center",font=("Arial",44,"bold"))
                wn.exitonclick()
            
        
            
    def head():
        import turtle
        wn=turtle.Screen()        
        jo=turtle.Turtle()
        jo.hideturtle()
        jo.speed(10)
        jo.pensize(8)
        jo.penup()
        jo.right(180)
        jo.forward(170)
        jo.left(90)
        jo.forward(190)
        jo.right(90)
        jo.pendown()
        jo.forward(120)
        jo.left(180)
        jo.forward(240)
        jo.left(180)
        jo.forward(120)
        jo.right(90)
        jo.forward(500)
        jo.right(90)
        jo.forward(200)
        jo.right(90)
            
        jo.forward(80)
        jo.right(90)
        jo.circle(40)
    
           

    def body():
        import turtle
        wn=turtle.Screen()        
        jo=turtle.Turtle()
        jo.hideturtle()
        jo.speed(10)
        jo.pensize(8)
        jo.penup()
        jo.goto(30,230)
        jo.right(90)
        jo.forward(80)
        jo.pendown()
        jo.forward(40)
        jo.forward(120)

    def rightleg():
        import turtle
        wn=turtle.Screen()        
        jo=turtle.Turtle()
        jo.hideturtle()
        jo.speed(10)
        jo.pensize(8)
        jo.penup()
        jo.goto(30,-10)
        jo.right(60)
        jo.pendown()
        jo.forward(120)

    def leftleg():
        import turtle
        wn=turtle.Screen()        
        jo=turtle.Turtle()
        jo.hideturtle()
        jo.speed(10)
        jo.pensize(8)
        jo.penup()
        jo.goto(30,-10)
        jo.right(120)
        jo.pendown()
        jo.forward(120)

    def rightarm():
        import turtle
        wn=turtle.Screen()        
        jo=turtle.Turtle()
        jo.hideturtle()
        jo.speed(10)
        jo.pensize(8)
        jo.penup()
        jo.goto(30,110)
        jo.right(30)
        jo.pendown()
        jo.forward(100)

    def leftarm():
        import turtle
        wn=turtle.Screen()        
        jo=turtle.Turtle()
        jo.hideturtle()
        jo.speed(10)
        jo.pensize(8)
        jo.penup()
        jo.goto(30,110)
        jo.right(150)
        jo.pendown()
        jo.forward(100)

    def rightfoot():
        import turtle
        wn=turtle.Screen()        
        jo=turtle.Turtle()
        jo.hideturtle()
        jo.speed(10)
        jo.pensize(8)
        jo.penup()
        jo.goto(90,-113.92)
        jo.left(20)
        jo.pendown()
        jo.forward(50)

    def leftfoot():
        import turtle
        wn=turtle.Screen()        
        jo=turtle.Turtle()
        jo.hideturtle()
        jo.speed(10)
        jo.pensize(8)
        jo.penup()
        jo.goto(-30,-113.92)
        jo.left(160)
        jo.pendown()
        jo.forward(50)

        jo.penup()
        jo.goto(30,210)
        jo.right(160)
        jo.forward(10)
        jo.right(45)
        jo.pendown()
        jo.forward(20)
        jo.penup()
        jo.right(135)
        jo.forward(15)
        jo.right(135)
        jo.pendown()
        jo.forward(20)

        jo.penup()
        jo.left(135)
        jo.forward(45)
        jo.right(225)
        jo.pendown()
        jo.forward(20)
        jo.penup()
        jo.right(135)
        jo.forward(15)
        jo.right(135)
        jo.pendown()
        jo.forward(20)




   
   







    import random
    import re   #imports to use the regex function

    christmas=["WHITE CHRISTMAS","RUDOLPH THE RED NOSED REINDEER","JINGLE BELL ROCK",
               "HERE COMES SANTA CLAUS","LITTLE DRUMMER BOY","ROCKIN AROUND THE CHRISTMAS TREE",
               "SANTA CLAUS IS COMING TO TOWN","GRANDMA GOT RUN OVER BY A REINDEER",
               "FELIZE NAVIDAD","BLUE CHRISTMAS","DO YOU HEAR WHAT I HEAR","WINTER WONDERLAND",
               "ALL I WANT FOR CHRISTMAS IS MY TWO FRONT TEETH","HOLLY JOLLY CHRISTMAS",
               "CHRISTMAS STORY","ELF","NIGHTMARE BEFORE CHRISTMAS","HOME ALONE","GREMLINS",
               "HOW THE GRINCH STOLE CHRISTMAS","DIE HARD","JINGLE ALL THE WAY","THE SANTA CLAUS",
               "BAD SANTA","CHRISTMAS VACATION"]


               

    cartoon=["MICKEY MOUSE","BUGS BUNNY","FRED FLINTSTONE",
             "SPONGE BOB SQUAREPANTS","SCOOBY DOO","BEAVIS AND BUTTHEAD",
             "PINK PANTHER","SPEED RACER","PIKACHU","JESSICA RABBIT",
             "SCROOGE MCDUCK","TEENAGE MUTANT NINJA TURTLES","REN AND STIMPY",
             "HE MAN","SPEEDY GONZALES","SNOOPY","POPEYE THE SAILORMAN",
             "TASMANIAN DEVIL","PETER GRIFFITH","GARFIELD","YOSEMITE SAM",
             "PINOCCHIO","ALADDIN","PETER PAN","THE INCREDIBLES","BETTY BOOP"]
    entertainment=["MICHAEL JACKSON","BRAD PITT","CHUCK NORRIS","ARNOLD SCHWARZENEGGER",
                   "GEORGE CLOONEY","TINA FEY","BILL MURRAY","WILL FERRELL","JIM CARREY",
                   "BEN STILLER","EDDIE MURPHY","SIMON PEGG","NEIL PATRICK HARRIS",
                   "ZACH GALIFIANAKIS","JACK BLACK","STEVE MARTIN","WOODY ALLEN",
                   "DAN AYKROYD","DANNY DEVITO","JOHN CANDY","CHEVY CHASE"]


    cgory=["christmas","cartoon","entertainment"]  #this is the list of categories
    cgorychoose=random.choice(cgory)   #this chooses a random list to choose the word from

    if cgorychoose=="christmas":      #these if statements choose a random word the previously randomly selected list
        answer=random.choice(christmas)
        cgorychoose="Christmas songs and movies"

    elif cgorychoose=="cartoon":
        answer=random.choice(cartoon)
        cgorychoose="famous cartoon characters"
 
    elif cgorychoose=="entertainment":
        answer=random.choice(entertainment)
        cgorychoose="famous entertainers"

    answerlist=(list(answer))  #creates a list with all of the characters the list

    answerlist=[x for x in answerlist if x.strip()]  #this took me forever to figure out. this removes the empty string from the list
    answerlist2=list(set(answerlist))   #this is the new list with the empty string removed.  I beleive the "set" function also modifies the list to make it only unique characters
    answerstring= ("".join(answerlist2))  #this turns the list with the empty string removed into a string
    anslength=len(answerstring)  #this gives the length of the string, and this was necessary to calculate how many correct guesses it takes until the puzzle is solved


    print ("OK, so this game is hangman")
    print ("Guess a letter of a word, and guess the word \n")
    print ("The category is " + cgorychoose + ".\n")

    rightchoices=(list(answer))  #this is a list of all the necessar right choice.  Not sure if it is still necessary since I originally put it here, and modified the code tremendously since then
    allchoices=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    wrongguesses=[] #creates an empty list of wrong guesses
    rightguesses=[] #creates an empty list of right guesses


    underscorePhrase = re.sub('[0-9a-zA-Z]', "_", answer) #the regex function replaces all chars in string with something else.  This took me a long time to figure out
    underscorePhraselist=(list(underscorePhrase))  #this turns the underscore phrase string that was made to be printed out, into a list, so that chars can be reinserted to show which answers are correct


    h="  ".join(underscorePhrase) #this will make an extra space between all chars in underscorePhrase string
    print (h + "\n")  #this prints the empty string of underscores
    count=0
    countwrongguesses=0
    countrightguesses=0
    while countwrongguesses<=8 or rgsl==anslength:  #while statement saying the game will be over with 8 wrong guesses (hangman), or if the number of right guesses are equal to the total number of unique characters in the answer string
        guess1=input("What is your guess?, or type 'solve' to guess at any time \n" )
        if guess1=="solve":  #can cut the game short to solve with this if statement
            solveguess1=input("OK smartypants...what is your guess...and spelling counts?")
            solveguess=solveguess1.upper()
            if solveguess==answer:
                answercap=answer.title()  #makes it capitalize each word of the answer for the next line
                print ("You cheated, but way to go!  You got it.  You correctly guessed " + answercap + ".")
                break
        guess=guess1.upper()  #makes sure the letter is in upper case, if not
        if len(guess)!=1:  #if more than one letter is added, it tells you you have to do it again.  This is not counted in the count
            print ("you can only enter a single letter at a time")
            continue
    
        if guess in rightguesses or guess in wrongguesses:  #if the letter has already been guessed, it tells you.  This is not counted in the count
            print ("You have already guessed that letter.  Please choose again")
            continue
        count+=1
        if not guess.isalpha():
            print ("It is forbidden to enter anything other than a letter of the alphabet")
            continue

        if guess in rightchoices:
            for n, i in enumerate(rightchoices):   #This is the part that I finally solved.  If it's in right choices, it adds it to the list
                if i==guess:
                    rightchoices[n]=guess
                    underscorePhraselist[n]=guess  #It adds the correct guess to the underscore phrase list in the correct position
        
            print ("\n\nYes...there is a %s \n"  %guess)
            allchoices.remove(guess)
            rightguesses.append(guess)  #adds the correct guess to the list, rightguesses
            countrightguesses+=1   #counts +1 to the counter countrightguesses
        
            print ("   ".join(underscorePhraselist))  #turning it into a string for a more visually appealing underscore list without brackets
            print ("\n")
            acr=(" ".join(allchoices))  #turns the choices left into a string for more visual appeal
            print ("Remaining letters\n" + acr)
        
            rgs= ("".join(rightguesses))  #turns the right guesses into a string for more visual appeal
            rgsl=len(rgs)
            print ("Correctly guessed letters\n" + rgs)  
        
            wgs= (" ".join(wrongguesses))  #turns the wrong guesses into a string for more visual appeal
        
        
        
            print ("Wrongly guessed letters\n" + wgs)
            if rgsl==anslength:
                print ("You win!")
                break
    
             
    

        else:  #The else statement for if the guess is wrong
       
            print ("No...there is no %s \n"  %guess)
            wrongguesses.append(guess)   #the wrong guess guess gets appended to the wrongguesses list
            countwrongguesses+=1
            hangman(countwrongguesses)
            allchoices.remove(guess)
            print ("   ".join(underscorePhraselist))
            print ("\n")
        
            acr=(" ".join(allchoices))
        
            print ("Remaining letters\n" + acr)
        
            rgs= (" ".join(rightguesses))
            print ("Correctly guessed letters\n" + rgs)
       
            wgs= (" ".join(wrongguesses)) 
        
            print ("Wrongly guessed letters\n" + wgs)
      

            if countwrongguesses>=8:
                print("That's it!  Game over!")
                break



"""Trivia"""


def trivia():
    import random
    print ("Welcome to trivia")
    print ("To win, you would need to answer 3 progressively more difficult questions")
    print ("If you get one wrong, the game is over")
    print ("A category will be chosen randomly \n")

    category=["math","hockey","minneapolis"]  #creates a list of the categories

    selection=random.choice(category)  #selects a random category

    print ("The category is " + selection + "\n")
    #creates a dictionary of questions and answers.  First set is level 1 difficulty.  Second set is level 2 difficulty.  Third set is level 3
    mathquestions={"What is 2+2?":"4", "What is 3 + 4":"7"}
    hockeyquestions={"What's a puck made of?":"rubber","What's Minnesota's team?":"wild"}
    minneapolisquestions={"Is it the capital?":"no","What's the sister city":"Saint Paul"}

    mathquestions2={"What is 2*6?":"12", "What is 3 * 4":"12"}
    hockeyquestions2={"How many goals is a hat trick?":"3","What's Minnesota's farm team?":"aeros","What was the Wild's first year in the NHL?":"1997"}
    minneapolisquestions2={"Is it the largest city in MN?":"yes","What river runs through it?":"Mississippi"}

    mathquestions3={"What is the square root of 9?":"3", "What is 2 squared":"4"}
    hockeyquestions3={"How many periods in a regulation game?":"3","How many minutes in a period?":"20"}
    minneapolisquestions3={"What is the baseball team name?":"twins","What is the football team name?":"Vikings"}


    if selection=="math":  #if math is the random selection, it goes into this if statement
        mq1=random.choice(list(mathquestions.keys()))  #selects a dictionary entry from the mathquestions dictionary
        print (mq1)
        ans=mathquestions.get(mq1)  #gets the answer for the corresponding question in the dictionary
        #print (ans)
        uans=input("Your answer: ")
        print (uans)
        if uans.lower()==ans.lower():  #makes sure it's in the correct uppercase/lowercase
            print ("Right!")
            print ("Now, on to question 2...and more difficult\n")
            mq2=random.choice(list(mathquestions2.keys()))  #goes on to question 2 in the same format
            print (mq2)
            ans2=mathquestions2.get(mq2)
            #print (ans2)
            uans2=input("Your answer: ")
            print (uans2)
            if uans2.lower()==ans2.lower():
                print ("Right!")
                print ("Now, on to question 3...and the most difficult of all!!!\n")
                mq3=random.choice(list(mathquestions3.keys()))
                print (mq3)
                ans3=mathquestions3.get(mq3)
                #print (ans3)
                uans3=input("Your answer: ")
                print (uans3)
                if uans3.lower()==ans3.lower():
                    print ("Right!")
                else:
                    print ("Incorrect!")
            else:
                print ("Incorrect!")
        else:
            print ("Incorrect!")  #if any of these are wrong, it is incorrect, and the game is over
    


    elif selection=="hockey":  #if hockey is the random selection, it goes into this if statement
        hq1=random.choice(list(hockeyquestions.keys()))
        print (hq1)
        ans=hockeyquestions.get(hq1)
        #print (ans)
        uans=input("Your answer: ")
        print (uans)
        if uans.lower()==ans.lower():
            print ("Right!")
            print ("Now, on to question 2...and more difficult\n")
            hq2=random.choice(list(hockeyquestions2.keys()))
            print (hq2)
            ans2=hockeyquestions2.get(hq2)
            #print (ans2)
            uans2=input("Your answer: ")
            print (uans2)
            if uans2.lower()==ans2.lower():
                print ("Right!")
                print ("Now, on to question 3...and the most difficult of all!!!\n")
                hq3=random.choice(list(hockeyquestions3.keys()))
                print (hq3)
                ans3=hockeyquestions3.get(hq3)
                #print (ans3)
                uans3=input("Your answer: ")
                print (uans3)
                if uans3.lower()==ans3.lower():
                    print ("Right!")
                else:
                    print ("Incorrect!")
            else:
                print ("Incorrect!")
        else:
            print ("Incorrect!")


    elif selection=="minneapolis":  #if minnepolis is the random selection, it goes into this if statement
        mplsq1=random.choice(list(minneapolisquestions.keys()))
        print (mplsq1)
        ans=minneapolisquestions.get(mplsq1)
        #print (ans)
        uans=input("Your answer: ")
        print (uans)
        if uans.lower()==ans.lower():
            print ("Right!")
            print ("Now, on to question 2...and more difficult\n")
            mplsq2=random.choice(list(minneapolisquestions2.keys()))
            print (mplsq2)
            ans2=minneapolisquestions2.get(mplsq2)
            #print (ans2)
            uans2=input("Your answer: ")
            print (uans2)
            if uans2.lower()==ans2.lower():
                print ("Right!")
                print ("Now, on to question 3...and the most difficult of all!!!\n")
                mplsq3=random.choice(list(minneapolisquestions3.keys()))
                print (mplsq3)
                ans3=minneapolisquestions3.get(mplsq3)
                #print (ans3)
                uans3=input("Your answer: ")
                print (uans3)
                if uans3.lower()==ans3.lower():
                    print ("Right!")
                else:
                    print ("Incorrect!")
            else:
                print ("Incorrect!")
        else:
            print ("Incorrect!")





money=500   #sets the initial amount of money you have

print ("Welcome to the Python Casino")
print ("You have $%d to start with" % money)
print ("Each spin is a $5 wager, or you can choose how much you would like to wager")
print ("Two of the same symbols will get you to a bonus game round")
print ("You must win the bonus game round in order to win any money")
print ("Three of the same will get you....MEGA JACKPOT!  Your total multiplied by one hundred million dollars")


choice=""
wager="5"
while True:    # I had to make the while loop very long, by copying and pasting everything outside of the while loop as well as inside in order to get the wager to stay the same
    
    spun=input("Press enter to spin  (c to change wager)(q to quit)  \n")  #sets the amount you want to wager

    if spun=="q":
        print ("Thanks for playing.  Your final tally is $" + str(money) + ".")
        print ("Don't spend it all in one place")
        break

    elif spun=="c" or spun=="C":
        wager=int(input("What is your new wager? "))
    elif spun=="":
        wager=int(wager)
        
        
    else:

        print ("You must enter a valid wager")
    

    import random
    rand1=random.randint(1,5)  #rand1, rand2, rand3 are three random numbers between 1 and 4
    rand2=random.randint(1,5)
    rand3=random.randint(1,5)

    def numbertosymbol(number):  #function that turns a number into a corresponding slot symbol
        if number is 1:
            return "CHERRY"
        if number is 2:
            return "BAR"
        if number is 3:
            return "7"
        if number is 4:
            return "COIN"
        if number is 5:
            return "DIAMOND"
    
    print (numbertosymbol(rand1)+ "  ",numbertosymbol(rand2)+ "  ",numbertosymbol(rand3))  # This print function prints out the actual slot result
    if rand1==rand2!=rand3:  #this is the win/lose if/elif statements.
        print ("\nBonus Game To Win!")
        money=money+wager
        hangmangame()
    elif rand1!=rand2==rand3:
        print ("\nBonus Game To Win!")
        money=money+wager
        wordscramble()
    elif rand2!=rand1==rand3:
        print ("\nBonus Game To Win!")
        money=money+wager
        trivia()
    elif rand1==rand2==rand3:
        print (("\n")+("J"*20)+("a"*20)+("c"*20)+("k"*20)+("p"*20)+("o"*20)+("t"*20)+("!"*80))
        money=wager * 100000000
    else:
        print("\nYou lose")
        money=money-wager
    print ("Now you have $" + str(money) + " total. Current wager is $" + str(wager))

    if money<=0:
        print ("You are out of money.  You are the weakest link.  Goodbye")
        break






