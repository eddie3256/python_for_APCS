#include <stdio.h>
#include <stdbool.h>

int main(){
    int a = 5.2;
    printf("%d\n", a);
    float b = 1.5;
    a = b;
    printf("%d\n", a);
    printf("%f\n", b);

    double c = 1.5;
    printf("%f\n", c);

    char d = 'A';
    printf("%c\n", d);

    bool e = true;
    printf("%d\n", e);

    int f[3] = {1, 2, 3};
    printf("%d\n", f);
}