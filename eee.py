#!/usr/bin/env python
# coding: utf-8

# Привет! Меня зовут Исмаилов Исмаил, я буду проверять твой проект :) Можешь обращаться ко мне на «ты». Если тебе комфортно, то и я буду к тебе так обращаться, если нет, то обязательно скажи об этом.
# 
# Пожалуйста, не удаляй мои комментарии, которые я буду оставлять в работе. Это особенно поможет, если твои проекты будут отправлены на повторную проверку. При повторных проверках у комментариев будут приписки: "Вторая итерация", "Третья итерация" и т.д. 
# 
# Ты тоже можешь реагировать на мои комментарии, но в таком случае постарайся, чтобы твои комментарии отличались от моих: например, выделяй их своим любимым цветом — так у нас не возникнет путаницы :)
# 
# Кстати, про цвета! Мои комментарии будут в следующей цветовой гамме: зелеными, желтыми и красными. Например:
# 
# <div class="alert-success"> 
# <b>Комментарий ревьюера 👍 </b>
#     
# В случае, если решение на отдельном шаге является полностью правильным. </div>
# 
# <div class="alert-warning"> 
# <b>Комментарий ревьюера 💡</b> 
#     
# В случае, если решение может стать еще лучше с некоторыми корректировками </div>
#  
# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌</b> 
#     
# В случае, если решение какого-то шага требует значительных изменений. Проект не может быть принят с первого раза, если ревью содержит комментарии, помеченные этим цветом </div>

#    
# <div class="alert alert-info">
# <center> Привет! Исмаил, оченнь приятно. Благодарю хорошего дня! </center> 
#     
# 
# </div>
# 

#    
# <div class="alert alert-info">
# <center> Сборный проект№1 </center> 
#     
# 
# </div>
# 

# <div class="alert alert-info">
# <b> У нас есть данный  о продажах игр, оценки пользователей и экспертов, жанры и платформы (например, Xbox или PlayStation). Нам нужно выявить определяющие успешность игры закономерности. Это позволит сделать ставку на потенциально популярный продукт и спланировать рекламные кампании.
# <br>Данные до 2016 года. Представим, что сейчас декабрь 2016 г., и мы планируем кампанию на 2017-й.</br>
#     
# В наборе данных попадается аббревиатура ESRB (Entertainment Software Rating Board) — это ассоциация, определяющая возрастной рейтинг компьютерных игр. ESRB оценивает игровой контент и присваивает ему подходящую возрастную категорию, например, «Для взрослых», «Для детей младшего возраста» или «Для подростков».
# </b> 
# <center> Цели: </center> 
# <br>  1. Открыть файл с данными и изучить общую информацию</br> 
# <br>  2. Подготовка данные</br>
# <br>  3. Исследовательский анализ данных</br>
# <br>  4. Портрет пользователя каждого региона</br> 
# <br>  5. Проверка гипотезы</br>
# <br>  6. Общий вывод</br>
# <center> Описание данных: </center> 
# 
# <br>Name — название игры</br> 
# <br> Platform — платформа</br> 
# <br> Year_of_Release — год выпуска</br> 
# <br> Genre — жанр игры</br> 
# <br> NA_sales — продажи в Северной Америке (миллионы проданных копий)</br> 
# <br> EU_sales — продажи в Европе (миллионы проданных копий)</br>  
# <br> JP_sales — продажи в Японии (миллионы проданных копий)</br> 
# <br> Other_sales — продажи в других странах (миллионы проданных копий)</br> 
# <br> Critic_Score — оценка критиков (максимум 100)</br> 
# <br> User_Score — оценка пользователей (максимум 10)</br> 
# <br> Rating — рейтинг от организации ESRB (англ. Entertainment Software Rating Board). Эта ассоциация определяет рейтинг  компьютерных игр и присваивает им подходящую возрастную категорию.</br> 
# 
# 
# </div>

# <div class="alert-success"> 
# <b>Комментарий ревьюера 👍 Вторая итерация </b>
# 
# Теперь здорово, что вступление есть

# In[1]:


