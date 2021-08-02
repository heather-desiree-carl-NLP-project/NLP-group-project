# Predicting Repository Languages

## Project Goals:
- Can we successfully predict a repository's coding languge based off the readme contents?
- What readme contents contribute to the prediction of a repository's coding language?


## Project Goals/Description
The goal of this project is to predict the primary programming language of each repository by scraping the repository's README file contents. This project was initiated by utilizing web scraping techniques to scrape README files from various Github repositories. After wrangling our data, our group conducted natural language processing exploration and modeling. We employed multiclass classification methods to create a machine learning model. The end goal was to create an NLP model to predict the programming language used in a github repository based on the words and word combinations found in the readme files.

### Projet Outline:
    
- Acquisiton of data:
    - Search for repositories on git hub with "customer" as a commonality.
    - Conduct web scraping of said repositories' readme contents.
- Prepare and clean data:
    - Remove repositories in languages other than english
    - Drop nulls
    - Lowercase all text
    - Remove stopwords (including customer, customers, i)
    - Tokenize the data
    - Stem and Lemmatize
    - Narrow data down to repo's top four languages (java, javascript, php and jupyter)
- Explore data:
    - Explore word clouds for top 4 languages
    - How often are words used?
        - Top 20 words for each language
    - Utilize bar graphs, bigrams and trigrams for top 4 languages
    - Analyze bigram and trigram word clouds for top 4 languages
- Modeling:
    - Make multiple models.
    - Use cleaned, stemmed and lemmatized data
    - Pick best model to move forward with.
    - Test Data.
    - Conclude results.
    
### Target variable
- Language

## Findings:
### Explore:
- PHP is the most commonly used coding language
- Bigrams and Trigrams have variable phrases for each language
    
### Modeling:
- Models Made:
    - Linear SVC
    - KNN
- Best Model:
    - Linear SVC (on lemmatized data)
- Model testing:
    - Train
        - XX%
    - Validate
        - XX%
- Performance:
    - Test
        - XX%


## Replicate My Project
### tools/libraries:
    1. python
    2. pandas
    3. scipy
    4. sci-kit learn
    5. numpy
    6. matplotlib.pyplot
    7. seaborn
    8. NLTK
    9. BeautifulSoup
* Steps to recreate
    1. If you wish to recreate this project download the json file for ...

    - Read the README.md
    - Download the data2.json file
    - Download the prepare.py, explore.py, model.py and project_final_notebook.ipynb files into your working directory, or clone this repository
    - Ensure your json file is named appropriately (data2.json)
    - Run the project_final_notebook.ipynb notebook


------------


## Data Dictionary

#### Target
Name | Description | Type
:---: | :---: | :---:
language | The repository's respective programming language | object
#### Features
Name | Description | Type
:---: | :---: | :---:
repo | The name of the specific repository | object
readme_contents | The contents of readme file scraped from that repo | object
cleaned | The readme contents with stopwords removed, text normalized and tokenized | object
stemmed | The cleaned data stemmed | object
lemmatized | The cleaned data lemmatized | object



## Recommendations/With More Time:
1. We would add in varying repo languages to see if we could increase the model's drop off on validate set.

