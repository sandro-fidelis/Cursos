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
        $nome = isset($_GET["nome"])?$_GET["nome"]:"[idade não informada]";
        $ano = isset ($_GET["ano"])?$_GET["ano"]: 0;
        $sexo = isset ($_GET["sexo"])?$_GET["sexo"]:"[sexo não informado]";
        $idade = date("Y") - $ano;
        echo "$nome tem $idade anos e é $sexo";
    ?>

    <a href="exercicio02.html">voltar</a>;
</div>
    
</body>
</html>