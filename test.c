#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>
#include <sys/types.h>
#include <signal.h>

int main(){
    pid_t pid = fork();
    if(pid < 0 ){
        printf("Forking fiald!\n");

        return 1;
    }
    else if(pid == 0){
        char *message= "child process excuting";
        char *path = "./testCHILD.txt";/*directory*/
        char *args[] = {"cat", path, NULL};
        execv("/bin/cat", args); 


    }
    else{
        char *parents = "./testPARENTS.txt"; /*directory*/
        
        wait(NULL);

        FILE *parents_path = fopen(parents, "r");
         if (parents_path == NULL) {
        perror("Error opening file");
      
         
        }
        int c;
            while ((c = fgetc(parents_path)) != EOF) {
                putchar(c);
            }
        fclose(parents_path);
        
    }
    return 0;
}
