/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula02;

/**
 *
 * @author sandr
 */
public class Caneta {
    String modelo;
    String cor;
    float ponta;
    int carga;
    boolean tampada;
    void status(){
        System.out.println("Qual o modelo ? " + this.modelo);
        System.out.println("Uma caneta " + this.cor);
        System.out.println("Qual o tamanho da ponta? " + this.ponta);
        System.out.println("Qual é a carga atual? " + this.carga);
        System.out.println("Está tampada ? " + this.tampada);
    }
    void rabiscar (){
    if (tampada == true ){
        System.out.println("ERRO Não posso rabiscar");
    }else{
        System.out.println("Estou rabiscando ");
    }
}
    void tampar(){
    this.tampada = true;       
    }
     
    void destampar(){
    this.tampada = false;    
    }
}