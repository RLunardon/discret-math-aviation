# Discret Math Aviation
Códigos Python utilizados no trabalho de Discreta/Aviação.

## APLICAÇÃO DE TEORIA DOS GRAFOS EM ROTAS AÉREAS

## VISÃO GERAL

Este repositório contém o código-fonte e o documento final do projeto acadêmico que modela a malha aérea brasileira como um grafo. O objetivo é aplicar algoritmos da Teoria dos Grafos para analisar a conectividade, eficiência e vulnerabilidade da rede de rotas aéreas para então otimizar os trajetos.

## SOBRE O PROJETO

O trabalho aborda o complexo problema de otimização de rotas aeronáuticas, que vai além da simples distância percorrida. O objetivo central é modelar uma rede de rotas aéreas nacionais para determinar o trajeto mais eficiente, considerando diversos fatores de custo operacional.

## COMPLEXIDADE DOS ALGORITIMOS

A complexidade temporal dos algoritmos de menor caminho (Dijkstra, Floyd-Warshall e A*) é determinada pela maneira como eles iteram sobre os vértices ($|V|$) e as arestas ($|E|$) de um grafo para garantir que encontraram o caminho ótimo.

## 1. Algoritmo de Dijkstra:

O algoritmo de Dijkstra resolve o problema do menor caminho de fonte única em grafos com pesos não negativos. Sua complexidade mais eficiente é $O((|V| + |E|) \log |V|)$ (usando um heap binário) e, teoricamente, pode ser $O(|E| + |V| \log |V|)$ (usando um heap de Fibonacci).

~> A complexidade é dominada pelo uso da fila de prioridade (Priority Queue). O algoritmo visita cada um dos $|V|$ vértices uma vez, extraindo-o da fila (custo $O(\log |V|)$ ). Além disso, ele inspeciona cada uma das $|E|$ arestas, o que pode levar a uma atualização na fila (também $O(\log |V|)$ ). O custo final é a soma desses fatores: o custo de processar todos os vértices e o custo de processar todas as arestas.

## 2. Algoritmo de Floyd-Warshall:

O algoritmo de Floyd-Warshall resolve o problema do menor caminho entre todos os pares de vértices (All-Pairs Shortest Path) e pode lidar com pesos negativos. Sua complexidade é fixa em $O(|V|^3)$.

~> A complexidade cúbica é direta, resultado da sua abordagem de programação dinâmica. O algoritmo é estruturado em três laços aninhados:

O laço externo itera sobre cada vértice ($|V|$), usando-o como um possível vértice intermediário ($k$).

Os dois laços internos iteram sobre todos os pares de vértices de origem ($i$) e destino ($j$).Como o passo de comparação e atualização dentro do loop mais interno é executado $|V| \times |V| \times |V|$ vezes, o custo é invariavelmente $O(|V|^3)$.

## 3. Algoritmo A* (A-estrela):

O A* resolve o problema do menor caminho de fonte única para destino único e é uma versão otimizada do Dijkstra, pois usa uma função heurística ($h$) para guiar a busca em direção ao destino.

~> No pior cenário (onde a heurística é ineficaz), o A* visita a mesma quantidade de nós que o Dijkstra e, portanto, sua complexidade degenera para a de Dijkstra: $O((|V| + |E|) \log |V|)$.

~> Na prática, quando a heurística é admissível (nunca superestima o custo real), o A* explora apenas uma fração do grafo. Nesses casos, o desempenho é dramaticamente melhor do que o Dijkstra. No entanto, sua complexidade teórica não pode ser garantida como menor que $O((|V| + |E|) \log |V|)$ porque depende de uma informação externa (a heurística) à estrutura do grafo em si.

## TECNOLOGIAS
Linguagem: Python
Biblioteca Principal: sys, itertools, heapq e math
Documentação: LaTeX

## COMO USAR
Após clonar o repositório e instalar as dependências, altere os valores e pesos dos vertices e arestas dentro do codigo

## DOCUMENTAÇÃO
O trabalho completo detalhando a metodologia e os resultados está disponível em PDF na pasta docs/.
Visualizar o Documento Final: docs/Trabalho_Matemática_Discreta.pdf

## AUTOR
Ramon Lunardon (FGV)
