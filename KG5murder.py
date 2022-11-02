import KG
import schooltics

tod = ["[☀️] DAY", "[☀️] AFTERNOON", "[🌙] NIGHT"]

def daycycler(daycount, cycle, tod):
	KG.pagebreak()
	KG.center(f"[📅][DAY {daycount}: {tod[cycle]}]")
	KG.pagebreak(n=True)
	

def murderdict(finder, text):
	dictionary = KG.gendict(finder[0])
	action = KG.thedict(dictionary, text)
	dictionary2 = KG.gendict(finder[1], Switch=True)
	twoact = KG.thedict(dictionary2, action)
	print(twoact)
	
	
## TEMPLATE ## -------------------------

## if I want a murder with a known actor, I'll go to events... or change all these. could also always just make it optional
def templatekill(victim, finder, daycount, cycle, tod):
	print("""
[❔] Somewhere else...

A shadowy figure contemplates how to write the fictional deaths of countless as-yet uncreated masses...

It holds its head, clearly caught in the throes of a headache...

But, regardless, it glares back into the blazing eye of its mobile phone...

...and writes.
""") # """

	if cycle < 2:
		cycle += 1
	elif cycle == 2:
		daycount += 1
		cycle = 0
		
	daycycler(daycount, cycle, tod)
	
	murderdict(finder, """this person runs into the dead body.
	
	and then another person runs into the dead body.
	
	its pretty gross. no one is happy
""")

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
			
	return cycle, daycount, [["list", "of" "clues"],

"""flavor text for the investigation

its very important
"""]
	
## END TEMPLATE ## -------------------------
	

##  KNIFE KILL ## --------------------------

def knife(victim, finder, daycount, cycle, tod):
	print(f"""
[❔] Somewhere else...
	
A shadowy figure trails behind another, making sure to keep hidden... its hands grip a wickedly sharp butcher's knife. 

It springs... 
	
There's a terrible commotion, the sound of struggling and a scream, cut short... transformed into a low gurgling, and, then... nothing.
	
The figure wipes its hands clean and slinks away...
	
...leaving behind a body.
""") # """

	if cycle < 2:
			cycle += 1
	elif cycle == 2:
			daycount += 1
			cycle = 0
	
	daycycler(daycount, cycle, tod)

	murderdict(finder, f"""[🕒] Time passes, and the body cools, resting on the kitchen tile undisturbed...
	
Until {finder[0]} decides it's a good time for a snack.

But, instead of getting some delicious, delicious food, {finder[0]} is met with the sight of {victim}... or, rather, {victim}'s body, lying in a slick of blood, a knife sticking through its neck.

Horrified, {finder[0]} shouts for help... and {finder[1]} rushes in from down the hall, nearly slipping in the blood in (er) haste.
""") #"""

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
			
	return cycle, daycount, [["knife", "blood", "kitchen", "struggle"],

"""The kitchen is full of blood and footprints. There's evidence everywhere...

The body is in the same place, facedown, knife through its neck. It's unpleasant to be around... but the students are determined to solve the case.
"""]

## END ## -----------------------------
	

## POISON KILL ## -----------------------

def poison(victim, finder, daycount, cycle, tod):
	# this should only happen if it's noon or afternoon
	print("""
[❔] Somewhere else...
	
A figure hums to themselves as they chop and mix and stir and boil... as they work, they periodically pause to glance in a book titled [☠️] THE BIG BOOK OF POISONS.

The pot finally comes to a boil and fills the room with a smell like sweet candied apples...

With a smile of pleasure, they turn off the heat and decant their concotion into a tiny vial. It's a poisonous green, and it bubbles furiously inside its container, as if it were alive...
""")

	if cycle < 2:
			cycle += 1
	elif cycle == 2:
			daycount += 1
			cycle = 0
	
	daycycler(daycount, cycle, tod)
	
	if cycle == 0:
		cycle += 1
		
	if cycle == 1:
		MEAL = "[LUNCH TIME]"
	if cycle == 2:
		MEAL = "[DINNER TIME]"
	
	murderdict(finder, f"""[🍽]{MEAL} rolls around and all the students gather in the cafeteria as usual...
	
{finder[0]} takes a bite of (his) meal and follows it up with sip of (his) drink... and starts to choke and sputter! [❗️]

There's a flutter of panic before {finder[1]} pounds on (his) back and (he) coughs it out, takes a deep gasp... and laughs. (HE)'s fine, false alarm!

Everyone is relieved...

...until {victim} suddenly turns bright green and slams facedown onto the table, dead.
""") #"""

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
			
	return cycle, daycount, [["book", "kitchen", "candied apples", "library", "poison", "green"],
"""The body has gone entirely green, food smeared around its face from where it fell face first into its plate.

Poison... the word moves around the room. There's a strange smell of sweet apples wafting throughout.
"""]

