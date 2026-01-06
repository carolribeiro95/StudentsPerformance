1 - Existe relação entre o gênero e a nota nas disciplinas?
Fazer um teste t para verificar diferença entre as médias de mulheres e homens.

2- Existe relação entre os grupos étnicos e o nível de formação dos pais?
Fazer um teste qui² para verificar associação entre os grupos e o nível de formação.

3 - Alunos que completaram o teste de preparação apresentaram maior média nas disciplinas?
Fazer um test t para verificar se há diferença estatística das médias das notas entre os grupos que fizeram a preparação e aqueles que  não fizeram.

4 - Existe relação entre as notas das disciplinas? Alunos que foram melhores em "reading" também foram em "writing"?
Fazer uma matriz de correlação de Pearson/Spearman para verificar associação entre as notas.

5 - Existe alguma relação entre alunos que possuem almoço gratuito com a média das notas?
Verificar através de um test t se há diferença estatística entre as médias das notas do alunos entre os grupos que possuem almoço gratuito e daqueles que pagam, ou seja, a renda dos alunos influenciam na média das notas?

6 - Existe alguma relação entre o nível de educação dos pais e a categoria de almoço dos alunos?
Fazer um teste qui² para verificar associação entre o nível de graduação e a categoria de almoço, ou seja, a renda dos pais está relacionada com a escolaridade?

7 - Alunos cujos pais possuem graduação apresentaram maior média de notas?
Fazer ANOVA para verificar se a média dos alunos é estatisticamente diferente de acordo com o nível de escolaridade dos pais.

## Existe relação entre o gênero e a nota nas disciplinas?

```python
# Gráficos boxplots da distribuição das notas por gênero
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='gender', y='math score')
plt.title('Distribuição das notas de matemática por gênero')
plt.show()
```

https://github.com/carolribeiro95/StudentsPerformance/issues/1#issue-3785461768

> Podemos observar nos gráficos boxplots acima que aparentemente a mediana das notas de matemática é maior para o gênero masculino e, em contrapartida, as medianas das notas de leitura e escrita são maiores para o gênero feminino, mas isso é estatisticamente significativo? Para verificar se realmente existe uma diferença entre as médias das notas entre os gêneros é necessário realizar um teste paramétrico de médias, o t de Student.
> 

```python
#%% Média das notas por gênero
df_medias = df.groupby('gender')[['math score','reading score', 'writing score']].mean()
df_medias.plot(kind='bar', figsize=(10,6))
plt.title('Média das notas por gênero')
plt.ylabel('Média das notas')   
plt.show()
```

![image.png](attachment:b0bac92a-7ddb-4610-9ede-70b3a847b6e0:image.png)

![image.png](attachment:73902d72-51bf-4d56-acef-c500a76494f2:image.png)

![image.png](attachment:9a25b56d-92e8-4c4f-b229-46a9b9f9b199:image.png)

![image.png](attachment:e8640c46-c402-4078-b414-72919f87fb98:image.png)

```python
# Médias das notas de matemática por gênero
media_male = df[df['gender'] == 'male']['math score'].mean()
media_female = df[df['gender'] == 'female']['math score'].mean()
print('Média das notas de matemática dos homens: %.2f' % media_male)
print('Média das notas de matemática das mulheres: %.2f' % media_female)
```

![image.png](attachment:535742f0-b4ce-49ef-a7b0-01cda9526699:image.png)

Aparentemente a média das notas de matemática dos homens é maior que a das mulheres, mas essa diferença é estatisticamente significativa?

