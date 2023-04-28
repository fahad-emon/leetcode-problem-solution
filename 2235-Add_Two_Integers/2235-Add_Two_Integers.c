#include<stdio.h>
int sum(int num1, int num2){
    int sum = ( num1 + num2 );
    return sum;
}

int main (){
    int a,b;
    scanf("%d%d",&a,&b);
    int sumofab = sum(a,b);
    printf("%d",sumofab);
    return 0;
}