## END ## -----------------------------
	
	
## SUICIDE ## -----------------------

def suicide(victim, finder, daycount, cycle,
tod):
	print("""
[❔] Somewhere else...

In a darkened room...

A figure in deep despair sits on a bed with its head held down to its knees.

A thick rope tied into a clumsy noose swings gently above them, its soft movements like invitations...

The day grows longer. The room grows darker.

Eventually, it raises its head, and contemplates the line with something like... hope.
""")

	if cycle < 2:
			cycle += 1
	elif cycle == 2:
			daycount += 1
			cycle = 0
	
	if cycle != 0:
		cycle = 0
		daycount += 1

	daycycler(daycount, cycle, tod)
	
	print("[🕒] The next day...\n")
	KG.dupetest(schooltics.day)
	print(f"{KG.dicons[-1]} {victim} is missing.\n")
	
	if cycle != 2:
			cycle = 2
			daycount += 1
	
	daycycler(daycount, cycle, tod)

	print(f"""[🕒] Free from its worries, the figure is light on its feet... so light that it doesn't even touch the ground, now, the figure needs no wings to fly.
	
Maybe that's why there's SO MANY FLIES IN HERE? Upupupu...\n""") # """
	
	if cycle < 2:
			cycle += 1
	elif cycle == 2:
			daycount += 1
			cycle = 0
	
	daycycler(daycount, cycle, tod)

	murderdict(finder, f"""{finder[0]} notices that no one's seen {victim} for a while now... (he) finds {finder[1]} and they go to {victim}'s room. 

The door is locked...

After a short discussion, they decide they'll break it down.

{finder[0]} and {finder[1]} work at it without much success... until...

[💥] {finder[1]} slams into it with all (er) might... and it splinters open! (E) trips into an enormous pile of buzzing flies...

That, and {victim}'s body. [☠️]
""") # """

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
	
	
	KG.knames[-1] = victim
	KG.kicon[-1] = KG.lookup(victim, "ico", Dead=True)
	KG.dreason[-1] = " committed suicide."
	
	return cycle, daycount, [["rope", "room", "suicide", "despair", "flies", "open window"],
	
"""The flies have all left through a crack in the window... and the body is truly a horrific mess... no one wants to even look at it.

The likely culprit here seems obvious, but the obvious isn't always the truth...
"""]

## END ## ---------------------------
	

## HOT WATER ## -----------------------

def hotwater(victim, finder, daycount, cycle, tod):
	print("""
[❔] Somewhere else...

The air is hot and heavy, full of steam... this must be the baths.

A figure soaks in the water, eyes closed, completely at ease...

...and completely oblivious to the other figure approaching behind them, obfuscated by the steam.

Then something heavy smashes into the back of their head and an arm wraps around their throat and pushes them under the surface...
""") # """

	if cycle == 1:
		cycle = 0
		daycount += 1
	elif cycle == 2:
		daycount += 1
		cycle = 0
	else:
		cycle += 1
		
	KG.pagebreak()
	
	print("\n[🕒] Some time later...\n")
		
	daycycler(daycount, cycle, tod)
	
	murderdict(finder, f"""{finder[0]} and {finder[1]} decide to go to the baths together for a soak and some conversation.

Strangely enough, when they get there, there's somebody floating facedown on the water... isn't it way too hot for that?

Then the realization strikes them... neither of them want to approach the body or check who it is, not really...

...but, in the end, {finder[1]} works up the nerve and turns the body over.

It's {victim}.
""") # """

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
			
	return cycle, daycount, [["bump", "hot water" "baths", "choked"],

"""The body has softened from the heat of the water... wait, does that mean they're all wading around in human soup? Gross...

The students get hot and sweaty fast... the baths aren't the best place for an investigation.
"""]

## END ## -------------------------

## CHOKED ## -----------------------

