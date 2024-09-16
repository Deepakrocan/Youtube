# and: Both conditions must be True.
# or: At least one condition must be True.
# not: Reverses the condition.

it_raining = True
it_cold = False

if it_raining and it_cold:
    print("It's raining and cold. stay inside")

elif it_raining or it_cold:
    print("Take precaution, it either raining or cold")

else:
    print("the weather is nice!")