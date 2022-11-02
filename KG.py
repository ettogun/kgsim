import random
import re
from sys import exit

import KG1intro # intro lines
import KG2flavor # delicious
import KG3craft # food and junk
import KG4weather # weather
import KG5murder # murders
import KG6trial # trial pers
import KG7events # event
import KG7eventsb # more event
import KG8execution # executions

import schoolint # intro
import schoolintd # day and night cycles
import schooltics # actions

def mud(argument):
    return argument.upper()

## EVENTS AND FLAGS


events = {
	"winflag": "no",
	"trialint": "no",
		}
		
murderlist = [
	KG5murder.knife,
	KG5murder.poison,
	KG5murder.suicide,
	KG5murder.hotwater,
	KG5murder.choked,
	KG5murder.pool,
	KG5murder.smash,
	KG5murder.oven,
	KG5murder.freeze
	]
	
executionlist = [
	KG8execution.fanmail,
	KG8execution.bythegun,
	KG8execution.slammer,
	KG8execution.thousandcuts,
	KG8execution.stonesoup,
	KG8execution.redherring,
	KG8execution.magicshow,
	KG8execution.bomb,
	KG8execution.snowcountry,
	KG8execution.highheel,
	KG8execution.railroaded,
	KG8execution.barkingmad,
	KG8execution.strongman
	]
	
funevents = [
	KG7events.obstaclecourse,
	KG7events.cookies,
	KG7events.robotto,
	KG7eventsb.funmagic
	]


# LIVING PLAYER VALUES


icons = [] # emojitar
players = [] # player characters
talents = [] # their talents, tic modifier
sex = [] # pronoun modifier
personality = [] # tic mod
secondary = [] # tic mod
likesa = [] # first like
likesb = [] # second like
dislikesa = [] # dislike
dislikesb = [] # dislike


# DEAD PLAYER VALUES starts with d


dplayers = []
dreason = []
dicons = []
dtalents = []
dsex = []
dpersonality = []
dsecondary = []
dlikesa = []
dlikesb = []
ddislikesa = []
ddislikesb = []


# THE KILLER starts with k


knames = []
kicon = []


# LISTS FOR LIKES/DISLIKES


likesc = []
dislikesc = []
alltastes = []


# BASIC COMMANDS


def id(list, thing):
	number = list.index(thing)
	return number
	
	
def randc(list):
	choice = random.choice(list)
	return choice
	
	
def rands(list, count):
	sample = random.sample(list, count)
	return sample
	

def dice(a, b):
	roll = random.randint(a, b)
	return roll
	

def party():
	count = len(players)
	return count


def multiappend(list, *stuff):
	for things in stuff:
		list.append(things)
		
		
def pagebreak(p=False, n=False, b=False):
	if p is True:
		input("\n" + ("-" * 42))
	elif n is True:
		input(("-" * 42) + "\n")
	elif b is True:
		input("\n" + ("-" * 42) + "\n")
	else:
		input("-" * 42)
		
		
def border():
	print("-" * 42)
		
		
def center(text):
	print(str.center(text, 42))
		
		
# CHARACTER GENERATOR

def namegen():
	border()
	schoolint.introtext()
	print("""You need to have at least 3 people, up to a maximum of 10.
	
Just say [DONE] if you're finished, and [EXIT] if you've changed your mind.
""")
	makechar = True
	while makechar is True and party() < 10:
		choice = input("> ")
		if choice.lower() not in ["", "done", "exit"] and choice not in players:
			genadd = True
			while genadd is True:
				gender = input("Sex (M or F or O): ")
				if gender.upper() in ["M", "F", "O"]:
					players.append(choice)
					sex.append(gender.upper())
					print(f"\n[✅] {choice} ({gender.upper()}) added!\n")
					genadd = False
				else:
					print("(M)ale, (F)emale, or (O)ther only, please!\n")
					continue
		elif choice.lower() == "done" and party() >= 3:
			makechar = False
		elif choice.lower() == "done" and party() < 3:
			print("\nThat's not enough people!\n")
		elif choice.lower() == "exit":
			print("\nGame exiting...\n\nWe hope you'll join us again some other time.")
			exit(0)
		elif choice == "":
			print("\nYou need to put a name.\n")
		elif choice in players:
			print("\nSorry, no duplicate names.\n")
	print("\nHere is your roster. Is this correct?\n")
	basic()
	choice = True
	while choice is True:
		print("\n1. [FINISH]")
		print("2. [EDITOR]\n")
		edit = input("> ")
		if edit.lower() in ["1", "finish"]:
			print("\nGame starting... selecting setting...")
			choice = False
		elif edit.lower() in ["2", "editor"]:
			choice = False
			editor()
		else:
			print("\nThat's not a choice.")
	brain()
	introchoice()


