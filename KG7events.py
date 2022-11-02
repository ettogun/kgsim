import KG
import random

tod = ["[☀️] DAY", "[☀️] AFTERNOON", "[🌙] NIGHT"]

def daycycler(daycount, cycle, tod):
	KG.center(f"[📅][DAY {daycount}: {tod[cycle]}]")
	KG.pagebreak(n=True)
	
def runthru(player, message):
	first = KG.gendict(player)
	action = KG.thedict(first, message)
	print(action)
	

## TEMPLATE ## ----------------------------

def template(daycount, cycle, tod):
	
	# generic time cycle
	if cycle < 2:
		cycle += 1
	elif cycle == 2:
		daycount += 1
		cycle = 0
	
	# daysplash
	daycycler(daycount, cycle,
	tod)
	KG.center("[📢] BING BONG DING DONG...")
	
	print("""
There's an announcement...
""")

	return(daycount, cycle, tod)
	
## END TEMPLATE ## -------------------------


## OBSTACLE COURSE ## ----------------------

def obstaclecourse(daycount, cycle, tod):
	
	if cycle != 0:
			cycle = 0
	daycount += 1	
		
	KG.center("[🕒] The next day...")
	KG.pagebreak()
	
	daycycler(daycount, cycle,
	tod)
	KG.center("[📢] BING BONG DING DONG...")
	
	print("""
There's an announcement...

"Hey, kids, you've been real boring lately, so I've got a special event to spice things up again. I don't want things to get stale between us..." [💔]

"...so I've cooked up an obstacle course! I'm sure it'll be no OBSTACLE to our love..."

"...and, it's not just any obstacle course, either. It's my specially-patented, copyrighted, trademarked, blah blah blah, blah blah blah..."

[‼️][MONOKUMA'S HEART-STOPPING, DEATH-DEFYING OBSTACLE COURSE OF DESPAIR][‼️]
""")
	
	KG.pagebreak()

	print("""
[🕒] A few hours later...

[📢] RRRRRRRRRIIIING! ALL PARTICIPANTS MUSTER OUT ON THE FIELD. And that means ALL of YOU. NO ONE is sitting out!

The students all gather together at the field... or, what used to be the field. It's not a field anymore.

Now it's...

[‼️][MONOKUMA'S HEART-STOPPING, DEATH-DEFYING OBSTACLE COURSE OF DESPAIR][‼️]

and it is... truly... despairing.
""")

	KG.pagebreak()
	
	print("""
[💬] Instead of an obstacle course, it seems more like a murder course...

Where there used to be grass, there's now scorched earth and a lake of fire... tiny floating "safe" platforms whirl around at breakneck speeds, ramming into each other with noises like small explosions. [💥]

Then there's a tube maze that loops and twists in on itself in impossible verticals, and, at one point, seems to drop straight into the earth...

If it's even possible to get through that, there's a corridor of swinging chainsaws. Monokuma pulls out a remote and presses a button, and the contraption suddenly bursts into flames...

Then, just before the finish line, there's a plastic kiddie pool with a rubber duck in it.
""")

	KG.pagebreak()
	
	print("""
Without any further ado, Monokuma pushes them to begin...
""")

	KG.pagebreak()
	
	courselose = [
"""(NAME) is too nervous to even try to step on the platforms!

Disqualified before (he) even begins! [💢] (HE)'s going STRAIGHT to the losers bench...""",
	
"""(NAME) tries to step on a platform and trips!

(HE) falls straight into the lake of fire! That's just sad...""",
	
"""(NAME) manages to get on a platform but (he) wobbles like mad...

...there's no surprise when (he) falls off and burns up in a flash!""",
	
"""(NAME) scrambles and takes a leap of faith...

...(he) lands on a platform and actually seems to be doing pretty well! That is, until the thing starts moving, sending (him) tumbling right off...""",
	
"""(NAME) takes a step on a platform... and falls right off!

(HE) disappears into the lake of fire in a burst of flame...""",
	
"""(NAME) tries (his) best to get on the platforms, but (he) doesn't even manage to land...

...(he) falls right into the fire and disappears in a flash of heat!""",
	
"""(NAME) gets on and wobbles on the platforms precariously and seems to be doing fine...

...but then it slams into another platform and (he)'s knocked off!

(HE) disappears into the flames! [🔥]""",
	
"""(NAME) gets across the platforms with no issues in an amazing display of agility and acrobatics...

...but then (he) crawls into the tube maze and no one sees (him) again.""",
	
"""(NAME) leaps from platform to platform absolutely effortlessly!

Then (he) crawls into the tube maze... and (he) never crawls out.""",
	
"""(NAME) gets through the across the lake of fire easily! It's incredibly impressive...

...but (he) gets a bad case of nerves and refuses to enter the tube maze!

Off to the loser's bench for you...""",
	
"""(NAME) barely manages to get across the lake of fire... sweat pours off (him) in droves, and (he)'s shaking from the adrenaline...

...(he) crawls into the tube maze... and, suddenly, he screams! It seems to get farther and farther away, like (he)'s falling...""",
	
"""(NAME) survives the lake of fire, gets out of the tube maze with only a little wear for (his) trouble, and reaches the hall of flaming chainsaws...

...(he) rolls in... and promptly gets cut into smithereens! Ohhh! There's blood everywhere!""",
	
"""(NAME) crosses the lake of fire with some trouble... climbs out of the tube maze covered in sweat...

...and completely balks at the hall of chainsaws.

(HE) won't take a single step in... well, off to the loser's bench for you! LOSER!""",
	
"""(NAME) struggles across the lake of fire, though (he)'s out of the tube maze in a flash... taking a deep breath, (he) runs into the hall of chainsaws...

...and gets completely pulverized! Ooooohhh man! Would you look at that!""",
	
"""(NAME) breezes through everything up til the hall of chainsaws... (he) gulps, takes a deep breath, runs through...

...and, at the very last second, (he) trips! (HE)'s promptly transformed into a spray of guts and gore! Oh my god!""",
	
"""(NAME) leaps across the platforms easily!

(HE) chooses a tunnel tube that spits (him) right out the other end!

(HE) rolls past the chainsaws with no problem...

...but then (he) falls face-first into the pool and sinks like a stone! How deep IS that thing?!""",
	
"""(NAME) manages to get through all three previous obstacles with little issue, but... faced with the kiddie pool now, (he) eyes it distrustfully...

...and gives up! (HE)'s disqualified and sent to the loser's bench! I can't believe it!!!""",
	
"""(NAME) manages to get past all the previous obstacles only a little singed...

...(he) steps into the kiddie pool and wades across...

...except, only a few steps away from the finish line, something grabs (his) leg and pulls (him) down... down WHERE?!""",
	]
	
	coursewin = [
"""(NAME) struggles across the lake of fire...

...(he) emerges from the tube maze looking traumatized, and nearly gets (his) head cut off running through the hall of chainsaws... but, (he) makes it...

...wading across the pool, at least, is no trouble... and (NAME) finishes the course! GOOD JOB!""",
	
"""(NAME) finishes the first three trials effortlessly...

...dog paddles across the pool like a champion...

...and finishes the course! GOOD JOB!!!""",
	
"""(NAME) barely manages to cross the lake of fire, though (he) luckily finds the easiest route through the tube mazes...

...(he) gets a little singed crawling through the chainsaw hall, but (he) pushes through, crosses the kiddie pool, and...

...finishes the course! AMAZING!!!"""
	]
	
	loselist = list(KG.players)
	random.shuffle(loselist)
	winnerlist = []
	
	winners = random.randint(0, 2)
	losers = len(KG.players) - winners
	
	losetics = random.sample(courselose, losers)
	
	if winners > 0:
		wintics = random.sample(coursewin, winners)
		for count in wintics:
			awinner = loselist.pop()
			winnerlist.append(awinner)
	
	print("\nAnd our first player up is...\n")
	for various in loselist:
		KG.center(various.upper() + "!\n")
		templist = []
		action = losetics.pop()
		templist.append(action)
		KG.onetic(various, templist)
		templist = []
		KG.pagebreak(b=True)
		
	if winners > 0:
		for win in winnerlist:
			KG.center(win.upper() + "!\n")
			templist = []
			goals = wintics.pop()
			templist.append(goals)
			KG.onetic(win, templist)
			templist = []
			KG.pagebreak(b=True)
			
	print("""After all the players finish the course... everyone reappears, somehow, seeming only slightly worse for wear...
""")

	KG.pagebreak()
	
	print("""
...then Monokuma reappears and seems to be in great spirits.

"Well, class, was that [HEART-POUNDING]? Wasn't that [DEATH-DEFYING]? [❤️]"

He gets a dreamy look on his face for a second, and then he shouts...

"Time to get back to work!"

And he disappears with a pop.
""")

	KG.pagebreak()
	
	KG.center("[❌] LOSERS")
	KG.center("Just look at these failures!\n")
	for losers in loselist:
		print(KG.icons[KG.players.index(losers)] + " " + losers)
	
	KG.pagebreak(b=True)
		
	if winners > 0:
		KG.center("[🏆] WINNERS")
		KG.center("Real champions here only!\n")
		for win in winnerlist:
			print(KG.icons[KG.players.index(win)] + " " + win)
		KG.pagebreak(b=True)
	
	cycle = 2
	
	return(daycount, cycle, tod)
			
	
