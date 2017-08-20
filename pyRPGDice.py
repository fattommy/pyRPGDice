#!/usr/bin/python

'''
This program is called "pyRPGDice" 
(sorry for the silly name XD ) and displays
the results of digitally thrown pseudo-random dice, 
that (in total/each) get modfied by modifiers as usual 
in most role playing games.
It was written in Python.
I personally wish you a lot of fun with it, because it
was a lot of fun for me writing it. :-)

It was written by Thomas Alexander Sommer, 
(e-mail) 74sommer@gmail.com
(XMPP) tommy1000@jabber.de .

Copyright (C) 2016,2017 Thomas Alexander Sommer, Neuss (Germany)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation version 2
of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You can find the GNU General Public License Version 2 from June 1991 below the source code :-) 

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

If you are to lazy to write a letter to the Free Software Foundation,
see http://www.gnu.org/licenses/gpl-2.0.html   ;-)
'''

'''
0. Read the instructions below, all of them!!!
1. Open a shell
2. Change into the directory in which this program is located
3. Make the program file executable or use the python command ("python pyRPGDice.py") 
4. Type "./pyRPGDice.py " or "python pyRPGDice.py " followed by the expressions you want to compute (They must be seperated by a ' ')

An expression consists of the following syntax and is seperated from
others by a ' ' or (Blank)Space or simply Blank.
(The syntax is given in form of a set of regular expressions.)
But at first I want to give you an overview of the parameters:
(Replace the numbers with any positive integer Numbers you see fit ;-) )

s|S             = sums up the modifiers given after the s or S operator
e|E             = lets you specify a modifier for each die
lt5             = Is the result of the expression < 5
le5             = Is the result of the expression <= 5
l5              = Outputs the smallest 5 results of the dice
gt5             = Is the result of the expression > 5
ge5             = Is the result of the expression >= 5
g5              = Outputs the highest 5 results of the dice
ml5              = Outputs the middle 5 results of the dice, with a tendency to the smaller results
mr5              = Outputs the middle 5 results of the dice, with a tendency to the higher results
c1,2            = Outputs the number of occurences of 1 and 2 in the results
ra              = Rerolls on all pairs of dice and sums up the results 
r1,5            = Rerolls on all pairs of 1s and 5s and sums up the results


Number          = [1|2|3|4|5|6|7|8|9]
Number_0        = [1|2|3|4|5|6|7|8|9|0]

dice_expr       = ([Number(Number_0)*[dDwW]Number(Number_0)*]['+'[Number(Number_0)*[dDwW]Number(Number_0)*]*[' '|s|S|e|e]?([+|-]Number(Number_0)*)*[ |ltNumber(Number_0)*|leNumber(Number_0)*|lNumber(Number_0)*|gtNumber(Number_0)*|geNumber(Number_0)*|gNumber(Number_0)*|c(Number(Number_0)*,)*..(Number(Number_0)*)|ra|r(Number(Number_0)*,)*..(Number(Number_0)*)|mlNumber(Number_0)*|mrNumber(Number_0)*])
range_expr      = (Number(Number_0)*-Number(Number_0)*([+|-]Number(Number_0)*)*)
<Expression>    = (dice_expr|range_expr)

<Parameters>    = (<Expression>' ')+


Examples:

"./pyRPGDice.py 2d6" rolls 2 six-sided dice without modifiers

"./pyRPGDice.py 2d6+3-1" rolls 2 six-sided dice with the modifiers +3 and -1 and sums everything up (this is the same as "./dice_beta.py 2d6s+3-1")

"./pyRPGDice.py 2d6e+3-1" rolls 2 six-sided dice with the modifiers +3 and -1. The first die gets modified with +3 and the second with -1

"./pyRPGDice.py 2d6+3-1lt5" equals to (2d6s+3-1)<5

"./pyRPGDice.py 2d6+6-3ge5" equals to (2d6s+6-3)>=5

"./pyRPGDice.py 2d6c1,2" counts the occurences of 1s and 2s on the two dice rolls

"./pyRPGDice.py 2d6e+6-3c1,2" counts the occurences of 1s and 2s on the two dice rolls, where the first die gets modified by +6 and the second die gets modified by -3
                            Lets assume we roll a 1 and a 5. 1+6=7 and 5-3=2 so we count zero 1s and one 2, which is printed

"./pyRPGDice.py 1-100" throws a 100-sided die and prints the result 

"./pyRPGDice.py 1-100+3-1" throws a 100-sided die, which gets modified by +3 and -1 (= +2)  and prints the result

"./pyRPGDice.py 10-20" throws a 10-sided die, with range r=[10,20], that is 10,11,12,..,19,20. The result will be in this interval.


Since version 3 you can also use:

"./pyRPGDice.py 2d6+3d4+5gt1" throws two six sided dice, three four sided dice, adds 5 to the sum and checks if the sum is greater than 1
(So at the beginning of each expression you can specify a sequence of dice (types) and their numbers seperated by a 'd' in the middle and by a '+' from each other.
What i mean is something like 1d10+1d8+4d6+3d4+1d2+4+3+1gt1)

just play with it a little, you will figure it out ;-)

This is the more or less final, third version of my program, pyRPGDice.
I have tested it, as good as one man can and fixed some bugs.
In my tests the program ran as expected, nevertheless if you find a bug, then report it.
I can't guarantee absolute correctnes, but who can?
Everyone makes mistakes, so do I.
So use pyRPGDice with some common sense and always check the results a second time.
If something doesn't seem right, write a bug report with your input, I will check if I can reproduce the reported bug and try to fix it as soon as I can.
Also: I do NOT recommend using earlier versions of this program, because they are not as thourougly tested as this final version.
Especially I advise you, NOT to use the second version of this program, because it is bug infested and will not be supported anymore.
The first version of this program is, as far as I can remember ok - if you like it clunkie, that is ;-) - but the first version won't be supported anymore, also.
Last but not least: Have fun with pyRPGDice. :-)

'''


#++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++
#++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++
#++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++
#++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++
#++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++
#++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++++++++script++++++



import sys
import random


mode='' #String, which describes the (current) script mode, ie. 'dice_mode' or 'range_mode' 
args=[] # array, which contains the given arguments by the shell, they are divided by ' ' and stored seperately in array elements



'''
Function for line breaks
'''

def wsp(w):
    if w>0:
        for i in range(0,w):
            print



'''
Function for parsing digits contained in strings into int digits
'''

def isDigit(str):
    if str == '1':
        return 1
    elif str == '2':
        return 1
    elif str == '3':
        return 1
    elif str == '4':
        return 1
    elif str == '5':
        return 1
    elif str == '6':
        return 1
    elif str == '7':
        return 1
    elif str == '8':
        return 1
    elif str == '9':
        return 1
    elif str == '0':
        return 1
    else:
        return 0





'''
Function for evaluating, ie. parsing the input string
'''

def evaluate(expr):
    expr+='    ' #Last +4*Blank
    mode=''
    
    
    '''
    
    Deciding program mode
    
    '''
    
    for i in range(0,len(expr)):
        if expr[i] == 'd' or expr[i] == 'D' or expr[i] == 'w' or expr[i] == 'W':
            mode = 'dice_mode'
            break
        elif expr[i] == '-':
            mode = 'range_mode'
            break
    '''        
    if mode!='dice_mode':
        mode= 'range_mode'
    '''
        
    #print expr,mode
    
    index = 0 #Index holds the evaluation index of the expression, which gets step by step parsed by this script
    numStr='' #temporary variable, which is used for the transformation of integers in a String (eg. '123') into real integers (eg. 123)
    

