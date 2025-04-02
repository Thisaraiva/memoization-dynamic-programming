## Integrantes da Equipe
- João Antonio David
- Thiago de Fretias Saraiva

---

# Relatório: Cálculo de Fibonacci com Recursividade e Memoization

## 1. Escolha do Problema
O problema escolhido foi o cálculo da sequência de Fibonacci, que é um problema clássico da computação e matemática. A sequência é definida como:

\[ F(n) = F(n-1) + F(n-2) \]

com os casos base:

\[ F(0) = 0, \quad F(1) = 1 \]

Esse problema foi escolhido pois pode ser resolvido de forma eficiente utilizando recursividade e memoization para otimizar a execução, reduzindo cálculos redundantes.

## 2. Estratégia de Resolução

A estratégia de resolução envolveu o uso de **recursividade** para calcular os valores da sequência e **memoization** para armazenar resultados intermediários e evitar recomputações desnecessárias.

### Recursividade
A solução foi baseada em uma função recursiva que calcula o valor de \( F(n) \) chamando recursivamente \( F(n-1) \) e \( F(n-2) \).

### Memoization
Para evitar cálculos repetidos, utilizamos um **dicionário (dict)** para armazenar valores já calculados. Dessa forma, se um valor já foi computado anteriormente, ele é recuperado diretamente do cache, reduzindo a complexidade do algoritmo.


## 3. Implementação e Uso do Cache

A implementação do cache foi feita utilizando um **dicionário Python** dentro da classe `FibonacciCalculator`.

### Mecanismo de Cache
- **Caso base**: Os valores de \( F(0) \) e \( F(1) \) são armazenados diretamente.
- **Consulta ao cache**: Antes de calcular um valor, verificamos se ele já está armazenado. Caso esteja, ele é retornado imediatamente.
- **Armazenamento de novos valores**: Se o valor ainda não estiver no cache, ele é calculado e armazenado para futuras consultas.

### Benefícios da Memoization
1. **Redução da complexidade temporal**: A solução passa de \( O(2^n) \) (exponencial) para \( O(n) \) (linear), tornando-a viável para valores altos de \( n \).
2. **Menos chamadas recursivas**: O uso do cache reduz drasticamente o número de chamadas recursivas, melhorando a eficiência do programa.


## 4. Conclusão
A implementação utilizando memoization mostrou-se extremamente eficaz para otimizar o cálculo da sequência de Fibonacci. O uso de cache eliminou recalculos desnecessários, reduzindo significativamente o tempo de execução. A interface criada permitiu ao usuário visualizar quais valores foram recuperados do cache e quais foram calculados do zero, demonstrando na prática os benefícios da memoization.

## OBS:

Para rodar o programa é necessário seguir os seguintes passos:

1º - Instalar o pacote Flask

``` python 
pip install flask 
```

2º - Rodar o programa com o comando abaixo:

```python
python app.py
```