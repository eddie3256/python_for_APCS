#include <stdio.h>
#include <stdbool.h>

int main(){
    for (int i = 1; i < 11; i++)
    {
        printf("%d", i);
    }
    printf("\n");
    for (int i = 1; i < 11; i++)
    {
        printf("%d", i);
        i++;
    }
    printf("\n");
    for (int i = 1; i < 21; i++)
    {
        if(i == 10){
            continue;
        }
        if(i == 15){
            break;
        }
        printf("%d", i);
    }
}