#******dice_mode************dice_mode************dice_mode************dice_mode************dice_mode************dice_mode************dice_mode****** 
#******dice_mode************dice_mode************dice_mode************dice_mode************dice_mode************dice_mode************dice_mode****** 
#******dice_mode************dice_mode************dice_mode************dice_mode************dice_mode************dice_mode************dice_mode****** 

    
    if mode == 'dice_mode':
        #print 'dice_mode'
        
        numberOfDiceTypes = 0
        diceNum=[]              # array, which contains the number of dice of each dice type
        diceType=[]             # array, which contains the given dice types
        dice_mod=''             # contains the dice modifier summation modus 'sum' or 'each'
        modifier=[]             # array of modifiers, either to the dice sum or to each die
        diceSum=0               # sum of the results of the dice
        results=[]              # array, which contains the results of the virtually thrown dice
        goal=0                  # goal for special expressions, e.g. '<= goal'
        found=0                 # special auxiliary variable for evaluating the given input (loop variable)
    
        index=0                 # contains the current position in the expression string
        numStr=''               #temporary variable, which is used for the transformation of integers in a String (eg. '123') into real integers (eg. 123)
        


        '''
        Calculating the number of different dice types
        
        '''
        
        for i in range(0,len(expr)):
            if expr[i] == 'd' or expr[i] == 'D' or expr[i] == 'w' or expr[i] == 'W':
                numberOfDiceTypes+=1
        
        '''
        Evaluating diceNum and diceType, ie. filling the corresponding arrays, with the correct values
        
        '''
        
        k=0
        while k<=numberOfDiceTypes:
            numStr=''
            
            if isDigit(expr[index]):
                while expr[index]!='d' and expr[index]!='D' and expr[index]!='w' and expr[index]!='W'  and expr[index]!='s' and expr[index]!='S' and expr[index]!='e' and expr[index]!='E' and expr[index]!='+' and expr[index]!='-' and expr[index]!='c' and expr[index]!='m' and expr[index]!='l' and expr[index]!='g' and expr[index]!='r' and expr[index]!=' ':
                    if isDigit(expr[index]):
                        numStr+=expr[index]
                    index+=1;            
                #print numStr
            if expr[index] =='d' or expr[index] =='D' or expr[index] =='w' or expr[index] =='W':
                if numStr!='': 
                    diceNum.append(int(numStr))
                numStr=''
                index+=1
            elif expr[index]=='+' or expr[index]=='-' or expr[index]=='s' or expr[index]=='S' or expr[index]=='e' or expr[index]=='E' or expr[index]=='+' or expr[index]=='-' or expr[index]=='c' or expr[index]=='m' or expr[index]=='l' or expr[index]=='g'  or expr[index]=='r' or expr[index]==' ':
                if numStr!='':
                    diceType.append(int(numStr))
                numStr=''
                index+=1
                k+=1
            if k==numberOfDiceTypes:
                index-=1    
        
        '''        
        wsp(2)                
        print numberOfDiceTypes    
        print 'diceType:',diceType
        print 'diceNum :',diceNum    
        wsp(1)
        '''
        
        
        #correcting the index, because it runned one digit to far
        index-=1
        
        '''
        print 'index:\t',index
        print 'charAt(index)', expr[index]
        '''
        
        '''
        Deciding dice_mod
        
        '''
        
        if expr[index] =='s' or expr[index]=='S' or expr[index]=='+' or expr[index]=='-' or expr[index]=='c' or expr[index]=='m' or expr[index]=='l' or expr[index]=='g'  or expr[index]=='r' or expr[index]==' ':
            dice_mod='sum'
        elif expr[index] == 'e' or expr[index]=='E':
            dice_mod='each'
        
        #print 'dice_Mod:', dice_mod
        
        
        '''                        
        #Checking if the previous block run one character to far and skipped an operator or the beginning of the sequence of modifiers
        
        if expr[index-1]=='+' or expr[index-1]=='-' or expr[index-1]=='c' or expr[index-1]=='m' or expr[index-1]=='l' or expr[index-1]=='g'  or expr[index-1]=='r':
            index-=1
        '''
        
        '''
        print 'After correction evaluation'
        print 'index:', index
        print 'charAt(index):', expr[index]
        print 'numStr:', numStr
        print 'diceMod: ', dice_mod
        '''
        
        #print expr[index]
        
        
        numStr=''
        found = 0
        end = 0
        term = 0
        
        '''
        
        evaluating modifiers

        '''                
        while end == 0:
            term=0
            if expr[index]=='c' or expr[index]=='m' or expr[index]=='l' or expr[index]=='g'  or expr[index]=='r'  or expr[index]==' ':
                end=1
                
            if expr[index]=='+':
                index+=1
                while term == 0:
                    if expr[index]=='c' or expr[index]=='m' or expr[index]=='l' or expr[index]=='g'  or expr[index]=='r'  or expr[index]==' ':
                        term = 1
                        end = 1
                    if expr[index]=='+' or expr[index]=='-':
                        term = 1
                        index-=1
                        break
                    if isDigit(expr[index]):
                        numStr+=expr[index]
                    index+=1
                #print numStr
                modifier.append(int(numStr))
                numStr=''
            
            if expr[index]=='-':
                index+=1
                while term == 0:
                    if expr[index]=='c' or expr[index]=='m' or expr[index]=='l' or expr[index]=='g'  or expr[index]=='r'  or expr[index]==' ':
                        term = 1
                        end = 1
                    if expr[index]=='+' or expr[index]=='-':
                        term = 1
                        index-=1
                        break
                    if isDigit(expr[index]):
                        numStr+=expr[index]
                    index+=1
                #print (int(numStr)*-1)
                modifier.append(int(numStr)*-1)
                numStr=''
            index+=1
        
        '''
        
        correcting current cursor position by a certain value, because the previous block increments the cursor position
        not always correctly    
        
        '''
        #print 'charAt(',index,')=', expr[index]
        if expr[index]!='c' and expr[index]!='m' and expr[index]!='l' and expr[index]!='g' and expr[index]!='r' and expr[index]!=' ': 
            index-=2
        elif expr[index]=='l' or expr[index]=='r':
            if expr[index-1]=='m':
                index-=1
        #print 'charAt(',index,')=', expr[index]    
        if expr[index]=='s' or expr[index]=='S' or expr[index]=='e' or expr[index]=='E' or isDigit(expr[index]):
            if expr[index-1]=='l' or expr[index-1]=='g':
                index-=1
            else:
                index+=1
        #print 'charAt(',index,')=', expr[index]
        if expr[index]==' ':
            for i in range(0,len(expr)):
                if expr[i]=='c':
                    index=i
                    break
                elif expr[i]=='g':
                    index=i
                    break
                elif expr[i]=='m':
                    index=i
                    break
                elif expr[i]=='l':
                    index=i
                    break
                elif expr[i]=='r':
                    index=i
                    break
        #print 'charAt(',index,')=', expr[index] 
        
        
        '''
        wsp(2)
        print 'After evaluating modifiers'
        print modifier
        print 'last: ' , expr[index]
        print 'Index: ' , index , '/' , len(expr)
        '''
        

#+evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation+        
#+evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation+        
#+evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation++evaluation+        
        


        '''                
        evaluating goal_operators or expression_operators
        
        '''        

