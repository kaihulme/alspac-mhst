import os
import numpy as np
import pandas as pd


def get_feature_types():
    """
    Multiple imputation with random forest using MissForest.
    """
    base_dir = os.getcwd()
    impute_dir = os.path.join(base_dir, "data/altered/imputed")
    data_path = os.path.join(base_dir, "data/altered/maps_feature_mapping.csv")
    df = pd.read_csv(data_path, index_col="X")
    features = df.columns
    dict_path = os.path.join(base_dir, "data/original/synthetic_data_dictionary.csv")
    dict_df = pd.read_csv(dict_path)
    dict_df = pd.DataFrame(dict_df[[dict_df.columns[0], dict_df.columns[3]]].dropna())
    dict_df = dict_df.rename(columns={dict_df.columns[0]: "feature", dict_df.columns[1]: "type"})
    dict_df = dict_df.set_index("feature")
    type_dict = dict_df.to_dict()["type"]
    dis_features, cat_features, nom_features, ord_features = [], [], [], []
    for feature in df:
        ftype = type_dict[feature]
        if ftype == "Discrete":
            dis_features.append(feature)
        elif ftype == "Continuous":
            cat_features.append(feature)
        elif ftype == "Nominal":
            nom_features.append(feature)
        elif ftype == "Ordinal":
            ord_features.append(feature)
        else:
            print(f"Unknown feature type - {feature} ({type_dict[feature]})")
    num_features = dis_features + cat_features
    cat_features = nom_features + ord_features
    bin_features = []
    for feature in nom_features:
        unique = df[feature].dropna().unique()
        if len(unique) > 2:
            print(f"{feature} is non-binary")
        else:
            bin_features.append(feature)
    return dis_features, cat_features, nom_features, ord_features