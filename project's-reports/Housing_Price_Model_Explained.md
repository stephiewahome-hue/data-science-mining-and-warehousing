# The House Price Guessing Game — Explained Simply

## The Goal

Imagine you have a list of 506 houses in Boston. For each house, you know things like:
- How many rooms it has
- How old it is
- How much crime happens nearby
- How good the nearby schools are (measured by student-to-teacher ratio)
- How far it is from job centers

The computer's job is to guess the **price** of a house just by looking at these clues.

## Step 1: Get the Information

The notebook loads a table of 506 houses. Each one has 13 clues (rooms, age, crime rate, etc.) plus the actual price, which is what we're trying to predict.

## Step 2: Look Around First

Before guessing anything, the notebook peeks at the data:
- Checks that nothing important is missing (nothing was — all 506 houses have complete info)
- Looks at which clues seem to matter most for price

It found that the **number of rooms** is a strong clue — more rooms usually means a pricier house. Crime rate and pollution level tend to push price *down*.

## Step 3: Study, Then Take a Test

The houses get split into two piles:
- **A big pile (80%, about 404 houses)** — used to *study* and learn patterns
- **A small pile (20%, about 102 houses)** — used to *quiz* the model afterward, on houses it has never seen

This is like studying with flashcards, then taking a test on new cards.

## Step 4: Try Three Different "Guessers"

The notebook trains three different guessing strategies and tests each one on the quiz pile:

| Guesser | How good is it? | Average mistake |
|---|---|---|
| **Linear Regression** (simple, straight-line guessing) | 80% | off by about $2,679 |
| **Random Forest** (a team of many small guessing trees voting together) | **93%** 🏆 | off by about $1,750 |
| **Gradient Boosting** (trees that learn from each other's mistakes one at a time) | 92% | off by about $1,791 |

*(The "how good" score means: out of all the differences in price between houses, what percent can this guesser correctly explain? Higher is better.)*

## Step 5: Double-Check It's Not a Fluke

Each guesser was re-tested a few more times on different slices of the study pile. Random Forest kept winning consistently, so its good score wasn't just luck.

## The Outcome 🏆

The **Random Forest** guesser won the competition.

- It correctly explains about **93% of why house prices differ** between houses.
- On average, its price guess is only off by about **$1.75** (values in the dataset are in thousands, so this is roughly $1,750 in real terms).
- The two biggest clues it relied on: **number of rooms** and **share of lower-income households nearby** — these mattered far more than any other clue.

**In one sentence:** if you show this model 100 new houses, it does a really good job estimating each one's price — good enough that the notebook recommends using Random Forest for real predictions.
