**Data Sources**

This analysis combines publicly available game-level and play-by-play NFL data for the 2025 season.

**Game-Level Data**

Game-level statistics were sourced from Pro-Football-Reference:

* https://www.pro-football-reference.com/

Data extracted includes:

* points scored
* total yards
* turnovers
* time of possession
* drive-level summaries

These datasets were used to construct weekly summaries for both the Chicago Bears and their opponents.

**Play-by-Play Data**

Play-level data was sourced from the nflverse project:

* https://github.com/nflverse/nflverse-data
* Direct dataset:
    https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2025.csv.gz

This dataset includes:

* yards gained per play
* play type
* game identifiers (week, teams)

**Explosive Play Calculation**

Explosive plays were defined as: yards_gained ≥ 20

Using play-by-play data, the following were computed:

* explosive plays (offense)
* explosive plays allowed (defense)
* explosive play differential

These were aggregated to the game level and merged with team statistics.

**Feature Engineering**

The following derived features were created:

* Yards Per Play Differential (YPP Diff)
    Measures relative offensive efficiency
* Turnover Margin
    Difference between takeaways and giveaways
* Explosive Play Margin
    Difference between explosive plays generated and allowed

These features were used as inputs for regression modeling.

**Notes**

* All data is publicly available and used for analytical purposes
* Game-level and play-level datasets were combined manually within the notebook
* Minor discrepancies between sources may exist due to differences in data collection methods
