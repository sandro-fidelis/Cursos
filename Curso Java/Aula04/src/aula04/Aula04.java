/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula04;

/**
 *
 * @author sandr
 */
public class Aula04 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Caneta c1 = new Caneta("Bic", 0.9f, "Preta");
        c1.status();
        Caneta c2 = new Caneta("kkk", 0.5f,"Amarela");
        c2.status();
    }
    
}
