# Diabetes Risk Classification — Report

## 1. What we did

We used the **Pima Indians Diabetes dataset** (`Data-diabetes.csv`) — 768 patients, 8 health measurements each, and one label (`Outcome`: 1 = has diabetes, 0 = doesn't).

We cleaned the data (some columns had `0` where that's medically impossible, e.g. blood pressure of 0 — these were treated as missing and filled with the median), then trained three classification models:

- Logistic Regression
- Support Vector Machine (SVM)
- Neural Network (MLP)

Each model was trained on 80% of the patients and tested on the remaining 20% it had never seen.

## 2. Results

| Model | Accuracy | ROC-AUC | Precision | Recall | F1 |
|---|---|---|---|---|---|
| Logistic Regression | 0.71 | 0.81 | 0.60 | 0.50 | 0.55 |
| SVM | 0.74 | 0.80 | 0.65 | 0.56 | 0.60 |
| Neural Network | 0.72 | 0.82 | 0.60 | 0.63 | 0.61 |

**Confusion matrices** (rows = actual, columns = predicted; order is [No Diabetes, Diabetes]):

- Logistic Regression: `[[82, 18], [27, 27]]`
- SVM: `[[84, 16], [24, 30]]`
- Neural Network: `[[77, 23], [20, 34]]`

**Key risk factors** (from Logistic Regression coefficients, ranked by influence):

1. **Glucose** (blood sugar) — by far the strongest predictor
2. **BMI** (body weight)
3. **Pregnancies**
4. **Diabetes Pedigree Function** (family history score)
5. **Age**
6. Insulin, Blood Pressure, Skin Thickness — minimal effect

## 3. Explaineation

We gave a computer 768 patient report cards and asked it to spot the pattern behind who gets diabetes.

- **Accuracy** tells us how many guesses out of 100 were right (71–74%, so roughly 7 out of 10).
- **ROC-AUC** (0.80–0.82) tells us how good the model is at telling sick and healthy people apart in general — like a solid B+.
- **Precision** tells us: when the model says "you have diabetes," how often it's actually right (60–65%).
- **Recall** tells us: out of everyone who really has diabetes, how many the model actually caught. This is the most important one for health, because missing a sick person is worse than a false alarm. The Neural Network caught the most (63%).

The single biggest clue the computer found was **blood sugar level** — much bigger than anything else. Weight (BMI) came in second, and the number of past pregnancies was third. Blood pressure and skin thickness barely mattered at all.

## 4. Conclusion

- **No single model was overwhelmingly better than the others** — all three landed in a similar range (71–74% accuracy, ~0.80–0.82 ROC-AUC), which suggests the dataset's ceiling for these features is around there, not that one algorithm is clearly superior.
- **SVM gave the best precision** (fewest false alarms), while the **Neural Network gave the best recall** (caught the most true diabetes cases) — a classic precision/recall trade-off. If missing a real case is the bigger concern (as it usually is in healthcare), the Neural Network is the safer pick; if minimizing false alarms matters more, SVM is preferable.
- **Glucose and BMI are the dominant risk signals** in this data, consistent with established medical understanding of type 2 diabetes — a good sanity check that the models learned something real rather than noise.
- **None of the models are accurate enough to replace a real medical diagnosis.** All still misclassify roughly a quarter to a third of cases. Their realistic role is as a **screening aid** — flagging higher-risk patients for follow-up testing, not making the final call.
- **Next steps to improve this further:** more data, additional health features (e.g. HbA1c, family history detail), hyperparameter tuning, and/or trying tree-based models (Random Forest, Gradient Boosting) which often perform well on this kind of tabular health data.