def choked(victim, finder, daycount, cycle, tod):
	print("""
[❔] Somewhere else...

The air is dark and still, and the air is filled with a repetitive scratching sound... In the dimness, a shape is visible, hunched over a table...

Are they drawing? Are they writing? There's no way to tell.

Regardless, they're so completely engrossed, they don't notice at all when another figure steps up behind them... well, not until cold fingers wrap around their neck.
""") # """

	if cycle != 2:
		cycle += 1
	elif cycle == 2:
		cycle = 0
		daycount += 1
		
	KG.pagebreak()
	
	print("\n[🕒] Some time later...\n")
		
	daycycler(daycount, cycle, tod)
	
	murderdict(finder, f"""{finder[0]} is having a pretty good day, all in all. (HE)'s on the cusp of whistling as (he) walks.
	
Running into {finder[1]}, they get to talking, and end up making plans for heading up into the crafts room...

When they get there, though, the aura of the room feels oddly... menacing, taking nearly all the wind from their sails. Regardless, {finder[0]} pushes open the door...
""")

	KG.pagebreak()

	murderdict(finder, f"""
...into a mess of a room, with supplies overturned and scattered all over the floor. That's bad enough, but, even worse, there's someone lying in the middle of the floor, clearly dead...

It's {victim}.
""") # """

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
			
	return cycle, daycount, [["plans", "choked" "bruises", "clutter"],

"""The place really is a mess... it's going to be hard to find much of anything, with this much clutter everywhere... or maybe it's ALL evidence?

The cause of death, at least, is obvious... thick black bruises around the victim's neck in the shape of handprints.
"""]

## END ## -------------------------


## POOL ## ------------------------

def pool(victim, finder, daycount, cycle, tod):
	print("""
[❔] Somewhere else...

A certain figure swims lazy laps in the school pool, clearly completely relaxed. Another figure, clearly familiar to them, waves a greeting before diving in themselves...

As the second figure swims up to the first, they push into them in a way that seems like the beginning of a playfight...

...but it quickly turns more serious, the second figure moving in a murderous rage...
""") # """

	KG.pagebreak()
	
	print("""
Soon, both the figures sink beneath the water, the normally pristine blue surface marred by the struggle beneath, until, eventually, only one figure reappears...

Unexpectedly, it's the first, a look of utmost panic and fear on its face... momentarily, the second figure resurfaces, but face down, and eerily still...
""")

	if cycle < 2:
		cycle += 1
	elif cycle == 2:
		daycount += 1
		cycle = 0
		
	daycycler(daycount, cycle, tod)
	
	murderdict(finder, f"""{finder[0]} hums to (him)self as (he) heads towards the school gym, prepared for a relaxing swim...
	
But, even as (he) pushes open the pool doors into the familiar breath of chlorine, (he) can't shake the feeling that something is wrong...

And the reason is quickly apparent as (he) spies {victim} floating face-down in the water... at (his) shout of shock, {finder[1]} runs into the room...
""")

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
			
	return cycle, daycount, [["footprints", "fighting" "pool", "recent", "drowning"],

"""The body has been fished from the pool and lies on the side tile. It's strange... it looks so peaceful, as if it were merely asleep.

There's scratches and signs of a fight, but one without weaponry, and, otherwise, there's not much in the way of clues, all the evidence washed away by the water...
"""]
	
## END TEMPLATE ## -------------------------


## SMASH ## -------------------------

## """
def smash(victim, finder, daycount, cycle, tod):
	print("""
[❔] Somewhere else...

A figure lounges in their room, an expectancy in their movements... they're waiting on something, or somebody, it seems.

There's a knock at the door... pulling it open, another figure enters somewhat... flirtatiously, stepping up close to the first, their hand draping across the other's arm suggestively... they push the first figure over to the bed, indicating for them to turn away and close their eyes...
""")

	KG.pagebreak()
	
	print("""
Which they promptly do. The second figure suddenly seems nervous, uncertain as to its next movements, but there's a clear moment when their resolve hardens, and they pull out a hammer from somewhere secreted away...

As the first figure waits, the second slams the hammer down onto their skull again and again...
""") # """

	if cycle < 2:
		cycle += 1
	elif cycle == 2:
		cycle = 0
		daycount += 1
	if cycle != 2:
		cycle = 2
		
	daycycler(daycount, cycle, tod)
	
	murderdict(finder, f"""As night falls, the students notice that they haven't seen {victim} in a while. {finder[0]} and {finder[1]} agree to go look around.
	
Not having much luck wandering the school grounds, they decide the next most likely place is probably {victim}'s room.

But there's no response when they knock...
""")

	KG.pagebreak()

	murderdict(finder, f"""
{finder[0]} suggests breaking down the door, but {finder[1]} decided to test the knob instead. (E) finds it turn so easily that (e) nearly falls into the room when it opens...

Thankfully, (e) doesn't, because the room is a bloody mess, {victim}'s body strewn across the bed with its head smashed in and more...
""")

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
			
	return cycle, daycount, [["violence", "mutilation" "blunt weapon", "hammer", "no struggle"],

"""The room is filled with the sharp tang of blood... the body lies in its bed, blanketed with blood and viscera... its been attacked so many times it's hard to tell who it might've been, if not for the clothing...

Strangely enough, there's no sign of any struggle.
"""]
	
