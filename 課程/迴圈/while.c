#include <stdio.h>
#include <stdbool.h>

int main(){
    int a = 0;
    while (a < 5)
    {
        a++;
        printf("%d", a);
    }

    printf("\n");
    a = 0;
    do
    {
        a++;
        printf("%d", a);
    } while (a < 0);
    
    
}