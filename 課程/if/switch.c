#include <stdio.h>
#include <stdbool.h>

int main(){
    int a = 0;
    switch (a)
    {
    case 5:
        printf("1");
        break;
    case 4:
        printf("2");
        break;
    case 3:
        printf("3");
        break;
    case 2:
        printf("4");
        break;
    case 1:
        printf("5");
        break;
    default:
        printf("6");
        break;
    }
}