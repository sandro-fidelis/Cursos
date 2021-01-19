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
        $m = array( array(6,4),
                    array(4,9),
                    array(3,2));
        $m[0] [1] = $m[2] [0]; // troca o valor do vetor na posição [0] [1] pelo valor do vetor da posição [2] [0] 
        print_r($m);
    ?>
    </pre>
</div>
    
</body>
</html>