import pandas as pd
from scipy import stats as st
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import math
data = pd.read_csv('/datasets/games.csv')


# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌</b> 
#     
# Нет необходимого вступления в проект: нужно рассказать, что за данные у тебя имеются, что вообще стоит делать, какие цели и задачи, что желаешь получить. Представь, что показываешь проект бизнесу / заказчику: заказчик не поймет даже, где оказался, потому что в проекте нет и названия, поэтому нужно стороннего читателя вводить в курс дела </div>

# <div class="alert alert-info">
#     
# <b> Откроем csv файл и подгрузим библиотеки с которыми будем работать по ходу проекта</b> 
# </div>

# In[2]:


data.info()


# <div class="alert alert-info">
# <b> Заменим названия столбцом</b> 
# </div>

# In[3]:


data.columns = map(str.lower, data.columns)
#data.rename(columns={'Name':'name', 'Platform': 'platform', 'Year_of_Release':'year_of_release', 'Genre':'genre', 'NA_sales':'na_sales', 'EU_sales':'eu_sales', 'JP_sales':'jp_sales', 'Other_sales':'other_sales', 'Critic_Score':'critic_score', 'User_Score':'user_score', 'Rating':'rating' }, inplace=True)


# <div class="alert-warning"> 
# <b>Комментарий ревьюера 💡</b> 
#     
# А если бы у тебя было сотни столбиков (что вполне возможно), то вручную писать совсем неоптимально. Это долго, повышает шанс ошибки и в целом - зачем писать самому, если есть Питон? Используй .str.lower

# In[4]:


data.isna().sum()


# <div class="alert alert-info">
# <b> в name 2 пропуска, их просто удалим чтобы не мешали. На общую картину это не повлияет. Заменит тип данных в year_of_release на интерджер(смысл года в флоат оставлять не вижу) для это нужно убрать пропусти.  Заменим их медианным значением, чтобы не терять часть данных в какие года что выходило
#     
#     Так же заполним  пропуски в data['name'] и genre на пустые значения</b> 
# </div>

# In[17]:


data['year_of_release'] = data['year_of_release'].fillna(0).astype(int)
data['name']= data['name'].fillna("")
data['genre']= data['genre'].fillna("")


# <div class="alert-warning"> 
# <b>Комментарий ревьюера 💡 </b>
# 
# Разве год выпуска отдельной взятой игры как-то зависит от медианы?

# <div class="alert alert-info">
# <b> Округлим данные по продажам и переведем их в интеджер, смысла от флоат тут не вижу, да и не понимаю(0.5 продажи это как вообще? хех)
#     
# Заменим tbd на 0(это значит что человек еще не поставил оценку, а только собирался. Значит этих данных нет, чтобы они нам не мешали заменим их 0м) тоже самое можно сказать и о пропусках в user_score, далее все расчеты и графики будем стоить от 1 и выше чтобы не путать данные) тоже самое сделаем с пропусками в rating и critic_score
#     
#     
# user_score  заполним пропуски нулями чтобы не терять часть данных и при этом можно было бы перевести их в интеджер
#     
# так же замени пропуски в rating на unknown чтобы видеть в каких регионах рейтинг не ставят и покупают без него
# </b> 
# </div>

# In[18]:


data['na_sales'] = data['na_sales'].round().astype(int)
data['eu_sales'] = data['eu_sales'].round().astype(int)
data['jp_sales'] = data['jp_sales'].round().astype(int)
data['other_sales'] = data['other_sales'].round().astype(int)

data['user_score'] = data['user_score'].replace(["tbd", "0"], '0', regex=True)
data['user_score'] = data['user_score'].fillna(0)
data['user_score'] = pd.to_numeric(data['user_score'])
data['user_score'] = data['user_score'].round().astype(int)
print(data['user_score'].unique())

data['rating'] = data['rating'].fillna('unknown')


# <div class="alert-success"> 
# <b>Комментарий ревьюера 👍 </b>
# 
# Верное решение обработать tbd, как nan

# In[19]:


data.info()


