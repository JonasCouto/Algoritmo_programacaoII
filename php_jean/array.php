<?php

    $cores = array('azul','vermelho', 'laranja');

    for($i = 0; $i < count($cores); $i++){
        echo $i.' -> '.$cores[$i]."\n";

    }

    // para cada item "cores" que temos no nosso array faremos algo  *percorrer a lista e não se preocupar com posição*
    foreach($cores as $cor){
        echo $cor."\n";
        
    }

    // valor do indice fica na variavel I,
    foreach($cores as $i=> $cor){
        echo $i.' -> '.$cor."\n";
        
    }

    // Array associativo.
    $idade = array(
        'Jonas'=> 35,
        'Jean'=> 28
    );

    foreach($idade as $nome=> $valor){
        echo $nome.' -> '.$valor."\n";
    }

    $people = array(
        array('name' => 'Kalle', 'salt' => 856412),
        array('name' => 'Pierre', 'salt' => 215863)
    );

    foreach($people as $i => $pessoa){
        echo $i."\n";
        // print_r($pessoa);
        // echo $pessoa['name'].'----'. $pessoa['salt']."\n";
        foreach($pessoa as $chave=> $valor){
            echo $chave.' -> '.$valor."\n";
        } 
    }

    // | name | salt
    // 1 | Kalle | 21212
    // 2 | Teste | 281819

?>