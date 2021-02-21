import random

country=['Turkey','Italy','America','Canada','France','Germany','England','Belgium','Spain','Greece','Korea','China','Japan','Portugal',
             'Bulgaria','Brazil','Mexico','Sweden','Romania','Russia','Vietnam','Zimbabwe','Bahamas','Afghanistan','Poland','Albania','Liberia',
             'Ghana','Libya','Algeria','Andorra','Zambia','Croatia','Cuba','Angola','Macedonia','Argentina','Barbados','Armenia','Australia',
             'Austria','Uzbekistan','Azerbaijan','Turkmenistan','Tuvalu','Uganda','Ukraine','Yemen','Uruguay','Bahrain','Bangladesh','KKTC']
            
class RandomWord(object):
     
    def __init__(self,country):
        self.word=random.choice(country).upper()
        self.check_word=""
        self.word_display=[]
        for x in self.word:
            self.word_display.append("_")
        print(self.word)

    def word_to_display(self, guessed_letter):
        index=0
        self.check_word=""
        for letter in self.word:
            if letter == guessed_letter:
                self.word_display.insert(index,guessed_letter)
                self.word_display.pop(index+1)
            index+=1
        if self.check!=1:
            for x in self.word_display:
                print(x,end=" ")
                self.check_word+=x
        
    def check(self):
        check_number=0
        for x in self.check_word:
            if x=="_":
                break
            else:
                check_number+=1

        if check_number==len(self.word):
            return 1
        else:
            return 0


class HangMan(object):
    
    def __init__(self):
       self.hang=[]
       self.create_hang()
       self.man=[]
       self.create_man()
    
    def create_hang(self):
        self.hang.append("*--------*")
        self.hang.append("|/       |")
        self.hang.append("|         ")
        self.hang.append("|         ")
        self.hang.append("|         ")
        self.hang.append("|         ")
        self.hang.append("|         ")
        self.hang.append("===============")
    
    def create_man(self):
        self.man.append("|      (-_-)")
        self.man.append("|        |")
        self.man.append("|       \|/")
        self.man.append("|        |")
        self.man.append("|       / \ ")

    def display_to_hang(self,wrong):
        index=0
        index2=0

        for x in self.hang:
            if index-2==wrong:
                for y in self.man:
                    if index2== wrong:
                        self.hang.insert(index,y)
                        self.hang.pop(index+1)
                        break
                    else:
                        pass
                    index2+=1
                break
            else:
                pass
            index+=1

        print()
        for i in self.hang:
            print(i)
     
    
class Game(object):

    def __init__(self):
        self.choosen_word=RandomWord(country)
        self.hangman=HangMan()
        self.wrong=-1
        self.live=5
        self.used_letters=[]
    
    def play(self):
        print("\n***** Welcome to Hangman! *****\n")
        name=input("What is your name? ")
        
        option=input("Would you like the rules to be explained? Please enter Y or N: ")
        
        if option.upper()=="Y":
            print("\nRules:",
                  "\nA random country word is chosen from the words in the list.",
                  "\nYou are expected to enter 1 letter in each round.",
                  "\nIf the letter you entered is not found in the word, the man begins to hang.",
                  "\nIf you see the picture below on the screen, you lost the game!",
                  "\n\t*--------*",
                  "\n\t|/       |"
                  "\n\t|       ( )",
                  "\n\t|        |",
                  "\n\t|       \|/",
                  "\n\t|        |",
                  "\n\t|       / \ ",
                  "\n\t===============")
        print("\n"+name.title()+", let's play hangman!")

        while self.live!=0:
            if len(self.used_letters)==0:
                self.hangman.display_to_hang(self.wrong)            
                self.choosen_word.word_to_display("")
            
            print("\nUsed letters: ",end=" ")
            for x in self.used_letters:
                print(x,end=" ")
            print("\t\tLive: "+str(self.live))
            
            entered_letter=input("\nPlease enter letter: ").upper()
            
            while entered_letter.isalpha()==False:
                entered_letter=input("You did not enter any letters. Please enter only letters: ").upper()
            
            if entered_letter not in self.used_letters:
                self.used_letters.append(entered_letter)
                
                if entered_letter not in self.choosen_word.word:
                    self.wrong+=1
                    self.live-=1
                    self.hangman.display_to_hang(self.wrong)

                    if self.live!=0:
                        self.choosen_word.word_to_display(entered_letter)
                    else:
                        print("\n\n\tGame Over !!!\n")
                else:
                    self.hangman.display_to_hang(self.wrong)
                    self.choosen_word.word_to_display(entered_letter)

                    if self.choosen_word.check()==1:
                        print("\n\n\tCongratulations "+name.title()+", you win :)\n")
                        break
            else:
                print("\n***You have entered this letter before!\n")
                self.choosen_word.word_to_display("")
            
game=Game()
game.play()