# <div class="alert alert-info">
# <b> Создадим и посчитаем продажи в новом столбце
#    </b> 
# </div>

# In[20]:


data['all_sales'] = data['na_sales']+data['eu_sales']+data['jp_sales']+data['other_sales']
print(data['all_sales'].head(10))


# <div class="alert-success"> 
# <b>Комментарий ревьюера 👍 </b>
#     
# Более изящная конструкция 
# 
# data[['na_sales','eu_sales','jp_sales', 'other_sales']].sum(axis = 1)

# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌</b>
# 
# Не выполнен пункт: "Опишите причины, которые могли привести к пропускам".

# <div class="alert alert-info">
# <b> посмотреть количество выпускаемых игр по годам мы не можем, нет данных будем считать что количество продаж соответвует количесву выпущен игр. Cтроим график всех продаж по годам. Лидерами являются 2007 и 2008 год

# In[21]:




data_saint = data.groupby('year_of_release')['all_sales'].sum().sort_values(ascending=False)

data_saint.plot(x='year_of_release', y='all_sales',  figsize=(12,5), kind='bar', grid=True, title='График продаж по годам');
plt.show()


# <div class="alert-warning"> 
# <b>Комментарий ревьюера 💡</b> 
# 
# Не забывай подписывать графики, это важно

# <div class="alert alert-info">
# <b> Смотрим, как менялись продажи по платформам.  
#    </b> 
# </div>

# In[22]:



data_top = data.pivot_table(index = 'platform', values = 'all_sales',  aggfunc=['sum']).reset_index(level='platform')
data_top.columns = ['платформа', 'всего продаж']
data_topp = data_top.sort_values(by='всего продаж', ascending=False)
print(data_topp.head(10))

#data_PS2 = data[data['platform'] == "PS2"]
#data_PS2['year_of_release'].hist(figsize=(5, 5))


# ,<div class="alert alert-info">
# <b> Стоим график топ 5 платформ исходя из обьема продаж. Пики их продаж в среднем 3-5 лет, но все стремятся к нулю после 2015, продаж уже почти не было. Скорее всего это связанно с тем, что было новая платформа которая забрала всех клиентов
#    </b> 
# </div>

# In[36]:


top_5_pl = ['PS2', 'X360', 'Wii', 'PS3', 'DS']
data_query = data.query('year_of_release >= 2000')
fig, ax = plt.subplots(1, 1, figsize = (18,5))

for top_5_pl in top_5_pl:
    data_pl = data_query[data_query['platform'] == top_5_pl]
    data_group = data_pl.groupby('year_of_release')['all_sales'].sum().reset_index()
    data_group.columns = ['year_of_release', 'sum']
    x =  data_group['year_of_release']
    y =  data_group['sum'] 
    ax.plot(x,y,   marker =".", label = top_5_pl)
plt.legend()
plt.show()
    
    


# In[ ]:



data_eu_sales = ['Action', 'Sports', 'Shooter', 'Racing', 'Platform']
data_query = data.query('year_of_release >= 2012')
fig, ax = plt.subplots(1, 1, figsize = (18,5))

for data_eu_sales in data_eu_sales:
    data_pl = data_query[data_query['genre'] == data_eu_sales]
    data_group = data_pl.groupby('year_of_release')['eu_sales'].sum().reset_index()
    data_group.columns = ['year_of_release', 'sum']
    x =  data_group['year_of_release']
    y =  data_group['sum'] 
    ax.plot(x,y,   marker ="*", label = data_eu_sales)
plt.legend()
plt.show()


#   <div class="alert alert-info">
# <b> возьмем данные за актуальный переод с 2012 года будем брать.
#    </b> 
# </div>

# <div class="alert-warning"> 
# <b>Комментарий ревьюера 💡</b> 
# 
#     
# Для целей прогнозирования продаж на следующий год даже в традиционных бизнесах редко берут данные более чем за 2-3 года. А в такой динамично меняющейся индустрии, как компьютерные игры и вовсе не стоит брать слишком большой временной интервал - иначе обязательно захватишь уже отжившие тренды. Но и слишком короткий период тоже брать не стоит.