## END OBSTACLE COURSE ## -------------------


## COOKIES ## ----------------------------

def cookies(daycount, cycle, tod):
	
	if cycle == 2:
		cycle = 0
		daycount += 1
	
	# daysplash
	daycycler(daycount, cycle,
	tod)
	
	death = 0
	choked = []
	baker = random.choice(KG.players)
	types = ["snickerdoodle", "chocolate chip", "sugar", "cinnamon", "lemon", "chocolate", "butter", "shortbread", "plain", "caramel", "vanilla", "milk", "strawberry", "confetti"]
	flavor = random.choice(types)
	bavi = KG.lookup(baker, "ico")
	
	KG.center("[🍪][A BATCH OF COOKIES]")
	runthru(baker, f"""
{bavi} {baker} is bored...

What to do?

After thinking over it for a while, (he) decides it's a good day to bake some {flavor} cookies.""") #"""
	
	input()
	
	runthru(baker, "(HE) makes the dough without too much trouble, and soon it's baking away in the oven... it smells REALLY good. [♥️]")
		
	input()
	
	runthru(baker, f"(HE) ends up a huge batch of {flavor} cookies, way too many to eat (him)self... so (he) decides to share with everyone.\n")
	
	KG.pagebreak()
	
	print(f"{bavi} {baker} offers the cookies around....")
	
	KG.pagebreak(n=True)
	
	counter = 0
	
	for person in KG.players:
		if person != baker:
			odds = random.randint(1, 100)
			icon = KG.lookup(person, "ico")
			if odds == 1 and death == 0:
				print(f"{icon} {person} takes a bite... and starts to choke!\n")
				choked.append(person)
				death = 1
			elif odds <= 10:
				message = random.choice([f"{icon} {person} takes a bite... and spits it out! It's disgusting...\n",
				
				f"{icon} {person} bites in, and a pained look crosses (his) face... oh, that tastes REALLY bad...\n",
				
				f"{icon} {person} takes a bite, and nearly spits it out again... it really isn't good.\n",
				
				f"{icon} {person} tries it... and REALLY hates it.\n"])
				runthru(person, message)
			elif odds > 10 and odds <= 20:
				message = random.choice([f"{icon} {person} doesn't take one.\n",
				
				f"{icon} {person} seems distrustful.\n",
				
				f"{icon} {person} thanks {baker}, but refuses a cookie.\n"])
				print(message)
			elif odds > 20 and odds <= 30:
				message = random.choice([f"{icon} {person} thinks this is the most amazing cookie (he)'s ever had!\n",
				
				f"{icon} {person} is in love... [❤️] ...with the cookie.\n",
				
				f"{icon} {person} really likes it!",
				
				f"{icon} {person} thinks the cookies are so good, (he) sneaks a few more when {baker} isn't looking!\n"])
				runthru(person, message)
			elif odds > 20:
				message = random.choice([f"{icon} {person} thinks it's delicious, and (his) mood improves.\n",
				
				f"{icon} {person} takes a bite, and... (he) loves it! [❤️]\n",
				
				f"{icon} {person} thinks it's so good, (he) takes another one...\n",
				
				f"{icon} {person} enjoys the cookie thoroughly.\n",
				
				f"{icon} {person} eats up (his) cookie in two bites... it's REALLY good.\n",
				
				f"{icon} {person} takes a bite and chews it thoughtfully... (he) likes it.\n",
				
				f"{icon} {person} thinks it's very good.\n",
				
				f"{icon} {person} considers the cookie carefully before biting into it... it's good...\n"])
				runthru(person, message)
			if len(KG.players) != 5:
				counter += 1
				if counter == 4:
					KG.pagebreak(n=True)
					counter = 0
					
	if death == 1:
		KG.pagebreak()
		runthru(choked[0], f"""
[❗️] {choked[0]} keeps hacking and gasping... (he) can't speak... ...(he) can't breathe!

{baker} blanches and rushes over to help, but the food stays stuck...
		
...and, in {baker}'s arms, {choked[0]} suffocates and dies! [‼️]
		""") #"""
		
		KG.pagebreak()
		
		print(f"""
Monokuma pops up and looks at {choked[0]} sadly...

"What a lame way to die..."
		
He leers at {baker}. "Looks like I'm going to have to prepare a special execution for you!"
		
"...hah! Just kidding! I'm not going to do that! I don't need to lose two of you bastards THAT quickly!" [💢]
		
"There IS gonna be a new rule, now, though."
""") #"""

		KG.pagebreak()
		
		print("[RULE #9] There is to be no more making and sharing of delicious baked treats (e.g. cookies, cakes, etc.,)")

		KG.pagebreak(n=True)
		
		print(f"""\"Heed it, and heed it well!"
		
Monokuma shakes his head again before he disappears along with the body.
""") #"""
		
		KG.dreason.append(f" choked on {baker}'s cookies.")
		KG.chardel(choked[0])
		
		KG.pagebreak(n=True)
		KG.center(f"Goodbye, {choked[0]}.")
		KG.center("And life continues on as normal...\n")
		
	else:
		KG.pagebreak()
		print("[💬] Overall, it was a good break.")
		KG.pagebreak()

	cycle += 1

	return(daycount, cycle, tod)
	
	
