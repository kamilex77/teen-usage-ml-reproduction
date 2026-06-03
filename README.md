# Teen Smartphone Usage & Addiction Prediction (R)

## Overview
This project reproduces and extends a previous machine learning study on predicting teen smartphone usage and addiction. The original analysis was implemented in Python; this version is fully reimplemented in R.

## Objectives
- Reproduce and validate previous results  
- Extend the dataset (survey and/or synthetic data)  
- Improve models with additional features and evaluation  
- Ensure full reproducibility  

## Methods
We compare several machine learning models (e.g. logistic regression, random forest, gradient boosting) with cross-validation and robustness checks.

## Data
- Original dataset from prior project  
- Extended dataset (new observations)  

## Requirements

### R Environment

The project was developed and tested using:

* R >= 4.3.0
* RStudio (recommended)

Required R packages:

```r
install.packages(c(
  "dplyr",
  "readr",
  "caret",
  "reshape2",
  "ggplot2",
  "e1071",
  "gridExtra",
  "patchwork",
  "googledrive",
  "rpart",
  "rpart.plot",
  "randomForest",
  "gbm",
  "viridis"
))
```

### Python Environment

A small Python script is used to generate synthetic observations.

Requirements:

```txt
pandas>=2.0
numpy>=1.24
```

Install with:

```bash
pip install -r requirements.txt
```

### Dataset

The dataset is automatically downloaded from Google Drive using the file ID provided in the code.

### Reproducing the Analysis

1. Clone the repository.
2. Install all required R packages.
3. (Optional) Create a Python environment and install dependencies from `requirements.txt` if you want to extend our dataset with generated records.
4. Open the project in RStudio.
5. Run the R Markdown document from start to finish.
6. Synthetic data will be generated automatically and used for the final evaluation step.

## Team
- Aleksandra Dobosz  
- Aleksandra Engel  
- Adam Gonet  
- Kamil Laskowski

### AI disclousure 
This readme and parts of coding (marked in file) were generated with ChatGPT. The outputs were checked by the authors. 
