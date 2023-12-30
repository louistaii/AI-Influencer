import pathlib


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def saveconfig(model,load):
    path = pathlib.Path(__file__).parent.resolve()
    
    
    if load == "Y" or load == "y" or load == "yes":
        load = 0
    else:
        load = 1
    
    autoprompt = input(f"{bcolors.BOLD}Enable auto prompt generation? [Y/N]: {bcolors.ENDC}")

    if autoprompt == "Y" or autoprompt == "y" or autoprompt == "yes":
        autoprompt = 0
    else:
        autoprompt = 1
    
    f = open(f"{path}/config/settings.txt", "w")
    f.writelines(f"{model} \n{load} \n{autoprompt}")
    f.close()
    print(f"{bcolors.HEADER}Settings saved.{bcolors.ENDC}")
    quit()



def main():
    print(f"{bcolors.HEADER}AI INFLUENCER SETUP{bcolors.ENDC}")
    print("")

    print("Select configuration \n1.) Low end PC config \n2.) High end PC config(Reccommended) \n3.) Custom")
    config = input("Enter 1, 2 or 3: ")
    
    if config == "1":
        saveconfig(1,"y") 
    elif config == "2":
        saveconfig(2,"y")
    else:
        print(f"{bcolors.HEADER}\nCustom Config Setup{bcolors.ENDC}")


    print(f"{bcolors.BOLD}Select Stable Diffusion model{bcolors.ENDC} \n 1.) SD v1-5 (for lower end PCs) \n 2.) SDXL 1.0 {bcolors.BOLD}(Best Quality){bcolors.ENDC} \n" )
    model = input('Enter 1 or 2: ')

    load = input(f"{bcolors.BOLD}\nUse smaller sized pre-trained model to decrease download time? [Y/N]: {bcolors.ENDC}")
    
    

    saveconfig(model,load)


if __name__ == "__main__":
    main()