## COOKIES ##  -------------------------
		
## ROBOT ## ----------------------------

# event that *turns someone into a robot. gives them robot icon... changes secondary personality to robot, write some trial lines

def robotto(daycount, cycle, tod):
	
	# generic time cycle
	if cycle == 2:
		cycle = 0
		daycount += 1
	elif cycle == 0:
		cycle += 1
	
	# daysplash
	daycycler(daycount, cycle,
	tod)
	KG.center("[📢] BING BONG...")
	
	print("""
There's an announcement...

"Everyone, report to the science lab RIGHT NOW! I repeat, report to the science lab..."

There's a science lab? The students murmur in confusion. If there IS one, none of them have ever seen it...
""")

	KG.pagebreak()

	print("""
...but it doesn't take them long to find it. It's impossible to miss... a giant, spaceship-shaped building [🛸], like something out of a sci-fi movie, dropped right into the middle of the school grounds. How did it get there? Did it fly?

In case there could be any doubt that it is the science lab, there's a giant billboard over the entrance with [SCIENCE LAB] spelled out in red neon lights.
""")

	KG.pagebreak()
	
	print("""
Without any delay, Monokuma sweeps them all inside. It's full of metal tubes and monitors with flickering screens, all sorts of who-knows-what...

[❔] In the center of the room, there's something covered with a sheet, clearly the main attraction. There's plenty of speculation about what it could possibly be.
""")

	KG.pagebreak()
	
	print("""
...not that the group has to wait long to find out. Monokuma doesn't spend a minute once everyone's inside before he pulls away the sheet to reveal...

[❕] some sort of metal horrorshow, surrounded with drills and sawblades, looking like nothing any of them have ever seen before.
""")

	KG.pagebreak()

	print("""
"Class!" Monokuma claps his hands (paws?) together. "I have something very BEARY special for you today."

He points at the machine pointedly.

"I've made a new invention that will improve your strength, intelligence, charisma, everything, all your stats, FIFTYFOLD! Once one of you goes on that table, you'll be better than you've ever been. You'll be better than human!"
""")

	KG.pagebreak()

	print("""
The only response from the room is a doubtful mutter, but he doesn't seem deterred.

"Ahahah, don't rush to volunteer, though! I mean it! [💢] This machine can only be used ONCE, so only ONE of you will get the chance!  And it's MY machine, so it's MY decision!"
""")

	KG.pagebreak()
	
	print("""
"...but I'm a very fair and loving Headmaster, so it's gotta be random. You see, I've written all your names on slips of paper and put them inside this hat. So, who's it gonna be?!"

He pulls a hat from out of nowhere, jams his paws into it, and takes out a slip of paper.

"A-hah! It's..."
""")

	project = KG.randc(KG.players)
	KG.pagebreak()
	
	runthru(project, f"""
[❗️] "{project}! You are the winner!"

Before {project} can make a move, metal arms shoot out of Monokuma's machine and wraps around (his) legs and arms!

They lift (him) bodily over to the table and tie (him) down tight...

The class gets a single glimpse of (his) fear-filled eyes before (he)'s covered up by whirring machinery, moving too quickly for the eye to see!
""")

	KG.pagebreak()
	
	runthru(project, f"""
The sounds of buzzing saws and cutting fill the air... it's so loud, no one can speak.

And then... absolute silence. The machine stops without any warning, lifting away blood-stained claws...

To reveal a pristine, metallic body. But... it still looks like {project}?

[❗️] [🤖] {project} is now a robot!
""")

	proid = KG.lookup(project, "id")
	KG.icons[proid] = "[🤖]"
	KG.secondary[proid] = "Robot"
	KG.pagebreak()
	
	if cycle < 2:
		cycle += 1
	elif cycle == 2:
		daycount += 1
		cycle = 0

	return(daycount, cycle, tod) # """
	
