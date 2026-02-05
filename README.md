QUESTION: If a customer in Florida (FL) submits a complain about an incorrect information on his/her payday loan via web, is that customer likely to get a timely response?

METHOD: 
- Built a multivariate logistic regression model to predict if a customer is likely to get a timely response.
- A comparison was made between balanced and unbalanced logistic regression models to assess the impact of class imbalance on predictive performance.
- Initially evaluated the model on the full dataset, then later implemented the 80/20 train-test split to assess the performance.

Results from the unbalanced logistic regression model: 
- R^2 (full dataset) = 0.9377
- R^2 (Trained 80% of the data) = 0.93717
- R^2 (Tested 20% of the data) = 0.93962

Results from the balanced logistic model (class_weight = 'balanced', max_iter = 1000):
- R^2 (full dataset) = 0.4216
- R^2 (Trained 80% of the data) = 0.4232
- R^2 (Tested 20% of the data) = 0.4123

Key Insights: After applying class balancing, the logistic regression model learned to distinguish both classes (“Yes” and “No”), improving fairness and predictive reliability. This demonstrates that, in the presence of class imbalance, logistic regression should incorporate class weight and iterations to prevent majority-class dominance and ensure meaningful performance across all classes.
