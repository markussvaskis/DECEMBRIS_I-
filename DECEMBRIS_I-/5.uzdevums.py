import datetime
pašreizējais_laiks = datetime.datetime.now().hour
if 5 <= pašreizējais_laiks < 12:
 print("labrīt!")
elif 12 <= pašreizējais_laiks < 18:
 print("labdien!")
else:
 print("labvakar!") 
