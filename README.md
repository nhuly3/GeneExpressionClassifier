# Author
- Ngan Nhu Ly
- nhu.ly@sjsu.edu
- CS 123A || San Jose State University

# GeneExpressionClassifier
The goal of this project was to apply machine learning techniques to synthetic biological data and determine whether we could accurately classify samples as having come from spaceflight or ground control conditions based solely on gene expression profiles.

# Files

- `expression_data.csv`: synthetic gene expression data (100 samples × 50 genes)
- `gene_classifier.py`: Python coding main program

---

## How to Run

Install dependencies:
pip install scikit-learn pandas numpy

Then run:
python gene_classifier.py expression_data.csv

If it does not work, please double check the location of your downloaded files using: 
cd ~/Downloads/gene_expression_classifier
gene_expression_classifier % ls

---

## Example Output
```
Confusion Matrix:
[[10  0]
 [ 1  9]]

Classification Report:
              precision    recall  f1-score   support

          GC       0.91      1.00      0.95        10
         FLT       1.00      0.90      0.95        10

    accuracy                           0.95        20
```
---
