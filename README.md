# sample randomization in the Rasch analysis
Sample randomization across time points for Rasch Analysis of Repeated Measures

## What we have:
A dataset of records of different participants that each participant was questioned (has entries) at different time points
![01](https://user-images.githubusercontent.com/82238399/206615620-d901c9da-ff59-4485-b030-b28ddc8d9aa8.png)

## What we want:
We need to randomly choose one time point for each participant's data 

## Remark:
some participants have one or more time points with missing data. In this situation, we must choose our random sample for these participants from complete (not missing) records of them.

## Solution:
In this python code, we use the random function in the python library (that uses the Mersenne Twister algorithm to generate random numbers) to choose a random time point for each participant.

## How to use the code:
Run the code in a python compiler like PyCharm or Atom.
### Don’t have programming knowledge? 
Copy and paste the code from the "sample-rand.py" file into an online compiler like https://www.programiz.com/python-programming/online-compiler/ and hit "Run"

## What is Rasch Analysis?
The Rasch model, named after Georg Rasch, is a psychometric model for analyzing categorical data, such as answers to questions on a reading assessment or questionnaire responses, as a function of the trade-off between the respondent's abilities, attitudes, or personality traits, and the item difficulty. For example, they may be used to estimate a student's reading ability or the extremity of a person's attitude to capital punishment from responses to a questionnaire. In addition to psychometrics and educational research, the Rasch model and its extensions are used in other areas, including the health profession, agriculture, and market research. (Wikipedia)
