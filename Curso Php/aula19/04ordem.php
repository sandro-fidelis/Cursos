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
     sort($v);// ordena os vetores
     print_r($v);
     rsort($v);//ordem reversa
     print_r($v);
     asort($v);//ordena os valores sem alterar os índices
     print_r($v);
     arsort($v);// coloca os valores em ordem reversa sem alterar os índices
     print_r($v); 
    ?>
    </pre>
</div>
    
</body>
</html>