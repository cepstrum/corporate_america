import random 

class Business_card(object):
	#Defines the Business Card class. id: intiger id of card for shuffling purposes, possession: if a player posses this card, set int to player number, special: special card ability
	def __init__(self, id, name, cost, income, consumer_type, pr_problem, special, possession):
		self.name = name
		self.cost = cost
		self.income = income
		self.consumer_type = consumer_type
		self.pr_problem = pr_problem
		self.possession = possession

class Player(object):
	#defining player class
	def __init__(self, number, name, money):
		self.name = name
		self.number = number
		self.money = money
		self.businesses = []
		self.hand_of_business_cards = []
		self.executive_orders = []
		self.is_prez = False
	def add_business(self, business):
		self.businesses.append(business)
	def add_card(self, card):
		self.hand_of_business_cards.append(card)
	def add_executive_orders(self, executive_order):
		self.executive_orders.append(executive_order)
	def add_prez(self):
		self.is_prez = True
	def remove_prez(self):
		self.is_prez = False

def draw_business_card(Player, list_of_cards, draw_how_many):
#input a Player object and the current deck of business cards.
#this function draws (draw_how_many) cards from the deck, returns it, and the new deck with that card removed.
	for x in range(0, 0 + draw_how_many):
		number_of_cards = len(list_of_cards)
		drawn_card = random.randint(0,number_of_cards - 1)
		Player.hand_of_business_cards.append(list_of_cards[drawn_card])
		list_of_cards.pop(drawn_card)	
	return (Player.hand_of_business_cards, list_of_cards)


#definition of all Business cards
#TO DO: add remaining cards
greenwash_consulting = Business_card(1, "GREENWASH CONSULTING", 6, 8, ["Green"], [], ["Lobbyist"], 0)
natural_beauty_rhinoplasty = Business_card(2, "NATURAL BEAUTY RHINOPLASTY", 8, 6, ["Luxury", "Health"], [], [], 0)
faux_news = Business_card(3, "FAUX  NEWS", 5, 4, ["Media"], [], ["Lobbyist", "Sponsered"], 0)
start_worrying_insurance = Business_card(4, "START WORRYING INSURANCE", 4, 4, ["Finance", "Health"], [], [], 0)
the_liberal_media = Business_card(5, "THE LIBERAL MEDIA", 5, 4, ["Media"], [], ["Lobbyist", "Sponsered"], 0)
hard_crock_cafe = Business_card(6,"HARD CROCK CAFE", 4, 4, ["Entertainment", "Food"], [], [], 0)
pu_power = Business_card(7, "PU POWER", 4, 8, ["Energy"], [], [], 0)
pharmopticon = Business_card(8, "PHARMOPTICON", 10, 6, ["Technology", "Health"], [], [], 0)
happy_ending_pictures = Business_card(9, "HAPPY ENDING PICTURES", 4, 8, ["Entertainment"], [], [], 0)
bank_of_shamerica = Business_card(10, "BANK OF SHAMERICA", 4, 4, ["Finance", "Home"], [], [], 0)
genetifood = Business_card(11, "GENETIFOOD", 10, 6, ["Technology", "Food"], [], [], 0)
big_journey_suvs = Business_card(12, "BIG JOURNEY SUVS", 12, 8, ["Transportation", "Luxury"], ["Polluting"], [], 0)
mud_hole_acupuncture = Business_card(13, "MUD HOLE ACUPUNCTURE", 5, 4, ["Health", "Green"], [], [], 0)
lights_camera_megachurch = Business_card(14, "LIGHTS CAMERA MEGACHURCH", 5, 4, ["Media"], [], ["Lobbyist", "Sponsered"], 0)
chupadinero_casino = Business_card (15, "CHUPADINERO CASINO", 10, 5, ["Entertainment", "Finance", "Sin"], [], [], 0)
sweatibank = Business_card(16, "SWEATIBANK", 4, 8, ["Entertainment"], [], [], 0)
start_up_labs = Business_card(17, "START UP LABS", 15, 4, ["Technology", "Finance"], [], ["Job Creater"], 0)
heavy_lid_dispensaries = Business_card(18, "HEAVY LID DISPENSARIES", 4, 5, ["Health", "Sin"], [], [], 0)
pantent_trolls = Business_card(19, "PATENT TROLLS", 4, 6, ["Finance"], [], [], 0)
naive_bottled_water = Business_card(20, "NAIVE BOTTLED WATER", 8, 6, ["Luxury", "Food"], ["Polluting"], [], 0)
factory_farms = Business_card(21, "FACTORY FARMS", 4, 10, ["Food"], ["Polluting", "Labor"], [], 0)
back_alley_business_models = Business_card(22, "BACK ALLEY BUSINESS MODELS", 4, 6, ["Finance"], [], ["Think Tank"], 0)
soal_of_coal = Business_card(23, "SOAL OF COAL", 12, 8, ["Energy", "Home"], ["Polluting"], [], 0)
something_hippie_farms = Business_card(24, "SOMETHING HIPPIE FARMS", 5, 4, ["Green", "Food"], [], [], 0)
jocks_trap = Business_card(25, "JOCK'S TRAP", 4, 4, ["Entertainment", "Health"], [], [], 0)
oggle_search = Business_card(26, "OGGLE SEARCH", 6, 4, ["Technology", "Media"], [], ["Sponsered"], 0)
solacel = Business_card(27, "SOLACEL", 10, 6, ["Energy", "Green"], [], [], 0)
speedbump_cycles = Business_card(28, "SPEEDBUMP CYCLES", 4, 4, ["Transportation", "Health"], [], [], 0)
bo_railroad = Business_card(29, "B.O. RAILROAD", 4, 8, ["Transportation"], [], [], 0)
bro_ribbon_draft = Business_card(30, "BRO RIBBON DRAFT", 4, 5, ["Food", "Sin"], [], [], 0)
business_card_deck = [greenwash_consulting, natural_beauty_rhinoplasty, faux_news, start_worrying_insurance, the_liberal_media, hard_crock_cafe, pu_power, pharmopticon, happy_ending_pictures, bank_of_shamerica, genetifood, big_journey_suvs, mud_hole_acupuncture, lights_camera_megachurch, chupadinero_casino, sweatibank, start_worrying_insurance, heavy_lid_dispensaries, pantent_trolls, naive_bottled_water, factory_farms, back_alley_business_models, soal_of_coal, something_hippie_farms, jocks_trap, oggle_searc...(line truncated)...



x = raw_input("How many players? (3-5) ")
while (x != "3") and (x != "4") and (x != "5"):
	x = raw_input("Please choose a number of players between 3 and 5")
print (x)
name1 = raw_input("Enter name for player 1: ")
player1 = Player(1, name1, 42)
name2 = raw_input("Enter name for player 2: ")
player2 = Player(2, name2, 42)
name3 = raw_input("Enter name for player 3: ")
player3 = Player(3, name3, 42)
if (x == "4") or (x == "5"):
	name4 = raw_input("Enter name for player 4: ")
	player4 = Player(4, name4, 42)
	if (x == "5"):
		name5 = raw_input("Enter name for player 5: ")
		player5 = Player(5, name5, 35)
		player1.money = 35
		player2.money = 35
		player3.money = 35
		player4.money = 35




print player3.money


#testing
#player1.hand_of_business_cards, list_of_business_cards = draw_business_card(player1, business_card_deck,2)
#print player1.hand_of_business_cards[0].name
#Sprint player1.hand_of_business_cards[1].name