#############################################################################################################################################################

        #expression without any operator, i.e. a simple expression
        
        if expr[index]==' ':
            #print 'Normal expression without goal evaluation'
            
            diceSum=0   # sum of the thrown dice
            modSum=0    # sum of the modifiers
            results=[]  # array, which contains the results of the randomly thrown dice (or the sums of each dice and their modifiers)
            
                              
            wsp(2)
            
            '''
            Throwing the random dice and saving the results of the dice in the results array
            According to dice_mod the diceSum (dice_mod=='sum') or the value of each die and its modifier (dice_mod=='each') gets also calculated.
            
            '''
            
            
                   
            x=1
            for i in range(0,len(diceType)):
                for j in range(0,diceNum[i]):
                    tmp = random.randint(1,diceType[i])
                    if dice_mod=='sum':
                        print x, '. die(d',diceType[i],'):', tmp
                        results.append(tmp)
                        x+=1
                    else:
                        if (x-1) < len(modifier):
                            print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                            results.append(tmp+modifier[(x-1)])
                        else:
                            print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                            results.append(tmp)
                        x+=1
                    diceSum+= tmp
                wsp(1)  
            
            '''
            calculating the sum of modifiers for dice_mod=='sum'
            
            '''
                
            for i in range(0, len(modifier)):
                modSum+=modifier[i]
            
            wsp(2)
            
            '''
            printing each modifier, if dice_mod=='sum'
            
            '''
            
            
            if dice_mod=='sum':
                for i in range(0,len(modifier)):
                    print (i+1), '. Modifier = ' , modifier[i]
                wsp(2)
            
            results = sorted(results)
            print 'Sorted dice List= ', results
            wsp(2)
            
            if dice_mod=='sum':                            
                print 'Dice Sum ' , diceSum
                wsp(1)
                print 'Modifier Sum ' , modSum
                wsp(2)
                result = diceSum + modSum
            else:
                result=0
                for i in range(0, len(results)):
                    result+= results[i]
            
            print 'Result: ' , result
            
            wsp(2)
            
            
            
       
       
       
       
#############################################################################################################################################################

        #expressions, which goal operators start with l, ie. l,lt,le
             
        if expr[index]=='l':
            #print 'left or <= or <'




#--------------
            if expr[index+1]=='t':
                #print '<'
                
                diceSum=0   #sum of dice
                modSum=0    #sum of modifiers
                index+=2    #jumping to the goal of the evaluation expression
                
                '''
                Evaluating the goal of that specific expression, ie. the number that limits the expression
                e.g. '1d6lt10' In this example, the last number, here 10 is the goal of the expression
                and this specific expression means, that the computer throws 1 six sided die, whichs result must be less than 10
                That means: 1d6<10, but don't write that in your shell, because it will confuse it with a pipe!!!
                (Something like 'bla.txt < ls -h')
                
                '''
                
                while expr[index]!= ' ':
                  if isDigit(expr[index]):
                       numStr+=expr[index]
                  index+=1
                goal=int(numStr)
                               
                wsp(2)
                
                
                '''
                Throwing the random dice and printing the results of the dice
                According to dice_mod the diceSum (dice_mod=='sum') or the value of each die and its modifier (dice_mod=='each') gets also calculated (and printed).
            
                '''
                                
                
                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print x, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                            else:
                                print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                            x+=1
                        diceSum+= tmp
                    wsp(1)
                
                
                
                for i in range(0, len(modifier)):
                    modSum+=modifier[i]
                
                
                wsp(2)
            
                if dice_mod=='sum':
                    for i in range(0,len(modifier)):
                        print (i+1), '. Modifier = ' , modifier[i]
                    wsp(2)
                
                results = sorted(results)
                print 'Sorted dice List= ', results
                wsp(2)
                
                if dice_mod=='sum':                            
                    print 'Dice Sum ' , diceSum
                    wsp(1)
                    print 'Modifier Sum ' , modSum
                    wsp(2)
                    result = diceSum + modSum
                else:
                    result=0
                    for i in range(0, len(results)):
                        result+= results[i]
                
                
                
                print 'Result: ' , result , ' < ' , goal , ' is ' , (result < goal)
                
                wsp(2)



#--------------                
            elif expr[index+1]=='e':
                #print '<='
                                
                diceSum=0
                modSum=0
                index+=2

       
                '''
                Evaluating the goal of that specific expression, ie. the number that limits the expression
                e.g. '1d6le10' In this example, the last number, here 10 is the goal of the expression
                and this specific expression means, that the computer throws 1 six sided die, whichs result must be less than or equal 10
                That means: 1d6<=10, but don't write that in your shell, because it will confuse it with a pipe!!!
                (Something like 'bla.txt < ls -h')
                
                '''
            
                while expr[index]!= ' ':
                  if isDigit(expr[index]):
                       numStr+=expr[index]
                  index+=1
                goal=int(numStr)
                                
                wsp(2)
                
                
                '''
                Throwing the random dice and printing the results of the dice
                According to dice_mod the diceSum (dice_mod=='sum') or the value of each die and its modifier (dice_mod=='each') gets also calculated (and printed).
            
                '''
                                
                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print x, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                            else:
                                print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                            x+=1
                        diceSum+= tmp
                    wsp(1)
                
                for i in range(0, len(modifier)):
                    modSum+=modifier[i]
                
                
                wsp(2)
            
                if dice_mod=='sum':
                    for i in range(0,len(modifier)):
                        print (i+1), '. Modifier = ' , modifier[i]
                    wsp(2)
                
                results = sorted(results)
                print 'Sorted dice List= ', results
                wsp(2)
                
                if dice_mod=='sum':                            
                    print 'Dice Sum ' , diceSum
                    wsp(1)
                    print 'Modifier Sum ' , modSum
                    wsp(2)
                    result = diceSum + modSum
                else:
                    result=0
                    for i in range(0, len(results)):
                        result+= results[i]
                
                   
                print 'Result: ' , result , ' <= ' , goal , ' is ' , (result <= goal)

                wsp(1)



#---------------                
            else:
                #print 'left'
                index+=1

                results=[] # array, which contains the results of the randomly thrown dice (or the sums of each dice and their modifiers)


                '''
                Evaluating the goal of that specific expression.
                This is the number, which specifies the first n smallest, ie. most left values, that are taken from the 
                sorted results array.
                
                eg. '3d6l2' gives you the values [6,2,1].
                Then the sorted array is [1,2,6].
                According to the expression you take the two smallest (most left) values out of that array and end up with
                the array [1,2]
                
                '''
            
                while expr[index]!= ' ':
                  if isDigit(expr[index]):
                       numStr+=expr[index]
                  index+=1
                goal=int(numStr)
                
                
                '''
                Throwing the random dice and saving the results of the dice or the sums of the results and modifiers in the results array
            
                '''
                
                            
                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print x, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                            else:
                                print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                            x+=1
                        diceSum+= tmp
                    wsp(1)
                                       
                results = sorted(results)  
                
                wsp(2)  
                print 'Sorted dice: ' , results
                wsp(2)
                print 'Results: ' , results[:goal]
                
        
        
           
#############################################################################################################################################################

        #expressions, which goal operators start with a 'g', ie. g, gt, ge

        if expr[index]=='g':
            #print 'right or >= or >'
            
            
            
            
            
#---------------            
            
            if expr[index+1]=='t':
                #print '>'
                
                diceSum=0
                modSum=0
                index+=2
                
                
                
                '''
                Evaluating the goal of that specific expression, ie. the number that limits the expression
                e.g. '1d6gt10' In this example, the last number, here 10 is the goal of the expression
                and this specific expression means, that the computer throws 1 six sided die, whichs result must be greater than 10
                That means: 1d6>10, but don't write that in your shell, because it will confuse it with a pipe!!!
                (Something like 'ls -h > bla.txt')
                
                '''
                                
                while expr[index]!= ' ':
                  if isDigit(expr[index]):
                       numStr+=expr[index]
                  index+=1
                goal=int(numStr)
                                
                wsp(2)
                
                '''
                Throwing the random dice and printing the results of the dice
                According to dice_mod the diceSum (dice_mod=='sum') or the value of each die and its modifier (dice_mod=='each') gets also calculated (and printed).
            
                '''
                
                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print x, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                            else:
                                print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                            x+=1
                        diceSum+= tmp
                    wsp(1)
                
                
                for i in range(0, len(modifier)):
                    modSum+=modifier[i]
                
                wsp(2)
                
                if dice_mod=='sum':
                    for i in range(0,len(modifier)):
                        print (i+1), '. Modifier = ' , modifier[i]
                    wsp(2)
                
                results = sorted(results)
                print 'Sorted dice List= ', results
                wsp(2)
                
                
                
                if dice_mod=='sum':                            
                    print 'Dice Sum ' , diceSum
                    wsp(1)
                    print 'Modifier Sum ' , modSum
                    wsp(2)
                    result = diceSum + modSum
                else:
                    result=0
                    for i in range(0, len(results)):
                        result+= results[i]
                    
                print 'Result: ' , result , ' > ' , goal , ' is ' , (result > goal)
                
                wsp(1)
                
                
