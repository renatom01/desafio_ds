"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    drop_features,
    encode,
    scale,
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=drop_features,
            inputs= "df_train",
            outputs="df_dropped",
            name="drop_features_node",
        ),
        node(
            func=encode,
            inputs= "df_dropped",
            outputs="df_encoded",
            name="encode_node",
        ),
        node(
            func=scale,
            inputs= "df_encoded",
            outputs= "df_scaled",
            name="scale_node",
        ),

    ])

