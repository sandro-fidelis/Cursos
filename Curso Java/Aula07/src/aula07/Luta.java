package aula07;

import java.util.Random;

public class Luta {
 //Atributos
 private Lutador desafiado;   
 private Lutador desafiante;
 private int rounds;
 private boolean aprovado;
 
 //Métodos principais
 public void marcarLuta(Lutador L1, Lutador L2){
   if (L1.getCategoria().equals(L2.getCategoria())
    && L1 != L2) {
       this.aprovado = true;
       this.desafiado = L1;
       this.desafiante = L2;        
   } else{
       this.aprovado = false;
       this.desafiado = null;
       this.desafiante = null;        
   }
}
 public void lutar(){
  if (this.aprovado){
      System.out.println("### DESAFIADO ###");
     this.desafiado.apresentar();
      System.out.println("### DESAFIANTE ###");
     this.desafiante.apresentar();
         
     Random aleatorio = new Random();
     int vencedor = aleatorio.nextInt(3); //0 1 2
      System.out.println("======== RESULTADO DA LUTA ===========");
     switch(vencedor){
         case 0://EMPATE
             System.out.println("Empatou");
            this.desafiado.empatarLuta();
            this.desafiante.empatarLuta();
             break;
             
         case 1:// DESAVIADO VENCE
             System.out.println("O vencedor foi o " + desafiado.getNome());
             this.desafiado.ganharLuta();
             this.desafiante.perderLuta();
             break;
         case 2://DESAFIANTE VENCE
             System.out.println("O vencedor foi o " + desafiante.getNome());
             this.desafiado.perderLuta();
             this.desafiante.ganharLuta();
             break;
     }
      System.out.println("==========================================");   
  }else{
      System.out.println("A luta não pode acontecer ");
  }
    
    
  }   

 //Métodos especiais

    public Lutador getDesafiado() {
        return desafiado;
    }

    public void setDesafiado(Lutador desafiado) {
        this.desafiado = desafiado;
    }

    public Lutador getDesafiante() {
        return desafiante;
    }

    public void setDesafiante(Lutador desafiante) {
        this.desafiante = desafiante;
    }

    public int getRounds() {
        return rounds;
    }

    public void setRounds(int rounds) {
        this.rounds = rounds;
    }

    public boolean getAprovado() {
        return aprovado;
    }

    public void setAprovado(boolean aprovado) {
        this.aprovado = aprovado;
    }
 
 
}