## CHARACTER EDITOR
		
		
def editor():
	edit = True
	print("\nWelcome to the editor.")
	print("How may I help you?\n")
	print("Current characters:\n")
	basic()
	while edit is True:
		print("\n1. [ADD] a character")
		print("2. [REMOVE] a character")
		print("3. [FINISH]\n")
		choice = input("> ")
		if choice.lower() in ["1", "add"] and party() < 10:
			newname = input("\nEnter a name for your new character: ")
			players.append(newname)
			genderflag = False
			while genderflag is False:
				newgend = input("M, F or O? ")
				if newgend.upper() in ["M", "F", "O"]:
					print(f"\n{newname} ({newgend.upper()}) added.")
					sex.append(newgend.upper())
					genderflag = True
				else:
						print("M, F, or O only, please.")
		elif choice.lower() and choice.lower() in ["add", "1"]:
			print("\nThat's too many people!")
			print("You have to remove one if you want to add another.")
		elif choice.lower() in ["remove", "2"] and party() > 3:
			basic()
			print("\nWho do you want to remove?\n")
			remflag = True
			while remflag is True:
				rem = input("> ")
				if rem in players:
					index = id(players, rem)
					del players[index]
					del sex[index]
					print(f"\n{rem} removed. Goodbye!")
					remflag = False
				elif rem not in players:
					print("Hey, did you spell that right? Please try again.")
		elif choice.lower() in ["remove", "2"]:
			print("\nYou need a minumum of 3 people!")
		elif choice.lower() in ["finish", "3"]:
			edit = False
			print("\nGame starting... selecting setting...".upper())
		else:
			print("\nThat's not an option.")


## ASSIGN ATTRIBUTES
			
			
def brain():
		
	iconlist = rands(KG2flavor.iconchoice, party())
	talented = rands(KG2flavor.talentchoice, party())
	
	for icon, talent in zip(iconlist, talented):
		avi = f"[{icon}]"
		icons.append(avi)
		talents.append(talent)
		
	for everyone in players:
		tastes = rands(KG2flavor.likes, 2)
		distastes = rands(KG2flavor.likes, 2)
		personality.append(randc(KG2flavor.persc))
		secondary.append(randc(KG2flavor.persc))
		likesa.append(tastes[0])
		likesb.append(tastes[1])
		dislikesa.append(distastes[0])
		dislikesb.append(distastes[1])
		multiappend(dislikesc, distastes[0], distastes[1])
		multiappend(likesc, tastes[0], tastes[1])
		multiappend(alltastes, tastes[0], tastes[1], distastes[0], distastes[1])


## PROFILING


def basic():
	c = 1
	for (a, b) in zip(players, sex):
		print(f"{c}. {a} ({b})")
		c += 1


def profile(name):
	b = id(players, name)
	print(f"""
Name: {players[b]}
Talent: {talents[b]}
Gender: {sex[b]}
Personality: {personality[b]}
Secondary: {secondary[b]}
Likes: {likesa[b]}, {likesb[b].lower()}
Dislikes: {dislikesa[b]}, {dislikesb[b].lower()}
""") # """


def allintro():
	center("[BEGIN INTRODUCTIONS]")
	pagebreak()
	# your full intro
	for person in players:
		no = id(players, person)
		center(f"{icons[no]} {person}, the SHSL {talents[no]}!")
		pagebreak()
		profile(person)
		onetic(person, KG1intro.classTics)
		onetic(person, KG1intro.lookTics)
		pagebreak(p=True)
		
	center("[END INTRODUCTIONS]")


## DICTS and TICS


def lookup(name, choice, Dead=False):
	# this thing looks up!
	
	if Dead is True:
		i = id(dplayers, name)
		a, b, c, d, e, f, g, h, j = [
		dsex[i], dicons[i], dtalents[i], dpersonality[i], dsecondary[i], dlikesa[i], dlikesb[i], ddislikesa[i], ddislikesb[i]]
	
	else:
		i = id(players, name)
		a, b, c, d, e, f, g, h, j = [
		sex[i], icons[i], talents[i], personality[i], secondary[i], likesa[i], likesb[i], dislikesa[i], dislikesb[i]]
	
	returndict = {
	"n" : name,
	"id" : i,
	"s" : a,
	"ico" : b,
	"tal" : c,
	"per" : d,
	"sec" : e,
	"la" : f,
	"lb" : g,
	"da" : h,
	"db" : j
	}
	
	return returndict[choice]
	
	
def avatar(name, Dead=False):
	if Dead is False:
		icon = icons[players.index(name)]
	else:
		icon = icons[dplayers.index(name)]
		
	return icon
	

