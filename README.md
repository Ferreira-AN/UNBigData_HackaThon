# Country diet quality forecast from socio-economic data
The purpose of this work is to find which variables, besides the own diet measurements, can strongly influence how healthy are the country meals.

## Process
Our process for discovering a solution to this problem is described below:

1. Find nutrition and relevant socio-economic datasets
2. Find a target metric that scores how healthy a country's food
3. Select the most relevant features to avoid multicolinearity
4. Build a model that can forecast the metric and explain the weights of the features
5. Visualize the feature's impact and the error

## Files
```
project
├── data (datasets folder)
├── scripts (scripts for dev)
├── models (dumped models folder)
└── *.ipynb (ordered notebooks with our solution steps)
```

## Develop
1. Clone the repo
2. Run `make` to install the dependencies and extract datasets
3. Run `jupyter lab`


## References

- Miller, V., Webb, P., Cudhea, F. et al. Global dietary quality in 185 countries from 1990 to 2018 show wide differences by nation, age, education, and urbanicity. Nat Food 3, 694–702 (2022). https://doi.org/10.1038/s43016-022-00594-9

- 2021 Global Nutrition Report: The state of global nutrition. Bristol, UK: Development Initiatives.
