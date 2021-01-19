package aula11;

public class Bolsista extends Aluno {

    public float getBolsa() {
        return bolsa;
    }

    public void setBolsa(float bolsa) {
        this.bolsa = bolsa;
    }
    
    private float bolsa;
    
    public void renovarBolsa(){
        System.out.println("Renovanso bolsa de " + this.getNome());
        
    }
    @Override
    public void pagarMensalidade(){
        System.out.println(this.getNome() + " é bolsista! Pagamento facilitado!");
    }
}
