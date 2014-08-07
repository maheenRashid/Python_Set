import Deck
import random

class Game:
	def __init__(self):
		self.deck=Deck.Deck(True);
	
	def deal(self):
		not_dealt=[];
		self.in_play=Deck.Deck();
		
		for i in range(len(self.deck)):
			if not(self.deck[i].dealt):
				not_dealt.append(i);
		idx=random.sample(not_dealt,12);
		for i in idx:
			self.deck[i].dealt=True;
			self.in_play.append(self.deck[i]);
	
	def isSet(self,idx):
		assert len(idx)==3;
		set=Deck.Deck();
		for i in idx:
			set.append(self.in_play[i]);
		return set.isSet();
	
game=Game();
game.deal();
game.in_play.print_deck();
print game.isSet([0,0,0]);
