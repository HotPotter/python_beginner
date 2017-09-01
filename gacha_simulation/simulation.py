# Rarity = Common, Rare, Epic, Legendary

# CardPool = [Card]
from collections import namedtuple, Counter
import random
import cfg
import csv

Card = namedtuple('Card', ['identity', 'rarity', 'name'])

'''
card_pool = [Card(1, 'L', 'Longname'),
             Card(2, 'C', 'Commu'),
             Card(3, 'E', 'Exit'),
             Card(4, 'R', 'Redbull'),
             Card(5, 'C', 'Coke'),
             ]
'''

card_pool = []

def load_heroes(): #load hero cfg to populate card_pool
    global card_pool
    with open('hero.csv') as f:
        for hero_id, rarity, name in csv.reader(f):
            print(rarity)
            card_pool.append(Card(int(hero_id), rarity, name))

load_heroes()

rates = {'L':cfg.DROP_RATE_L,
         'C':cfg.DROP_RATE_C,
         'E':cfg.DROP_RATE_E,
         'R':cfg.DROP_RATE_R,
         } #load drop rate cfg

card_pool_rates = [rates[card.rarity] for card in card_pool] #provide list for random.choices

print(card_pool)
print('rates:', card_pool_rates)
print()

'''
cards = []
for _ in range(0, 100): # draw 100 times
    random_cards = random.choices(card_pool, card_pool_rates)
    card = random_cards[0]
    # print(card, card.identity, card.rarity)
    cards.append(card)
'''
cards = random.choices(card_pool, card_pool_rates, k=100) # draw 100 times

counter = Counter() #sum the result, count cards, Counter() is from the library
for card in cards:
    counter[card.identity] += 1 # count for every draw of a unique card

print(counter)
print(counter[5])

L = list(counter.items()) #extract key value out of counter
L.sort(key=lambda t: t[0]) # sort by card identity
for hero_id, count in L:
    print(f'hero {hero_id}: {count}')
