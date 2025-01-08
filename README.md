# Jogo da Cobrinha - Python

Este é um jogo simples da cobrinha desenvolvido em Python utilizando a biblioteca Pygame. O projeto foi criado como uma aplicação que utiliza conceitos de **Orientação a Objetos**, **serialização de objetos** e **interfaces gráficas**, aplicando princípios como **herança**, **polimorfismo** e **encapsulamento total**. O código foi modelado utilizando UML para definir as relações e abstrações de forma clara.

## Tecnologias Utilizadas

- **Python 3**
- **Pygame**: Para a criação da interface gráfica e animações do jogo.
- **JSON**: Para salvar e carregar o placar (pontuação máxima).

## Conceitos de Orientação a Objetos Aplicados

O projeto utiliza conceitos de orientação a objetos para modelar os elementos do jogo:

- **Herança**: As classes `Snake` e `Food` herdam da classe base `GameObject`, que define atributos e métodos comuns a todos os objetos do jogo.
- **Polimorfismo**: O método `draw()` é sobrescrito nas classes filhas para desenhar diferentes objetos na tela.
- **Encapsulamento**: A classe `Snake` possui dados internos como a posição do corpo e direção, que são modificados apenas através de métodos específicos, garantindo maior controle sobre o estado do jogo.
- **Serialização de Objetos**: O placar é salvo em um arquivo JSON, permitindo que o jogo armazene a pontuação máxima alcançada entre as execuções.

## Funcionalidades

- **Jogo da Cobrinha**: O jogador controla a cobrinha que se move pela tela, comendo a comida para crescer.
- **Pontuação**: A pontuação aumenta cada vez que a cobrinha come a comida. O placar mais alto é salvo em um arquivo JSON (`placar.json`).
- **Interface Gráfica**: Utiliza a biblioteca Pygame para desenhar a tela, cobrinha, comida e o placar.
- **Persistência de Dados**: O placar é salvo e carregado entre execuções do jogo.

## Instruções para Execução

1. Certifique-se de que o Python 3 está instalado em sua máquina.
2. Instale o Pygame utilizando o comando:

   ```bash
   pip install pygame
3. Clone este repositório:
   
   ```bash
    git clone https://github.com/seu-usuario/jogo-da-cobrinha.git

4. Navegue até a pasta do projeto e execute o jogo:
   ```bash
   python jogo_da_cobrinha.py

## Arquivos Importantes

- **jogo_da_cobrinha.py**: O código principal do jogo, onde a lógica do jogo e a interface gráfica são implementadas.
- **placar.json**: Arquivo utilizado para armazenar a pontuação mais alta alcançada.















