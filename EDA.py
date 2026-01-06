# %% Importando bibliotecas
 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   
import numpy as np
import os

#%% Importando o dataset

df = pd.read_csv('StudentsPerformance.csv')
df.head()
df.columns
df.shape


# %% Verificar se tem valores nulos

df.info()

# %%
df.describe()
# %%
# Existe correlação entre as notas?
# Correlação de Pearson

df[['math score','reading score', 'writing score']].corr()

# Correlação de Spearman
df[['math score','reading score', 'writing score']].corr(method='spearman')


# %% Gráfico Boxplot 
# Existe relação entre o gênero e a nota nas disciplinas?
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='gender', y='math score')
plt.title('Distribuição das notas de matemática por gênero')
plt.show()
# %%
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='gender', y='writing score')
plt.title('Distribuição das notas de escrita por gênero')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='gender', y='reading score')
plt.title('Distribuição das notas de leitura por gênero')
plt.show()

#%% Histograma das notas por gênero
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='math score', hue='gender', kde=True, bins=20)
plt.title('Distribuição das notas de matemática por gênero')
plt.show()
# %% Histograma das notas de leitura por gênero
plt.figure(figsize=(10,6))  
sns.histplot(data=df, x='reading score', hue='gender', kde=True, bins=20)
plt.title('Distribuição das notas de leitura por gênero')
plt.show()
# %% Histograma das notas de escrita por gênero
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='writing score', hue='gender', kde=True, bins=20)
plt.title('Distribuição das notas de escrita por gênero')
plt.show()

#%% Média das notas por gênero
df_medias = df.groupby('gender')[['math score','reading score', 'writing score']].mean()
df_medias.plot(kind='bar', figsize=(10,6))
plt.title('Média das notas por gênero')
plt.ylabel('Média das notas')   
plt.show()

#%% Verificar a normalidade dos dados de notas de matemática
from scipy.stats import shapiro
significancia = 0.05
confianca = 1 - significancia
# Teste de Shapiro-Wilk para normalidade
stat, p = shapiro(df['math score'])
print('Estatística=%.3f, p=%.3f' % (stat, p))
if p > significancia:
    print('A amostra segue uma distribuição normal (não rejeita H0)')
else:
    print('A amostra não segue uma distribuição normal (rejeita H0)')

#%% Verificar a normalidade dos dados de notas de escrita
from scipy.stats import shapiro
significancia = 0.05
confianca = 1 - significancia
# Teste de Shapiro-Wilk para normalidade
stat, p = shapiro(df['writing score'])
print('Estatística=%.3f, p=%.3f' % (stat, p))
if p > significancia:
    print('A amostra segue uma distribuição normal (não rejeita H0)')
else:
    print('A amostra não segue uma distribuição normal (rejeita H0)')
#%% Verificar a normalidade dos dados de notas de leitura

from scipy.stats import shapiro
significancia = 0.05
confianca = 1 - significancia
# Teste de Shapiro-Wilk para normalidade
stat, p = shapiro(df['reading score'])
print('Estatística=%.3f, p=%.3f' % (stat, p))
if p > significancia:
    print('A amostra segue uma distribuição normal (não rejeita H0)')
else:
    print('A amostra não segue uma distribuição normal (rejeita H0)')
# %% Test t de Student para avaliar diferença entre as médias das notas por gênero
from scipy import stats
n = len(df)
print('Tamanho da amostra: %d' % n)
# Médias das notas de matemática por gênero
media_male = df[df['gender'] == 'male']['math score'].mean()
media_female = df[df['gender'] == 'female']['math score'].mean()
print('Média das notas de matemática dos homens: %.2f' % media_male)
print('Média das notas de matemática das mulheres: %.2f' % media_female)

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
    print('Não rejeita H0: Não há evidências suficientes para afirmar que a média \
          das notas de matemática dos homens é maior que a das mulheres')

# %% Test t de Student para avaliar diferença entre as médias das notas por gênero
from scipy import stats
n = len(df)
print('Tamanho da amostra: %d' % n)
# Médias das notas de leitura por gênero
media_male = df[df['gender'] == 'male']['reading score'].mean()
media_female = df[df['gender'] == 'female']['reading score'].mean()
print('Média das notas de leitura dos homens: %.2f' % media_male)
print('Média das notas de leitura das mulheres: %.2f' % media_female)
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
    
