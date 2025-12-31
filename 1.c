#include <stdio.h>
#include <limits.h>

int main(){
    int array[5] = {3,-4,5,-6,7};
    int max_sum = INT_MAX;//

    for(int i = 0; i < 5;i++){
        for(int j = i; j < 5;j++){
            int sum = 0;
            for(int k = i;k<=j;k++){
                sum+=array[k];
            }
            if (max_sum < sum){
                max_sum = sum; 
            }
        }
        printf("\n");

    }
    printf("%d",max_sum);

}