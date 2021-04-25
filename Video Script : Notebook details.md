# Video Sctructure



## Introduction (Monty)

- Explain how we distribute work.
- Our literature and data imputation were separated by half-half of the whole group.

## Initial Thinking / Work So Far ( KKF)

Pre prosessing. imputation

- Why we justification for it and our progress so far at the moment.

- We've tried different types of data imputation for those missing data and we need to demonstrate why we used random forest at some of the particular point for instance.

## Challenges

- Our Challenges shall be distributed into the initial thinking / work so far section too.
- In general, what cost most of our time is what are those missing values and how do we carefully impute the data without just roughly delete those features.

## Things To Do (Elvis)

- Video / Report

---

# Our Notebooks

## Dimentionality Reduction PCA

As our first notebook, we imported a chunky dataframe with 13734 rows * 82 columns with many `NaN` before our pre-prosessing steps. To get good results with dimisionality reduction methods, we used `StandScaler` in sklearn for our data-scaling.

As we seen the dataset contains a lot of `NaN` values, this must be resolved before our PCA dimension reduction, therefore we replaced those missing values with `-1` to get a practical PCA result and the plot the result.

## Pandas Data profiling

In this notebook, we imported `pandas_profiling` package to generate a report of our dataframe. For each columns to shows the following statistics as a reference of our data analysis:

- The types of colums in a data frame.
- Essential information such as types, unique values and mussing values.
- Highlited the highly correlated variables.
- Detailed information about our missing values.

## Feature Mapping Correlation

In this notebook, we've analysed the correlation of each feature, ignoring all `NaN`s and handling with different data types such as object. A dictionary was created for those catagorical features mapping as float64 indexes, and we visualised the Pearson, Kendall, and Spearman correlations with heatmaps respectively.

Pandas `corr` is able to handle most of the missing values, but we can see a few of the features have no correlation between them. This is likely due to there being no rows in the dataframe where the feature pairs both have a value. It seems for every pair there is at least one row where both values exist, so this is not the reason. Another possibilty is that there is only one value that is non-NaN for that feature. As we can see from this the only features that have only 1 unique value (exluding NaNs) are the ones which have no value in the correlation heatmap.

## KNN Imputation / Random Forest 

In these early notebooks, different kinds of imputation were practiced as individual playgrounds.

## Missing Value Analysis & Handling (NOT FINISHED YET - MAIN STUFF HERE)

In this notebook, we analysed all our missing values, counted the percentage of each one and explored some methods for missing value imputation.

Apart from `sex` and `birth_order` with no missing values, the histogram shows that around 40% of the entreis have between 60-70% of the features missing.

In all those missing values, some of the feature only have one unique value other than `NaN`, we found these features and carefullu decided how to impute these `NaN`s as random values or No. We partially used the strategy of logical substitution. Take `comp_int_bed_16` and `comp_noint_bed_16` for example. One states whether the subject has a computer in their room with internet and the other without. It is possible that they have both, but it is unlikely.

It may make sense to impute `No` to `comp_noint_bed_16` when `comp_int_bed_16` is `Yes` and vice versa. This will still leave some NaN values, but should impute enough `No` values to these columns for other imputation methods to start working giving some more variability. There's other similar test for logical substitutions too.