#-------------                
            elif expr[index+1]=='e':
                #print '>='
                
                diceSum=0
                modSum=0
                index+=2
                
                
                '''
                Evaluating the goal of that specific expression, ie. the number that limits the expression
                e.g. '1d6le10' In this example, the last number, here 10 is the goal of the expression
                and this specific expression means, that the computer throws 1 six sided die, whichs result must be less than or equal 10
                That means: 1d6<=10, but don't write that in your shell, because it will confuse it with a pipe!!!
                (Something like 'bla.txt < ls -h')
                
                '''
                            
                while expr[index]!= ' ':
                  if isDigit(expr[index]):
                       numStr+=expr[index]
                  index+=1
                goal=int(numStr)
                                
                wsp(2)
                
                
                '''
                Throwing the random dice and printing the results of the dice
                According to dice_mod the diceSum (dice_mod=='sum') or the value of each die and its modifier (dice_mod=='each') gets also calculated (and printed).
            
                '''

                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print x, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                            else:
                                print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                            x+=1
                        diceSum+= tmp
                    wsp(1)
                
                
                
                for i in range(0, len(modifier)):
                    modSum+=modifier[i]

                wsp(2)
            
                if dice_mod=='sum':
                    for i in range(0,len(modifier)):
                        print (i+1), '. Modifier = ' , modifier[i]
                    wsp(2)

                results = sorted(results)
                print 'Sorted dice List= ', results
                wsp(2)
                    
                if dice_mod=='sum':                            
                    print 'Dice Sum ' , diceSum
                    wsp(1)
                    print 'Modifier Sum ' , modSum
                    wsp(2)
                    result = diceSum + modSum
                else:
                    result=0
                    for i in range(0, len(results)):
                        result+= results[i]
                    
                print 'Result: ' , result , ' >= ' , goal , ' is ' , (result >= goal)

                wsp(2)
                

#-------------                
            else:
                #print 'right'
                index+=1
                
                results=[]


                '''
                Evaluating the goal of that specific expression.
                This is the number, which specifies the last n greatest, ie. most left values, that are taken from the 
                sorted results array.
                
                eg. '3d6g2' gives you the values [6,2,1].
                Then the sorted array is [1,2,6].
                According to the expression you take the two greatest (most right) values out of that array and end up with
                the array [2,6]
                
                '''
   
                while expr[index]!= ' ':
                  if isDigit(expr[index]):
                       numStr+=expr[index]
                  index+=1
                goal=int(numStr)
                
                
                
                '''
                Throwing the random dice and saving the results of the dice or the sums of the results and modifiers in the results array
            
                '''
                
                               
                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print x, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                            else:
                                print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                            x+=1
                        diceSum+= tmp
                    wsp(1)    
                    
                results = sorted(results)  
                
                wsp(2)  
                print 'Sorted dice: ' , results
                wsp(2)
                print 'Results: ' , results[-goal:]
        
        
        

        
#############################################################################################################################################################

        #the counter expression, which counts the appearances of the values specified after the 'c' and seperated by ','
        
        if expr[index]=='c':
            #print 'count'
            
            index+=1
            
            end=0
            term=0
            numStr=''
            
            counter=[]  # array of numbers, which appearence in the results array should be counted
            results=[]  # array, which contains the values of the dice (or the sums of dice and teir modifiers)
            counted=[]  # array, which contains the numbers of appearences of the corresponding counters in the counter array
            
            '''
            Evaluating the counters, which get stored in the counter array
            They should be divided by ','
            
            '''
            
            while end==0:
                term=0
                if expr[index]==' ':
                    end=1
                if isDigit(expr[index]):                       
                    while term == 0:
                        if expr[index]==' ':
                            term = 1
                            end = 1
                        if expr[index]==',':
                            term = 1
                            index+=1
                            break
                        if isDigit(expr[index]):
                            numStr+=expr[index]
                        index+=1
                    counter.append(int(numStr))
                    numStr=''
            
            #print counter
            
            wsp(2)
            
            
            
            '''
            Throwing the random dice and saving the results of the dice or the sums of the results and modifiers in the results array
            Also printing these results
            
            '''
            
            x=1
            for i in range(0,len(diceType)):
                for j in range(0,diceNum[i]):
                    tmp = random.randint(1,diceType[i])
                    if dice_mod=='sum':
                        print x, '. die(d',diceType[i],'):', tmp
                        results.append(tmp)
                        x+=1
                    else:
                        if (x-1) < len(modifier):
                            print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                            results.append(tmp+modifier[(x-1)])
                        else:
                            print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                            results.append(tmp)
                        x+=1
                    diceSum+= tmp
                wsp(1)
            
            
            
                                       
            results = sorted(results)
            
            wsp(1)
            
            print 'Sorted dice =', results
            
            wsp(2)
            
            
            # initialising the counted array
            
            for i in range(0,len(counter)):
                counted.append(0)
            
            '''
            Counting the appearences of the counters in the results array and storing them in the counted array
            
            '''
            
            for i in range(0,len(counter)):
                for j in range(0,len(results)):
                    if counter[i] == results[j]:
                        counted[i]+=1
                    j+=1
                i+=1
            

            #Printing the number of counted appearances of each specified counter (if their value is greater than zero)

            for i in range(0,len(counter)):
                if counted[i]>0:
                    print 'Number of ',counter[i],'\'s = ' , counted[i] 
                    wsp(1)
            


#############################################################################################################################################################

        '''
        Expressions, which goal operators start with a 'r', ie. 'ra' or 'r' followed by a sequence of numbers, that are seperated by ','
        These expressions let the computer reroll on (specific) pairs
        ''' 
        
        if expr[index]=='r':
            #print 'reroll on pairs'
            