# """ IGNORE THIS LINE THANKS # """

		
def gendict(name, taste="", Switch=False, Dead=False):
	# yer general dictionary
	if Dead is False:
		sexid = lookup(name, "s")
	elif Dead is True:
		sexid = lookup(name, "s", Dead=True)
	
	if sexid == "M":
		a, b, c, d, e, f = ["He", "he", "His", "his", "Him", "him"]
	elif sexid == "F":
		a, b, c, d, e, f = ["She", "she", "Her", "her", "Her", "her"]
	elif sexid == "O":
		a, b, c, d, e, f = ["E", "e", "Er", "er", "Em", "em"]
	
	if Switch is False:
		named, aa, bb, cc, dd, ee, ff = ["(NAME)", "(HE)", "(he)", "(HIS)", "(his)", "(HIM)", "(him)"]
	elif Switch is True:
		named, aa, bb, cc, dd, ee, ff = ["(NAME2)", "(E)", "(e)", "(ER)", "(er)", "(EM)", "(em)"]
	
	prodict = {
	"(FLAVOR)": taste.lower(),
	named: name,
	aa : a,
	bb : b,
	cc : c,
	dd : d,
	ee : e,
	ff : f
	}
	
	return prodict
		
		
def thedict(dictionary, message):
	# THE dictionary, one and only
	regex = re.compile("|".join(map(re.escape, dictionary.keys())))
	action = regex.sub(lambda match: dictionary[match.group(0)], message)
	return action


def groupaction(list):
	# 3-5 characters perform a group action
	# do I need this?
	iconcollect = []
	pick = dice(3, 5)
	if pick > party():
		pick = 3
	chosen = rands(players, pick)
	for persons in chosen:
		iconcollect.append(avatar(persons))
	end = chosen.pop()
	if len(chosen) >= 2:
		joint = ", and "
	else:
		joint = " and "
	print("".join(iconcollect) + " " + ", ".join(chosen) + joint + end + randc(list))
	
	
def onetic(player, list):
	# performs a single gendered tic with friend, if necessary. can have no people, theoretically
	tic = randc(list)
	
	if "(NAME2)" in tic:
		needfriend = True
		while needfriend is True:
			friend = randc(players)
			if friend != player:
				printcons = avatar(player) + avatar(friend) + " "
				needfriend = False
				
	elif "(NAME)" in tic or "(HE)" in tic or "(he)" in tic or "(HIS)" in tic or "(his)" in tic or "(HIM)" in tic or "(him)" in tic:
		printcons = avatar(player) + " "
		
	else:
		printcons = ""

	dictionary = gendict(player)
	action = thedict(dictionary, tic)
	
	if "(NAME2)" in tic:
		dictionary2 = gendict(friend, Switch=True)
		twoact = thedict(dictionary2, action)
		print(printcons + twoact)
	
	else:
		print(printcons + action)
	

def dupetest(list):
	# tries to avoid duplicates, sends an automated flavor, too
	secondchance = dice(1, 100)
	
	if len(list) >= party() and secondchance > 45:
		mixedtics(list, Random=True)
	else:
		dupetics(list)
			
	
def dupetics(list, Dead=False, Mourn=False):
	# every character does a random action with random flavor from player tastes. dupes allowed.
	templist = []
	for persons in players:
		tic = randc(list)
		if "(NAME2)" in tic:
			needfriend = True
			while needfriend is True:
				if Dead is False and Mourn is False:
					friend = randc(players)
					if friend != persons:
						printcons = avatar(persons) + avatar(friend) + " "
						needfriend = False
				elif Dead is True:
					friend = dplayers[-1]
					printcons = avatar(persons) + " "
					needfriend = False
				elif Mourn is True:
					friend = randc(dplayers)
					printcons = avatar(persons) + " "
					needfriend = False
				else:
					continue
			
		elif "(NAME)" in tic:
			printcons = avatar(persons) + " "
		else:
			printcons = ""
			
		flavor = randc(alltastes)
		dictionary = gendict(persons, flavor)
		action = thedict(dictionary, tic)
		
		if "(NAME2)" in tic and Dead is False and Mourn is False:
			dictionary2 = gendict(friend, Switch=True)
			action = thedict(dictionary2, action)
			
		elif "(NAME2)" in tic and Dead is True or Mourn is True:
			dictionary2 = gendict(friend, Switch=True, Dead=True)
			action = thedict(dictionary2, action)
		
		fullact = printcons + action
		templist.append(fullact)
		
	random.shuffle(templist)
	
	counter = 0
	if len(templist) > 4:
		for each in templist:
			print(each + "\n")
			counter += 1
			if counter == 4:
				pagebreak(n=True)
				counter = 0
	elif len(templist) <= 4:
		for each in templist:
			print(each + "\n")
			
			
