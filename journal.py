# enter in a journal entry

import sys
from datetime import datetime
from datetime import date
today = date.today()
#get date string for file timestamp
d4 = today.strftime("%d-%b-%Y")
print("d4 =", d4)
dofweek =datetime.today().strftime('%A')

#try except



    #menu conditional
jorref =input('todolist(t) or reflection(r): ')
if jorref == ('t' or 'r') :
   print(jorref)
elif  jorref != ('r' or 't'):
   print('invalid input')
   sys.exit(1)


    #reflection or journal entry
ref=[]

if jorref == "t":
   print ("todos")
   while True:
      x=input('what is todolist entry , enter "e" to end:    ')
      if x == "e":
         break
      ref.append(x)
   todofile = 'todolist_'+d4+'_'+dofweek+'.txt'
   with open(todofile, 'a+') as f:
      for item in ref:
         f.write("%s\n" % item)


else:
   print ("Reflections ")
   while True:
      x=input('what is Reflection entry , enter "e" to end:   ')
      if x == "e":
         break
      ref.append(x)


      jfile = 'journal_'+d4+'_'+dofweek+'.txt'
      with open(jfile, 'a+') as f:
         for item in ref:
            f.write("%s\n" % item)