#---------------
            
            if expr[index+1]=='a':
                #print 'reroll on all pairs'
                  
                counter=[]  #contains the values, that should be counted, ie. the sides of the dice
                results=[]  #contains the results of the dice thrown
                resultsDiceType=[] # contains the dice type of each result
                
                counted=[]  #contains the number of appearences of each counter in the results array
                countedDiceType=[[]] # contains the dice Types of the counted values 
                
                end=0
                term=0
                numStr=''
                
                '''
                Initialising the counter array
                Keep in mind, that range(a,b) gives you the values a,..,b-1, that is [a,b)
                '''
                
                index+=2
                
                maxVal = max(diceType)
                for i in range(1,(maxVal+1)):
                    counter.append(i)
                
                '''
                print 'maxVal: ', maxVal
                print 'counter: ', counter
                '''
                                                
                wsp(2)
                
                '''
                Throwing the random dice and saving the results of the dice or the sums of the results and modifiers in the results array
                Also printing these results
                
                '''
                diceCounter=0
                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        diceCounter+=1
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print diceCounter, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            resultsDiceType.append(diceType[i])
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print diceCounter, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                                resultsDiceType.append(diceType[i])
                            else:
                                print diceCounter, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                                resultsDiceType.append(diceType[i])
                            x+=1
                    wsp(1)
                
                
                #results = sorted(results)
                
                #test values
                #results=[1,1,1,1]

                
                '''
                Initialising the counted and countedDiceType arrays
                
                '''
                
                for i in range(0,len(counter)):
                    counted.append(0)
                    countedDiceType.append([])
                
                
                '''
                Storing the number of appearences of each counter (in the results array) in the counted array
                
                '''
                
                '''
                print 'counter:  ', counter
                print 'counted:  ', counted
                print 'cntDiceT: ', countedDiceType
                print 'results:  ', results
                print 'resDiceT: ', resultsDiceType
                '''
                
                '''
                Counting the results in the counter array and saving their diceType in countedDiceType
                '''
                
                 
                for i in range(0,len(counter)):
                    for j in range(0,len(results)):
                        if counter[i]==results[j]:
                            counted[i]+=1
                            countedDiceType[i].append(resultsDiceType[j])
                
                '''
                wsp(1)
                print 'counter:  ', counter
                print 'counted:  ', counted
                print 'cntDiceT: ', countedDiceType
                print 'results:  ', results
                print 'resDiceT: ', resultsDiceType
                '''
                
                '''
                print 'Before rerolling'
                print 'Results: ', results
                print 'counter: ', counter
                print 'counted: ', counted
                print 'pairsTmp: ', pairsTmp
                print 'pairs  : ', pairs
                wsp(1)
                '''
                
                '''
                Rerolling pairs
                
                '''
                for i in range(0,len(countedDiceType)):
                    if len(countedDiceType[i])>1:
                        countedDiceType[i]=sorted(countedDiceType[i])
                
                '''
                wsp(1)
                print 'counter:  ', counter
                print 'counted:  ', counted
                print 'cntDiceT: ', countedDiceType
                print 'results:  ', results
                print 'resDiceT: ', resultsDiceType
                '''
                
                outer=0
                ausg=0
                while outer==0:
                    for i in range(0,len(countedDiceType)):
                        if len(countedDiceType[i])>1:
                            inner=0
                            while inner==0:
                                countedDiceType[i]=sorted(countedDiceType[i])
                                #print counter
                                #print countedDiceType
                                #print i,':', countedDiceType[i]
                                
                                if len(countedDiceType[i])>1:
                                    tmp0=countedDiceType[i][0]
                                    tmp=[]
                                    cnt=1
                                    for j in range(1,len(countedDiceType[i])):
                                        if tmp0==countedDiceType[i][j]:
                                            cnt+=1
                                        else:
                                            break
                                    if cnt >1:
                                        if ausg==0:
                                            wsp(1)
                                            print 'Rerolling pairs: '
                                            wsp(1)
                                            ausg=1
                                        for j in range(0,cnt):
                                            rn=random.randint(1,countedDiceType[i][0])
                                            tmp.append(rn)
                                            diceCounter+=1
                                            print diceCounter,'. die: (d',countedDiceType[i][0],'):' , rn
                                            results.append(rn)
                                            resultsDiceType.append(countedDiceType[i][0])
                                        print                                            
                                        tmp=sorted(tmp)
                                        for c in range(0,len(counter)):
                                            for j in range(0,len(tmp)):
                                                if counter[c] == tmp[j]:
                                                    countedDiceType[c].append(countedDiceType[i][0])
                                        for j in range(0,cnt):
                                            countedDiceType[i].pop(0)
                                    elif cnt==1:
                                        countedDiceType[i].pop(0)
                                else:
                                    inner=1
                                    if len(countedDiceType[i])==1:
                                        countedDiceType[i].pop(0)
                        elif len(countedDiceType[i])==1:
                            countedDiceType[i].pop(0)
                    x=0
                    for i in range(0,len(countedDiceType)):
                        if len(countedDiceType[i])<1:
                            x+=1    
                    if x >= len(countedDiceType):
                        outer=1
                
                
                
                #print 'cntDiceT: ', countedDiceType 
                
                        
                '''
                print 'After Rerolling'
                print 'Results: ', results
                print 'counter: ', counter
                print 'counted: ', counted
                print 'pairTmp: ', pairsTmp
                print 'pairs  : ', pairs
                '''
                
                wsp(1)                
                print 'Results            = ', results
                wsp(1)
                print 'Results(diceTypes) = ', resultsDiceType                
                wsp(2)
                results = sorted(results)
                print 'Results(sorted)    = ', results
                wsp(1)
                
                
                if dice_mod=='sum':
                    diceSum=0
                    for i in range(0,len(results)):
                        diceSum+=results[i]                
                    wsp(1)
                    print 'Total Dice Sum = ', diceSum
                    wsp(1)
                    modSum=0
                    for i in range(0,len(modifier)):
                        modSum+=modifier[i]
                    print 'Total modifier Sum = ', modSum
                    wsp(1)
                    print 'Total sum (dice+modifier) =', (diceSum+modSum)
                    wsp(1)
                else:
                    diceSum=0
                    for i in range(0, len(results)):
                        diceSum+= results[i]
                    wsp(1)
                    print 'Total dice sum', diceSum
                
                
                
                
                
                
                results.append(0)                
                tmpP = results[0]
                cnt = 0
                for i in range(0,len(results)):
                    if tmpP==results[i]:
                        cnt+=1
                    else:
                        print 'Number of', results[i-1],'\'s = ', cnt, ' (total: ', results[i-1] * cnt,')'
                        tmpP=results[i]
                        cnt=1
                wsp(1)
                
                
                
                
                
