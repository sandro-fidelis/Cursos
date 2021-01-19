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
       $nota1 = $_GET["n1"];
       $nota2 = $_GET["n2"];
       $m = ($nota1 + $nota2)/2;
       echo "A média entre $nota1 e $nota2 é $m<br>";
       //$sit = ($m>6) ? "Aprovado": "Reprovado"; // pode ser assim ou na forma abaixo
       echo "Este aluno foi " . (($m>6) ? "Aprovado": "Reprovado");
    ?>
</div>
    
</body>
</html>