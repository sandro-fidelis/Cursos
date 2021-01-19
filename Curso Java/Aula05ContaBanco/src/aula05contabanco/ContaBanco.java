/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula05contabanco;

/**
 *
 * @author sandr
 */
public class ContaBanco {
 //ATRIBUTOS   
    public int numConta;
    protected String tipo;
    private String dono;
    private float saldo;
    private boolean status;
    public float valor;

    public void ContaBanco(float saldo, boolean status) {
        this.saldo = 0;
        this.status = false;
    }

    public int getNumConta() {
        return numConta;
    }

    public void setNumConta(int numConta) {
        this.numConta = numConta;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getDono() {
        return dono;
    }

    public void setDono(String dono) {
        this.dono = dono;
    }

    public float getSaldo() {
        return saldo;
    }

    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public boolean getStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }
    // MÉTODOS PERSONALIZADOS
    public void estadoAtual(){
        System.out.println("================================");
        System.out.println("Conta: " + this.getNumConta());
        System.out.println("Tipo: " + this.getTipo());
        System.out.println("Dono: " + this.getDono());
        System.out.println("Saldo: " + this.getSaldo());
        System.out.println("Status: " + this.getStatus());
    }
    
    public void abrirConta(String tipo){
       this.setTipo(tipo);
       this.setStatus(true);
       
       if (tipo == "cc"){
           this.setSaldo(50);
       }else if (tipo == "cp"){
           this.setSaldo(150);
    }
        System.out.println("Conta aberta com sucesso!");
    }
    
    public void fecharConta(){
        if (this.getSaldo() > 0){
            System.out.println("A conta NÃO pode ser fechada ainda tem dinheiro ");
        }else if (this.getSaldo() < 0 ){
            System.out.println("Saldo negativo: Aconta não pode ser fechada");   
        }else{
            this.setStatus(false);
            System.out.println("Conta fechada com sucesso!");
        }
}
    
    public void depositar(float valor){
        if (this.getStatus()){
            this.setSaldo(this.getSaldo() + valor);
            System.out.println("Depósito realizado com sucesso! na conta de: " + this.getDono());
        } else {
                  System.out.println("Impossível depositar em uma caonta fechada");  
        }
}
    public void sacar(float valor){
        if (this.getStatus()){
            if (this.getSaldo() >= valor){
                this.setSaldo(this.getSaldo() - valor);
                System.out.println("Saque realizado da conta de " + this.getDono());
          } else {
        System.out.println("Saldo insuficiente para saque");
            }
            }else{
        System.out.println("Impossível sacar de uma conta fechada");
         }
    }
    public void pagarMensal(){
    int vmensal;
    if (this.getTipo() == "cc"){
    vmensal = 12;        
    }else if (this.getTipo() == "cp"){
          vmensal = 20;
    }
    if (this.getStatus()){
       this.setSaldo(this.getSaldo() - valor);
        System.out.println("Mensalidade paga com sucesso! por " + this.getDono() );
    } else {
            System.out.println("Impossível pagar uma conta fechada!");
    }
    }
}