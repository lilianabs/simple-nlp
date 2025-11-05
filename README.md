# simple-nlp
This repo contains tools for preprocessing text for training machine learning models.

## Usage example

### Using sklearn's Pipeline

```
from simple_nlp.cleaner import *
from sklearn.pipeline import Pipeline


data = [
"Hello, this is a sample tweet! #NLP #Python @user1 😊 https://example.com",
"Another example with emojis 😂 and a url www.google.com",
]

# Create a pipeline
pipeline = Pipeline([
('remove_urls', RemoveURLs()),
('remove_mentions', RemoveMentions()),
('remove_hashtags', RemoveHashtags()),
('remove_html_tags', RemoveHtmlTags()),
('remove_emojis', RemoveEmojis()),
('remove_extra_spaces', RemoveExtraSpaces()),
#('spell_check', SpellCheckerCleaner())
])

# Transform the data
cleaned_data = pipeline.fit_transform(data)

# Print the cleaned data
print(cleaned_data)
```

### Using a single class

```
from simple_nlp.cleaner import SpellCheckerCleaner

texts = ["corect the speling erors plese", "anothr sentnce with misstakes"]
spell_cleaner = SpellCheckerCleaner()
cleaned = spell_cleaner.transform(texts)
print(cleaned)
```

## Developer's Guide

To set up a development environment, follow these steps:

1. Create a new Python environment:

   ```
   python -m venv venv
   ```

1. Activate the Python environment:

   ```
   source venv/bin/activate
   ```

1. Update pip:

   ```
   python -m pip install --upgrade pip
   ```
1. Install setup tools:
    
    ```
    pip install -U pip setuptools wheel
    ```

2. Install the project requirements:

   ```
   python -m pip install -r requirements.txt
