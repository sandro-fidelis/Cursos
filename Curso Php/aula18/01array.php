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
    <pre>
    <?php
    $n =array(3,5,8,2);
    $n[] = 7;
    print_r($n);
    ?>
    </pre>
    
    <pre>
    <?php
    echo "<br>";
    $c = range(5,20,2); //array começa com 5 e termina em 20 passando de 2 em 2
    print_r($c);
    ?>
    </pre>

    
</div>
    
</body>
</html>