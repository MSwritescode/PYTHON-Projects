''' This mini project is a Python Application which presents the working of a MEDICAL STORE MANAGMENT SYSTEM.
This project is developed by Mohit Sharma under the guidance of Dr. Arvind Sharma Sir, HoD-CS, DAV, Kota'''

# Source Code:

# Medical Store Python Project

a=["paracitamol","surfaz-sn","ondem-md-4","pantaford-dsr","tribs","avomine"]
b=[20,72.57,46.58,89,42,20]
c=[100,25,50,100,60,100]
d={"MEDICINE NAME":a,"PRICE":b,"QUANTITY":c}

# printing the welcome note to the user

print("""
                    .......................................................................................
                    ///////////////////////////////////////////////////////////////////////////////////////
                  ....................WELCOME TO MEDICAL STORE MANAGMENT SYSTEM..........................
           ///////////////////////MADE BY: Mohit Sharma  CLASS: XII-D  ///////////////////////////////////// 
 <<<<<<<<<<<<<<<<<<<<<< D.A.V. PUBLIC SCHOOL, KOTA >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                   .......................................................................................

""")
# the main loop starts
while(True):

    print("""
             1=>ADD MEDICINE
             2=>SELL MEDICINE
             3=>DETAILS OF OLD STOCK
             4=>DELETE MEDICINE (NOTE: You can delete those medicines that are expired or damaged)
             5=>EDIT MEDICINE DETAILS
             6=>EXIT
     
    """)
    print( )
    e=int(input("ENTER YOUR CHOICE:"))
    # if the user wants to add new medicines
    if e==1:
        # prompting the details of new medicines from the users
        print("\n  !!!!BEFORE ADDING THE MEDICINE TO THE STOCK PLEASE CHECK THE EXPIRY DATE OF IT!!!!")
        print( )
        
        f=str(input("ENTER THE MEDICINE NAME:"))
        # if entered medicine is already in the stock
        if f in a:
            print("\n                               !!!!!MEDICINE ALREADY IN THE STOCK!!!!!!")
            z=a.index(f)
            i=str(input("\nDO YOU WANT TO UPDATE THE PRICE AND THE QUANTITY ? ( Y / N ):"))
            if i =="y":
                g=int(input("\nENTER THE PRICE:"))
                h=int(input("ENTER THE QUANTITY:"))
                b[z]=g
                c[z]+=h
                # asking the user tp print the details of the updated details of the medicine
                y=str(input("\nDO YOU WANT TO SEE THE DETAILS OF THE UPDATED DETAILS ? ( Y / N ):"))
                print("MEDICINE NAME\tPRICE\tQUANTITY")
                print(".............\t.....\t........")
               
                if y == "y":
                    print( )
                    print(a[z],end="\t")
                    print(b[z],end=
                          "\t")
                    print(c[z], end=" ") 
                else:
                    print("  \n!!!!!NOT PRINTING THE DETAILS!!!!!")
            else:
                continue
        # if the entered medicine is not in the stock
        else:
            g=int(input("\nENTER THE PRICE:"))
            h=int(input("ENTER THE QUANTITY:"))
            # adding the details in the old stock list
            a.append(f)
            b.append(g)
            c.append(h)
            # asking user to print the detailss of the stock
            g=str(input("\nDO YOU WANT TO SEE THE DETAILS OF THE MEDICINES?( Y / N ):"))
            # if user wants the details than print the details
            if g== "y":
                print( )
                print("medicine name:",a[len(a)-1])
                print("price:",b[len(b)-1])
                print("quantity:",c[len(c)-1])
           
            # if user doesn't want the details of the stock 
            else:
                print("!!!!!\nNOT PRINTING THE DETAILS!!!!!")
        # asking the user to run the program again or not
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break
    # if user wants to sell the medicines
    elif e==2:
        print( )
        # prompting the medicine name by the user
        i=str(input("ENTER THE MEDICINE NAME:"))
        # if the medicine is in the stock
        if i in a:
            print( )
            # asking the quantity the user wants to sell
            j=int(input("ENTER THE QUANTITY:"))
            # storing the index no. of medicine in the stock list in a varible k
            k=a.index(i)
            #i f the required quantity is available
            if (j <=c[k]):
                c[k]-=j

                print("\nMEDICINE IS IN STOCK")
                # printing the receipt
                print("\n                           !!!!BEFORE SELLING THE MEDICINE PLEASE CHECK THE EXPIRY DATE OF THE MEDICINE!!!!")
                print( )
                z=str(input("DO YOU WANT TO PRINT THE RECEIPT?( Y / N ):"))
                if z=="y":
                    print( )
                    print("""
                                    RECEIPT
                                  ...........
                              
                            MEDICINE NAME:""",i)# medicine name

                    print("                            TOTAL PRICE   :",j*b[k])# total price
                else:# if user don't wants to print the reciept
                    continue

                # asking user to print the details of medicine he had sold
                z=str(input("\nDO YOU WANT TO SEE THE DETAILS OF THE SOLD MEDICINE IN THE STOCK? ( Y / N ):"))
                # if user wants the details the print the details
                if z=="y":
                    print("\nMEDICINE NAME:",a[k])
                    print("PRICE:",b[k])
                    print("QUANTITY LEFT:",c[k])
                # if user doesn't wants the details 
                else:
                    print("\n                                          NOT PRINTING THE DETAILS")
                
            # if the required quantity is not available in the stock
            else:

                print("\n                                         THIS NO. OF MEDICINES NOT AVAILABLE")
                
        # if the required medicine is not available
        else:

            print("\n                                                   MEDICINE NOT AVAILABLE")
            print("\n                                    !!!!PLEASE ADD THE MEDICINE TO THE STOCK FIRST!!!!")
        # asking the user to run the program again or not?
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break
    # if user wants to see the details of the stock
    elif e==3:
        print( )
        print("MEDICINE NAME\tPRICE\tQUANTITY")
        print(".............\t.....\t........")
        print( )
        for k in range(len(a)):
            print(a[k],end="\t")
            print(b[k],end="\t")
            print(c[k])
          
        # asking the user to run the program again or not?
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break
    # if user wants to delete no. of medicines from the stock
    elif e==4:
        print( )
        f=str(input("ENTER MEDICINE NAME:"))
        # if entered medicine is found in the stock
        if f in a:
            i=a.index(f)
            print( )
            g=int(input("ENTER THE QUANTITY YOU WANT TO MINUS:"))
            if g <=c[i]:
                c[i]-=g
                print("\n                                  EDITED SUCCESFULLY")
                print( )    
                print("\nMEDICINE NAME:",a[i])
                print("QUANTITY LEFT:",c[i])
            else:
                print("\n                  !!!!!THIS NO. OF MEDICINE IS NOT AVAILABLE IN THE STOCK!!!!!")
                
        # if entered medicine is not found in the stock
        else:
            print( )
            print("                                     !!!!!ENTERED MEDICINE IS NOT IN THE STOCK!!!!!")
        # asking the user to run the program again or not?
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break

    # if user wants to edit the stock details
    elif e==5:
        print( )
        g=str(input("MEDICINE NAME:"))
        # if entered medicine is found in tha stock
        if g in a:
            i=a.index(g)
            # asking for the editing choices
            print("""\nYOU WANT TO EDIT
                    1==PRICE
                    2==QUANTITY
                    """)
            print( )
            f=int(input("ENTER YOUR CHOICE:"))
            # if user wants to edit the price
            if(f==1):
                h=int(input("\nENTER THE NEW PRICE:"))
                b[i]=h
                print( )
                print("                                     UPDATED SUCCESFULLY")
                z=str(input("DO YOU WANT TO SEE THE DETAILS OF EDITED MEDICINE ? ( Y / N ):"))
                if z=="y":
                    print("\nMEDICINE NAME:",a[i])
                    print("NEW PRICE:",b[i])
                else:
                    print("                             \n !!!!! NOT PRINTING THE DETAILS !!!!!")
            # if user wants to edit the quantity
            elif f==2:
                print( )
                # asking th user that he wants to increase or decrease the no. of stock
                print("""
                            1=INCREASE QUANTITY
                            2=DECREASE QUANTITY
                            """)
                p=int(input("ENTER YOUR CHOICE:"))
                # if the user  wants to increase the no. of medicines in the stock
                if p==1:
                    print( )
                    h=int(input("ENTER THE INCREMENT IN THE QUANTITY:"))
                    c[i]+=h
                    print( )
                    print("                                             UPDATED SUCCESFULLY")
                # if the user wants to decrease the the no. of medicines in the stock
                else:
                    i=a.index(g)
                    print( )
                    h=int(input("ENTER THE DECREMENT IN THE QUANTITY:"))
                    if h<=c[i]:# checking that the entered quantity is available osr not
                        c[i]-=h
                        print( )
                        print("                                             UPDATED SUCCESFULLY")
                    else:
                        print("\n                     !!!!!THIS NO. OF MEDICINE IS NOT AVAILABLE IN THE STOCK!!!!!")
                z=str(input("DO YOU WANT TO SEE THE DETAILS OF THE EDITED MEDICINE ? ( Y / N ):"))
                if z=="y":
                    print("\nMEDICINE NAME:",a[i])
                    print("NEW QUANTITY:",c[i])
                else:
                    print("    !!!!! NOT PRINTING THE DETAILS!!!!!")
        # if entered medicine is not found n the stock    
        else:
            print( )
            print("       !!!!!MEDICINE NOT IN THE STOCK!!!!!")
        # asking the user to run the program again or not
        s=str(input("\nDO YOU WANT TO RUN THE PROGRAM AGAIN? ( Y / N ):"))
        if s =="y":
            continue
        else:
            break
    # if user wants to exit from the software
    elif e==6:
        # at the end printing the thank you note
        print( )
        print("""        ////////////////////<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>///////////////////
        ;;;;;;;;;;;;;;;;;;;;THANK YOU FOR USING THIS SOFTWARE :) ;;;;;;;;;;;;;;;;;;;
        ///////////////////<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>///////////////////
                """)
        # taking the user out of the whole loop    
        break
    print( )
