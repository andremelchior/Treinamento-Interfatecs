#include <iostream>
#include <cstdio>
 
int main() {
 
   int qtd, cod;
   float total;
   std::cin >> cod >> qtd;
   
   if (cod == 1){
       total = 4.00 * qtd;
   } else if (cod == 2){
        total = 4.50 * qtd;
   } else if (cod == 3){
        total = 5.00 * qtd;
   } else if (cod == 4){
        total = 2.00 * qtd;
   } else if (cod == 5){
        total = 1.50 * qtd;
   }
   
   printf("Total: R$ %.2f\n", total);
   return 0;
}