#-------------                
            else:
                #print 'reroll on specific pairs'
                
                counter=[]  #contains the values, that should be counted, ie. the sides of the dice
                results=[]  #contains the results of the dice thrown
                resultsDiceType=[] # contains the dice type of each result
                
                counted=[]  #contains the number of appearences of each counter in the results array
                countedDiceType=[[]] # contains the dice Types of the counted values 
                
                end=0
                term=0
                numStr=''
                
                
                index+=1
                
                                
                '''
                Evaluating the counters, which get stored in the counter array
                They should be divided by ','
            
                '''
                
                while end==0:
                    term=0                
                    if expr[index]==' ':
                        end=1
                    if isDigit(expr[index]):
                       
                        while term == 0:
                            if expr[index]==' ':
                                term = 1
                                end = 1
                            if expr[index]==',':
                                term = 1
                                index+=1
                                break
                            if isDigit(expr[index]):
                                numStr+=expr[index]
                            index+=1
                        counter.append(int(numStr))
                        numStr=''
                                
                wsp(2)
                
                print 'counter: ', counter
                
                
                
                '''
                Throwing the random dice and saving the results of the dice or the sums of the results and modifiers in the results array
                Also printing these results
                
                '''
                
                diceCounter=0
                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        diceCounter+=1
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print diceCounter, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            resultsDiceType.append(diceType[i])
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print diceCounter, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                                resultsDiceType.append(diceType[i])
                            else:
                                print diceCounter, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                                resultsDiceType.append(diceType[i])
                            x+=1
                    wsp(1)
                
                
                
                '''
                Initialising the counted and countedDiceType arrays
                
                '''
                
                for i in range(0,len(counter)):
                    counted.append(0)
                    countedDiceType.append([])
                
                
                '''
                Storing the number of appearences of each counter (in the results array) in the counted array
                
                '''
                
                '''
                print 'counter:  ', counter
                print 'counted:  ', counted
                print 'cntDiceT: ', countedDiceType
                print 'results:  ', results
                print 'resDiceT: ', resultsDiceType
                '''
                
                '''
                Counting the results in the counter array and saving their diceType in countedDiceType
                '''
                
                 
                for i in range(0,len(counter)):
                    for j in range(0,len(results)):
                        if counter[i]==results[j]:
                            counted[i]+=1
                            countedDiceType[i].append(resultsDiceType[j])
                
                '''
                wsp(1)
                print 'counter:  ', counter
                print 'counted:  ', counted
                print 'cntDiceT: ', countedDiceType
                print 'results:  ', results
                print 'resDiceT: ', resultsDiceType
                '''
                
                '''
                print 'Before rerolling'
                print 'Results: ', results
                print 'counter: ', counter
                print 'counted: ', counted
                print 'pairTmp: ', pairsTmp
                print 'pairs  : ', pairs
                wsp(1)
                '''
                
                
                '''
                Rerolling pairs
                
                '''
                
                for i in range(0,len(countedDiceType)):
                    if len(countedDiceType[i])>1:
                        countedDiceType[i]=sorted(countedDiceType[i])
                
                '''
                wsp(1)
                print 'counter:  ', counter
                print 'counted:  ', counted
                print 'cntDiceT: ', countedDiceType
                print 'results:  ', results
                print 'resDiceT: ', resultsDiceType
                '''
                
                outer=0
                ausg=0
                while outer==0:
                    for i in range(0,len(countedDiceType)):
                        if len(countedDiceType[i])>1:
                            inner=0
                            while inner==0:
                                countedDiceType[i]=sorted(countedDiceType[i])
                                #print counter
                                #print countedDiceType
                                #print i,':', countedDiceType[i]
                                
                                if len(countedDiceType[i])>1:
                                    tmp0=countedDiceType[i][0]
                                    tmp=[]
                                    cnt=1
                                    for j in range(1,len(countedDiceType[i])):
                                        if tmp0==countedDiceType[i][j]:
                                            cnt+=1
                                        else:
                                            break
                                    if cnt >1:
                                        if ausg==0:
                                            wsp(1)
                                            print 'Rerolling pairs: '
                                            wsp(1)
                                            ausg=1
                                        for j in range(0,cnt):
                                            rn=random.randint(1,countedDiceType[i][0])
                                            tmp.append(rn)
                                            diceCounter+=1
                                            print diceCounter,'. die: (d',countedDiceType[i][0],'):' , rn
                                            results.append(rn)
                                            resultsDiceType.append(countedDiceType[i][0])
                                        print                                            
                                        tmp=sorted(tmp)
                                        for c in range(0,len(counter)):
                                            for j in range(0,len(tmp)):
                                                if counter[c] == tmp[j]:
                                                    countedDiceType[c].append(countedDiceType[i][0])
                                        for j in range(0,cnt):
                                            countedDiceType[i].pop(0)
                                    elif cnt==1:
                                        countedDiceType[i].pop(0)
                                else:
                                    inner=1
                                    if len(countedDiceType[i])==1:
                                        countedDiceType[i].pop(0)
                        elif len(countedDiceType[i])==1:
                            countedDiceType[i].pop(0)
                    x=0
                    for i in range(0,len(countedDiceType)):
                        if len(countedDiceType[i])<1:
                            x+=1    
                    if x >= len(countedDiceType):
                        outer=1
                
                        
                '''
                print 'After Rerolling'
                print 'Results: ', results
                print 'counter: ', counter
                print 'counted: ', counted
                print 'pairTmp: ', pairsTmp
                print 'pairs  : ', pairs
                '''
                
                
                wsp(1)                
                print 'Results            = ', results
                wsp(1)
                print 'Results(diceTypes) = ', resultsDiceType                
                wsp(2)
                results = sorted(results)
                print 'Results(sorted)    = ', results
                wsp(1)
                
                
                
                if dice_mod=='sum':
                    diceSum=0
                    for i in range(0,len(results)):
                        diceSum+=results[i]                
                    wsp(1)
                    print 'Total Dice Sum = ', diceSum
                    wsp(1)
                    modSum=0
                    for i in range(0,len(modifier)):
                        modSum+=modifier[i]
                    print 'Total modifier Sum = ', modSum
                    wsp(1)
                    print 'Total sum (dice+modifier) =', (diceSum+modSum)
                    wsp(1)
                else:
                    diceSum=0
                    for i in range(0, len(results)):
                        diceSum+= results[i]
                    wsp(1)
                    print 'Total dice sum', diceSum
                
                
                results.append(0)                
                tmpP = results[0]
                cnt = 0
                for i in range(0,len(results)):
                    if tmpP==results[i]:
                        cnt+=1
                    else:
                        print 'Number of', results[i-1],'\'s = ', cnt, ' (total: ', results[i-1] * cnt,')'
                        tmpP=results[i]
                        cnt=1
                
                
        
#############################################################################################################################################################

        '''
        Expressions, which goal operators start with 'm', ie. 'ml' or 'mr'
        These expressions print the middle lower or middle higher values of the thrown dice
        
        '''

         
        if expr[index]=='m':
            #print 'middle'        
            #print 'charAt :', index,' is ', expr[index]



#---------------
        
            if expr[index+1]=='l':
                #print 'middle left'
                
                numStr=''   #temporary variable, which is used for the transformation of integers in a String (eg. '123') into real integers (eg. 123)
                goal=0      #Number of elements, which are taken from the (left) middle of the results array
                results=[]  #Results of the dice thrown
                finals=[]   #Final result of the chosen array elements
                
                index+=2
                
                '''
                Evaluating the goal of that specific expression.
                This is the number, which specifies the middle n values, that are taken from the sorted results array.
                This is a little complicated, but I will give you an easy example.
                
                eg. '5d6ml2' gives you the values [5,2,1,3,4].
                Then the sorted array is [1,2,3,4,5].
                According to the expression you take the two middle values out of that array, with a tendency to the lower values (, ie. to the left)
                and end up with the array [2,3]
                
                eg. '5d6ml3' gives you the values [5,2,1,3,4].
                Then the sorted array is [1,2,3,4,5].
                According to the expression you take the three middle values out of that array, with a tendency to the lower values (, ie. to the left)
                and end up with the array [2,3,4]
                
                The latter example is how an optimal middle function should work, but depending on the specified value for the goal, this optimal funtion
                isn't defined for all values of goal.
                Think about it.
                What should the two middle elements of a five element array be?
                To compensate for this shortcomming I have created the middle left and middle right functions, that are defined for (almost) all combinations
                of array lenght and goal size(, that make any sense).
                
                '''
                            
                while expr[index]!= ' ':
                  if isDigit(expr[index]):
                       numStr+=expr[index]
                  index+=1
                  
                goal=int(numStr)
                
                #print goal
                                
                wsp(2)
                
                '''
                Throwing the random dice and saving the results of the dice or the sums of the results and modifiers in the results array
                Also printing these results
                
                '''
                
                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print x, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                            else:
                                print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                            x+=1
                        diceSum+= tmp
                    wsp(1)
                
                results = sorted(results)
            
                wsp(2)
                
                #Some test results
                #results=[1,2,3,4,5,6,7,8,9,10]
                
                
                print 'Thrown dice: ', results
                wsp(1)
                
                '''
                Deciding, which elements of the results array should be chosen and printed
                And printing them
                '''
                
                if goal>=len(results):
                    print 'Results: ', results
                else:
                    if len(results)%2==0:
                        if goal%2==0:
                            #print 'both even'                        
                            finals = results[ ((len(results)/2)-(goal/2)) : ((len(results)/2)+(goal/2)) ]
                            print 'Results:', finals
                        
                        else:
                            #print 'diceNum even, goal odd'
                            finals = results[ (((len(results)/2)-1)-((goal/2))) : ((len(results)/2)+((goal/2))) ]
                            print 'Results:', finals
                    else:
                        if goal%2==0:
                            #print 'diceNum odd, goal even'
                            finals = results[ (((len(results)/2))-((goal/2))) : ((len(results)/2)+((goal/2))) ]
                            print 'Results:', finals
                        else:
                            #print 'both odd'
                            finals = results[ ((len(results)/2)-(goal/2)) : (((len(results)/2)+1)+(goal/2)) ]
                            print 'Results:', finals
                wsp(1)
