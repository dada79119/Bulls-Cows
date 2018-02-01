import random
import re

# random 4 digits
answer = random.sample([0,1,2,3,4,5,6,7,8,9],4)
#print(answer[0],answer[1],answer[2],answer[3])

while True:
    input_v = input("Guess 4 number : ")
    if not input_v.isdigit():
        print("not number")
    elif len(input_v) != 4 : #check input text must be 4 digits number
        print(" Your Guess Number must be 4 numbers!")
    else:
        re=[]
        for i in range(0,len(input_v)):
            if answer[i] == int(input_v[i]) : 
               re.append("A")
            elif  int(input_v[i]) in answer and int(input_v[i]) != answer[i]:
               re.append("B")
    
        r1=r2=0
        for s in re:
            if s=='A':
                r1+=1
            elif s=='B':
                r2+=1
                
        prompt = str(r1)+"A"+str(r2)+"B"    
        print(prompt) #show prompt 
        if prompt == '4A0B':
            print('You Got it !!!')
            enter_key = input("Press Any Key to play again or Ctrl+C exit...")
            # continue this game give random 4 digits
            answer = random.sample([0,1,2,3,4,5,6,7,8,9],4)
