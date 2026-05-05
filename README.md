**Chicago Bears 2025 Game Outcome Analysis**--

Author

Shri Patel
LinkedIn: https://www.linkedin.com/in/shripatel2003/

**Executive Summary**

For a quick overview of the analysis, see the one-page summary:

[Download Executive Summary](./bears-2025-executive-summary.pdf)

This project analyzes the Chicago Bears 2025 season to identify which team-level statistics best explain game outcomes and point differential.

The goal was to move beyond traditional volume-based metrics (like time of possession) and evaluate whether efficiency and impact-based metrics provide stronger predictive power.


**Key Findings**

* Time of Possession was not a reliable indicator of winning.
* Yards Per Play Differential (YPP Diff) showed a strong relationship with point differential (r ≈ 0.71).
* Model performance improved significantly after adding:
    * Turnover Margin
    * Explosive Play Margin (20+ yard plays)
* Third Down Conversion Rate was tested but did not improve model performance, suggesting its effect is already captured by efficiency metrics.

**Final Model**

The final regression model uses three key features:
  point_diff ≈
  YPP_diff
  + turnover_margin
  + explosive_play_margin

This combination provided the best balance of:

* interpretability
* predictive accuracy
* simplicity


**Methods**

* Data cleaning and merging game-level datasets
* Feature engineering (YPP, turnovers, explosive plays)
* Correlation analysis
* Linear regression modeling
* Model evaluation using:
    * R²
    * Mean Absolute Error (MAE)

**Why This Matters**

This analysis shows that:

* Efficiency metrics > volume metrics
* Turnovers and explosive plays significantly influence outcomes beyond overall efficiency

For football analytics, this suggests that evaluating performance through possession-based metrics alone may be misleading.
