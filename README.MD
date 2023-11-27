# Artificial Intelligence


## **🎓 Course Information**

- **Subject Code** : 203105322
- **Faculty**: Mr Smaranjit Ghose (Assistant Professor)
- **Semester**: 5
- **Year**: 2023
- **Divisions** (under direct tutelage): 5B5, 5B6, 5B7, 5B8, 5B17


## **📚 Study Material**


|Unit | Name | Lecture Material | 
|-----|------|-------------------|
| 1 | Introduction to Artificial Intelligence | [Unit 1 Material](https://github.com/smaranjitghose/ParulUniversityAI/blob/master/Unit%201.pptx) | 
| 2 | Exploratory Data Analysis | [Unit 2 Material](https://github.com/smaranjitghose/ParulUniversityAI/tree/master/EDA) | 
| 3 | State Space Search| - [Unit 3 Material](https://docs.google.com/presentation/d/1RWcXZaFgThKbOM9FM3CF5n7nMAgfsE83FDUiGRMaDKI/edit?usp=sharing)| 
| 4 | Knowledge Representation | [Unit 4 Material ](https://docs.google.com/presentation/d/18pDtVmlpP-T_C7N3oGf7H9FEWf291R2jNWYC75ZeVt4/edit?usp=sharing)| 
| 5 | Fuzzy Logic |[Unit 5 Material](https://docs.google.com/presentation/d/1RMfno0017k02J1oSIuOoX7YoV3khmST4DXqt8vl1ohE/edit?usp=sharing) | 
| 6 | Natural Language Processing | [Unit 6 Material](https://docs.google.com/presentation/d/1XqtA8Dp2i1oFqXcCwo3gZSKZ7KtyO02HZG8WcXg6_9Q/edit?usp=sharing) | 
| 7 | Machine Learning | Discussed via hands on | 
| 8 | Fundamentals of Neural Networks and Expert Systems | [Unit 7 Material](https://docs.google.com/presentation/d/1LQ_25SeSRHHSAZdFcG1r77Rufk58vlcOSkKDPBU-yqg/edit?usp=sharing) | 




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

