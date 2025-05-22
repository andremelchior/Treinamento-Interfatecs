#include <iostream>
 
int main() {
 
    int n;

    std::cin >> n; //7
    
    //6 vezes para testar par + 6 vezes para testar impar.
    for(int i = 0; i < 12; i++){ //0 (T), 1 (T), 2 (T), 3 (T)...
        
        //se o resto da divisão por 2 for maior que 0 = impar.
        if(n % 2 > 0){ //7 impar? (T), //8 impar? (F), //9 impar? (T), 
			//10 impar? (F), 11 impar? (T), 12 impar? (F), 13 impar? (T),
			//14 impar? (F), 15 impar? (T), 16 impar? (F), 17 impar? (T).
			
            std::cout << n << std::endl; //7, 9, 11, 13, 15, 17.
        }
        
        n++; //7->8->9->10->11->12...
    } //1 < 6? (T) -> 2 (teste de condicao).
 
    return 0;
}
