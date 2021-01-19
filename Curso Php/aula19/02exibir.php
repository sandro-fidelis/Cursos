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
     $v = array("A","J","M","X","K");
     print_r($v);
     $v[] = "O"; // ou array_push($v,"O") adiciona um vetor no final
     print_r($v);
     array_pop($v);//remove o valor do último vetor
     print_r($v);
    ?>
    </pre>
</div>
    
</body>
</html>