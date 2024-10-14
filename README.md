# 14/10/2024

### 1. **Imprimindo uma mensagem**
   - **Objetivo:** Compreender o básico sobre como o Python exibe mensagens na tela.
   - **Explicação:** O primeiro passo em programação é aprender como o computador pode nos mostrar algo na tela. Isso é feito com a função `print()`, que mostra qualquer texto que colocarmos entre parênteses e aspas.

   - **Instruções detalhadas:** Escreva um programa que mostre a frase `"Olá, mundo!"` na tela.
   - **Passos:**
     1. Abra um editor de código (como o VSCode ou IDLE).
     2. Escreva o código abaixo:
        ```python
        print("Olá, mundo!")
        ```
     3. Execute o programa.

   - **O que deve acontecer:** A tela deve mostrar o texto:  
     ```
     Olá, mundo!
     ```

### 2. **Soma de dois números**
   - **Objetivo:** Aprender a receber dados do usuário e realizar uma operação matemática simples.
   - **Explicação:** O Python permite que você receba informações do usuário com a função `input()`. No entanto, o que você recebe de `input()` sempre é um texto (string), então você precisa converter para número usando `int()`.

   - **Instruções detalhadas:** Crie um programa que pergunte ao usuário dois números, some-os e exiba o resultado.
   - **Passos:**
     1. Use `input()` para pedir os números ao usuário.
     2. Use `int()` para converter os números digitados.
     3. Some os dois números e use `print()` para mostrar o resultado.
     4. Código exemplo:
        ```python
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        soma = numero1 + numero2
        print("A soma é:", soma)
        ```

   - **O que deve acontecer:** Quando o programa for executado:
     ```
     Digite o primeiro número: 5
     Digite o segundo número: 3
     A soma é: 8
     ```

### 3. **Calculando a média**
   - **Objetivo:** Praticar operações matemáticas com múltiplos números e trabalhar com variáveis.
   - **Explicação:** Neste exercício, você vai aprender a trabalhar com mais de uma variável, coletando três notas do usuário, somando e dividindo para calcular a média.

   - **Instruções detalhadas:** Escreva um programa que pergunte três notas e calcule a média aritmética.
   - **Passos:**
     1. Receba três números do usuário usando `input()`.
     2. Converta os números para inteiros com `int()`.
     3. Some as três notas e divida o resultado por 3 para obter a média.
     4. Código exemplo:
        ```python
        nota1 = int(input("Digite a primeira nota: "))
        nota2 = int(input("Digite a segunda nota: "))
        nota3 = int(input("Digite a terceira nota: "))
        media = (nota1 + nota2 + nota3) / 3
        print("A média é:", media)
        ```

   - **O que deve acontecer:** O programa deve mostrar algo assim:
     ```
     Digite a primeira nota: 7
     Digite a segunda nota: 8
     Digite a terceira nota: 6
     A média é: 7.0
     ```

### 4. **Convertendo Celsius para Fahrenheit**
   - **Objetivo:** Aplicar uma fórmula matemática simples em Python.
   - **Explicação:** Você vai converter uma temperatura em graus Celsius para Fahrenheit usando uma fórmula. Aqui você aprenderá como usar variáveis e fazer cálculos com elas.

   - **Instruções detalhadas:** O usuário deve informar uma temperatura em Celsius, e o programa deve converter para Fahrenheit.
   - **Passos:**
     1. Peça ao usuário a temperatura em Celsius.
     2. Use a fórmula `F = (C * 9/5) + 32` para converter.
     3. Exiba o resultado em Fahrenheit.
     4. Código exemplo:
        ```python
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("A temperatura em Fahrenheit é:", fahrenheit)
        ```

   - **O que deve acontecer:** O resultado será algo como:
     ```
     Digite a temperatura em Celsius: 25
     A temperatura em Fahrenheit é: 77.0
     ```

### 5. **Número par ou ímpar**
   - **Objetivo:** Usar condicionais (if/else) para tomar decisões.
   - **Explicação:** Você vai aprender a usar uma condição para verificar se um número é par ou ímpar. Números pares são divisíveis por 2, e números ímpares não são.

   - **Instruções detalhadas:** O programa deve pedir um número e dizer se ele é par ou ímpar.
   - **Passos:**
     1. Peça ao usuário para digitar um número.
     2. Use o operador `%` (resto da divisão) para verificar se o número é divisível por 2.
     3. Exiba "par" ou "ímpar" dependendo do resultado.
     4. Código exemplo:
        ```python
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")
        ```

   - **O que deve acontecer:** Exemplo de resultado:
     ```
     Digite um número: 7
     O número é ímpar.
     ```


### 6. **Contando caracteres**
   - **Objetivo:** Aprender a trabalhar com strings e contar o número de caracteres em um texto.
   - **Explicação:** Você vai usar a função `len()` para contar quantos caracteres uma palavra possui.

   - **Instruções detalhadas:** Peça ao usuário para digitar uma palavra e mostre quantos caracteres ela tem.
   - **Passos:**
     1. Use `input()` para pegar a palavra do usuário.
     2. Use a função `len()` para contar os caracteres.
     3. Exiba a contagem de caracteres.
     4. Código exemplo:
        ```python
        palavra = input("Digite uma palavra: ")
        print("A palavra tem", len(palavra), "caracteres.")
        ```

   - **O que deve acontecer:** Exemplo:
     ```
     Digite uma palavra: Python
     A palavra tem 6 caracteres.
     ```


Esses exercícios foram estruturados com mais detalhes para ajudar quem está começando a aprender Python.