```python
# %% Test t de Student de amostras independentes
#para avaliar diferença entre as médias das notas por gênero
from scipy import stats
n = len(df)
print('Tamanho da amostra: %d' % n)
# Definindo as hipóteses
# H0: A média das notas de matemática dos homens é igual à das mulheres
# H1: A média das notas de matemática dos homens é maior que a das mulheres
male_math = df[df['gender'] == 'male']['math score']
female_math = df[df['gender'] == 'female']['math score']
stat, p_valor = stats.ttest_ind(male_math, female_math, alternative='greater')

print('Estatística=%.3f, p=%.3f' % (stat, p_valor))
alpha = 0.05
if p_valor < alpha:
    print('Rejeita H0: A média das notas de matemática dos homens é maior que a das mulheres')
else:
    print('Não rejeita H0: Não há evidências suficientes para afirmar que \
     a média das notas de matemática dos homens é maior que a das mulheres')

```

![image.png](attachment:65005e38-5118-4ec4-9f30-184e71827db6:image.png)

***Para um nível de significância de 5% podemos afirmar que a média das notas de matemática dos homens é maior que a das mulheres.***

A média das notas de leitura das mulheres é maior que a médias das notas de leitura dos homens?

![image.png](attachment:2f22da66-ec28-4353-9278-9604dd552490:image.png)

Aparentemente a média das notas de leitura das mulheres é maior que a dos homens, mas essa diferença é estatisticamente significativa?

```python
# Definindo as hipóteses
# H0: A média das notas de leitura dos homens é igual à das mulheres
# H1: A média das notas de leitura das mulheres é maior que a dos homens
male_read = df[df['gender'] == 'male']['reading score']
female_read = df[df['gender'] == 'female']['reading score']
stat, p_valor = stats.ttest_ind(female_read, male_read, alternative='greater')
print('Estatística=%.3f, p=%.3f' % (stat, p_valor))
alpha = 0.05
if p_valor < alpha:
    print('Rejeita H0: A média das notas de leitura das mulheres é maior que a dos homens')
else:
    print('Não rejeita H0: Não há evidências suficientes para afirmar que a média \
          das notas de leitura das mulheres é maior que a dos homens')
```

![image.png](attachment:1d563f42-9c73-4a32-9aa8-baa968f7a7d9:image.png)

***Podemos afirmar então que, para um nível de significância de 5%, existe sim diferença na média das notas de leitura das mulheres, sendo maior que a média das notas de leitura dos homens.***

---

## Existe relação entre as notas das disciplinas? Alunos que foram melhores em "reading" também foram em "writting"?

### Matriz de correlação de Pearson

![image.png](attachment:c36bf335-103a-4d9e-8273-bd7aa22ce2ed:image.png)

> Observe que existe uma forte correlação positiva entre “writing” e “reading”, de 0.95. Isso é um forte indício que quanto maior a nota em “writing”, maior será a nota em “reading” e vice-versa.
> 

### Matriz de correlação de Spearman

Como os dados não seguem uma distribuição normal, a correlação de Spearman é mais confiável

![image.png](attachment:a560cbd9-6fd9-4405-9657-ba77c02d3b30:image.png)

Podemos observar que de fato há uma correlação alta e positiva entre as notas “writing” e “reading”, de 0.948.

> Resposta: Existe, portanto, relação entre as notas das disciplinas de escrita e leitura. Alunos que vão bem em leitura, tendem a tirar notas altas também em escrita, apresentando uma correlação positiva alta entre as duas disciplinas com base nas matrizes de correlação abaixo.
> 

## Existe alguma relação entre alunos que possuem almoço gratuito com a média das notas?

```python
almoco = df['lunch']
almoco
```

![image.png](attachment:ce196159-6ee1-4289-9050-621fd113447a:image.png)

```python
standard_lunch = df[df['lunch'] == 'standard']['media score']
print(f'Média das notas dos alunos com almoço padrão: {standard_lunch.mean():.2f}')
free_lunch = df[df['lunch'] == 'free/reduced']['media score']
print(f'Média das notas dos alunos com almoço gratuito: {free_lunch.mean():.2f}')
```

![image.png](attachment:094428a5-9991-4558-8e43-fd97388b8e68:image.png)

