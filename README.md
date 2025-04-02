# memoization-dynamic-programming

## Relatório da tarefa está apresentado no arquivo `report.md`


## Problema que use Memoization (Programação dinâmica)

**Vence:** 22 de abril de 2025 às 23:59

**Instruções:**

Segue abaixo a proposta de atividade formatada, permitindo que cada equipe escolha um dos 10 problemas listados para implementar uma solução recursiva com memoization. A atividade está estruturada de forma a orientar os alunos quanto aos requisitos e à forma de apresentação.

**Descrição da Atividade:**

Em equipe, escolha **um** dos problemas listados abaixo (pode ser que sua equipe já tenha um problema atribuído) e implemente uma solução utilizando **recursividade** com **memoization** (programação dinâmica). A ideia é resolver o problema de forma a otimizar a performance, armazenando os resultados das chamadas recursivas anteriores em um cache implementado com uma hashtable (ou equivalente), garantindo acesso em tempo O(1). Ao final, a equipe deverá apresentar a solução implementada e explicar o funcionamento do algoritmo.

**Problemas Disponíveis para Escolha:**

* **Fibonacci com Recursão Otimizada:** (Gabriel Costa)
    * Calcular o n-ésimo número da sequência de Fibonacci, evitando cálculos repetidos.
* **Caminhos em uma Grade (Grid Paths):** (Vitor de Oliveira)
    * Contar quantos caminhos existem do canto superior esquerdo até o inferior direito de uma grade, movendo apenas para baixo ou para a direita.
* **Problema da Mochila (Knapsack Problem):** (Ícaro)
    * Determinar o maior valor que pode ser carregado por uma mochila com capacidade limitada, dado um conjunto de itens com pesos e valores.
* **Subsequência Comum Máxima (Longest Common Subsequence - LCS):** (Roni)
    * Encontrar a maior subsequência comum entre duas sequências (ex.: strings).
* **Edição de Texto (Edit Distance / Levenshtein Distance):** (Marlon)
    * Determinar o número mínimo de operações (inserção, exclusão, substituição) necessárias para transformar uma string em outra.
* **Divisão de Palavras (Word Break):** (Taiga)
    * Verificar se uma string pode ser segmentada em palavras contidas em um dicionário.
* **Partição de Conjunto com Soma Igual (Partition Equal Subset Sum):** (Sabine)
    * Verificar se é possível dividir um conjunto de inteiros em dois subconjuntos com soma igual.
* **Triângulo Mínimo (Minimum Path Sum in Triangle):** (Michael)
    * Encontrar o caminho com a menor soma da parte superior até a base de um triângulo de números.
* **Número de Árvores Binárias de Busca (Unique BSTs):** (Isabela)
    * Dado um número n, contar quantas árvores binárias de busca distintas podem ser construídas com n nós.
* **Palindromic Substrings (Contagem de Substrings Palíndromas):** (Ruan)
    * Dado uma string, contar quantas substrings distintas dentro dela são palíndromas.

**Requisitos da Atividade:**

* **Entrega:** 08/04/25
* **Trabalho em Equipe:** A atividade deve ser realizada em grupo
* **Estratégia:** Utilizar uma abordagem recursiva com memoization (programação dinâmica)
* **Cache de Resultados:**
    * Os resultados das chamadas recursivas devem ser armazenados em um cache.
    * O cache deve ser implementado utilizando uma hashtable (ou estrutura equivalente) para garantir acesso em tempo O(1).
* **Implementação Recursiva:**
    * A solução para o problema escolhido deve ser implementada de forma recursiva.
    * Cada função recursiva deve verificar o cache antes de realizar novos cálculos, evitando repetições.
* **Bibliotecas ou Classes para Implementação de Hashtable (Exemplos):**
    * Python: `dict`
    * Ruby: `Hash`
    * Go: `map`
    * Rust: `HashMap` (em `std::collections`)
    * C#: `Dictionary<TKey, TValue>`
    * Java: `HashMap<K, V>`

**Entrega e Apresentação:**

A equipe deverá entregar o código fonte (sem necessidade de incluir exemplos detalhados do código na descrição da atividade) e preparar uma breve apresentação explicando:

* A escolha do problema;
* A estratégia de resolução utilizando recursividade e memoization;
* Como o cache foi implementado e utilizado para otimizar o algoritmo.