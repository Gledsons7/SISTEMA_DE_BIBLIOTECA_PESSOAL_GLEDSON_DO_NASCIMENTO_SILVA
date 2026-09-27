 # Biblioteca Pessoal

## Descrição

Sistema de gerenciamento de uma biblioteca digital/pessoal,
desenvolvido utilizando os princípios de Programação Orientada a Objetos.

## Objetivo

O projeto tem como objetivo permitir o gerenciamento de publicações,
usuários, leituras, regras de leitura, relatórios e persistência dos dados.

## Diagrama UML

Abaixo está o diagrama UML contendo as principais classes,
interfaces, atributos, métodos e relacionamentos do sistema.

![Diagrama UML](UML_Diagrama_Entregavel_1.0.0.png)

## Estrutura de Classes

### Publicações

- Publicacao
- Livro
- Revista
- PublicacaoDigital
- LivroDigital
- Catalogavel

### Usuários e Leituras

- Usuario
- Leitura
- RegraLeitura
- RegraPadrao

### Relatórios e Persistência

- Relatorio
- Repositorio
- RepositorioJSON
- RepositorioSQLite
