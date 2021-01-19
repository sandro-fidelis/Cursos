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
     $v = array(2=>"A",5=>"J",0=>"M",3=>"X",4=>"K");
     print_r($v);
     ksort($v);// ordena somente os índices dos vetores
     print_r($v);
     krsort($v);//ordem reversa somente dos índices dos vetores
     print_r($v);
    ?>
    </pre>
</div>
    
</body>
</html>