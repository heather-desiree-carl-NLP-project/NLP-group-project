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
    - How often are words used?
        - Count of words
        - Percentage of words
    - Explore word clouds for top 4 languages
        - Is there anything that stands out?
    - Utilize bar graphs, bigrams and trigrams for top 4 languages
        - Is there anything of importance?
    - Analyze bigram and trigram word clouds for top 4 languages
        - What did you notice?
- Modeling:
    - Make multiple models.
    - Pick best model.
    - Test Data.
    - Conclude results.
    
### Target variable
- Language

## Findings:
### Explore:
- PHP is the most commonly used coding language 
    
### Modeling:
- Baseline:
    - XX%
- Models Made:
    - Logistic Regression
    - KNN
    - Decision Tree
    - Random Forest
    - Ridge Classifier
    - SDG Classifier
- Best Model:
    - SDG Classifier
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
    1. f you wish to recreate this project download the csv files for red wine and white wine and save them to your repo. Then you can run this notebook. Check out the README for the skills required. More information about this data can be found here.

    - Read the README.md
    - Download the prepare.py, explore.py, model.py and final_notebook.ipynb files into your working directory, or clone this repository
    - Ensure your csv files are named appropriately ('winequality-red.csv' and 'winequality-white.csv', should be defaults from links above)
    - Run the final_notebook.ipynb notebook


------------


## Data Dictionary

#### Target
Name | Description | Type
:---: | :---: | :---:
life_expectancy | The average life expectancy in years of that country's population | float
#### Features
Name | Description | Type
:---: | :---: | :---:
repo | The name of the specific repository | object
language | Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)  | float
readme_contents | The contents of readme file associated to that repo | object
cleaned | Indicates whether a country is developed or still developing | int
stemmed | Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population) | float
lemmatized | Number of Infant Deaths per 1000 population | int




## Recommendations/With More Time:
1. I would prefer to continue to impute the remainder of my nulls as opposed to just dropping the rest of them.
2. I would explore more clustering possibilities to create new features and see how I can create more correlated features.
3. I would assess the outliers and/or utilize different scaling methods to see if that has a varying impact on model performance.

