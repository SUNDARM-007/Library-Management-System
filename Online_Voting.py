import pyttsx3
print("'WELCOME TO POLL YOUR VOTE IN THE ELECTIVE COURSE' \n")
COURSE1="C"
COURSE2="PYTHON"
COURSE3="JAVA"
COURSE4="HTML"
COURSE5="SQL"
pyttsx3.speak('WELCOME TO POLL YOUR VOTE IN THE ELECTIVE COURSE')
#VOTERS_ID=[100,101,102,103,104,105,106,107,108,109,110]
VOTERS_ID=[100,101,102,103,104]
NO_OF_VOTERS=len(VOTERS_ID)
print("TOTAL NUMBER OF VOTERS: ",NO_OF_VOTERS)
VOTED_LIST=[]

try:
    def Vote():
        C1=0
        C2=0
        C3=0
        C4=0
        C5=0
        while True:
           if(VOTERS_ID==[] or len(VOTED_LIST)>(NO_OF_VOTERS/2)):
               for i in range(114):
                   print("*",end='')
               J='POLLING IS OVER'
               print('\n''\n',J.center(113,'.'),'\n')
               pyttsx3.speak("RESULTS OF THE ELECTION")
               if((C1>C2)and(C1>C3)and(C1>C4)and(C1>C5)):
                   print(f"'{COURSE1}' WON THE ELECTION WITH '{C1}' VOTES \n")
                   pyttsx3.speak(f"'{COURSE1}' WON THE ELECTION WITH '{C1}' VOTES")
                   print(f"PERCENTAGE OF {COURSE1}:",round((C1/NO_OF_VOTERS*100),2),"%",'\n')
               elif((C2>C1)and(C2>C3)and(C2>C4)and(C2>C5)):
                   print(f"'{COURSE2}' WON THE ELECTION WITH '{C2}' VOTES \n")
                   pyttsx3.speak(f"'{COURSE2}' WON THE ELECTION WITH '{C2}' VOTES")
                   print(f"PERCENTAGE OF {COURSE2}:",round((C2/NO_OF_VOTERS*100),2),"%",'\n')
               elif((C3>C1)and(C3>C2)and(C3>C4)and(C3>C5)):
                   print(f"'{COURSE3}' WON THE ELECTION WITH '{C3}' VOTES \n")
                   pyttsx3.speak(f"'{COURSE3}' WON THE ELECTION WITH '{C3}' VOTES")
                   print(f"PERCENTAGE OF {COURSE3}:",round((C3/NO_OF_VOTERS*100),2),"%",'\n')
               elif((C4>C1)and(C4>C2)and(C4>C3)and(C4>C5)):
                   print(f"'{COURSE4}' WON THE ELECTION WITH '{C4}' VOTES \n")
                   pyttsx3.speak(f"'{COURSE4}' WON THE ELECTION WITH '{C4}' VOTES")
                   print(f"PERCENTAGE OF {COURSE4}:",round((C4/NO_OF_VOTERS*100),2),"%",'\n')
               elif((C5>C1)and(C5>C2)and(C5>C3)and(C5>C4)):
                   print(f"'{COURSE5}' WON THE ELECTION WITH '{C5}' VOTES \n")
                   pyttsx3.speak(f"'{COURSE5}' WON THE ELECTION WITH '{C5}' VOTES")
                   print(f"PERCENTAGE OF {COURSE5}:",round((C5/NO_OF_VOTERS*100),2),"%",'\n')
               elif((C1==C2)or(C1==C3)or(C1==C4)or(C1==C5)or(C2==C3)or(C2==C4)or(C2==C5)or(C3==C4)or(C3==C5)or(C4==C5)):
                   print("AS THERE IS A TIE BETWEEN THE VOTES OF COURSES, THERE IS A NEED OF CONDUCTING RE ELECTION \n")
                   pyttsx3.speak("AS THERE IS A TIE BETWEEN THE VOTES OF COURSES, THERE IS A NEED OF CONDUCTING RE ELECTION")
               print(f"TOTAL VOTES OF '{COURSE1}': {C1} ({round(C1/NO_OF_VOTERS*100,2)} %)\nTOTAL VOTES OF '{COURSE2}': {C2} ({round(C2/NO_OF_VOTERS*100,2)} %)\nTOTAL VOTES OF '{COURSE3}': {C3} ({round(C3/NO_OF_VOTERS*100,2)} %)\nTOTAL VOTES OF '{COURSE4}': {C4} ({round(C4/NO_OF_VOTERS*100,2)} %)\nTOTAL VOTES OF '{COURSE5}': {C5} ({round(C5/NO_OF_VOTERS*100,2)} %)")
               pyttsx3.speak(f"PERCENTAGE OF {COURSE1} is {round(C1/NO_OF_VOTERS*100,2)}")
               pyttsx3.speak(f"PERCENTAGE OF {COURSE2} is {round(C2/NO_OF_VOTERS*100,2)}")
               pyttsx3.speak(f"PERCENTAGE OF {COURSE3} is {round(C3/NO_OF_VOTERS*100,2)}")
               pyttsx3.speak(f"PERCENTAGE OF {COURSE4} is {round(C4/NO_OF_VOTERS*100,2)}")
               pyttsx3.speak(f"PERCENTAGE OF {COURSE5} is {round(C5/NO_OF_VOTERS*100,2)}")
               break
           else:
               VOTER=int(input("ENTER YOUR VOTER ID: "))
               if VOTER in VOTED_LIST:
                   print("YOU HAVE ALREADY VOTED \n")
               elif VOTER in VOTERS_ID:
                   print("NOTE: PLEASE ENTER THE ALLOTTED CHOICE FOR THE COURSES")
                   print(f"1. {COURSE1}\n2. {COURSE2}\n3. {COURSE3}\n4. {COURSE4}\n5. {COURSE5}")
                   CHOICE=int(input("ENTER YOUR CHOICE: "))
                   if(CHOICE==1):
                       C1+=1
                       print(f"YOU HAVE VOTED FOR '{COURSE1}' \n")
                       pyttsx3.speak('THANK YOU FOR VOTING')
                       VOTERS_ID.remove(VOTER)
                       VOTED_LIST.append(VOTER)
                   elif(CHOICE==2):
                       C2+=1
                       print(f"YOU HAVE VOTED FOR '{COURSE2}' \n")
                       pyttsx3.speak('THANK YOU FOR VOTING')
                       VOTERS_ID.remove(VOTER)
                       VOTED_LIST.append(VOTER)
                   elif(CHOICE==3):
                       C3+=1
                       print(f"YOU HAVE VOTED FOR '{COURSE3}' \n")
                       pyttsx3.speak('THANK YOU FOR VOTING')
                       VOTERS_ID.remove(VOTER)
                       VOTED_LIST.append(VOTER)
                   elif(CHOICE==4):
                       C4+=1
                       print(f"YOU HAVE VOTED FOR '{COURSE4}' \n")
                       pyttsx3.speak('THANK YOU FOR VOTING')
                       VOTERS_ID.remove(VOTER)
                       VOTED_LIST.append(VOTER)
                   elif(CHOICE==5):
                       C5+=1
                       print(f"YOU HAVE VOTED FOR '{COURSE5}' \n")
                       pyttsx3.speak('THANK YOU FOR VOTING')
                       VOTERS_ID.remove(VOTER)
                       VOTED_LIST.append(VOTER)
                   else:
                       print("PLEASE ENTER A VALID CHOICE \n")
               else:
                   print("YOU ARE NOT ALLOWED TO VOTE IN THIS POLL BOOTH \n")
        pyttsx3.speak("THE ELECTIVE COURSE WENT ON SUCCESSFULLY")
except:
    Vote()
Vote()
