package aula12animais;

public class Aula12Animais {

    public static void main(String[] args) {
        Mamifero m = new Mamifero();
        Reptil r = new Reptil();
        Peixe p =new Peixe();
        Ave a = new Ave();
        Canguru c = new Canguru();
        Cachorro k = new Cachorro();
        Cobra j = new Cobra();
        Tartaruga t = new Tartaruga();
        GoldFish g = new GoldFish();
        Arara e = new Arara();
        
        
        c.locomover();
        k.locomover();
        c.emitirSom();
        k.emitirSom();
        
       /* m.setPeso(35.3f);
        m.setCorPelo("Marrom");
        m.alimentar();
        m.locomover();
        m.emitirSom();
        
        a.locomover();
        p.locomover();
        r.locomover();*/
        
    }
    
}