#   <div class="alert alert-info">
# <b> Учту это
#    </b> 
# </div>

#   <div class="alert alert-info">
# <b> возьмем топ 5 платформ после 2012 года по продажам. Потенцеально прибильные PS4, это хорошо видно на грфике так же х360, рс3, 3DS,  XOne. у всех у них падают продажи и если выбирать среди них самую прибыльную это рс4, но тоже в перспиктиву пары лет, видими все так есть другая платфаорма куда они все уходят. Держу пари это стим или ориджин был))
#    </b> 
# </div>

# In[15]:


data_top = data_query.pivot_table(index = 'platform', values = 'all_sales',  aggfunc=['sum']).reset_index(level='platform')
data_top.columns = ['платформа', 'всего продаж']
data_topp = data_top.sort_values(by='всего продаж', ascending=False)
print(data_topp.head(5))


#   <div class="alert alert-info">
# <b> постоим ящик с усами. убедимся в наших топ 5
#    </b> 
# </div>

# In[16]:


data_query.pivot_table(index='year_of_release', columns='platform', values='all_sales', aggfunc='sum').boxplot()
#sample[0:10].plot.box(title='Plotting boxplot using pandas')


#   <div class="alert alert-info">
# <b> Выберем самую популярную платформу РS4 и и посмотрим как влияют продажи внутри одной популярной платформы отзывы пользователей и критиков. Можно заметить, что продажи и отзывы есть небольшя зависимоть корреляция 0.37 значит что 37 процентов продаж зависили тот отзывов. 
#    
#    </b> 
# </div>

# <div class="alert-success"> 
# <b>Комментарий ревьюера 👍 </b>
#     
# Боксплот построен верно

# In[17]:


#data[['critic_score', 'user_score', 'all_sales']].corr()['all_sales']

#station_stat_multi = data_query.pivot_table(index='name', values=['critic_score', 'user_score', 'all_sales'], aggfunc='mean')
#
#pd.plotting.scatter_matrix(station_stat_multi, figsize=(9, 9))

data_corr = data_query.query('platform == "PS4"')
data_corr = data_corr.query('user_score >= 1')

station_stat_multi = data_corr.pivot_table(index='name', values=['critic_score', 'user_score', 'all_sales'], aggfunc='median')
print(station_stat_multi.corr())
pd.plotting.scatter_matrix(station_stat_multi, figsize=(9, 9))


#   <div class="alert alert-info">
# <b> Постоим подобные графики и выявление корреляции по другим платформам и посмтим на результат. У платформы X360 схожая зависимость коррелиции и отзывов близка к 0.37. Можно сказать, что эта платформа тоже зависит от отзывов.
#    
#    </b> 
# </div>

# In[18]:


data_cor = data_query.query('platform == "X360"')
data_cor = data_cor.query('user_score >= 1')

station_stat_multi = data_cor.pivot_table(index='name', values=['critic_score', 'user_score', 'all_sales'], aggfunc='median')
print(station_stat_multi.corr())
pd.plotting.scatter_matrix(station_stat_multi, figsize=(9, 9))


#   <div class="alert alert-info">
# <b> У платформы PS3 схожая зависимость коррелиции и отзывов близка к 0.37. Можно сказать, что эта платформа тоже зависит от отзывов. Так же наблюдается интересная тенденция к продажам. У лидера зависимость больше. Сейчас мы смотрим топ3 и явно идет спад коррелиции, можно сказать, что отзывы напрямую зависят от продаж
#    
#    </b> 
# </div>

# In[19]:


data_cor = data_query.query('platform == "PS3"')
data_cor = data_cor.query('user_score >= 1')

station_stat_multi = data_cor.pivot_table(index='name', values=['critic_score', 'user_score', 'all_sales'], aggfunc='median')
print(station_stat_multi.corr())
pd.plotting.scatter_matrix(station_stat_multi, figsize=(9, 9))