#-------------        
            elif expr[index+1]=='r':
                #print 'middle right'
                
                numStr=''   #temporary variable, which is used for the transformation of integers in a String (eg. '123') into real integers (eg. 123)
                goal=0      #Number of elements, which are taken from the (left) middle of the results array
                results=[]  #Results of the dice thrown
                finals=[]   #Final result of the chosen array elements
                
                index+=2
                                
                '''
                Evaluating the goal of that specific expression.
                This is the number, which specifies the middle n values, that are taken from the sorted results array.
                This is a little complicated, but I will give you an easy example.
                
                eg. '5d6mr2' gives you the values [5,2,1,3,4].
                Then the sorted array is [1,2,3,4,5].
                According to the expression you take the two middle values out of that array, with a tendency to the higher values (, ie. to the right)
                and end up with the array [3,4]
                
                eg. '5d6mr3' gives you the values [5,2,1,3,4].
                Then the sorted array is [1,2,3,4,5].
                According to the expression you take the three middle values out of that array, with a tendency to the higher values (, ie. to the right)
                and end up with the array [2,3,4]
                
                The latter example is how an optimal middle function should work, but depending on the specified value for the goal, this optimal funtion
                isn't defined for all values of goal.
                Think about it.
                What should the two middle elements of a five element array be?
                To compensate for this shortcomming I have created the middle left and middle right functions, that are defined for (almost) all combinations
                of array lenght and goal size(, that make any sense).
                
                '''
                
                while expr[index]!= ' ':
                  if isDigit(expr[index]):
                       numStr+=expr[index]
                  index+=1
                
                  
                goal=int(numStr)
                
                #print goal
                                
                wsp(2)
                
                '''
                Throwing the random dice and saving the results of the dice or the sums of the results and modifiers in the results array
                Also printing these results
                
                '''
                
                x=1
                for i in range(0,len(diceType)):
                    for j in range(0,diceNum[i]):
                        tmp = random.randint(1,diceType[i])
                        if dice_mod=='sum':
                            print x, '. die(d',diceType[i],'):', tmp
                            results.append(tmp)
                            x+=1
                        else:
                            if (x-1) < len(modifier):
                                print x, '. die(d',diceType[i],'):', tmp , " + " , modifier[(x-1)] , ' = ' , (tmp+modifier[(x-1)])
                                results.append(tmp+modifier[(x-1)])
                            else:
                                print x, '. die(d',diceType[i],'):', tmp , " + " , 0 , ' = ' , tmp
                                results.append(tmp)
                            x+=1
                        diceSum+= tmp
                    wsp(1)
                
                
                results = sorted(results)
                                
                wsp(2)
                
                #Some test results
                #results=[1,2,3,4,5,6,7,8,9,10]
                
                
                print 'Thrown dice: ', results
                wsp(1)
                
                '''
                Deciding, which elements of the results array should be chosen and printed
                And printing them
                '''
                
                if goal>=len(results):
                    print 'Results: ', results
                else:
                    if len(results)%2==0:
                        if goal%2==0:
                            #print 'both even'                        
                            finals = results[ ((len(results)/2)-(goal/2)) : ((len(results)/2)+(goal/2)) ]
                            print 'Results:', finals
                        
                        else:
                            #print 'diceNum even, goal odd'
                            finals = results[ (((len(results)/2))-((goal/2))) : (((len(results)/2)+1)+((goal/2))) ]
                            print 'Results:', finals
                    else:
                        if goal%2==0:
                            #print 'diceNum odd, goal even'
                            finals = results[ (((len(results)/2)+1)-((goal/2))) : (((len(results)/2)+1)+((goal/2))) ]
                            print 'Results:', finals
                        else:
                            #print 'both odd'
                            finals = results[ (((len(results)/2))-(goal/2)) : (((len(results)/2)+1)+(goal/2)) ]
                            print 'Results:', finals 
                wsp(1)
                
        
        wsp(1)
        
#******range_mode************range_mode************range_mode************range_mode************range_mode************range_mode************range_mode******        
#******range_mode************range_mode************range_mode************range_mode************range_mode************range_mode************range_mode******        
#******range_mode************range_mode************range_mode************range_mode************range_mode************range_mode************range_mode******        



        
    elif mode == 'range_mode':
        #print 'range_mode'

#bookmark


        
        expr+='  '
        
        modifier=[] #array, which contains the modifiers
        goal=0      
        found = 0
        numStr=''   #temporary variable, which is used for the transformation of integers in a String (eg. '123') into real integers (eg. 123)
        
        minVal=0    #Minimal value of the thrown special die
        maxVal=0    #Maximal value of the thrown special die
        modSum=0    #Sum of all modifiers
        
        
        '''
        Evaluating the minVal
        '''
        
        while found==0:
            if expr[index]=='-' or expr[index]==':':
                found = 1
            if isDigit(expr[index]):
                numStr+=expr[index]
            index+=1
        
        #print numStr
        
        minVal = int(numStr)
        

        '''
        Evaluating the maxVal
        '''        
        
        numStr=''
        found=0
        
        while found==0:
            if expr[index]=='+' or expr[index]=='-' or expr[index]==' ':
                found = 1
            if isDigit(expr[index]):
                numStr+=expr[index]
            index+=1
        
        #print numStr
        
        maxVal = int(numStr)


        #correcting the index by -1, because in the evaluation process the index runs one digit to far
        index-=1
        
        
        numStr=''
        found = 0
        end = 0
        term = 0
        
        '''
        Evaluating modifiers
        
        '''
                
        while end == 0:
            term=0
            if expr[index]==' ':
                end=1
                
            if expr[index]=='+':
                index+=1
                while term == 0:
                    if  expr[index]==' ':
                        term = 1
                        end = 1
                    if expr[index]=='+' or expr[index]=='-':
                        term = 1
                        index-=1
                        break
                    if isDigit(expr[index]):
                        numStr+=expr[index]
                    index+=1
                #print numStr
                modifier.append(int(numStr))
                numStr=''
            
            if expr[index]=='-':
                index+=1
                while term == 0:
                    if expr[index]==' ':
                        term = 1
                        end = 1
                    if expr[index]=='+' or expr[index]=='-':
                        term = 1
                        index-=1
                        break
                    if isDigit(expr[index]):
                        numStr+=expr[index]
                    index+=1
                #print (int(numStr)*-1)
                modifier.append(int(numStr)*-1)
                numStr=''
            
            index+=1
        
        
        #correcting the index by -2, because in the evaluation of the modifiers, the index runs two digits to far    
        index-=2
        
        #print modifier
        
        '''
        Throwing the special random die
        
        '''
        
        tmp = random.randint(minVal,maxVal)
        
        
        wsp(2)
        
        print 'Die: ' , tmp
        
        wsp(2)
        
        '''
        Calculating the sum of modifiers and printing it, if it is greater than zero
        
        '''
        
        for i in range(0,len(modifier)):
            modSum+=modifier[i]
            print i , '. modifier =' , modifier[i] 
        
        
        if modSum>0:
            wsp(2)
            print 'Sum of modifiers = ' , modSum
            wsp(2)
        
        
        #printing the result, ie. the value of the thrown die and the sum of modifiers
        print 'Result = ' , (tmp+modSum)
        
        wsp(2)
        

#******main************main************main************main************main************main************main************main************main************main******
#******main************main************main************main************main************main************main************main************main************main******
#******main************main************main************main************main************main************main************main************main************main******
#******main************main************main************main************main************main************main************main************main************main******
#******main************main************main************main************main************main************main************main************main************main******


def main():
    
    
    
    '''
    Running through the list of arguments given by sys.argv and appending them to the args array
    Keep in mind, that the String 'python dice.py' is the first argument at position zero in the array
    '''
    
    for expr in sys.argv:
        args.append(expr)
    
    '''
    Evaluating each given argument with the evaluate function specified at the top of this file
    Keep in mind, that the first argument at position zero in the array is not evaluated, because it
    is the program call (ie. 'python dice.py')
    
    '''
    
    for i in range(1,len(args)):
        evaluate(args[i])
    
    '''
    Returning zero, which means, that the program endet without any errors
    '''
    return 0;


'''
Calling the main function, ie. running the program
'''

main()




#******license************license************license************license************license************license************license************license************license
#******license************license************license************license************license************license************license************license************license
#******license************license************license************license************license************license************license************license************license
#******license************license************license************license************license************license************license************license************license
#******license************license************license************license************license************license************license************license************license
#******license************license************license************license************license************license************license************license************license
#******license************license************license************license************license************license************license************license************license
#******license************license************license************license************license************license************license************license************license
#******license************license************license************license************license************license************license************license************license
#******license************license************license************license************license************license************license************license************license



