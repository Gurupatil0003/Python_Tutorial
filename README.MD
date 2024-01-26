<h2><div style="font-family: Trebuchet MS; background-color: #1b191d; color: #FFFFFF; padding: 12px; font-size: 35px; line-height: 1.5;text-align: center; line-height: 1.;">🅶🆄 🆁🅰🅽🅽🅰 🅶🅾🆄🅳🅰--🅳🅰🆃🅰🆂🅲🅸🅴🅽🆃🅸🆂🆃👨‍💻</div> 


# Python Full Stack Development


## **🎓 Course Information**

- **Subject Code** : 
- **Faculty**: Mr Guranna Gouda  (Assistant Professor)
- **Semester**: 4
- **Year**: 2023
- **Divisions** (under direct tutelage): 4B17,4B18,4B19


## **📚 Study Material**


| Unit--1 | Name                                      | Lecture Material                                                | PPT Materials |
|------|-------------------------------------------|-----------------------------------------------------------------|---------------|
| 1    | Introduction to Python                    | [Unit 1 Python Introduction](https://bytexl.app/content/3zeuvj5n3/python/3zh4pzccw/introduction-to-python/history-and-features-of-python) | [PPT Materials](https://bytexl.app/course-catalog-groups/3z7naufue/python/course-catalog/3zmbcmqva/topic-a1-introduction-to-python)          |
| 2    | Data types & Variables   | [Unit 1 Material](https://bytexl.app/content/3zeuvj5n3/python/3zh4wu3su/introduction-to-python/basic-data-types-and-variables)| [PPT Materials](https://bytexl.app/course-catalog-groups/3z7naufue/python/course-catalog/3z7nbws4y/topic-a2-data-types-variables)          |
| 3    | Operators      | [Unit 1 Material](https://bytexl.app/content/3zeuvj5n3/python/3zh4wu3su/introduction-to-python/basic-data-types-and-variables) | [PPT Materials](https://bytexl.app/course-catalog-groups/3z7naufue/python/course-catalog/3zmhpqs5y/topic-a3-operators)          |
| 4    |  Conditional Statements                           | [Unit 1 Material](https://bytexl.app/content/3zeuvj5n3/python/3zmz4fncs/control-flow/conditional-statements)| [PPT Materials](https://bytexl.app/course-catalog-groups/3z7naufue/python/course-catalog/3zmhpn74h/topic-a4-conditional-statements)          |
| 5    | Iterative Statements  and Loops                       | [Unit 1 Material](https://bytexl.app/content/3zeuvj5n3/python/3zmz4me59/control-flow/looping-statements)  | [PPT Materials](https://bytexl.app/course-catalog-groups/3z7naufue/python/course-catalog/3zn7n2z2v/topic-a4-1-iterative-statements)          |
| 6    |  Lists                             | [Unit 1 Material](https://bytexl.app/content/3zeuvj5n3/python/3zmz7br4p/data-structures/list-and-tuples-with-methods)             | [PPT Materials](https://bytexl.app/course-catalog-groups/3z7naufue/python/course-catalog/3zn7mmsuz/topic-a5-lists)          |
| 7    |  Tuples                            | [Unit 1 Material](https://bytexl.app/content/3zeuvj5n3/python/3zmz7br4p/data-structures/list-and-tuples-with-methods)                                             | [PPT Materials](https://bytexl.app/course-catalog-groups/3z7naufue/python/course-catalog/3zn7mt3dd/topic-a6-tuples)          |
| 7    |  Sequences, Dictionaries ,set                       | [Unit 1 Material](https://bytexl.app/content/3zeuvj5n3/python/3zmzavfcn/data-structures/dictionaries-and-dictionary-methods)                                             | [PPT Materials](https://bytexl.app/course-catalog-groups/3z7naufue/python/course-catalog/3zn8342mv/topic-a7-sequences-dictionaries)          |


**EDA Hands-On** 

|Sl no | Dataset | Solution|
|------|---------|---------|
|1|[Iris](https://www.kaggle.com/datasets/uciml/iris)||
|2|[Titanic](https://www.kaggle.com/competitions/titanic)| [Titanic_EDA](./EDA_Problems/Titanic_EDA.ipynb)|
| 3 | [IPL 2008-2022 matches dataset](https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset) | [IPL EDA](./EDA_Problems/IPL_EDA.ipynb) | 



**EDA Practice Problems**

|Sl No|Dataset|Solution|
|-----|-------|--------|
|1|[Boston Housing](https://www.kaggle.com/c/boston-housing)||
| 2 | [U.S. International Air Traffic 1990-2020 dataset ](https://www.kaggle.com/datasets/parulpandey/us-international-air-traffic-data)| | 
| 3 | [Forbes Highest Paid Athletes 1990-2019 dataset](https://www.kaggle.com/datasets/parulpandey/forbes-highest-paid-athletes-19902019) | | 
| 4 | [Covid-19 Clinical Trials dataset](https://www.kaggle.com/datasets/parulpandey/covid19-clinical-trials-dataset) | | 
| 5 | [Palmer Archipelago dataset](https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data)| | 
| 6 |[PIMA Indians Diabetes](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)||
| 7 |[Amazon Review for Sentiment Analysis](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)||

## Course Announcements 📢

[Check here for the latest announcements](./Announcements.MD)



Pandas Exercise 2 Soln (Temp)

```
prices = [float(value[1 : -1]) for value in chipo.item_price]

# reassign the column with the cleaned prices
chipo.item_price = prices

# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity','choice_description'])

# chipo_filtered

# select only the products with quantity equals to 1
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]
chipo_one_prod
```


## 👜 Supplementary Material

- [datetime module](./datetime_tutorial.ipynb)

- [Image Processing Mini Project](https://colab.research.google.com/drive/1UkrggIS9EpSge2y7z0PU_8g73IydpBc7?usp=sharing)

- [Assignment Submission EDA](https://colab.research.google.com/drive/1TZHy1kM7La-aQbfXnLPTgxBLHbZtDaqN?usp=sharing)

<!-- 

- os module
- pathlib module
- glob module
- random module
- requests module
- math module
- collections module
- Polars for Data Science
- Plotly for Data Science
- Pandas Tricks
- Matplotlib Tricks
- Streamlit for Data Science
- Advanced Python 1
- Advanced Python 2
- Advanced Python 3
- Advanced Python 4
- Advanced Python 5
- Advanced Python 6
- Advanced Python 7
- Advanced Python 8
- Advanced Python 9
- Advanced Python 10


-->

