import os
import pyttsx3

pyttsx3.speak("Welcome to my program")
print("Welcome To My Program") 

print(
"""\nPress 1 for Numerical Menu
Press 2 for Word Menu
Press 3 for Exit""")

while True:
    c=int(input("Enter your choice : "))
    if c==1:
            print("""
Press 1 for Chrome
Press 2 for Notepad
Press 3 for Date
Press 4 for Gmail
Press 5 for Exit
                """)

            ch=int(input("Enter your choice: "))

            if ch==1:
                print("Opening Chrome")
                pyttsx3.speak("Opening Chrome")
                os.system("Chrome")

            elif ch==2:
                print("Opening Notepad")
                pyttsx3.speak("Opening Notepad")
                os.system("notepad")

            elif ch==3:
                print("Showing Date")
                pyttsx3.speak("showing date")
                os.system("date")

            elif ch==4:
                print("Opening GMAIL")
                pyttsx3.speak("Opening GMAIL")
                os.system("https://mail.google.com/mail")

            elif ch==5:
                print("Goodbye...")
                pyttsx3.speak("Goodbye buddy, See you soon")
                break

            else:
                print("invalid command")
                pyttsx3.speak("invalid command")
                break


    elif int (c)==2:
            p=input("Write your Commands : ")

            if (("chrome" in p) or ("google" in p) or ("brave" in p) or ("browser" in p)) and (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)):
                pyttsx3.speak("starting Chrome browser")
                os.system("chrome")

            elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("editor" in p) or ("text editor" in p) or ("notepad" in p)):
                pyttsx3.speak("starting notepad")
                os.system("notepad")

            elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("date" in p) or ("calender" in p)):
                pyttsx3.speak("showing date")
                os.system("date")

            elif (("compose" in p) or ("send" in p) or ("write" in p) or ("get" in p)) and (("gmail" in p) or ("email" in p) or ("mail" in p)):
                pyttsx3.speak("opening gmail")
                os.system("chrome   https://mail.google.com/mail")

            elif (("exit" in p) or ("quit" in p) or ("stop" in p)):
                print("goodbye buddy, see you soon...")
                pyttsx3.speak("goodbye buddy, see you soon")
                break

            else:
                pyttsx3.speak("invalid command please try again")
                print("Invalid Command")
                if input()=='':
                    break

    elif int (c)==3:
            print("goodbye buddy, see you soon")
            pyttsx3.speak("goodbye buddy, see you soon")
            break

    else:
            print("Invalid input", end=" ")
            pyttsx3.speak("Invalid input, please try again")
            continue