#   <div class="alert alert-info">
# <b> У платформы 3DS схожая зависимость коррелиции и отзывов близка к 0.37. И я бы сказал что эта платформа в будущем может стать номер один по продажам исходя из корреляции по отзывам. В сумме ее корреляция от отзывам 0.42(критиков и пользователей) что является самой большой среди тех которые исследовали. Если выбирать Сриди пратформ какая в будущем вышла бы в топ по продажам можно сказать, что эта платформа была бы лидером.
#    </b> 
# </div>

# In[20]:


data_cor = data_query.query('platform == "3DS"')
data_cor = data_cor.query('user_score >= 1')

station_stat_multi = data_cor.pivot_table(index='name', values=['critic_score', 'user_score', 'all_sales'], aggfunc='median')
print(station_stat_multi.corr())
pd.plotting.scatter_matrix(station_stat_multi, figsize=(9, 9))


# <div class="alert-success"> 
# <b>Комментарий ревьюера 👍 </b>
# 
# Хорошие диаграммы рассеивания. Корреляция тоже подсчитана верно

#   <div class="alert alert-info">
# <b> Самые прибыльный жанр это  shooter. Полсе Платформ и спорт потом все остальные.
#    </b> 
# </div>

# In[21]:


data_genre = data_query.groupby('genre')['all_sales'].mean().sort_values(ascending=False)
data_genre.plot(x='genre', y='all_sales',  figsize=(12,5), kind='bar', grid=True);
plt.show()


# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌</b> 
#     
# Общие продажи - плохая метрика для поиска наиболее прибыльного жанра. За высокими показателями общих продаж может скрываться множество мелких игр с низкими продажами. Или 2-3 звезды и куча провалов. Лучше найти жанр, где игры стабильно приносят высокий доход - для этого стоит рассмотреть средние или медианные продажи

#   <div class="alert alert-info">
# <b>  Составим портрет пользователя каждого региона Самые популярные платформы (топ-5)
#    </b> 
# </div>

#   <div class="alert alert-info">
# <b>  Лидирующая платформа у каждого региона своя. у Северной Америки лидер X360 у Японии  3DS(хотя в Сев. Америке она на 5м месте) в Евпропе же лидер PS4, в Америке он на 2м месте, а в Японии и вовсе отсутсвует.
#    </b> 
# </div>

# In[22]:


data_na_sales = data_query.pivot_table(index = 'platform', values = 'na_sales',  aggfunc=['sum']).reset_index(level='platform')
data_na_sales.columns = ['платформа', 'всего продаж']
data_topp = data_na_sales.sort_values(by='всего продаж', ascending=False)
print(data_topp.head(5))

data_jp_sales = data_query.pivot_table(index = 'platform', values = 'jp_sales',  aggfunc=['sum']).reset_index(level='platform')
data_jp_sales.columns = ['платформа', 'всего продаж']
data_topp = data_jp_sales.sort_values(by='всего продаж', ascending=False)
print(data_topp.head(5))

data_eu_sales = data_query.pivot_table(index = 'platform', values = 'eu_sales',  aggfunc=['sum']).reset_index(level='platform')
data_eu_sales.columns = ['платформа', 'всего продаж']
data_topp = data_eu_sales.sort_values(by='всего продаж', ascending=False)
print(data_topp.head(5))


#   <div class="alert alert-info">
# <b>  В Америке самый популярный жарн шутер, потом Action, в Японии Role-Playing самый популярный. В Евпропе примерно как и в Америке Action потом шутер. Думаж жанры в которые играют в Японии так отличаются от других стан потому что выборка не досточна большая, может у них свои ценности и взгляды на жизнь не знаю)) хотя на втором месте у них так же Action
#    </b> 
# </div>

# In[23]:


data_na_sales = data_query.pivot_table(index = 'genre', values = 'na_sales',  aggfunc=['sum']).reset_index(level='genre')
data_na_sales.columns = ['жанр', 'всего продаж']
data_topp = data_na_sales.sort_values(by='всего продаж', ascending=False)
print(data_topp.head(5))

