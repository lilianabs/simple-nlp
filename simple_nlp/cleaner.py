import re
import string
from typing import Optional, List, Any

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
        return [re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE) for text in X]
    

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