## END ROBOTTO ## ------------------------


## PEACE ## ----------------------------

def peace(daycount, cycle, tod):
	
	# generic time cycle
	cycle = 0
	daycount += 1
	
	# daysplash
	daycycler(daycount, cycle,
	tod)
	KG.center("[📢] DING DONG...")
	
	print("""
There's an announcement...

"Good morning, folks... it's a beautiful day today..."

[❔] Monokuma's wake-up call comes as normal, the same way as any other day, but there's a strange feeling in the air. Something is different...
""")

	KG.pagebreak()
	
	print("""
A determination has filled the hearts of the students. When they meet for breakfast, a discussion starts up...

And, hearing their talk and unusual sense of cooperation, Monokuma soon appears in their midst.
""")

	KG.pagebreak()
	
	print("""
"Ahaha, kids, what's all this talk I'm hearing about? It can't be true, right? My ears must be deceiving me..."

There's no deception. The students turn towards him as a whole and announce their intentions: an absolute peace. They've agreed that they'll live the rest of their lives here together, forever.
""")

	KG.pagebreak()
	
	print("""
"What??? WHAT? That's not in the contract! You can't do this!" [💢] Monokuma stomps his feet petulantly on the table. It'd be almost cute if it wasn't with so much force that the table starts to crack beneath the beating...

But his anger is no use. The students are true to their word, and their lives soon fall into an easy peace.
""")

	KG.pagebreak()
	
	marry = random.sample(KG.players, 2)
	
	print(f"""
Eventually, {marry[0]} and {marry[1]} end up getting married, and all the students attend happily... [❤️]

The rest of their story is lost to history.

[THE END]
""")

	return(daycount, cycle, tod)
	
	
## END TEMPLATE ## -------------------------

