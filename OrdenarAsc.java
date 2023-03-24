package basicos.EstrucuturaD;

import java.util.Arrays;

// método para ordenar el arreglo de forma acendente.
public class OrdenarAsc {
    public static void main (String args[]){
        int num [] = {2,5,6,4,51,93,52};
        Arrays.sort(num);
        for(int i=0; i<num.length;i++){
            System.out.println(""+num[i]);
        }
    }        
}
