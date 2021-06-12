# %%

from os import error
soemthing = open('enigme3.txt','r')
line=[]
for linee in soemthing:
  strip_line=linee.strip()
  haja=strip_line.split()
  line.append(haja)  
  # %%
erreur=0
premier=["05","06","07"]
sang=["A+","A-","AB+","AB-","O+", "O-","B+","B-"]
NIN=["00","01","10","11"]

for i in range(len(line)):
    if(len(line[i])==7):
        date = line[i][3].split("/")
        d=int(date[0])
        m=int(date[1])
        y=int(date[2])
        mass= line[i][3].split("/")
        year=mass[2][1:4]
        erreur1=0 
        erreu=0
        err=0
        win=0
        try:
            int(line[i][0])  
            err+=1
        except:
            pass
        try:
            int(line[i][1])  
            erreu+=1
        except:
            pass
        try:
            int(line[i][2])  
            erreur1+=1
        except:
            pass
        if(erreur1!=0 or err!=0 or erreu!=0 ):
            win+=1
        
        if(len(line[i][4])!=10 or line[i][4][0:2] not in premier):#check phone number
            erreur+=1
            print("num")
        elif(line[i][6]not in sang):#check grp sanguin
           print("sang")
           erreur+=1
        elif(y<1988 or y>2001 or m<=0 or m>12 or d<=0 or d>31):#check date de naissance
            erreur+=1
            print("date")
        elif((line[i][5][0:2]) not in NIN or (line[i][5][2:5])!=year or len(line[i][5])!=18):#check NIN
            print((line[i][5][0:2]),(line[i][5][2:5]),len(line[i][5]))
            erreur+=1
            print("nin")
        elif(win!=0):#check prenom et nom
            erreur+=1
            print("name")
    if(len(line[i])==6):
         date = line[i][2].split("/")
         d=int(date[0])
         m=int(date[1])
         y=int(date[2])
         mass= line[i][2].split("/")
         year=mass[2][1:4]
         erreu=0
         err=0
         win1=0
         try:
             int(line[i][0])  
             err+=1
         except:
             pass
         try:
             int(line[i][1])  
             erreu+=1
         except:
             pass
         if( err!=0 or erreu!=0 ):
             win1+=1
        
         if(len(line[i][3])!=10 or line[i][3][0:2] not in premier):#check phone number
             erreur+=1
             print("num")
         elif(line[i][5]not in sang):#check grp sanguin
             erreur+=1
             print("grp")
         elif(y<1988 or y>2001 or m<=0 or m>12 or d<=0 or d>31):#check date de naissance
             erreur+=1
             print("date")
         elif((line[i][4][0:2]) not in NIN or (line[i][4][2:5])!=year or len(line[i][4])!=18):#check NIN
             erreur+=1
             print("nin")
         elif(win1!=0):#check prenom et nom
             erreur+=1
             print("name")
print(erreur)

           
        
            



        




    
            



# %%