''' 

                    GNU GENERAL PUBLIC LICENSE

Version 2, June 1991

Copyright (C) 1989, 1991 Free Software Foundation, Inc.  
51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

Preamble

The licenses for most software are designed to take away your freedom to share and change it. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change free software--to make sure the software is free for all its users. This General Public License applies to most of the Free Software Foundation's software and to any other program whose authors commit to using it. (Some other Free Software Foundation software is covered by the GNU Lesser General Public License instead.) You can apply it to your programs, too.

When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for this service if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs; and that you know you can do these things.

To protect your rights, we need to make restrictions that forbid anyone to deny you these rights or to ask you to surrender the rights. These restrictions translate to certain responsibilities for you if you distribute copies of the software, or if you modify it.

For example, if you distribute copies of such a program, whether gratis or for a fee, you must give the recipients all the rights that you have. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.

We protect your rights with two steps: (1) copyright the software, and (2) offer you this license which gives you legal permission to copy, distribute and/or modify the software.

Also, for each author's protection and ours, we want to make certain that everyone understands that there is no warranty for this free software. If the software is modified by someone else and passed on, we want its recipients to know that what they have is not the original, so that any problems introduced by others will not reflect on the original authors' reputations.

Finally, any free program is threatened constantly by software patents. We wish to avoid the danger that redistributors of a free program will individually obtain patent licenses, in effect making the program proprietary. To prevent this, we have made it clear that any patent must be licensed for everyone's free use or not licensed at all.

The precise terms and conditions for copying, distribution and modification follow.
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. This License applies to any program or other work which contains a notice placed by the copyright holder saying it may be distributed under the terms of this General Public License. The "Program", below, refers to any such program or work, and a "work based on the Program" means either the Program or any derivative work under copyright law: that is to say, a work containing the Program or a portion of it, either verbatim or with modifications and/or translated into another language. (Hereinafter, translation is included without limitation in the term "modification".) Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not covered by this License; they are outside its scope. The act of running the Program is not restricted, and the output from the Program is covered only if its contents constitute a work based on the Program (independent of having been made by running the Program). Whether that is true depends on what the Program does.

1. You may copy and distribute verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice and disclaimer of warranty; keep intact all the notices that refer to this License and to the absence of any warranty; and give any other recipients of the Program a copy of this License along with the Program.

You may charge a fee for the physical act of transferring a copy, and you may at your option offer warranty protection in exchange for a fee.

2. You may modify your copy or copies of the Program or any portion of it, thus forming a work based on the Program, and copy and distribute such modifications or work under the terms of Section 1 above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices stating that you changed the files and the date of any change. 
    b) You must cause any work that you distribute or publish, that in whole or in part contains or is derived from the Program or any part thereof, to be licensed as a whole at no charge to all third parties under the terms of this License. 
    c) If the modified program normally reads commands interactively when run, you must cause it, when started running for such interactive use in the most ordinary way, to print or display an announcement including an appropriate copyright notice and a notice that there is no warranty (or else, saying that you provide a warranty) and that users may redistribute the program under these conditions, and telling the user how to view a copy of this License. (Exception: if the Program itself is interactive but does not normally print such an announcement, your work based on the Program is not required to print an announcement.) 

These requirements apply to the modified work as a whole. If identifiable sections of that work are not derived from the Program, and can be reasonably considered independent and separate works in themselves, then this License, and its terms, do not apply to those sections when you distribute them as separate works. But when you distribute the same sections as part of a whole which is a work based on the Program, the distribution of the whole must be on the terms of this License, whose permissions for other licensees extend to the entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest your rights to work written entirely by you; rather, the intent is to exercise the right to control the distribution of derivative or collective works based on the Program.

In addition, mere aggregation of another work not based on the Program with the Program (or with a work based on the Program) on a volume of a storage or distribution medium does not bring the other work under the scope of this License.

3. You may copy and distribute the Program (or a work based on it, under Section 2) in object code or executable form under the terms of Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable source code, which must be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or, 
    b) Accompany it with a written offer, valid for at least three years, to give any third party, for a charge no more than your cost of physically performing source distribution, a complete machine-readable copy of the corresponding source code, to be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or, 
    c) Accompany it with the information you received as to the offer to distribute corresponding source code. (This alternative is allowed only for noncommercial distribution and only if you received the program in object code or executable form with such an offer, in accord with Subsection b above.) 

The source code for a work means the preferred form of the work for making modifications to it. For an executable work, complete source code means all the source code for all modules it contains, plus any associated interface definition files, plus the scripts used to control compilation and installation of the executable. However, as a special exception, the source code distributed need not include anything that is normally distributed (in either source or binary form) with the major components (compiler, kernel, and so on) of the operating system on which the executable runs, unless that component itself accompanies the executable.

If distribution of executable or object code is made by offering access to copy from a designated place, then offering equivalent access to copy the source code from the same place counts as distribution of the source code, even though third parties are not compelled to copy the source along with the object code.

4. You may not copy, modify, sublicense, or distribute the Program except as expressly provided under this License. Any attempt otherwise to copy, modify, sublicense or distribute the Program is void, and will automatically terminate your rights under this License. However, parties who have received copies, or rights, from you under this License will not have their licenses terminated so long as such parties remain in full compliance.

5. You are not required to accept this License, since you have not signed it. However, nothing else grants you permission to modify or distribute the Program or its derivative works. These actions are prohibited by law if you do not accept this License. Therefore, by modifying or distributing the Program (or any work based on the Program), you indicate your acceptance of this License to do so, and all its terms and conditions for copying, distributing or modifying the Program or works based on it.

6. Each time you redistribute the Program (or any work based on the Program), the recipient automatically receives a license from the original licensor to copy, distribute or modify the Program subject to these terms and conditions. You may not impose any further restrictions on the recipients' exercise of the rights granted herein. You are not responsible for enforcing compliance by third parties to this License.

7. If, as a consequence of a court judgment or allegation of patent infringement or for any other reason (not limited to patent issues), conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot distribute so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not distribute the Program at all. For example, if a patent license would not permit royalty-free redistribution of the Program by all those who receive copies directly or indirectly through you, then the only way you could satisfy both it and this License would be to refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under any particular circumstance, the balance of the section is intended to apply and the section as a whole is intended to apply in other circumstances.

It is not the purpose of this section to induce you to infringe any patents or other property right claims or to contest validity of any such claims; this section has the sole purpose of protecting the integrity of the free software distribution system, which is implemented by public license practices. Many people have made generous contributions to the wide range of software distributed through that system in reliance on consistent application of that system; it is up to the author/donor to decide if he or she is willing to distribute software through any other system and a licensee cannot impose that choice.

This section is intended to make thoroughly clear what is believed to be a consequence of the rest of this License.

8. If the distribution and/or use of the Program is restricted in certain countries either by patents or by copyrighted interfaces, the original copyright holder who places the Program under this License may add an explicit geographical distribution limitation excluding those countries, so that distribution is permitted only in or among countries not thus excluded. In such case, this License incorporates the limitation as if written in the body of this License.

9. The Free Software Foundation may publish revised and/or new versions of the General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.

Each version is given a distinguishing version number. If the Program specifies a version number of this License which applies to it and "any later version", you have the option of following the terms and conditions either of that version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of this License, you may choose any version ever published by the Free Software Foundation.

10. If you wish to incorporate parts of the Program into other free programs whose distribution conditions are different, write to the author to ask for permission. For software which is copyrighted by the Free Software Foundation, write to the Free Software Foundation; we sometimes make exceptions for this. Our decision will be guided by the two goals of preserving the free status of all derivatives of our free software and of promoting the sharing and reuse of software generally.

NO WARRANTY

11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. 


'''
