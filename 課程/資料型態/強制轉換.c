#include <stdio.h>
#include <stdbool.h>

int main(){
    float a = 5.5;
    a = (int)a;
    printf("%d\n", a); //會有進位問題

    int b = 1;
    b = (float)b;
    printf("%f\n", b);

    return 0;
}