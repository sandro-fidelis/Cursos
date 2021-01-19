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
    $n= isset($_GET["num"])? $_GET["num"]:1;
    echo "Analizando o Número $n...<br>";
    echo "Números Múltiplos: ";
    $nm = 0;
    $tm = 0;
    for($cm = 1; $cm <=$n; $cm++){
        if($n%$cm==0){
            $tm++;
            $nm = $nm + $cm; 
            echo "$cm, ";
        }
    }
    echo "<br>";
    echo "Total de Múltiplos: $tm<br>";
    if($tm == 2){
        $p = " É PRIMO!";
    }else{
        $p = "NÃO É PRIMO!";
    }

    echo "Resultado: $n .$p <br>";
    
    ?>
    <a href="exercico.html">Voltar</a>
</div>
    
</body>
</html>