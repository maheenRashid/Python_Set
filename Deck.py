import itertools

class Card(object):
	def __init__(self,color=None,shade=None,number=None,shape=None,dealt=False):
		self.color = color
		self.shade = shade
		self.number = number
		self.shape = shape
		self.dealt = dealt
	
	def print_card(self):
		print self.color,self.shade,self.number,self.shape;
	
class Deck(list):
	
	def __init__(self,full=False):
		if full:
			shades=['fill','empty','stripe'];
			colors=['red','blue','green'];
			shapes=['curvy','oval','diamond'];
			numbers=range(3);
			all_lists=[colors,shades,numbers,shapes];
			
			
			for c in colors:
				for sh in shades:
					for n in numbers:
						for s in shapes:
							self.append(Card(c,sh,n,s,False));
		else:
			self=[];
	
	
	def isSet(self):
		bool=self.isSet_attr(self[0],self[1],self[2],'color');
		bool=bool and self.isSet_attr(self[0],self[1],self[2],'shape');
		bool=bool and self.isSet_attr(self[0],self[1],self[2],'number');
		bool=bool and self.isSet_attr(self[0],self[1],self[2],'shade');
		return bool;
	
	def isSet_attr(self,a,b,c,attr):
		attr_list=[eval('a.'+attr),eval('b.'+attr),eval('c.'+attr)];
		print attr_list;
		attr_set=set(attr_list);
		print attr_set
		print len(attr_set)
		if len(attr_set)==1 or len(attr_set)==3:
			print "true"
			return True;
		else:
			print "false"
			return False;
	
	def print_idx(self,idx):
		for i in idx:
			self[i].print_card();
	
	def print_deck(self):
		for i in self:
			i.print_card();