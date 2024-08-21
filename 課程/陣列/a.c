#include <stdio.h>
#include <stdbool.h>

int main(){
    int a[3];
    for (int i = 0; i < 3; i++){
        printf("%d ", a[i]);
    }

    printf("\n");
    int b[] = {1, 2, 3};
    for (int i = 0; i < 3; i++){
        printf("%d", b[i]);
    }

    printf("\n");
    int f[3] = {1, 2, 3};
    for (int i = 0; i < 3; i++){
        printf("%d", f[i]);
    }

    /*
    printf("\n");
    int g[1] = {1, 2, 3};
    for (int i = 0; i < 3; i++){
        printf("%d", g[i]);
    }*/

    printf("\n");
    int h[5] = {1, 2, 3};
    for (int i = 0; i < 5; i++){
        printf("%d", h[i]);
    }
    printf("\n");
    float j[3] = {1, 2, 3};
    for (int i = 0; i < 3; i++){
        printf("%f ", j[i]);
    }
    printf("\n");
    int k[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    for (int i = 0; i < 3; i++){
        for (int l = 0; l < 3; l++){
        printf("%d ", k[i][l]);
        }
    }
    int m[3][3][3][3][3] = {};
    
}