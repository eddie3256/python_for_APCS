#include <stdio.h>
#include <stdbool.h>

int main(){
    printf("%d\n", 2+3);
    printf("%d\n", 2-3);
    printf("%d\n", 2*3);
    printf("%d\n", 2/3);

    int a = 1;
    a = a + 1;
    printf("%d\n", a);
    a += 1;
    printf("%d\n", a);
    a++;
    printf("%d\n", a);
    ++a;
    printf("%d\n", a);

    printf("%d\n", 2>3);
    printf("%d\n", 2<3);
    printf("%d\n", 2==3);
    printf("%d\n", 2!=3);

    printf("%d\n", 1 && 0);
    printf("%d\n", 1 || 0);
    printf("%d\n", !1);

    

}