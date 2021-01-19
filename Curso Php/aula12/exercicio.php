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
    $num= isset ($_GET["num"])? $_GET["num"]:1;
    echo "<h1>Calculando a tabuada de $num</h1><br>";
    $c = 1;
    do {
        $r = $num * $c;
        echo "$num X $c = $r<br>";
        $c++;
    }while($c<=10);
    ?>
    <a href="exercicio.html">Voltar</a>
</div>
</body>
</html>