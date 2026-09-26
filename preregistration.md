# Analysis Preregistration

## Research question
Among college students, is greater weekly study time associated with a higher end-of-term exam score?

## Hypotheses
- **Null hypothesis (H0):** There is no linear association between weekly study time and exam score (population slope = 0).
- **Alternative hypothesis (H1):** Greater weekly study time is associated with a higher exam score (population slope > 0).
- Expected direction: positive.

## Population, sample, and exclusions
- **Target population:** College students completing an end-of-term examination.
- **Unit of analysis:** One student.
- **Planned sample:** 100 observations for the synthetic pipeline fixture.
- **Inclusion rules:** A row must contain a unique student ID, weekly study hours from 0 to 80, sleep hours from 0 to 24 per night, and an exam score from 0 to 100.
- **Exclusion rules:** Duplicate student IDs, missing values in analysis variables, and values outside the stated ranges will be excluded before analysis.
- **Stopping rule:** For the synthetic fixture, analysis stops at 100 valid observations. No additional observations are added after analysis begins.

## Variables and measures
- **Outcome:** `exam_score`, measured on a 0–100 scale.
- **Primary predictor:** `study_hours_per_week`, numeric hours studied per week.
- **Control variable:** `sleep_hours_per_night`, numeric average hours slept per night.
- **Transformation:** No transformation is planned.
- **Missing data:** Rows with missing values in the outcome, predictor, or control variable are excluded (complete-case analysis).
- **Data source:** The attached dataset is synthetic and is used only to test the reproducible analysis pipeline; it is not evidence about real students.

## Analysis plan
1. Validate the input schema and apply the preregistered inclusion/exclusion rules.
2. Calculate Pearson's correlation between weekly study hours and exam score.
3. Fit an ordinary least-squares linear regression predicting exam score from weekly study hours, with sleep hours as a control.
4. Use a two-sided alpha of 0.05 for the primary statistical test, while the preregistered directional hypothesis is positive.
5. Report the estimated study-time coefficient, 95% confidence interval, p-value, and R-squared.
6. Robustness check: repeat the regression using only observations with study time between the 1st and 99th percentiles of the synthetic sample and compare the estimated study-time coefficient with the primary result.
7. Check linearity and residual behavior descriptively; no post-hoc model changes are planned based on these checks.

## Deviations
No deviations are planned. Any later deviation from this preregistration must be recorded below with a timestamp and a reason.

| Timestamp | Deviation | Reason |
|---|---|---|
| None | None | No deviation at preregistration time |
