import os
from datetime import datetime
from colorama import Fore, Back, Style, init

init(autoreset=True)
def botLoadingMessage():
    print(Fore.YELLOW + "==================================================================================================")
    print(Fore.YELLOW + "======================================== Loading Bot! ============================================")
    print(Fore.YELLOW + "==================================================================================================")

def botIsReadyForUseMessage():
    print(Fore.GREEN + "==================================================================================================")
    print(Fore.GREEN + "==================================== Bot is ready for use! =======================================")
    print(Fore.GREEN + "==================================================================================================")
    
def closingBotMessage():
    print(Fore.YELLOW + "==================================================================================================")
    print(Fore.YELLOW + "======================================== Closing Bot! ============================================")
    print(Fore.YELLOW + "==================================================================================================")

    
def botIsClosedMessage():
    print(Fore.RED + "==================================================================================================")
    print(Fore.RED + "======================================== Bot is closed! ===========================================")
    print(Fore.RED + "==================================================================================================")
    
def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def botErrorMessage(message: str):
    print(Fore.RED + message)
    
def botLogMessage(message: str):
    print(Fore.LIGHTBLACK_EX + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Fore.LIGHTBLUE_EX + " INFO     " + Fore.MAGENTA + message)

def loadedCogMessage(cogName: str):
    botLogMessage("cog loaded: " + cogName)