Project 4: Ultradian Analyses
=============================
## Statement of problem


Ultradian rhythm is widely observed in mammalian behavioural patterns. Ultradian analysis aims to find the time-specific patterns in behavioral records, without specifying the length of cycle in advance (but need to be within 1 hour to 1 day). Typical ultradian period for rats includes 4, 12 and 24 hours. For example, we expect rats to be inactive in the nighttime. Ingestions and movements mostly happened in the daytime. It would be informative to study the ultradian cycle of the behaviour of mouse and we need to answer the following questions for this study: 
- What is the variable of interest for the periodic patterns ?
- Summary of activity: Food and water ingestion, distance traveled , movement intensity, AS probability.
- Spatial variable: Spatially discrete the data to cells each with its primary functions such as food cell, water cell, etc.  Examine ultradian cycle of  the spatial probability densities of the occupancy time in each cells. 
- How to subset the data?
- Basic subset: 16 strains.
- Strains may not be the primary influence for the variation of ultradian rhythms. We may look into the cycle for each mouse and detect the most important factors influencing the  ultradian rhythms. 
- How to choose the frequency or period ?
- The Lomb-Scargle (LS) periodogram spectral analysis technique, a widely used tool in period detection and frequency analysis.
- What is the connection with other subprojects?
- Ultradian rhythms could be treated as one feature for clustering the 16 strains. We may also subset the data using the results of the cluster and analysis the rhythm similarities and differences across clusters. 

## Statement of statistical problem
- How to determine the optimal bin intervals for constructing the time series?
- The bin interval may vary according to the frequency. Bin interval examples: 5 min, 30 min, 1 hour etc. Need to look into the data. 
- How to test the autocorrelation coefficient for the data and assess the model?
-  Use the AIC to select best time lags for the time series model and the K statistics to test the goodness of fit.
- For longitudinal data analysis, how to build the model? Which is the fixed effect or  random effect?


## Exploratory Analysis
- Data investigation
- Think about known/expected cycles - time to digest, IS/AS cycle, etc.
- Try to investigate cycles that are greater than 24 hours to avoid missing cycles.
- During the acclimatization period, investigate difference in cycles.
- Plots
- Plots for determining optimal bin intervals for constructing the time series.
- Plots for discovering the frequency or period.
- General time series plots for getting intuitions for each variables.
- Models
- Usage of Lomb-Scargle (LS) periodogram spectral analysis technique, a widely used tool in period detection and frequency analysis

## Data Requirements Description
- Input:  records for each strains (total of  16), each feature of interest (food, water, distance, active_state probability ...), in a duration of 12 days (excluding 4 acclimation days) . 
- Processed: using one-minute time bins of movement records to binary score the activity into 0 (IS: inactive state) and 1 (AS: active state); using thirty-minute bins of food records to calculate the amount of chows consumed by mice; using LS periodogram technique to select the appropriate time bins for above.
- Output: different patterned visualization for each feature, with the appropriate time bins that presents the most significant ultradian pattern.



## Method and models
- Seasonal decomposition.
- Decomposition based on the rate of change.
- the Trend Component  that reflects the long term progression of the series (secular variation)
- the Cyclical Component  that describes repeated but non-periodic fluctuations
- the Seasonal Component  reflecting seasonality (seasonal variation)
- the Irregular Component  (or "noise") that describes random, irregular influences. It represents the residuals of the time series after the other components have been removed.

- Decomposition based on predictability.
- Longitudinal data analysis.
- Definition: A longitudinal study refers to an investigation where participant outcomes and possibly treatments or exposures are collected at multiple follow-up times.
-Strategies for Analyzing Longitudinal Data: 
- Traditional Repeated Measures ANOVA
- Mixed Models Anova
- Regression
- Multilevel Modeling

- Autocorrelation analysis. 
- Autocorrelation, also known as serial correlation or cross-autocorrelation, is the cross-correlation of a signal with itself at different points in time (that is what the cross stands for). Informally, it is the similarity between observations as a function of the time lag between them. It is a mathematical tool for finding repeating patterns, such as the presence of a periodic signal obscured by noise, or identifying the missing fundamental frequency in a signal implied by its harmonic frequencies. It is often used in signal processing for analyzing functions or series of values, such as time domain signals.


##Testing Framework Outline
- Generate random samples to see whether they are consistent with results before.


## Reference
- Lloyd, David, and Ernest L. Rossi, eds. Ultradian rhythms in life processes: An inquiry into fundamental principles of chronobiology and psychobiology. Springer Science & Business Media, 2012.
- Stephenson, Richard, et al. "Sleep-Wake Behavior in the Rat Ultradian Rhythms in a Light-Dark Cycle and Continuous Bright Light." Journal of biological rhythms 27.6 (2012): 490-501.