def mixedtics(list, flavor="", Dead=False, Mourn=False, Random=True):
	# every character does a random action with random flavor from player tastes. unique only, can set flavor.
	uniquetics = rands(list, party())
	templist = []
	for persons in players:
		tic = uniquetics.pop()
		if "(NAME2)" in tic:
			needfriend = True
			while needfriend is True:
				if Dead is False and Mourn is False:
					friend = randc(players)
					if friend != persons:
						printcons = avatar(persons) + avatar(friend) + " "
						needfriend = False
				elif Dead is True:
					friend = dplayers[-1]
					printcons = avatar(persons) + " "
				elif Mourn is True:
					friend = randc(dplayers)
					printcons = avatar(persons) + " "
				else:
					continue
			
		elif "(NAME)" in tic:
			printcons = avatar(persons) + " "
		else:
			printcons = ""
			
		if Random is True:
			flavor = randc(alltastes)
			dictionary = gendict(persons, flavor)
			action = thedict(dictionary, tic)
			
		elif Random is False:
			dictionary = gendict(persons, flavor)
			action = thedict(dictionary, tic)
			
		if "(NAME2)" in tic and Dead is False and Mourn is False:
			dictionary2 = gendict(friend, Switch=True)
			action = thedict(dictionary2, action)
			
		elif "(NAME2)" in tic and Dead is True or Mourn is True:
			dictionary2 = gendict(friend, Switch=True, Dead=True)
			action = thedict(dictionary2, action)
		
		fullact = printcons + action
		templist.append(fullact)
		
	random.shuffle(templist)
	
	counter = 0
	if len(templist) > 4:
		for each in templist:
			print(each + "\n")
			counter += 1
			if counter == 4:
				pagebreak(n=True)
				counter = 0
	elif len(templist) <= 4:
		for each in templist:
			print(each + "\n")
	

def loveorhate(like, list, choice):
	# might add more text to this eventually
	fullicon = icons[id(list, like)] + " " + players[id(list, like)]
	thing = like.lower()
	
	if choice == "love":
		print(f"{fullicon} is so happy. [❤️]")
		print(f"{fullicon} loves {thing}!\n")
	if choice == "hate":
		print(f"{fullicon} hates this. [💢]")
		print(f"{fullicon} hates {thing}!\n")
		
		
def tastetest(like):
	# just a connector for loveorhate
	for tastes in alltastes:
		if tastes == like and like in likesa:
			loveorhate(like, likesa, "love")
		if tastes == like and like in likesb:
			loveorhate(like, likesb, "love")
		if tastes == like and like in dislikesa:
			loveorhate(like, dislikesa, "hate")
		if tastes == like and like in dislikesb:
			loveorhate(like, dislikesb, "hate")
		
		
### BEGIN SETTING AND EVENTS


def introchoice():
	print("\n[✅] Your setting is:\n")
	border()
	center("[HOPE'S PEAK ACADEMY][🏫]")
	border()
	print("\nWould you like to read the introduction?")
	print("\n1. [YES]")
	print("2. [NO]\n")
	looping = True
	while looping is True:
		intropt = input("> ")
		if intropt.lower() in ["yes", "1"]:
			schoolint.fullintro()
			looping = False
		elif intropt.lower() in ["no", "2"]:
			print("\nLet's get everyone ready...")
			pagebreak(p=True)
			allintro()
			print("\nWe hope you have a wonderful school life!")
			pagebreak()
			looping = False
		else:
			print("\nYes or no, please.\n")
	schoolintd.day1()
	daycycle()
			
			
def chardel(player):
	dplayers.append(player)
	
	a = id(players, player)
	likesc.remove(likesa[a])
	likesc.remove(likesb[a])
	
	list = [icons, sex, talents, personality, secondary, likesa, likesb, dislikesa, dislikesb]
	
	dlist = [dicons, dsex, dtalents, dpersonality, dsecondary, dlikesa, dlikesb,  ddislikesa, ddislikesb]
	
	for alive, dead in zip(list, dlist):
		dead.append(alive.pop(a))
		
	players.remove(player)
	
	
def killroll():
	killer = randc(players)
	knames.append(killer)
	kicon.append(avatar(killer))
	victimflag = True
	while victimflag is True:
		victim = randc(players)
		if victim != killer:
			victimflag = False
		else:
			continue
	dreason.append(f" was murdered by {killer}.")
	chardel(victim)
	return killer, victim
	
	
def murderscenes(killed, finders, daycount, cycle, tod):
	random.shuffle(murderlist)
	play = murderlist.pop()
	return play(killed, finders, daycount, cycle, tod)
	
	
def executions(killer):
	random.shuffle(executionlist)
	play = executionlist.pop()
	return play(killer)
	
	
def randevents(daycount, cycle, tod):
	random.shuffle(funevents)
	play = funevents.pop()
	return play(daycount, cycle, tod)


def finalresults():
	center("[FINAL RESULTS]\n")
	i = 0
	for thedead in dicons:
		print("[☠️] " + dplayers[i] + dreason[i] + "\n")
		i += 1
		

def menu(a):
	# breakfast isn't real okay
	center(f"[🍽][{a} TIME]\n")
	thefood = randc(KG3craft.cook)
	thedrink = randc(KG3craft.drink)
	adjective = randc(KG3craft.adjcook)
	center(f"The class is served a {adjective} meal of")
	center(f"{thefood.lower()} and {thedrink.lower()}.\n")
	tastetest(thefood)
	tastetest(thedrink)
	

