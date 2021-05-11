import os
import numpy as np
import pandas as pd
from missingpy import MissForest
from adsmh.utils.utils import get_feature_types


def impute(n_imputations):
    """
    Multiple imputation with random forest using MissForest.
    """
    base_dir = os.getcwd()
    to_impute_path = os.path.join(base_dir, "data/altered/imputed/maps_fixed_binary_bands.csv")
    toimpute_df = pd.read_csv(to_impute_path).set_index("X")
    dis_features, cat_features, nom_features, ord_features = get_feature_types()

    missforest = MissForest(max_iter=10, n_jobs=-1)
    cat_idxs = np.asarray([np.where(toimpute_df.columns == cat)[0][0] for cat in cat_features])
    missforest_imputations = []
    for i in range(n_imputations):
        print(f"\nImputation {i}:\n")
        missforest_df = toimpute_df.copy()
        missforest_df = missforest.fit_transform(missforest_df, cat_vars=cat_idxs)
        missforest_imputations.append(missforest_df)

    missforest_dir = os.path.join(base_dir, "data/altered/imputed/multiple/missforest")
    if not os.path.isdir(missforest_dir):
        os.makedirs(missforest_dir)
    for i, data in enumerate(missforest_imputations):
        path = os.path.join(missforest_dir, "missforest_imputation_{0}.csv".format(i+1))
        df = pd.DataFrame(data, columns=toimpute_df.columns)
        df.to_csv(path)

    print("\nImputation complete!\n")