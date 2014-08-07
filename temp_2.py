import itertools
import random

#set up the deck
def getDeck():
	deck=list(itertools.product(range(3),range(3),range(3),range(3),[False]));
	idx=['col','shape','fill','num','dealt'];
	deck=[dict(zip(idx,x)) for x in deck];
	return deck
	
def deal(deck):
	not_dealt=[x for x in range(len(deck)) if not(deck[x]['dealt'])];
	idx=random.sample(not_dealt,12);
	in_play=list([]);
	print idx
	for i in idx:
		# print deck[i]['dealt']
		deck[i]['dealt']=True;
		in_play.append(deck[i]);
	return in_play,deck
	
		
# print deck;
deck=getDeck();
in_play,deck=deal(deck);
picked=[0,1,2];
picked=[in_play[i] for i in picked];
keys_all=picked[0].keys();
picked=[ len(set([one_dict.get(key) for one_dict in picked])) for key in picked[0].keys() if not(key=='dealt')];
print picked
print picked.count(2)==0
picked=[1,3,1,3]
print picked.count(2)==0
print picked
# picked=zip(*picked);
# print picked



# print a
# a.update(in_play[picked[1]]);
# print a

# print deck