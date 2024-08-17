#include <stdio.h>
#include <stdbool.h>

const int x = 5;
#define A 6

int main(){
    int a = 0;
    int b = 1, c = 2;
    int d = A;
    int e = x;
    #define B 3
    printf("%d %d %d %d %d %d %d %d", a, b, c, d, e, A, x, B);

}