def daycycle():
	daycount = 2 # the day
	cycle = 0 # time of day
	event = 0 # rising event chance
	funevent = 0 # fun event chance
	pagebreak()
	tod = ["[☀️] DAY", "[☀️] AFTERNOON", "[🌙] NIGHT"]
	theweather = ["[☀️] SUNNY", "[🌤] CLOUDY", "[🌧] RAINY", "[⛈] STORMY", "[☃️] SNOWY"]
	
	while events["winflag"] == "no":
		center(f"[📅][DAY {daycount}: {tod[cycle]}]")
		pagebreak(n=True)
		if cycle == 0:
			dailyweather = randc(theweather)
			center(f"[📢] {randc(schooltics.loudspeaker)}...\n")
			print("There's an announcement...\n")
			print(f"\"{randc(schooltics.gmorning)}\"\n")
			print(f"\"Today the weather is {dailyweather}.\"\n")
			if dailyweather == theweather[0]:
				wreport = KG4weather.sunny
				daymood = KG4weather.sunmood
				daytic = schooltics.day
				noontic = schooltics.noon
			elif dailyweather == theweather[1]:
				wreport = KG4weather.cloudy
				daymood = KG4weather.sunmood
				daytic = schooltics.day
				noontic = schooltics.noon
			elif dailyweather == theweather[2]:
				wreport = KG4weather.rainy
				daymood = KG4weather.rainmood
				daytic = schooltics.rainyday
				noontic = schooltics.rainynoon
			elif dailyweather == theweather[3]:
				wreport = KG4weather.stormy
				daymood = KG4weather.stormmood
				daytic = schooltics.stormyday
				noontic = schooltics.stormynoon
			elif dailyweather == theweather[4]:
				wreport = KG4weather.snowy
				daymood = KG4weather.snowmood
				daytic = schooltics.snowyday
				noontic = schooltics.snowynoon
			if event < 30:
				mooda = 0
				moodb = 3
			elif event >= 30 and event <= 70:
				mooda = 1
				moodb = 4
			elif event > 70:
				mooda = 2
				moodb = 5
			print('"' + randc(wreport) + '"' + "\n")
			pagebreak(n=True)
			print(f"[🕙] {daymood[mooda]}\n")
			pagebreak(n=True)
			dupetest(daytic)
			
		elif cycle == 1:
			print(f"[🕛] {daymood[moodb]}\n")
			pagebreak(n=True)
			menu("LUNCH")
			pagebreak(n=True)
			dupetest(noontic)
			
		elif cycle == 2:
			menu("DINNER")
			pagebreak(n=True)
			center("[💤][NIGHT TIME]\n")
			print(f"{randc(schooltics.goodnight)}\n")
			dupetest(schooltics.night)
			
		funevent += dice(0, 30)
		#if funevent < 100:
			#print(f"Funevent is at {funevent}.")
		if funevent >= 100 and party() > 2:
			pagebreak()
			center(f"[❔] Something's happening...")
			event = 10
			pagebreak()
			daycount, cycle, tod = randevents(daycount, cycle, tod)
			funevent = 0
		
		event += dice(10, 30)
		if event >= 100 and party() > 2:
			# print(f"Event is at {event}! Event flag triggered!\n")
			if cycle < 2:
				cycle += 1
			elif cycle == 2:
				daycount += 1
				cycle = 0
			event = 0
			pagebreak()
			center(f"[📅][DAY {daycount}: {tod[cycle]}]")
			border()
			# MURDER HERE
			murderer, murdered = killroll()
			cycle, daycount, cluelist = murderscenes(murdered, rands(players, 2), daycount, cycle, tod)
			murderer = knames[-1]
			center(f"Someone has killed {murdered}!\n")
			if cycle < 2:
				cycle += 1
			elif cycle == 2:
				daycount += 1
				cycle = 0
			if cycle == 2:
				pagebreak()
				center(f"[📅][DAY {daycount}: {tod[cycle]}]")
				pagebreak(n=True)
				print("\"Oh? Oh? Isn't that terrible?\"\n\n\"So late at night and you just saw a dead body. Try not to let it haunt you TOO MUCH, kiddos. You have an investigation tomorrow.\"")
				pagebreak(b=True)
				dupetics(schooltics.murdersleep, Dead=True)
				daycount += 1
				cycle = 0
			pagebreak()
			center(f"[📅][DAY {daycount}: {tod[cycle]}]")
			border()
			difficulty = investigation(murderer, cluelist)
			if cycle < 2:
				cycle += 1
			elif cycle == 2:
				daycount += 1
				cycle = 0
			if cycle == 2:
				pagebreak()
				center(f"[📅][DAY {daycount}: {tod[cycle]}]")
				pagebreak(n=True)
				print("\"Phew! That was a good long day of investigating... you did investigate, right...?\"\n\n\"Well, whether you did or didn't, you have a trial tomorrow... good night!\"")
				pagebreak(b=True)
				dupetics(schooltics.trialsleep, Dead=True)
				daycount += 1
				cycle = 0
			pagebreak()
			center(f"[📅][DAY {daycount}: {tod[cycle]}]")
			border()
			trial(murderer, murdered, difficulty)
		#elif event < 100 and party() > 2:
			#print(f"Event at {event}. Nothing's happened yet.")
			#pagebreak(p=True)
		if len(players) == 2 and events["winflag"] == "no":
			if cycle < 2:
				cycle += 1
			elif cycle == 2:
				daycount += 1
				cycle = 0
			center(f"[📅][DAY {daycount}: {tod[cycle]}]")
			border()
			events["winflag"] = "yes"
			print("\nUh oh. Only two people left? We can't hold a trial with a single person.\n")
			print("So what's going to happen next? Kids, I'm waiting...\n")
			pagebreak(n=True)
			twoending = dice(1, 2)
			if twoending == 1:
				print(f"[🕊] {icons[0]}{icons[1]} {players[0]} and {players[1]} decide to live together in peace for the rest of their days...\n")
				pagebreak(n=True)
				finalresults()
				print("...\n")
				print("So that's it, huh? Thanks for playing!\n")
				center("[THE END]")
			if twoending == 2:
				fkill = randc(players)
				ficon = icons.pop(id(players, fkill))
				fname = players.pop(id(players, fkill))
				print(f"{ficon}{icons[0]} {fname} snaps and murders {players[0]}!\n")
				dreason.append(f" was murdered by {fkill}.")
				chardel(players[0])
				finalresults()
				print("...\n")
				print(f"{ficon} {fname} is victorious!\n")
				print(f"[🏆] CONGRATULATIONS, {fname.upper()}! YOU'VE WON!\n")
				center("[THE END]")
				
				
		if cycle < 2:
			cycle += 1
		elif cycle == 2:
			daycount += 1
			cycle = 0

