<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="_css/estilo.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<div>
    <?php
        $nome = "Sandro Fidelis";
        echo "Seu nome é ". strtolower($nome); //  todas em letras minúsculas
        echo "<br>";
        echo "Seu nome é ". strtoupper($nome); // todas as letras em maiúsculas
        echo "<br>";
        $nome2 = "mara fidelis";
        echo "Seu nome é ". ucfirst($nome2);// Maiúsculas na primeira palavra
        echo "<br>";
        echo "Seu nome é " . ucwords($nome2);// Miaúsculas nas primeiras letaras das palavras
        echo "<br>";
        echo "Seu nome ao contrário é ". strrev($nome2);
        echo "<br>";
        $frase = "Estou aprendendo PHP";
        $pos = strpos($frase, "PHP");// posição da palavra na frase
        echo "A string PHP foi encontrada na posição ". $pos;
        echo "<br>";
        $pos = stripos($frase, "php");//posição da palavra ingnorando a caixa alta = case sensitive
        echo "A string PHP foi encontrada na posição ". $pos;
        echo "<br>";
        $frase2 = "Estou aprendendo PHP no curso em Vídeo de PHP";
        $cont = substr_count($frase2,"PHP"); // quantidade de palavras na frase. Ex PHP
        echo "<br>";
        echo$frase2;
        echo "<br>";
        echo "PHP encontado $cont vezes";
        $site = "Curso em Vídeo";
        $sub = substr($site,0,5);// mostra somente as primeiras 5 letras (0,5)
        echo "<br>";
        echo $sub;
        echo "<br>";
        $txt = str_repeat("Php",5); //repete a palavra 'PHP' 5 vezes
        echo "O texto gerado foi $txt";
        echo "<br>";
        $frase3 = "Gosto de estudar PHP!!!";
        $novaFrase = str_replace("PHP", "JAVA" ,$frase3);// subtitui a palavra PHP poR JAVA
        echo $novaFrase;
   ?>
</div>
    
</body>
</html>