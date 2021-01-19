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
     array_unshift($v,"O");// adiciona um valor no início do vetor
     print_r($v);
     array_shift($v);//remove o primeiro valor do vetor
     print_r($v);
    ?>
    </pre>
</div>
    
</body>
</html>