A média das notas dos alunos com almoço padrão aparenta ser maior que a média das notas dos alnos com almoço gratuito, mas vamos verificar se existe diferença estatisticamente significativa entre as médias.

Teste estatístico t para amostras independentes

```python
from scipy import stats
stat, p_valor = stats.ttest_ind(standard_lunch, free_lunch, alternative='greater')
print('Estatística=%.3f, p=%.3f' % (stat, p_valor))
alpha = 0.05
if p_valor < alpha:
    print('Rejeita H0: A média das notas dos alunos com almoço padrão é maior \
    que a dos alunos com almoço gratuito')
else:
    print('Não rejeita H0: Não há evidências suficientes para afirmar que a média \
          das notas dos alunos com almoço padrão é maior que a dos alunos com almoço gratuito')
```

![image.png](attachment:edb5810b-10af-444d-9331-05cf74e294ed:image.png)

Com base no teste t, podemos afirmar com um nível de significância de 5% que alunos com almoço padrão possuem média maior que alunos com almoço gratuito, ou seja, a renda dos alunos influencia na média das notas.

---

## Alunos que completaram o teste de preparação apresentaram maior média nas disciplinas?

```python
media_teste_completed = df[df['test preparation course'] == 'completed']['media score']
print(f'Média das notas dos alunos que completaram o curso de preparação: {media_teste_completed.mean():.2f}')
media_teste_none = df[df['test preparation course'] == 'none']['media score']   
print(f'Média das notas dos alunos que não completaram o curso de preparação: {media_teste_none.mean():.2f}')
```

![image.png](attachment:971c31d7-0041-4905-81e1-d2e9bbfef47e:image.png)

Podemos observar que a média das notas dos alunos que completaram o curso de preparação para o teste é maior que a média dos alunos que não completaram, porém vamos verificar se de fato essa diferença é estatisticamente significativa para um nível de confiança de 95%

```python
from scipy import stats
stat, p_valor = stats.ttest_ind(media_teste_completed, media_teste_none, alternative='greater')
print('Estatística=%.3f, p=%.3f' % (stat, p_valor))
alpha = 0.05    
if p_valor < alpha:
    print('Rejeita H0: A média das notas dos alunos que completaram o curso de preparação\
           é maior que a dos alunos que não completaram')
else:
    print('Não rejeita H0: Não há evidências suficientes para afirmar que a média \
          das notas dos alunos que completaram o curso de preparação é maior que a dos alunos que não completaram')
```

![image.png](attachment:4adf1b4c-bf60-4f22-ac23-2be244a0bf45:image.png)

Para um nível de confiança de 95% podemos afirmar que a média dos alunos que completaram o curso de preparação para o teste é maior que daqueles que não completaram.

---

## Existe relação entre os grupos étnicos e o nível de formação dos pais?

Estratégia - ANACOR (Análise de Correspondência)

1. Análise da significância estatística da associação entre as variáveis e suas
categorias por meio do teste qui-quadrado (χ2).
    
    Tabela de contingência
    
    ```python
    from scipy.stats import chi2_contingency
    contingency_table = pd.crosstab(df['race/ethnicity'], df['parental level of education'])
    contingency_table
    ```
    
    ![image.png](attachment:dd7e1e22-943f-4b42-9607-c6b58cb76c0f:image.png)
    
    Estatística Qui²
    
    ```python
    tab = chi2_contingency(contingency_table)
    
    print("Race/ethnicity x Parental level of education")
    print(f"Estatística qui²: {round(tab[0], 2)}")
    print(f"p-valor da estatística: {round(tab[1], 4)}")
    print(f"graus de liberdade: {tab[2]}")
    ```
    
    ![image.png](attachment:350c4190-ee2a-43ee-93ec-fa0167955ac6:image.png)
    
    Para um nível de significância de 5%, como p-valor > 0.05, não rejeitamos H0 e portanto as variáveis se relacionam de forma aleatória e não faz sentido prosseguir com ANACOR.
    
    Os grupos étnicos não possuem relação com o grau de escolaridade dos pais.
    

