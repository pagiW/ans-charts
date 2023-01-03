import matplotlib.pyplot as plt
from data import data
import random

getSeg = lambda segment, type: tuple(filter(lambda obj: obj[type] == segment, data))
sects = tuple(set([obj['Segment Type'] for obj in data]))
type = tuple(set([obj['Segment Description'] for obj in data]))

question = random.choice(type)
print(question)

results = getSeg(question, 'Segment Description')

final = {element['Answer']: element['Percentage'] for element in results}
print(final)

fg, ax = plt.subplots()

ax.axis('equal')

ax.pie(tuple(final.values()), labels=tuple(final.keys()))

plt.savefig(f'{question}_fig.jpg')
plt.close()