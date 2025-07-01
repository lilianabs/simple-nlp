import re
import string
from typing import Optional, List, Any
from spellchecker import SpellChecker

import spacy
from sklearn.base import BaseEstimator, TransformerMixin

class TextCleaner(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        pass
    
    def fit(self, X: List[str], y: Optional[Any] = None) -> None:
        return self
    
    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        return X
    
    
class RemoveURLs(TextCleaner):
    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        url = re.compile(r'https?://\S+|www\.\S+')
        return [url.sub(r'',text) for text in X]
    

class RemoveEmojis(TextCleaner):
    """
    Remove emojis from a list of strings
    """
    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "\U00002702-\U000027B0"
            "\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE,
        )
        return [emoji_pattern.sub(r"", text) for text in X]


class RemoveHtmlTags(TextCleaner):
    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        html = re.compile(r'<.*?>')
        return [html.sub(r'', text) for text in X]

 
class RemovePunctuation(TextCleaner):
    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        table = str.maketrans('', '', string.punctuation)
        return [text.translate(table) for text in X]
    

class RemoveMentions(TextCleaner):
    """
    Remove mentions from a list of strings
    """
    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        return [re.sub(r'@\w+', '', s) for s in X]
    

class RemoveHashtags(TextCleaner):
    """
    Remove hashtags from a list of strings
    """
    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        return [re.sub(r'#\w+', '', s) for s in X]
 
class RemoveExtraSpaces(TextCleaner):
    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        return [re.sub(r'\s+', ' ', text).strip() for text in X]


class RemovePunctuation(TextCleaner):
    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        table = str.maketrans('','',string.punctuation)
        return [text.translate(table) for text in X]


class SpellCheckerCleaner(TextCleaner):
    def __init__(self) -> None:
        super().__init__()
        self.spell_checker = SpellChecker(language='en')

    def _correct_spelling(self, text: str) -> str:
        words = text.split()
        misspelled_words = self.spell_checker.unknown(words)
        corrected_text = [
            self.spell_checker.correction(word) if word in misspelled_words else word
            for word in words
        ]
        return " ".join(corrected_text)

    def transform(self, X: List[str], y: Optional[Any] = None) -> List[str]:
        return [self._correct_spelling(text) for text in X]