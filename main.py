import os  # accessing the os functions

import Capture_Image
import check_frame
import Train_Image
import Recognize
import mail

# creating the title bar function

def title_bar():
    os.system('cls')  # for windows

    # title of the program

    print("\t*****************************")
    print("\t***** Attendance System *****")
    print("\t*****************************")


# creating the user main menu function

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "MENU", 10 * "*")
    print("[0] Check Frame")
    print("[1] Capture Faces")
    print("[2] Train Images")
    print("[3] Recognize & Attendance")
    print("[4] Auto Mail")
    print("[5] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))
            if choice == 0:
                testing()
                break
            elif choice == 1:
                CaptureFaces()
                break
            elif choice == 2:
                Trainimages()
                break
            elif choice == 3:
                RecognizeFaces()
                break
            elif choice == 4:
                mailing()
                break
                mainMenu()
            elif choice == 5:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-4")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-4\n Try Again")
    exit



def testing():
    check_frame.camer()
    key = input("Press Enter key to return main menu")
    mainMenu()


def mailing():
    mail.mail()
    key = input("Press Enter key to return main menu")
    mainMenu()


# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Press Enter key to return main menu")
    mainMenu()


# -----------------------------------------------------------------
# calling the train images from train_images.py file

def Trainimages():
    Train_Image.TrainImages()
    key = input("Press Enter key to return main menu")
    mainMenu()


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file

def RecognizeFaces():
    Recognize.recognize_attendence()
    key = input("Press Enter key to return main menu")
    mainMenu()


# ---------------main driver ------------------
mainMenu()