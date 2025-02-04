#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <io.h>

int main() {
    SetConsoleTitleA("KynPas DiscordBot");
    
    chdir("..");

    const char *command = "python src/main.py";

    int status = system(command);
    
    if (status == -1) {
        perror("Erro ao executar o comando");
        return EXIT_FAILURE;
    }
    
    return EXIT_SUCCESS;
}