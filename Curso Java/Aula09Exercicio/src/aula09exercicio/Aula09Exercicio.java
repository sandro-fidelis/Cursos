package aula09exercicio;

public class Aula09Exercicio {

    public static void main(String[] args) {
    Pessoa[] p = new Pessoa[2];
    Livro[] L = new Livro[3];
    
    p[0] = new Pessoa("Sandro", 40, "Masculino");
    p[1] = new Pessoa("Mara", 41, "Feminino");
    
    L[0] = new Livro("Biblia", "Deus", 1865, p[0]);
    L[1] = new Livro("Teologia Sistematica", "Pentecost", 845, p[1]);
    L[2] = new Livro("O monge e o Executivo", "João Pinheiro", 658, p[0]);
    
        L[0].abrir();
        L[0].folhear(100);
        L[0].avancarPag();
        System.out.println(L[0].detalhes());
        
        System.out.println(L[1].detalhes());
    }
}
