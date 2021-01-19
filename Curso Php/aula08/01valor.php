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
        $valor = $_GET["v"];
        echo "O valor digitado foi $valor";
        $rq = sqrt($valor);
        echo "<br>A raiz quadrada de $valor é " . number_format($rq,2);
    ?>

    <a href="exercicio01.html">voltar</a>;
</div>
    
</body>
</html>