def investigation(killer, cluelist):
	center("[🔎][INVESTIGATION TIME]")
	pagebreak(n=True)
	print(cluelist[1])
	pagebreak(n=True)
	difficulty = 150
	clues = ["[❌]", "[⭕️]", "[‼️]"]
	cluegood = ["discovers something shocking!", "searches the area thoroughly and seems satisfied.", "seems particularly absorbed in a single idea...", "spends the time deep in thought.", "searches the room thoroughly.", "seems focused on a particular clue.", "seems to be convinced of the answer...", "seems thoroughly determined.", "finds something very interesting...", "finds a multitudes of clues.", "comes to a conclusion.", "finds something very curious.", "seems absolutely certain.", "seems very convinced.",]
	cluenorm = ["searches through the room, though doesn't come to any particular conclusion.", "tries to help.", "finds one or two strange things.", "notices something unusual.", "points out something interesting.", "notices a few things.", "does a cursory search, but doesn't really notice much.", "only finds a few things.", "finds one or two interesting things.", "is grossed out by the body...", "feels uncomfortable in the room.", "mostly stands back, but does try to help.", "helps out a bit.", "mostly supports the others.", "does see something interesting.", "does some searching."]
	cluebad = ["seems to be half-asleep.", "doesn't look for clues at all.", "isn't any help.", "muddles the investigation scene more than anything.", "makes a bunch of theories that leaves the others scratching their heads.", "goes to bed instead.", "takes a stress nap.", "refuses to be in the same room as a dead body.", "is entirely unhelpful.", "is entirely unhelpful and smug about it.", "spends the time watching TV instead.", "decides it's a good time to go somewhere else.", "tries to help but it's useless.", "doesn't manage to find anything...", "has no luck finding any clues.", "is entirely useless.", "doesn't have any luck.", "doesn't find a thing.", "finds nothing of value."]
	for persons in players:
		parta = f"{avatar(persons)} {persons} "
		roll = dice(1, 100)
		if persons == killer:
			liar = randc([cluegood, cluenorm, cluebad])
			if liar == cluegood:
				clue = clues[0]
			elif liar == cluenorm:\
				clue = clues[1]
			elif liar == cluebad:
				clue = clues[2]
			partb = randc(liar)
			if liar == cluegood or liar == cluenorm:
				partc = f"\nFocus: [{randc(cluelist[0])}]\n"
			else:
				partc = "\n"
			difficulty += dice(0, 50)
		elif roll <= 30:
			clue = clues[0]
			partb = randc(cluebad)
			partc = "\n"
		elif roll >= 31 and roll < 80:
			clue = clues[1]
			partb = randc(cluenorm)
			partc = f"\nFocus: [{randc(cluelist[0])}]\n"
			difficulty -= dice(10, 30)
		elif roll >= 80:
			clue = clues[2]
			partb = randc(cluegood)
			partc = f"\nFocus: [{randc(cluelist[0])}]\n"
			difficulty -= dice(20, 40)
		print(clue + parta + partb + partc)
	if difficulty <= 100:
		rating = "CLEAR"
		catcher = "This seems pretty simple."
	if difficulty > 100 and difficulty < 150:
		rating = "CLOUDY"
		catcher = "It's a bit uncertain..."
	if difficulty >= 150:
		rating = "SHROUDED IN FOG"
		catcher = "None of this makes any sense..."
	pagebreak(n=True)
	center("[⭕️][INVESTIGATION COMPLETE]\n")
	center("[CLARITY]")
	center(f"{rating}\n")
	center(f"{catcher}\n")
	return difficulty
	
	
