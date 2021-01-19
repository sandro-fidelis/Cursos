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
        $t="Aqui temos um texto gigante em PHP que vai mostrar o  funcionamento da função wordwrap ";
        $r = wordwrap($t, 20, "<br>"); //wordwrap = quebra de linha
        echo $r;
     ?>   
</div>
    
</body>
</html>