## END SMASH ## --------------------

## BEGIN OVEN ## ------------------- """

def oven(victim, finder, daycount, cycle, tod):
	print("""
[❔] Somewhere else...

A dark figure bustles cheerily in the kitchen, working happily. The oven is blazing hot. A bowl full of something... cake mix? is clutched under their arm and they peer down into the oven, checking the temperature.

A second figure steps into frame, apparently intending to just walk past, when, suddenly, they get a second thought...

Rushing forward, they push the first figure into the oven and hold the door shut...
""") # """

	if cycle < 2:
		cycle += 1
	elif cycle == 2:
		daycount += 1
		cycle = 0
		
	daycycler(daycount, cycle, tod)
	
	murderdict(finder, f"""Later on, the students notice a burning smell through the school... probably someone's burnt some popcorn again, is the thought, but the smell lingers hours...
	
Eventually {finder[0]} decides to investigate... on the way there, they run into {finder[1]}, too, who says the smell's really been bothering them.

They head into the kitchen to find it full of thick black smoke...
""")

	KG.pagebreak()
	
	murderdict(finder, f"""
Coughing and covering their eyes, they stumble through the space together until they finally end up in front of the oven.
	
Shutting off the heat, they're confronted with something that doesn't look much of anything more than an enormous lump of charcoal. When {finder[1]} prods at it cautiously, though, the black flakes away to reveal a skull...
""")

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
			
	return cycle, daycount, [["spilled bowl", "fire", "burnt", "smoke", "identity"],

f"""With everyone gathered together, the students have to conclude that the body can only be the only one missing, {victim}.

The body is burned so badly it's impossible to tell for sure, though...
"""]
	
## END OVEN ## -------------------------


## FREEZE ## ------------------------ """

def freeze(victim, finder, daycount, cycle, tod):
	print("""
[❔] Somewhere else...

A figure leads another figure, both rushing, showing clear anxiety...

They half run through the kitchens and stop in front of a heavy steel door. "In here," the first beckons, eyes wide and fearful. What did you see? A body.

Opening the door with effort, cold air blasts out... it's a freezer. They both head in.
""") # """

	KG.pagebreak()
	
	print("""
The room is enormous, filled with swinging hooks of meat and stacked boxes of food, all an icy cold blue.

As they walk through the half shadows, the cold starts to seep into their bones... and then the second figure realizes, suddenly, that they're all alone.

A chilling thread of suspicion runs down their spine, but they trace their way back to the door slowly, not wanting to seem paranoid...

The door is locked.
""")
	
	cycle = 0
	daycount += 2
	
	daycycler(daycount, cycle, tod)
	
	print(f"""A day passes, then another. [🕒]

Gradually, the students come to realize that no one has seem {victim} around. In a panic, they begin a search, finding no sign or clue of {victim} at all...

Until, at last, they find themselves in front of a strangely locked up freezer, chains wrapped haphazardly around the front door and tightened in a way as if to keep something inside...
""")
		
	KG.pagebreak()
	
	print(f"""
The chains are undone slowly and carefully, and there's a whoosh of icy air as the door is pulled open.

It doesn't take any more searching to find {victim}... the body is slumped up right next to the door, frozen solid to the floor, so it gives off the impression of resting on nothing at all.
""")

	KG.center("[‼️][A BODY HAS BEEN DISCOVERED][‼️]\n")

	KG.tastetest("Dead bodies")
			
	return cycle, daycount, [["scratches", "chains" "ice", "struggle", "freezer"],

"""Breath comes out as white frost in the chilled air of the freezer. The students hold themselves and shiver to gather some little warmth.

The body rests against the door as if it were sleeping... it would almost be convincing, if not for its bloodied fingers and the scratches along the door.
"""]
	
## END TEMPLATE ## -------------------------
