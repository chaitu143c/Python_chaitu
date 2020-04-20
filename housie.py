'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#!/usr/bin/python
import random
import copy

list = [];
input1 = 's';
begn = 1;
end = 90;
seq =[];
seq.extend(range(begn,end+1));
reset_seq =copy.deepcopy(seq);
print(seq);
print("Housie program");
print("Press 'n' to generate next number\nPress 'd' to display generated numbers till now\nPress 'r' to reset\nPress 'e' to exit");
while (True):
 input1 = input("Enter a command:");
 if input1 == 'n':
  if(len(seq) == 0):
   print("You reached end of the sequence please reset");      
   break;
  next = random.choice(seq);
  seq.remove(next);
  list.append(next);
  print(next);
 if input1 == 'd':
  print(list.sort());
 if input1 == 'r':
  list = [];
  seq = reset_seq;
  print(seq);
 if input1 == 'e':
  break;

    
