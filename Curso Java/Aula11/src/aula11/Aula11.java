package aula11;

public class Aula11 {

    public static void main(String[] args) {
 
        //Pessoa p1 = new Pessoa();
        
      /*  Visitante v1 = new Visitante();
        v1.setNome("Sandro");
        v1.setIdade(40);
        v1.setSexo("Masculino");
        System.out.println(v1.toString());*/
        
        Aluno a1 = new Aluno();
        a1.setNome("Claudio");
        a1.setMatricula(1212);
        a1.setCurso("Informática");
        a1.setIdade(18);
        a1.setSexo("Masculimo");
        a1.pagarMensalidade();
        
        Bolsista b1 = new Bolsista();
        b1.setMatricula(1212);
        b1.setNome("Jubileu");
        b1.setBolsa(12.5f);
        b1.setSexo("Masculino");
        b1.pagarMensalidade();
        
    }
    
    
}
