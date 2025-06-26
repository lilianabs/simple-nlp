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