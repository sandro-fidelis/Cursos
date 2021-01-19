package aula09exercicio;
//Atributos
public class Pessoa {
    private String nome;
    private int idade;
    private String sexo;

    //Métodos Especiais
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public String getSexo() {
        return sexo;
    }

    public Pessoa(String nome, int idade, String sexo) {
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }
    
    //Métodos publicos
    public void fazerAniverssario(){
      this.idade = this.idade + 1;
    }
}
