# Named Entity Recognition - API

This is simple Flask API for named entity extraction using Spacy.


## Requirements
- Flask
- Spacy

## Install libraries

```shell
pipenv install
pipenv shell
```

## Run api

```shell
python api.py
```


## Test
Replace the <Text HERE> with some text to test the endpoint.

```shell
curl -d "text=<TEXT HERE>" -X POST http://localhost:5000/api/v1/resources/ner-analyse
```

## Use Streamlit to test spacy 

You want maybe save some time and test spacy asap. Streamlit allows developers to test the performance of a model by using a nice user interface. You should try it. It's great!

```shell
streamlit run app.py
```



## Spacy labels

For more information please go to  the Spacy documentation [page](https://spacy.io/api/annotation#named-entities)

| Label       | Description					                         |
|-------------|------------------------------------------------------|
| PERSON      | People, including fictional.                         |
| NORP        | Nationalities or religious or political groups.      |
| FAC         | Buildings, airports, highways, bridges, etc.         |
| ORG         | Companies, agencies, institutions, etc.              |
| GPE         | Countries, cities, states.                           |
| LOC         | Non-GPE locations, mountain ranges, bodies of water. |
| PRODUCT     | Objects, vehicles, foods, etc. (Not services.)       |
| EVENT       | Named hurricanes, battles, wars, sports events, etc. |
| WORK_OF_ART | Titles of books, songs, etc.                         |
| LAW         | Named documents made into laws.                      |
| LANGUAGE    | Any named language.                                  |
| DATE        | Absolute or relative dates or periods.               |
| TIME        | Times smaller than a day.                            |
| PERCENT     | Percentage, including ”%“.                           |
| MONEY       | Monetary values, including unit.                     |
| QUANTITY    | Measurements, as of weight or distance.              |
| ORDINAL     | “first”, “second”, etc.                              |
| CARDINAL    | Numerals that do not fall under another type.        |





#### Author: Jimmy Vila