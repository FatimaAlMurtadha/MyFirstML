# First DataSet: student_performence_finalscore:
### Dataset count
- 8000 rows and 18 columns
### Numerical Features (Hours_Studied , Sleep_Hours , Stress_Level , Final_Sc ore): --
- correlations
- scatter plots
- regression

### Categorical Features (Gender, Study+Method , Diet_Quality):
- countplots
- boxplots
- group analysis

### No missing Values
### No duplicates
### Data Types are correct
### Insight
- Previous_GPA (max = 6.7): 
    1. Ether that dataset is synthetic
    2. OR another system is used here

### Final_Score (22 -> 99 )
### Hours_Studied ( max = 12 )
### Sleep_Hours ( 3 -> 10 )
### Stress_Level ( 1 -> 10 ) --> scale

## Columns that would effect Final_Score
    1. Positive Correlation:
        - Hours_Studied
        - Attendance
        - Previouse_GPA
    2. Negative Correlation
        - Stress_Level
        - Screen_Time
        - Exam_Anxiety_Score

# 1. Numerical Columns: 
['Age', 'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Stress_Level',
       'Screen_Time', 'Previous_GPA', 'Tutoring_Sessions_Per_Week',
       'Exam_Anxiety_Score', 'Final_Score'] ( 8000 rows × 10 columns)

    - 1. more (Hours_Studied) => more Final score -> Strong positive correlation (Scatter plot)
    - 2. more (exam anxiety) less performance (Final score) -> Strong negative correlation
    - 3. more (Tutoring Sessions Per Week) more (Final Score) -> Correlation != causation -> we can't prove the the reason directly.
    - 4. more (Stress Level) less (Final Score) -> negative correlation 
    - 5. Who has a previous Good performance ability Would mostly still be good.
    - 6. (Screen Time) can cause a less final score -> Weak negative correlation
    - 7. Age -> No correlation

### Most important Positive factors:
1. Hours_Studied               --> 0.59    correlation
2. Tutoring_Sessions_Per_Week  --> 0.47    correlation
3. Previous_GPA                --> 0.29    correlation

### Most important Negative factors:
1. Exam_Anxiety_Score          --> -0.49    correlation
2. Stress_Level                --> -0.29    correlation
3. Screen_Time                 --> -0.13    correlation


# 2. Categorical columns
['Student_ID', 'Gender', 'Part_Time_Job', 'Study_Method', 'Diet_Quality',
       'Internet_Quality', 'Extracurricular', 'Family_Income_Level'] ( 8000 rows × 8 columns )

    - 3 unique values
    - Top = male
    - Part_Time_Job : yes/ no -- interssting / Do part time work effect final score
    - Most of Study_Method are offline interresting
    - Family_Income_Level: Middle =- dominant -- Analysis

# Final Summary 11-05-2026
## Key Correlations with Final Score

- Hours_Studied shows a strong positive correlation with Final_Score.
- Exam_Anxiety_Score has a strong negative correlation with performance.
- Tutoring sessions are positively associated with academic success.
- Screen time shows a weak negative relationship with scores.

# The cleaned df
- shape (8000, 17)

# Hypothesis 
- ( Students who study more hours tend to get higher final scores)
- (Higher exam anxiety may negatively affect academic performance)
- ( Student with tutoring session may achieve better score)


-------------------------------------------------------------------------------------------------------------------------


### DATA STORYTELLING - Correlation Heatmap ( Student Performance Final Score) 
- More hours studied + Tutoring sessions per week -> higher final score ( strong - positive - logic).
- More exam anxiety score + stress level -> less final score ( strong - negative - logic)
- Better Previous GPA -> good final score as before.
- Screen time + sleep hours -> final score ( weak - negative - logic)
- Age -> final score ( NO correlation at all) 
##### 1. Regular hours studied + tutoring sessions + previous GPA == Best positive factors for good final score
##### 2. Anxiety + stress + screen time == Worst negative factors on final score

### DATA STORYTELLING ( Hours studied vs Final score)
- More hours studied -> higher final score ( strong - positive - consistent relationship)
- BUT some students study a lot -> less final score (+ the opposite is true) -> ( Normal Variance)
- High-Performance Zone:
    1. hours studied ( 8 : 12 hours)
    2. final score ( 85 : 100 )
- Low-Performance Zone:
    1. hours studied ( 0 : 3 hours)
    2. final score ( 20 : 60 )
#### 1. Studying is the strongest factor affecting performance.
#### 2. Studying is not the only factor effecting high final score

### DATA STORYTELLING ( Exam anxiety vs Final score)
-  Higher exam anxiety score -> lower final score ( strong - negative - consistent)
- High-Performance Zone 
    1. ( 0 : 3 anxiety level)
    2. ( 80 : 100 final score)
- Lower-Performance Zone:
    1. ( 7: 10 anxiety level)
    2. ( decrease , absence of high score )
#### 1. Anxiety students clearly get lower scores.
#### 2. Anxiety may effect final score more than Hours_Studied

### DATA STORYTELLING ( Distribution of final score ) - The level of difficulty of the educational system and the performance of the students as a whole
- Overall performance is very high ( Most are above 80 - Peak 90 : 100 - Right-skewed ).
- Distribution is biased towards high scores.
- There are few weak students.

### DATA STORYTELLING ( Final score by study method "Online , Offline , Hybrid")
- (OFFLINE) Studying face-to-face tend to achieve better results ( Offline -> higher final score ).
- (ONLINE) Students still succeed in but may struggle with poor performance ( online -> weaker final score )..
- (HYBRID) Average performance and results ( hybrid -> medium final score ).

### DATA STORYTELLING (Pairplot of academic and psychological factors)
- Academic performance depends on a combination of academic effort and psychological state (Studying reduces anxiety).
- Anxiety and stress impair performance but the anxiety effect is stronger than stress.
