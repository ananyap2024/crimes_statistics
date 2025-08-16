import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

HELP_TEXT="""
   This is a program showing records of 5
   diffrent crimes across the 20 different states of india
   in the years 2019,2020
   This program also shows crime rate stats year wise.
   Crime Rate is calculated as crime per one lakh (100,000) of population.
   
   1- Crime against children
      1A- Year wise data
      
   2- Crime against women
      2A- Year wise data
      
   3- Human trafficking
      3A- Year wise data
      
   4- Crimes committed by juveniles
      4A- Year wise data

   5- Crime rates across the years 2000-2020
   
   q/quit - Quit the program
   h/help - Print this help text
   """

print(HELP_TEXT)
  
while True:
    choice=input("Enter crime:")
    
    if choice in ("q", "quit"):
        print("Quitting...")
        
    
    elif choice in ("h", "help"):
        print(HELP_TEXT)

    elif choice=="1":
        print("Crime against children:\n")
        df1=pd.read_csv(r"C:\Users\91900\OneDrive\Desktop\ananya\programs\python\crimes\crime against children.csv")
        print(df1)
        print('\n')
        print('\n Years available for selection are 2019,2020\n ')
        
        year=input("Enter year:")
                
        if year=='2019':
                x=df1['2019']
                y=df1['State']
                explode = (0,0.1,0,0.4,0,0,0,0,0,0,0.1,0.4,0,0,0,0,0.4,0.1,0)
                plt.pie(x, labels=y, explode=explode,autopct='%1.1f%%', textprops={'fontsize': 8},
                        wedgeprops={'edgecolor':'black', 'linewidth':1})
                plt.axis('equal')
                plt.title('Crime against children in the year 2019')
                plt.legend(y,loc='best')
                plt.show()
                
                
        elif year=='2020':
                x=df1['2020']
                y=df1['State']
                explode = (0,0.1,0,0.4,0,0,0,0,0,0,0.1,0.4,0,0,0.5,0,0,0.1,0)
                plt.pie(x, labels=y, explode=explode, autopct='%1.1f%%',textprops={'fontsize': 8},
                        wedgeprops={'edgecolor':'black', 'linewidth':1})
                plt.axis('equal')
                plt.title('Crime against children in the year 2020')
                plt.legend(y,loc='best')
                plt.show()

            
        else:
                print('Given value does not represent any crime\n')
                print(HELP_TEXT)

    elif choice=='1A':
            print('Crime against children stats yearwise')
            df1=pd.read_csv(r"C:\Users\91900\OneDrive\Desktop\ananya\programs\python\crimes")
            print(df1)
            states=df1['State']
            y=df1['2019']
            z=df1['2020']
            n=19
            r = np.arange(n)
            width = 0.25
            plt.bar(r,y, color = 'b',
            width = width, label='2019')
            plt.bar(r + width,z, color = 'g',
            width = width, label='2020')
            
            plt.xlabel('States')
            plt.ylabel('No.of cases registered')
            plt.title('Crime against children in 2019,2020')
            plt.xticks(r,states)
            plt.xticks(rotation = 60)
            plt.legend(loc='upper left')
            plt.show()

            

    elif choice=='2':
        print('Crime against women:\n')
        df2=pd.read_csv(r"C:\Users\91900\OneDrive\Desktop\ananya\programs\python\crimes")
        print(df2)
        print('\n')
        print('\n Years available for selection are 2019,2020\n ')
        

        year=input("Enter year:")
            
        if year=='2019':
            x=df2['State']
            y=df2['2019']
            plt.bar(x,y, color="#77AC30", edgecolor="#7E2F8E")
            plt.xticks(rotation = 60)
            plt.ylabel('No.of cases filed')
            plt.xlabel('States')
            plt.title('Crime committed against women in the year 2019')
            plt.show()
            
        elif year=='2020':
            y=df2['2020']
            x=df2['State']
            plt.bar(x,y, color="#77AC30", edgecolor="#7E2F8E")
            plt.xticks(rotation = 60)
            plt.ylabel('No.of cases filed')
            plt.xlabel('States')
            plt.title('Crime committed against women in the year 2020')
            plt.show()

        else:
            print('Given value does not represent any crime\n')
            print(HELP_TEXT)



    elif choice=='2A':
        print('Crime against women stats yearwise')
        df2=pd.read_csv(r"C:\Users\91900\OneDrive\Desktop\ananya\programs\python\crimes")
        print(df2)
        States=df2['State']
        y=df2['2019']
        z=df2['2020']
        plt.plot(States,y, "c--", marker = 'o', label='2019')
        plt.plot(States,z, "#D95319", marker = '*', label='2020')
        plt.xticks(rotation = 60)
        plt.xlabel('States')
        plt.ylabel('No.of cases registered')
        plt.title('Crime against women in 2019,2020')
        plt.legend(loc='upper left')
        plt.show()
            
            

    elif choice=='3':
        print("Human Trafficking: \n")
        df3=pd.read_csv(r"C:\Users\91900\OneDrive\Desktop\ananya\programs\python\crimes")
        print(df3)
        print('\n')
        print('\n Years available for selection are 2019,2020\n ')
        
        year=input("Enter year:")
            
        if year=='2019':
            y=df3['2019']
            x=df3['State']
            plt.stem(x,y, "#A2142F")
            plt.xticks(rotation = 45) 
            plt.ylabel('No.of cases filed')
            plt.xlabel('States')
            plt.title('Human Trafficking cases in the year 2019')
            plt.show()

        elif year=='2025':
            print ('<we are>'
                   '/n' '<coming_back>'
                   '/n' '<SIRIUS-2025>')
        
            
        elif year=='2020':
            y=df3['2020']
            x=df3['State']
            plt.stem(x,y, "#A2142F")
            plt.xticks(rotation = 45) 
            plt.ylabel('No.of cases filed')
            plt.xlabel('States')
            plt.title('Human Trafficking cases in the year 2020')
            plt.show()

        else:
            print('Given value does not represent any crime\n')
            print(HELP_TEXT)


    elif choice=='3A':
        df3=pd.read_csv(r"C:\Users\91900\OneDrive\Desktop\ananya\programs\python\crimes")
        print(df3)
        States=df3['State']
        y=df3['2019']
        z=df3['2020']
        plt.plot(States,y, "c--", marker = 'o', label='2019')
        plt.plot(States,z, "#D95319", marker = '*', label='2020')
        plt.xticks(rotation = 60)
        plt.xlabel('States')
        plt.ylabel('No.of cases registered')
        plt.title('Human trafficking cases in 2019,2020')
        plt.legend(loc='best')
        plt.show()
        
            
    
    elif choice=='4':
        df4=pd.read_csv( r"C:\Users\91900\OneDrive\Desktop\ananya\programs\python\crimes\Crime Committed by Juveniles.csv")
        print(df4)
        print('\n')
        print('\n Years available for selection are 2019,2020\n ')
        

        year=input("Enter year:")
        
        if year=='2019':
            x=df4['State']
            y=df4['2019']
            plt.step(x,y ,'m', marker='p')
            plt.xticks(rotation = 45)
            plt.ylabel('No.of cases filed')
            plt.xlabel('States')
            plt.title('Murder cases in the year 2019')
            plt.show()

        elif year=='2020':
            x=df4['State']
            y=df4['2020']
            plt.step(x,y, 'm', marker='*')
            plt.xticks(rotation = 45)
            plt.ylabel('No.of cases filed')
            plt.xlabel('States')
            plt.title('Murder cases in the year 2020')
            plt.show()

        else:
            print('Given value does not represent any crime\n')
            print(HELP_TEXT)


    elif choice=='4A':
        df4=pd.read_csv(r"C:\Users\91900\OneDrive\Desktop\ananya\programs\python\crimes\Crime Committed by Juveniles.csv")
        print(df4)
        states=df4['State']
        y=df4['2019']
        z=df4['2020']
        n=19
        r = np.arange(n)
        width = 0.25
        plt.bar(r,y, color = 'b',
        width = width, label='2019')
        plt.bar(r + width,z , color = 'g',
        width = width, label='2020')
        plt.xlabel('States')
        plt.ylabel('No.of cases registered under Murders')
        plt.title('Murder cases registered in 2019,2020')
        plt.xticks(r,states)
        plt.xticks(rotation = 60)
        plt.legend(loc='best')
        plt.show()



    elif choice =='5':
        
        print('Total crime rate over the years 2001-2020')
        df5 = pd.read_csv(r"C:\Users\91900\OneDrive\Desktop\ananya\programs\python\crimes\crime rates over the years 2000-2020.csv")
        print(df5)
        x=df5['Year']
        y = df5['Crime Rate']
        plt.plot(x,y, 'r--', marker='*')
        plt.xlabel('Years')
        plt.ylabel('Crime Rate in %')
        plt.title('Total crime rate over the years 2001-2020')
        plt.xticks(x)
        plt.grid()
        plt.show()

    else:
       print(HELP_TEXT)###

       



    
         


       
         
    


            
    
                        