def trial(killer, victim, difficulty):
	center("[⚖️][CLASS TRIAL]")
	pagebreak(n=True)
	if events["trialint"] == "no":
		print("""The class is called to gather together in an elevator that sinks deep beneath the earth...

No one speaks.

When it finally stills, the doors slide open to reveal... a vast cavern decorated like a royal hall.

There's a circle of stands in the center of the room, each with a portrait of a student on it, including the dead... and they all surround a judge's chair in which Monokuma is sitting.
""")
		pagebreak()
		center("Welcome to the [⚖️][CLASS TRIAL]!")
		pagebreak()
		print("""
The objective here is to debate and discuss with your fellow students to determine who the killer is.

Once a consensus is reached, it's time to take a vote... if the vote is correct, the killer is executed and the rest of the class goes on to see another day.

Otherwise, the killer wins their freedom, among other yet more fabulous prizes... and it's sayonara to the rest of you.

Are you ready? Let's begin.
""")
		events["trialint"] = "yes"
	else:
		print("\"Looks like it's time for another class trial! Are you ready? Let's get to it!\"\n")
	pagebreak(n=True)
	if difficulty <= 100:
		rating = "EASY"
	if difficulty > 100 and difficulty < 150:
		rating = "NORMAL"
	if difficulty > 150:
		rating = "HARD"
	logic = 0
	center(f"[DIFFICULTY] {rating}")
	center(f"[KILLER] ???")
	center(f"[VICTIM] {victim}\n")
	minimum = party()
	arguments = dice(2, 4)
	odds = minimum * arguments
	counter = 0
	
	for value in range(1, (odds + 1)):

		argue = randc(players)
		quality = dice(1, 100)
		key = randc(["per", "sec"])

		if lookup(argue, key) in ["Normal", "Responsible", "Calm", "Modest", "Practical"]:
			actlist = KG6trial.normal
	
		elif lookup(argue, key) in ["Friendly", "Peppy", "Cheerful", "Kind", "Gentle", "Good"]:
			actlist = KG6trial.cheer
			
		elif lookup(argue, key) in ["Quiet", "Blank", "Cool", "Cold", "Mysterious"]:
			actlist = KG6trial.quiet
			
		elif lookup(argue, key) in ["Annoying", "Dumb", "Weird"]:
			actlist = KG6trial.dumb
			
		elif lookup(argue, key) in ["Obsessive", "Scary"]:
			actlist = KG6trial.scary
			
		elif lookup(argue, key) in ["Clever", "Nerdy"]:
			actlist = KG6trial.smart
			
		elif lookup(argue, key) in ["Chuuni", "Geeky"]:
			actlist = KG6trial.dork
			
		elif lookup(argue, key) in ["Energetic", "Athletic"]:
			actlist = KG6trial.sporty
			
		elif lookup(argue, key) in ["Angry", "Tough"]:
			actlist = KG6trial.mad
			
		elif lookup(argue, key) in ["Victim", "Shy", "Awkward", "Lonely"]:
			actlist = KG6trial.shy
			
		elif lookup(argue, key) == "Smug":
			actlist = KG6trial.smug
		
		elif lookup(argue, key) in ["Cute", "Childish"]:
			actlist = KG6trial.baby
			
		elif lookup(argue, key) in ["Refined", "Elegant", "Polite"]:
			actlist = KG6trial.fancy
			
		elif lookup(argue, key) in ["Relaxed", "Slacker", "Lazy"]:
			actlist = KG6trial.lazy
			
		elif lookup(argue, key) in ["Tired", "Gloomy"]:
			actlist = KG6trial.sad
			
		elif lookup(argue, key) in ["Forgetful", "Naive", "Oblivious"]:
			actlist = KG6trial.huh
			
		elif lookup(argue, key) in ["Funny", "Prankster", "Bully", "Rude"]:
			actlist = KG6trial.bully
			
		elif lookup(argue, key) == "Popular":
			actlist = KG6trial.popular
			
		elif lookup(argue, key) in ["Passionate", "Serious"]:
			actlist = KG6trial.focus
			
		elif lookup(argue, key) == "Robot":
			actlist = KG6trial.robot
			
		elif lookup(argue, key) == "Furry":
			actlist = KG6trial.furry

		if argue == killer:
			response = random.randint(0, 2)
			misdirection = dice(1, 30)
			change = -misdirection
					
		elif quality <= 30:
			response = 0
			change = dice(1, 10)
		elif quality >= 31 and quality < 80:
			response = 1
			change = dice(10, 30)
		elif quality >= 80:
			response = 2
			change = dice(25, 50)
			
		logic += change
			
		if response == 0:
			eyecatcher = "[❔]"
			followup = randc([
				"The class is entirely unconvinced!",
				"No one pays any attention!",
				"The point falls flat!",
				"It doesn't seem very successful...",
				"No one cares...",
				"It doesn't seem to work very well...",
				"It's a failure!",
				"It doesn't work at all.",
				"That doesn't make sense!",
				"What's the point?",
				"The class is lost...",
				"What's that supposed to mean?",
				"The class doesn't agree!",
				"It's not helpful!",
				"No one cares!",
				"No one gets it.",
				"Everyone ignores it.",
				"Everyone is lost...",
				"That's just confusing!",
				"It's just confusing!",
				])
		elif response == 1:
			eyecatcher = "[⭕️]"
			followup = randc([
				"The class gives it some consideration.",
				"That makes sense.",
				"Everyone listens.",
				"It sounds reasonable.",
				"It seems like it went over well.",
				"It seems a reasonable success.",
				"It seems to have worked somewhat.",
				"The class seems a bit more convinced.",
				"The point seems like a good one.",
				"The point incites some discussion...",
				"That makes some sense.",
				"Things seem clearer now.",
				"The class understands more.",
				"It seems to help a little.",
				"The class is somewhat convinced.",
				"Everyone thinks it's reasonable.",
				])
		elif response == 2:
			eyecatcher = "[‼️]"
			followup = randc([
				"Everyone is astounded!",
				"It's a great success!",
				"Huh. That makes a lot of sense!",
				"Everything seems clearer.",
				"It's incredibly convincing!",
				"What a great point!",
				"Everything makes sense now!",
				"That makes a lot of sense!",
				"It's incredibly helpful!",
				"Things are much clearer now!",
				"Fascinating!",
				"The case seems much clearer...",
				"The point seems to lead somewhere!",
				"It's incredibly helpful.",
				"No one can argue.",
				"It's a very good point.",
				"How shocking!",
				"Everyone is amazed!",
				"Everyone agrees!",
				"The class gasps in shock and awe!",
				"Everyone is convinced!",
				"It's a resounding success!",
				])
			
		onetic(argue, actlist[response])
		print(eyecatcher + " " + followup + "\n")
		counter += 1
		if counter == 4:
			pagebreak(n=True)
			counter = 0
			
	if logic <= difficulty and killer == victim:
		center("[❌][TRIAL LOST]\n")
		center(f"[DIFFICULTY] {rating}")
		center(f"[KILLER] {killer}")
		center(f"[VICTIM] {victim}\n")
		
		print(f""""WOW! [💢] Are you all kidding me? It was A SUICIDE. And you all GOT THAT WRONG. [💢] {killer.upper()} CAN'T EVEN WIN!!! [💢]"
		
"What am I supposed to do with a game with NO WINNER... well, I'm not gonna let you kiddos escape getting executed, if you were hoping for that. The rules are the rules."
		
Monokuma shakes his head in disappointment.
		
"Guess it'll save the company some
money... buh-bye.\"""") # """

		events["winflag"] = "yes"
		
		finalresults()
		for avis, people in zip(icons, players):
			print(f"[☠️] {people} was executed for losing the trial.\n")
		center("[THE END]")
		
	elif logic <= difficulty:
		center("[❌][TRIAL LOST]\n")
		center(f"[DIFFICULTY] {rating}")
		center(f"[KILLER] {killer}")
		center(f"[VICTIM] {victim}\n")
		center(f"""The class has voted incorrectly!
		
{killer} has won the game, and the rest of the class is sent to the execution chamber...
""") # """
		events["winflag"] = "yes"
		finalresults()
		chardel(killer)
		for avis, people in zip(icons, players):
			print(f"[☠️] {people} was executed for losing the trial.\n")
		print("...\n")
		print(f"{kicon[-1]} {knames[-1]} is victorious!\n")
		print(f"[🏆] CONGRATULATIONS, {killer.upper()}! YOU'VE WON!\n")
		center("[THE END]")
		
	elif logic > difficulty and killer == victim:
		center("[⭕️][TRIAL COMPLETE]\n")
		center(f"[DIFFICULTY] {rating}")
		center(f"[KILLER] {killer}")
		center(f"[VICTIM] {victim}\n")
		center(f""""Yes! Good job."
		
"{killer} did it! {killer.upper()} KILLED {victim.upper()}!!!" [💢]
		
"Now, what does that mean, kids?"
		
"It means..."
		
"There won't be an execution..." [💔] """) # """
		pagebreak(p=True)
		
	elif logic > difficulty:
		center("[⭕️][TRIAL COMPLETE]\n")
		center(f"[DIFFICULTY] {rating}")
		center(f"[KILLER] {killer}")
		center(f"[VICTIM] {victim}\n")
		center(f"The class correctly votes for {killer}.\n\n{killer} is sent off to the execution chamber...\n")
		executions(killer)
		dreason.append(" was executed by trial.")
		chardel(killer)
		pagebreak()