data_jp_sales = data_query.pivot_table(index = 'genre', values = 'jp_sales',  aggfunc=['sum']).reset_index(level='genre')
data_jp_sales.columns = ['жанр', 'всего продаж']
data_topp = data_jp_sales.sort_values(by='всего продаж', ascending=False)
print(data_topp.head(5))

data_eu_sales = data_query.pivot_table(index = 'genre', values = 'eu_sales',  aggfunc=['sum']).reset_index(level='genre')
data_eu_sales.columns = ['жанр', 'всего продаж']
data_topp = data_eu_sales.sort_values(by='всего продаж', ascending=False)
print(data_topp.head(5))


#   <div class="alert alert-info">
# <b>  График популярный жанров в Японии. зачем не знаю, просто сделал пусть будет))
#    </b> 
# </div>

# In[34]:



data_eu_sales = ['Action', 'Sports', 'Shooter', 'Racing', 'Platform']
data_query = data.query('year_of_release >= 2012')
fig, ax = plt.subplots(1, 1, figsize = (18,5))

for data_eu_sales in data_eu_sales:
    data_pl = data_query[data_query['genre'] == data_eu_sales]
    data_group = data_pl.groupby('year_of_release')['eu_sales'].sum().reset_index()
    data_group.columns = ['year_of_release', 'sum']
    x =  data_group['year_of_release']
    y =  data_group['sum'] 
    ax.plot(x,y,   marker ="*", label = data_eu_sales)
plt.legend()
plt.show()


#   <div class="alert alert-info">
# <b>  Посмотрим как рейтинг влиял на продажи по регионам с помощью круговых диаграм.
# В Америке 44 процента игр это с рейтингом М(для взрослых)
#     
# В Японии этим рейтингом особо не пользовались, а те кто пользовались предпочитали игры с рейтингом Е(для всех) тут сложно судить из-за того что данных мало
# 
# В Европе 44 процента игр это с рейтингом М(для взрослых) совпадение с Америкой. У них много чего свопадает хех
#    </b> 
# </div>

# In[25]:


#data_eu_sales = data_query.pivot_table(index = 'rating', values = 'na_sales',  aggfunc=['sum']).reset_index(level='rating')
#data_eu_sales.columns = ['рейтинг', 'всего продаж']
#data_topp = data_eu_sales.sort_values(by='всего продаж', ascending=False)
#print(data_topp.head(5))

#small_cat_totals = data_eu_sales[data_eu_sales['всего продаж'] < 100]


data_query.groupby(['rating']).sum().plot(
    kind='pie', y='na_sales', autopct='%1.0f%%') 

data_query.groupby(['rating']).sum().plot(
    kind='pie', y='jp_sales', autopct='%1.0f%%', )

data_query.groupby(['rating']).sum().plot(
    kind='pie', y='eu_sales', autopct='%1.0f%%', )


# <div class="alert-success"> 
# <b>Комментарий ревьюера 👍 </b>
#     
# Отлично сделанный пункт. Хорошие графики, верные выводы и, самое главное, не теряется важная информация с пропусками
#     
# Иногда пропуск сам по себе является ценной информацией. Например, нужно держать в уме, для каких стран создавалась система ESRB? Будут ли стараться авторы игр для локального рынка других стран получить рейтинг ESRB?

