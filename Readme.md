# Compare Team/Department Performance using Z-scores

This repository demonstrates how Z-scores are used to compare relative team performance on various metrics.

![alt text](asset/preview.png)


## Getting Started

### Dependencies

* pandas
* numpy
* scipy
* statsmodels
* matplotlib

### Usage

Simply, run ```main.ipynb```to compare team/department performance on available metrics. 

More metrics can be added easily by following the factory design pattern in ```Metric.py``` and custom logic can be implemented as desired.

In this example, we did not perform any transformations on the normalised metrics because the QQ plot indicates that all metrics approximately follow a normal distribution. For your custom dataset, a transformation may be necessary. Be sure to change ```_, eligble_col``` to ```team_nominal_roll, eligble_col``` in your code. 
### Explaination

The arrows indicate how extreme the outliers are in terms of their Z-scores.

⬆️⬆️⬆️ = x > 1.96\
⬆️⬆️ = x > 1.5\
⬆️ = x > 1\
⬇️ = x < -1\
⬇️⬇️ = x < -1.5\
⬇️⬇️⬇️ = x < -1.96

## Acknowledgments

Dataset is provided by [Mexwell](https://www.kaggle.com/datasets/mexwell/employee-performance-and-productivity-data). Click on the hyperlink to be referred to the original source on Kaggle.

