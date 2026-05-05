**Overview**

This project analyzed the Chicago Bears 2025 season to identify which team-level metrics best explain game outcomes and scoring margin.

The goal was to move beyond traditional volume-based statistics and focus on efficiency and high-impact plays.

**Efficiency Drives Outcomes**

Yards Per Play Differential (YPP Diff) was the strongest single predictor of game outcomes.

* Strong correlation with point differential (r ≈ 0.71)
* Consistently aligned with wins and losses
* Outperformed volume-based metrics such as time of possession

Teams that are more efficient per play tend to win, regardless of total yardage or possession time.

**Turnovers Significantly Shift Outcomes**

Adding turnover margin to the model resulted in a substantial improvement:

* Mean Absolute Error (MAE) reduced from 7.1 → 4.9
* Improved prediction accuracy across multiple games

Interpretation:

* Turnovers act as high-impact events that can override efficiency advantages


Even efficient teams lose when they give away possessions.

**Explosive Plays Explain Outliers**

In games where the model struggled, explosive plays (20+ yards) helped explain the gap.

* Captured large deviations from expected outcomes
* Improved prediction accuracy, especially in high-variance games

Big plays disproportionately impact scoring and can break expected trends.

**Not All Metrics Add Value**

Third-down conversion rate was tested but did not improve model performance.

* Increased MAE when added to the model
* Likely redundant with efficiency metrics like YPP

More features do not always improve a model—feature relevance matters more than quantity.


**Overall Conclusion**

Game outcomes for the Bears in 2025 were best explained by a combination of:

* Efficiency (YPP Differential)
* Mistakes (Turnover Margin)
* High-Impact Plays (Explosive Plays)

Traditional metrics like time of possession and third-down conversion rate were less reliable indicators when evaluated alongside these factors.

**Implications**

This analysis suggests that:

* Efficiency-based metrics should be prioritized over volume-based metrics
* Turnovers and explosive plays are critical in understanding deviations from expected performance
* Simple, well-selected features can outperform more complex or redundant models