#%% Existe alguma relação entre alunos que possuem almoço gratuito com a média das notas?
almoco = df['lunch']
almoco

# Cálculo da média das notas
df['media score'] = round(df[['math score','reading score', 'writing score']].mean(axis=1), 2)
df

standard_lunch = df[df['lunch'] == 'standard']['media score']
print(f'Média das notas dos alunos com almoço padrão: {standard_lunch.mean():.2f}')
free_lunch = df[df['lunch'] == 'free/reduced']['media score']
print(f'Média das notas dos alunos com almoço gratuito: {free_lunch.mean():.2f}')
stat, p_valor = stats.ttest_ind(standard_lunch, free_lunch, alternative='greater')
print('Estatística=%.3f, p=%.3f' % (stat, p_valor))
alpha = 0.05
if p_valor < alpha:
    print('Rejeita H0: A média das notas dos alunos com almoço padrão é/\n maior que a dos alunos com almoço gratuito')
else:
    print('Não rejeita H0: Não há evidências suficientes para afirmar que a média \
          das notas dos alunos com almoço padrão é maior que a dos alunos com almoço gratuito')
    
# %%
# Alunos que completaram o teste de preparação apresentaram maior média nas disciplinas?
teste_prep = df['test preparation course']
teste_prep

media_teste_completed = df[df['test preparation course'] == 'completed']['media score']
print(f'Média das notas dos alunos que completaram o curso de preparação: {media_teste_completed.mean():.2f}')
media_teste_none = df[df['test preparation course'] == 'none']['media score']   
print(f'Média das notas dos alunos que não completaram o curso de preparação: {media_teste_none.mean():.2f}')
stat, p_valor = stats.ttest_ind(media_teste_completed, media_teste_none, alternative='greater')
print('Estatística=%.3f, p=%.3f' % (stat, p_valor))
alpha = 0.05    
if p_valor < alpha:
    print('Rejeita H0: A média das notas dos alunos que completaram o curso de preparação\né maior que a dos alunos que não completaram')
else:
    print('Não rejeita H0: Não há evidências suficientes para afirmar que a média\n das notas dos alunos que completaram o curso de preparação é maior que a dos alunos que não completaram')

#%% Relação entre a renda dos pais e a conclusão do curso de preparação para o teste com base no lunch
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='lunch', hue='test preparation course')
plt.title('Relação entre o tipo de almoço e a conclusão do curso de preparação para o teste')
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(data=df, x='lunch')
plt.title('Contagem de alunos por tipo de almoço')
plt.show()

#%% Existe relação entre os grupos étnicos e o nível de formação dos pais?
# Teste qui-quadrado de independência
from scipy.stats import chi2_contingency
contingency_table = pd.crosstab(df['race/ethnicity'], df['parental level of education'])
contingency_table
# %%
# Realizando o teste qui-quadrado
tab = chi2_contingency(contingency_table)

print("Race/ethnicity x Parental level of education")
print(f"Estatística qui²: {round(tab[0], 2)}")
print(f"p-valor da estatística: {round(tab[1], 4)}")
print(f"graus de liberdade: {tab[2]}")

#%% Existe alguma relação entre o nível de educação dos pais 
# e a categoria de almoço dos alunos?

contingency_table2 = pd.crosstab(df['parental level of education'], df['lunch'])
contingency_table2

tab_2 = chi2_contingency(contingency_table2)
print("Parental level of education x Lunch")
print(f"Estatística qui²: {round(tab_2[0], 2)}")
print(f"p-valor da estatística: {round(tab_2[1], 4)}")
print(f"graus de liberdade: {tab_2[2]}")

#%% Alunos cujos pais possuem graduação apresentaram maior média de notas?
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

 
#%% Gráfico de barras da média das notas por nível de educação dos pais
df_medias_educ = df.groupby('parental level of education')['media score'].mean().sort_values()
df_medias_educ.plot(kind='bar', figsize=(10,6))
plt.title('Média das notas por nível de educação dos pais')
plt.ylabel('Média das notas')
plt.show()