#   <div class="alert alert-info">
# <b>  Нулевая гипотеза: Средние пользовательские рейтинги платформ Xbox One и PC одинаковые    </b> 
# <br> Альтернативаня гипотеза:Средние пользовательские рейтинги платформ Xbox One и PC  разные </br>
# 
# <br> Так как стоит задача сравнить средние значеия двух независивых совокупностей, для проведния эксперимета будем использовать независимый двухвыброчнй t-критерий, который и предназначен для этого. Так как задача стоит ответить на вопрос о равенстве средних, а не о том, больше ли, или меньше одно из них, альтернативную гипотезу изложим как двухсторонюю.</br>    
#     
#     
# 
# 
# <br>Статистический вывод: на имеющихся данных, на уровне значимости 5% (уровне доверия 95%) есть основания отвергнуть
# нулевую гипотезу в пользу альтернативы.</br>
# <br>Средние пользовательские рейтинги жанров Action и Sports разные</br>
# <br>Проверяем гипотезу строгим математическим правилом — статистическим критерием Стьюдента.</br>
# 
# <br>В результате получаем величину p-value. Она лежит в диапазоне от 0 до 1 и означает вероятность увидеть текущую или более экстремальную разницу между группами при условии верности нулевой гипотезы.</br>
# 
# <br>Значение p-value сравнивается с уровнем значимости 0.05. Если оно больше, принимаем нулевую гипотезу о том, что различий нет, иначе считаем, что между группами есть статистически значимая разница.</br>
# <br>Исходя из обьема данных и выборки с которой мы работает возьмем уровень значимости(доверия) 5%.</br>
# 
# <br>Вывод делается на выборке с 2012 года по 2016 год</br>
# 
# <br>Вывод:Не получилось отвергнуть нулевую гипотезу</br>
# 
# 
# 
# </div>

# In[26]:


#data_eu_sales = data_query.pivot_table(index = 'rating', values = 'jp_sales',  aggfunc=['sum']).reset_index(level='rating')
#data_eu_sales.columns = ['рейтинг', 'всего продаж']
#data_topp = data_eu_sales.sort_values(by='всего продаж', ascending=False)
#print(data_topp.head(5))


# In[27]:


games_clean = data_query.dropna(subset=['user_score'])
xbox_one = games_clean.query('platform == "XOne"')['user_score']
pc = games_clean.query('platform == "pc"')['user_score']

results = st.ttest_ind(xbox_one, pc, equal_var= False)
 
alpha = 0.05

if results.pvalue < alpha:
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")


#   <div class="alert alert-info">
# <b>   
# Так как стоит задача сравнить средние значеия двух независивых совокупностей, для проведния эксперимета будем использовать независимый двухвыброчнй t-критерий, который и предназначен для этого. Так как задача стоит ответить на вопрос о равенстве средних, а не о том, больше ли, или меньше одно из них, альтернативную гипотезу изложим как двухсторонюю.</b>    
#  
# </div>

# <div class="alert-success"> 
# <b>Комментарий ревьюера 👍 Третья итерация </b>
# 
# Да, здорово

#   <div class="alert alert-info">
# <b>  Нулевая гипотеза: Средние пользовательские рейтинги жанров Action и Sports одинаковые 
# <br> Альтернативаня гипотеза:Средние пользовательские рейтинги жанров Action и Sports разные </br>
# 
# <br> Так как стоит задача сравнить средние значеия двух независивых совокупностей, для проведния эксперимета будем использовать независимый двухвыброчнй t-критерий, который и предназначен для этого. Так как задача стоит ответить на вопрос о равенстве средних, а не о том, больше ли, или меньше одно из них, альтернативную гипотезу изложим как двухсторонюю.</br>    
#     
#     
# 
# 
# <br>Статистический вывод: на имеющихся данных, на уровне значимости 5% (уровне доверия 95%) есть основания отвергнуть</br>
# нулевую гипотезу в пользу альтернативы.
# <br>Средние пользовательские рейтинги жанров Action и Sports разные</br>
# 
# <br>Проверяем гипотезу строгим математическим правилом — статистическим критерием Стьюдента.</br>
# 
# <br>В результате получаем величину p-value. Она лежит в диапазоне от 0 до 1 и означает вероятность увидеть текущую или более экстремальную разницу между группами при условии верности нулевой гипотезы.</br>
# 
# <br>Значение p-value сравнивается с уровнем значимости 0.05. Если оно больше, принимаем нулевую гипотезу о том, что различий нет, иначе считаем, что между группами есть статистически значимая разница.</br>
# 
# <br>Исходя из обьема данных и выборки с которой мы работает возьмем уровень значимости(доверия) 5%.</br>
# 
# <br>Вывод делается на выборке с 2012 года по 2016 год</br>
# 
# <br>Вывод:Не получилось отвергнуть нулевую гипотезу</br>
# 
# 
#    </b> 
# </div>

