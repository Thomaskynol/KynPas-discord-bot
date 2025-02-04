import os
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
    
def loadedCogMessage(cogName: str):
    print(Fore.GREEN + f"Loaded {cogName}")
    
def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def botErrorMessage(message: str):
    print(Fore.RED + message)
    
def botLogMessage(message: str):
    print(Fore.CYAN + message)