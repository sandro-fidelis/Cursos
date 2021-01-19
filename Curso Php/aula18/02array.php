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
        <table border="1"><tr>
    <?php
        $c = range(5,20,2);
        foreach($c as $v){ // para cada elemento do vetor $c será colocado em $v
            echo "<td>$v ";
        }
    ?>
    </table>    
    </pre>

    <pre>
    <?php
        $v = array ( 3=>5,
                     1=>9,
                     0=>8,
                     7=>7);
        unset($v[0]);// remove o vetor da posição "0"
        print_r($v);
    ?>
    </pre>
</div>
    
</body>
</html>