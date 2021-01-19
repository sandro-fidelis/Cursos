package aula07;

public class Lutador {
//ATRIBUTOS
private String nome;
private String nacionalidade;
private int idade;
private float altura;
private float peso;
private String categoria;
private int vitorias;
private int derrotas;
private int empates;

    public String getNome() {
        return nome;
    }

    public void setNome(String no) {
        this.nome = no;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public float getAltura() {
        return altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public float getPeso() {
        return peso;
    }

    public void setPeso(float peso) {
        this.peso = peso;
        this.setCategoria();
    }

    public String getCategoria() {
        return categoria;
    }

    private void setCategoria() {
        if (this.peso < 52.2){
            this.categoria = "INVÁLIDO";
        }else if
                (this.peso <= 70.3){
                this.categoria = "Leve";
                }else if
                (this.peso <= 83.9){
                this.categoria = "Media";
                }else if
                (this.peso <= 120.2){
                this.categoria = "Pesado";
        }else
                this.categoria = "Inválido";
                
                        }
                
                
               
    

    public int getVitorias() {
        return vitorias;
    }

    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public void setEmpates(int empates) {
        this.empates = empates;
    }


//MÉTODOS PÚBLICOS
public void apresentar(){
    System.out.println("===========================================");
    System.out.println("Lutador: " + this.getNome());
    System.out.println("Nacionalidade " + this.getNacionalidade());
    System.out.println(this.getIdade()+ " anos ");
    System.out.println(this.getAltura() + " m de Altura");
    System.out.println("Pesando " + this.getPeso() + " kgs ");
    System.out.println("Ganhou " + this.getVitorias());
    System.out.println("Perdeu " + this.getDerrotas());
    System.out.println("Empatou " + this.getEmpates());    
}
public void status(){
    System.out.println(this.getNome());
    System.out.println("é um peso "+ this.getCategoria());
    System.out.println(this.getVitorias() + " Vitórias");
    System.out.println(this.getDerrotas() + " Derrotas");
    System.out.println(this.getEmpates() + " Empates");
    
}
public void ganharLuta(){
    this.setVitorias(this.getVitorias() + 1);
}
public void perderLuta(){
    this.setDerrotas(this.getDerrotas() + 1);
}
public void empatarLuta(){
    this.setEmpates(this.getEmpates() + 1);
}

//MÉTODOS ESPECIAIS

    public Lutador(String no, String na, int id, float al, float pe, int vi, int de, int em) {
        this.nome = no;
        this.nacionalidade = na;
        this.idade = id;
        this.altura = al;
        this.setPeso(pe);
        this.vitorias = vi;
        this.derrotas = de;
        this.empates = em;
    }
    
    


}