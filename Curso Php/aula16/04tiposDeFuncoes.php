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
        // STRLEN e TRIM
        $nome ="   sandro jose fidelis   ";
        echo(strlen($nome));//tamanho da string total = 25
        $novo = trim($nome);// elimina os espaços da string no começo e no fim = 19
        echo("<br>$novo<br>");
        echo(strlen($novo));// escreve o novo tamanho da string
    ?>

    <?php
        //LTRIM
        echo"<br><br>";
        $nome = "   sandro jose fidelis   ";
        echo(strlen($nome));
        $novo = ltrim($nome);//elimina apenas os espaços em branco do inicio da string
        echo("<br>$novo<br>");
        echo(strlen($novo));// novo tamanho

        //função RTRIM = elimina apenas os ultimos espaços em branco da string
    ?>


</div>
    
</body>
</html>