score=0    #intializing the score to 0
print("Quiz")
print("-------------------------------------------------------------------------------------")
print("\n")

print("1) What country has the highest life expectancy?")
print("\n")
print("A) India")
print("B) China")
print("C) Hong Kong")
print("D) US")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="C" or answer=="c"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")
print("Score:- ",score)   #this statement ensures that the score is shown after the quiz

print("\n")
print("2) Which language has the more native speakers?")
print("\n")
print("A) English")
print("B) Hindi")
print("C) Germany")
print("D) Spanish")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="D" or answer=="d"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")
print("Score:- ",score)   #this statement ensures that the score is shown after the quiz

print("\n")
print("3) What year was the United Nations established?")
print("\n")
print("A) 1900")
print("B) 1945")
print("C) 2000")
print("D) 2015")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="B" or answer=="b"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")
print("Score:- ",score)   #this statement ensures that the score is shown after the quiz

print("\n")
print("4) Who has won the most total Academy Awards?")
print("\n")
print("A) Walt Disney")
print("B) Rami Malek")
print("C) Will Smith")
print("D) Brenan Fraser")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="A" or answer=="a"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")
print("Score:- ",score)   #this statement ensures that the score is shown after the quiz

print("\n")
print("5) How many minutes are in a full week?")
print("\n")
print("A) 10,080 minutes")
print("B) 10,000 minutes")
print("C) 5,000 minutes")
print("D) 1,00,000 minutes")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="A" or answer=="a"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")
print("Score:- ",score)   #this statement ensures that the score is shown after the quiz

print("\n")
print("6) How many elements are in the periodic table?")
print("\n")
print("A) 15")
print("B) 10")
print("C) 50")
print("D) 18")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="D" or answer=="d"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")
print("Score:- ",score)   #this statement ensures that the score is shown after the quiz

print("\n")
print("7) What company was originally called Cadabra?")
print("\n")
print("A) Flipkart")
print("B) Amazon")
print("C) Google")
print("D) Microsoft")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="B" or answer=="b"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")
print("Score:- ",score)   #this statement ensures that the score is shown after the quiz

print("\n")
print("8) What country drinks the most coffee per capita?")
print("\n")
print("A) US")
print("B) UK")
print("C) Finland")
print("D) France")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="C" or answer=="c"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")
print("Score:- ",score)   #this statement ensures that the score is shown after the quiz

print("\n")
print("9) How many bones do we have in an ear?")
print("\n")
print("A) 0")
print("B) 1")
print("C) 2")
print("D) 3")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="D" or answer=="d"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")
print("Score:- ",score)   #this statement ensures that the score is shown after the quiz

print("\n")
print("10) What is the world's fastest bird?")
print("\n")
print("A) Peregrine Falcon")
print("B) Eagle")
print("C) Vulture")
print("D) Penguin")
print("\n")

answer=input("Slect an option from A-D:- ")
print("\n")

if(answer=="A" or answer=="a"):    #this statement ensures that both upper case and lowercase inputs are considered
    print("Correct!")
    score=score+1   #the score is incremented by 1 if answer is correct
else:
    print("Incorrect")

print("\n")

if score>8:              #this statement tells if your score is greater than 8 it should add 3 to your score and print excellent
    score=score+3
    print("Excellent!!")
    print("\n")
    print("Score:- ",score)

if score>5 and score<8:    #this statement tells if your score is greater than 5 but less than 8 it should add 2 to your score and print very good
    score=score+2
    print("Very Good!!")
    print("\n")
    print("Score:- ",score)

if score>=1 and score<5:    #this statement tells if your score is greater than 1 but less than 5 it should add 1 to your score and print good
    score=score+1
    print("Good!!")
    print("\n")
    print("Score:- ",score)

if score==0:               #this statement tells if your score is equal to 0 it should print better luck next time
    print("Better Luck Next Time")
    print("\n")
    print("Score:- ",score)
