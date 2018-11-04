import random
print "                                                                  STONE , PAPER , SCISSORS"
print "1.Enter 'st' for stone."
print "2.Enter 'p' for paper."
print "3.Enter 'sc' for scissors."
c1 = 0 # player's points
c2 = 0 # computer's points
list = ['st','p','sc']
a = 5
while (a):
        a = a-1
        s1 = raw_input("Enter your move : ")
        print "Computer, your turn!!"
        s2 = list[random.randint(0,len(list)-1)]
        print s2
        if s1 == s2:
                print "Same move"
        elif s1 == 'st' and s2 == 'p':
                c2 += 1
                print "Computer, good job!"
                print "Player :",c1
                print "Computer :",c2
        elif s1 == 'st' and s2 == 'sc':
                c1 += 1
                print "Player, good job!"
                print "Player :",c1
                print "Computer :",c2
        elif s1 == 'p' and s2 == 'sc':
                c2 += 1
                print "Computer, good job!"
                print "Player :",c1
                print "Computer :",c2
        elif s1 == 'p' and s2 == 'st':
                c1 += 1
                print "Player, good job!"
                print "Player :",c1
                print "Computer :",c2
        elif s1 == 'sc' and s2 == 'st':
                c2 += 1
                print "Computer, good job!"
                print "Player :",c1
                print "Computer :",c2
        elif s1 == 'sc' and s2 == 'p':
                c1 += 1
                print "Player, good job!"
                print "Player :",c1
                print "Computer :",c2
print "Player's total points :",c1
print "Computer's total points :",c2              
if c1 > c2:
        print "Player, you won!!!!!"
elif c2 > c1:
        print "Computer, you won!!!!!"
else:
        print "It's a draw."
        


















