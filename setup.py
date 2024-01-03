import pathlib
import psutil
import torch

class bcolors:
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


path = pathlib.Path(__file__).parent.resolve()

def igsaveconfig(username, password, hashtag, algo, confirm):
    f = open(f"{path}/config/igsettings.txt", "w")
    f.writelines(f"{username}\n{password}\n{hashtag}\n{algo}\n{confirm}")
    f.close()
    igconfig()

def iginfo(hashtag, algo, confirm):
    username = input("Instagram username (without the @): ")
    password = input("Password: ")
    igsaveconfig(username,password,hashtag,algo,confirm)
    igconfig()

def ighashtag(username,password,confirm):
    print("\nInput wanted hashtags in captions (eg.'#like4like #follow4follwow'). Leave blank if no hashtags are needed")
    hashtag = input("hashtags: ")
    yesno = input("Enable increase followers algorithm? [Y/N]: ")
    if yesno.lower == 'y':
        algo = 0
    else:
        algo = 1
    
    igsaveconfig(username,password,hashtag,algo,confirm)
    igconfig()

def igconfirm(username, password,hashtag,algo):
    
    choice = input("Require confirmation before posting? [Y/N]:")
    if choice.lower() == 'y':
        confirm = 0
    else:
        confirm =1

    igsaveconfig(username,password,hashtag,algo,confirm)
    igconfig()  
    

def igconfig(): 

    f = open(f"{path}/config/igsettings.txt", "r")
    username, password, hashtag, algo, confirm = f.read().splitlines()
    f.close()

    print(f"{bcolors.BOLD}\nMenu{bcolors.ENDC} \n1.) Input / change login info \n2.) Hashtags settings \n3.) Confirmation before posting \n4.) Quit")
    
    choice = input("Enter 1, 2, 3 or 4: ")
    if choice == "1":
        iginfo(hashtag,algo,confirm)
    if choice == "2":
        ighashtag(username, password,confirm)
    if choice == "3":
        igconfirm(username, password,hashtag,algo)
    if choice == "4":
        quit()


def recommended():
    ram = (round(psutil.virtual_memory().total / (1024.0 **3)))
    
    if torch.cuda.is_available():
        # Get the total GPU memory
        total_memory = torch.cuda.get_device_properties(0).total_memory
        vrammb = total_memory / (1024 ** 2)
        vram = round(vrammb/(1000))
    else:
        vram = 0

    print(f"You have {ram} GB of ram and {vram} GB of VRAM")
    
    if ram<=4 and vram <=2:
        print(f"{bcolors.BOLD}Low Tier PC config recommended{bcolors.ENDC}")
    elif ram >6 and vram >=10:
        print(f"{bcolors.BOLD}High Tier PC config recommended{bcolors.ENDC}")
    else:
        print (f"{bcolors.BOLD}Mid Tier PC config recommended{bcolors.ENDC}")


def saveconfig(model,steps):
    # for auto prompt
    autoprompt = input("Enable auto prompt generation? [Y/N]:")
    if (autoprompt.lower() == 'y'):
        autoprompt = 0
    else:
        autoprompt = 1


    enablebotchoice = input("Link Instagram bot to image generator? [Y/N]:")
    if (enablebotchoice.lower() == 'y'):
        enablebot = 0
    else:
        enablebot = 1


    f = open(f"{path}/config/aisettings.txt", "w")
    f.writelines(f"{model} \n{steps} \n{autoprompt} \n{enablebot}")
    f.close()
    print(f"{bcolors.HEADER}Settings saved.{bcolors.ENDC}")
    
    if enablebot == 0:
        print(f"{bcolors.HEADER}Instagram Bot Config.{bcolors.ENDC}")
        igconfig()

    quit()


def aiconfig():
    print("Select configuration \n1.) Low Tier PC config \n2.) Mid Tier PC config \n3.) High Tier PC config \n4.) Custom")
    config = input("Enter 1, 2, 3 or 4: ")
    
    if config == "1":
        saveconfig(1,30)
    if config == "2":
        saveconfig(2,60)
    if config == "3":
        saveconfig(2,100)
        
    print(f"{bcolors.HEADER}\nCustom Config Setup{bcolors.ENDC}")

    print("Choose Stable Diffusion model: \n1.) SD v1-5 (Realistic Vision v6) \n2.) SDXL v 1.0 (SDXL Yamer's Realistic)")
    model = input("Enter 1 or 2: ")
    print(f"More inference steps leads to higher RAM/VRAM usage but better generated image quality. {bcolors.BOLD}We recommend any in the range of 30 to 100{bcolors.ENDC}")
    steps = input("Input number of inference steps: ")
    saveconfig(model, steps)


def main():
    print(f"{bcolors.HEADER}AI INFLUENCER SETUP{bcolors.ENDC}")
    print("")
    recommended()
    aiconfig()




if __name__ == "__main__":
    main()