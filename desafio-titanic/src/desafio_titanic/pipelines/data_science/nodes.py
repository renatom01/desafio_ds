"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.5
"""
import pandas as pd
import logging
from typing import Dict, Union, List
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score

def split_data (df: pd.DataFrame):
    train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
    y_train = train_set['Survived']
    X_train = train_set.drop(['Survived'], axis=1) 
    y_test = test_set['Survived']
    X_test = test_set.drop(['Survived'], axis=1)
    return dict(
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
    )

def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:
    classifier = DecisionTreeClassifier(max_depth=8)
    classifier.fit(X_train,y_train)
    return classifier

def evaluate_model(
    classifier: DecisionTreeClassifier, X_test: pd.DataFrame, y_test: pd.Series
):
    y_pred = classifier.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    f1_score = f1_score(y_test, y_pred)

#    logger = logging.getLogger(__name__)
#    logger.info("Model has accuracy of %.3f on test data.", score)
    return {"accuracy_score": {"value": score, "step": 1}}



#def evaluate_model(
#    X_test: pd.DataFrame, 
#    y_test: pd.DataFrame,
#    classifier: DecisionTreeClassifier
#    ) -> Dict[str, Union[float, List[float]]]:
#
#    y_pred = classifier.predict(X_test)
#    
#    accuracy = accuracy_score(y_test,y_pred)

    #y_pred = pd.DataFrame(y_pred, columns = ['price_predict'])
    #return y_pred, {"accuracy_score": {"value": accuracy, "step": 1}}        
