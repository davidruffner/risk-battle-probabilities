# risk-battle-probabilities
Scripts to calculate the odds of battles in the Game of Risk.

## Usage
```bash
python risk.py
python risk2v2.py
python risk3v1.py
```

## Calculation of risk battle odds.

### General case
When the offense has more than three armies and defense has more than two:

- Probability of defense losing two armies:
0.37
- Probability of offense losing two armies:
0.29
- Probability of both losing a single army:
0.34


### 2 vs 2
When the offense and
defense only have two armies, the offensive probabilities go way down
compared to the general case:

- Probability of defense losing two armies:
0.23
- Probability of offense losing two armies:
0.45
- Probability of both losing a single army:
0.32

### 3 vs 1
When the offense has three
armies and the defense only has one, the defense is at a significant
disadvantage:

- Probability of defense losing one army:
0.66
- Probability of offense losing one army:
0.34

So the probability of winning with three vs two is .66 and of losing is .34
So it's really pretty bad to have those ones by themselves.
However, is it worth it to split up all your armies so that all your
countries have two? I don't think so from experience. I like having large
armies to that I can win a series of battles deep into enemy territory.
