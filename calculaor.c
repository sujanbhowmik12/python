#include<stdio.h>
int main() {
    float x,y,z;
    printf(" enter the x:");
    scanf("%f",&x);
    printf("enter y:");
    scanf("%f", &y);
    char operator;
    printf("enter operator('+', '-', '*', '/'):");
    scanf(" %c", &operator);

     switch(operator) {
     case'+' :
     z=x+y;
     printf("%.2f + %.2f = %.2f\n", x,y,z);
     break;
     case'-' :
     z=x-y;
      printf("%.2f - %.2f = %.2f\n", x,y,z);
      break;
     case'*' :
     z=x*y;
      printf("%.2f * %.2f = %.2f\n", x,y,z);
      break;
     case'/' :
     z=x/y;
      printf("%.2f / %.2f = %.2f\n", x,y,z);
      break;

     }
    return 0;
}