---

## Existe alguma relação entre o nível de educação dos pais e a categoria de almoço dos alunos?

```python
contingency_table2 = pd.crosstab(df['parental level of education'], df['lunch'])
contingency_table2

tab_2 = chi2_contingency(contingency_table2)
print("Parental level of education x Lunch")
print(f"Estatística qui²: {round(tab_2[0], 2)}")
print(f"p-valor da estatística: {round(tab_2[1], 4)}")
print(f"graus de liberdade: {tab_2[2]}")
```

![image.png](attachment:bc864580-4c22-459d-b8d3-8f73b9a82302:image.png)

Para um nível de significância de 5%, como p-valor > 0.05, então aceitamos H0 e, portanto, o nível de escolaridade dos pais não se relaciona com o tipo de “Lunch”, ou seja, a renda.

---

## Alunos cujos pais possuem graduação apresentaram maior média de notas?

![image.png](attachment:e16d37d6-1294-4e08-8af0-9c398ec970c9:image.png)

```python
# Teste ANOVA one-way
from scipy.stats import f_oneway
grupo1 = df[df['parental level of education'] == "bachelor's degree"]['media score']
grupo2 = df[df['parental level of education'] == "some college"]['media score']
grupo3 = df[df['parental level of education'] == "master's degree"]['media score']
grupo4 = df[df['parental level of education'] == "associate's degree"]['media score']
grupo5 = df[df['parental level of education'] == "high school"]['media score']
grupo6 = df[df['parental level of education'] == "some high school"]['media score']
stat, p_valor = f_oneway(grupo1, grupo2, grupo3, grupo4, grupo5, grupo6)
print('Estatística=%.3f, p=%.3f' % (stat, p_valor))
alpha = 0.05
if p_valor < alpha:
    print('Rejeita H0: Pelo menos um dos grupos apresenta média diferente dos outros')  
else:
    print('Não rejeita H0: Não há evidências suficientes para afirmar que as médias dos grupos são diferentes')

# Teste post-hoc Tukey HSD
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=df['media score'],
                          groups=df['parental level of education'],
                          alpha=0.05)
print(tukey.summary())
```

| **Termo Original** | **Tradução Sugerida** | **Nível de Escolaridade** |
| --- | --- | --- |
| **Some High School** | Ensino Médio Incompleto | Básico |
| **High School** | Ensino Médio Completo | Médio |
| **Some College** | Ensino Superior Incompleto | Superior |
| **Associate's Degree** | Tecnólogo / Graduação Curta | Superior |
| **Bachelor's Degree** | Graduação (Bacharelado) | Superior |
| **Master's Degree** | Mestrado | Pós-graduação |

![image.png](attachment:7a724735-f6ef-4155-b5b5-e8411a71804c:image.png)

- Resultados:
    - A média dos alunos cujos pais possuem associate’s degree são maiores do que “high school” e “some high school”.
        - Como o `meandiff` é negativo (-6.47 e -4.46) na ordem em que os grupos aparecem (Associate's sendo o grupo 1), isso confirma que a média do "Associate's Degree" é significativamente **maior**.
    - A média dos alunos cujos pais possuem “bachelor’s degree” são maiores que “high school” e “some high school”
    - A média dos alunos cujos pais possuem “master’s degree” são maiores que “high school” e “some high school”
    - A média dos alunos cujos pais possuem “some college” foram maiores que “high school”

Embora existam pequenas diferenças numéricas entre as médias dos grupos de ensino superior, elas não são grandes o suficiente para serem consideradas estatisticamente diferentes. Para o  estudo, o grande divisor de águas na performance dos alunos parece ser se os pais possuem algum nível de ensino superior versus apenas o ensino médio.