# In[28]:


games_clean = data_query.dropna(subset=['user_score'])
xbox_one = games_clean.query('genre == "Action"')['user_score']
pc = games_clean.query('genre == "Sports"')['user_score']

results = st.ttest_ind(xbox_one, pc, equal_var= False)
 
alpha = 0.05

if results.pvalue < alpha:
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")


# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌</b> 
#     
# Нулевые гипотезы всегда про равенство.
#     
# Подробнее: https://allatambov.github.io/psms/pdf/hypo-test.pdf

# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌</b> 
# 
# Ничего не сказано про выбранный статистический тест (критерий). Подробнее: https://habr.com/en/company/uchi_ru/blog/500918/

# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌ Вторая итерация </b> 
#     
# Все еще не сказано про критерий. Глянь статью на Хабре, пожалуйста, это поможет тебе 

# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌</b> 
#     
# Нет итогового вывода

#   <div class="alert alert-info">
# <b> 
#   <center> Вывод: </center> 
#    <br> В ходе работы были замечены следующие особенности: </br>
#     <br> </br>
#    <br> 1. Лидерами являются 2007 и 2008 год </br>
#    <br> 2. 'PS2', 'X360', 'Wii', 'PS3', 'DS' являлись самыми популярными платформами  </br>
#    <br> 3. Самая популярную платформу РS4   </br>
#    <br> 4. У продаж и отзывывов есть небольшя зависимоть корреляция 0.37 значит что 37 процентов продаж зависили тот отзывов. </br>
#    <br> 5. Самый прибыльный жанр это  shooter </br>
#    <br> 6. У Северной Америки платформа лидер X360</br>
#    <br> 7. у Японии платформа лидер 3D</br>
#    <br> 8. в Евпропе платформа лидер PS4</br>
#    <br> 9. В Америке самый популярный жарн шутер, потом Action</br>
#    <br> 10. В Японии Role-Playing самый популярный</br>
#    <br> 11. В Евпропе примерно как и в Америке Action потом шутер. Думаж жанры в которые играют в Японии так отличаются от других стан потому что выборка не досточна большая, может у них свои ценности и взгляды на жизнь не знаю)) хотя на втором месте у них так же Action</br>
#    <br> 12. В Америке 44 процента игр это с рейтингом М(для взрослых)</br>
#    <br> 13. В Японии этим рейтингом особо не пользовались, а те кто пользовались предпочитали игры с рейтингом Е(для всех) тут сложно судить из-за того что данных мало</br>
#    <br> 14. В Европе 44 процента игр это с рейтингом М(для взрослых) совпадение с Америкой. У них много чего свопадает хех</br>
#    <br> 15. Между Европой и Америкой инресная зависимость между выбором жанром игры и рейтингом, почти одинаковые</br>
#     </b> 
# </div>

# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌</b> 
#     
# Отличный проект, тобою проделана большая работа, ты молодец!
#     
# Сперва похвалю за наличие везде в проекте промежуточных выводов, комментариев и рассуждений. Каждый пункт у тебя достаточно хороший, просто в каждом из них есть по ошибке. Тем не менее, я уверен, что ты довольно легко с ними сможешь справиться
# 
# Что обязательно стоит доработать: написать, какой статистический критерий для проверки гипотез был выбран и почему именно он; переформулировать гипотезы; посмотреть иначе на самые популярные / прибыльные жанры; доработать пункт с подготовкой данных; добавить вступление в проект; добваить итоговый вывод
# 
# Также я оставил несколько желтых комментариев. Думаю, и они будут тебе полезны.
# 
# Буду ждать доработок :) Удачи!

# <div class="alert-danger"> 
# <b>Комментарий ревьюера ❌ Вторая итерация </b> 
#     
# Практически все ошибки исправлены, осталось доработать пункт с проверкой гипотез

# <div class="alert-success"> 
# <b>Комментарий ревьюера 👍 Третья итерация </b>
# 
# Проект стал еще лучше, принимаю. Успехов в дальнейшей учебе!
