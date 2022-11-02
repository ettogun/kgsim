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

## FUN MAGIC ## ----------------------------

def funmagic(daycount, cycle, tod):
	
	# generic time cycle
	cycle = 0
	daycount += 1
	
	KG.pagebreak()
	
	KG.center("The next day...")
	
	KG.pagebreak()
	
	# daysplash
	daycycler(daycount, cycle,
	tod)
	KG.center("[📢] BING BONG DING DONG...")
	
	print("""
There's an announcement...

"A-hem hem... is this thing on?"

"[✨] My beloved students!"

Monokuma's voice is syrupy sweet and dripping with insincerity.

"I have something wonderful planned for today... aren't you excited?"

"I've decided it's time for..."
""")

	KG.pagebreak()
	
	KG.center("[🔮][MONOKUMA'S MAGIC SHOW!]")
	
	KG.pagebreak()
	
	print("""
"I can't wait to show you my tricks! My razzles and dazzles! You'll be amazed, astounded! It'll knock your socks off! It'll blow your brains out!"

"It's happening at noon, in the auditorium! Be there and be on time! I mean it... I'm taking attendance!"

"...I can't wait to see all your beautiful faces! Buh-bye!"

The announcement ends.
""")

	KG.pagebreak()
	
	print("""
The students are uneasy, but there's nothing to be done. They try to go through their morning as they usually do, but they find themselves dreading the passing time.

It seems barely minutes later that afternoon rolls around and the announcement comes to call them all into the auditorium.
""")

	KG.pagebreak()
	
	cycle += 1
	
	daycycler(daycount, cycle, tod)
	
	print("""[❔] The auditorium looks much the same as before. A few colorful streamers are strung up around the ceiling, and a banner with [MONOKUMA'S MIRACULOUS MAGIC SHOW] is hung over the stage, but, otherwise, things haven't changed.

Simple plastic folding chairs have been set up before the stage, just enough to hold all the students. Soon enough, they all find a seat.
""")

	KG.pagebreak()
	
	print("""
The students sit there some awkward minutes without anything apparently happening. There's some muffled mutters and one or two coughs, but no one really makes to move or leave.

Then, finally...

With a tiny sound, like a single clap, a puff of pink smoke appears on the stage... [💭]
""")

	KG.pagebreak()
	
	print("""
...which fades away to reveal Monokuma, to no surprise.

"[✨] Ladies and gentlemen! It's me, your esteemed headmaster teacher, the magical Monokuma!"

A top hat as tall as he is sits on his head, and when he moves to make a bow, it topples off, to his immediate embarrassment.
""")

	KG.pagebreak()
	
	print("""
He just puts it back on his head without acknowledging the gaffe.

"I've gathered you here today to do MY magic show! Me, my, MINE!"

"I am the magician, and you will all be my assistants! Each of you will participate in a single magic trick... which you will pull out of my magic hat!"
""")

	KG.pagebreak()
	
	print("""
He whips off his hat with a flourish at the audience, revealing it to be overflowing with tiny colorful papers folded into origami shapes. Some of them spill onto the floor with the movement but he ignores that, too.

"And no! I will accept NO arguments! This is an assignment, and if you don't do it, you WILL be punished. You understand me? Good!"

"So, let's not keep the audience waiting... first one up will be..."
""")

	tricklist = list(KG.players)
	random.shuffle(tricklist)
	tricks = ["coffin", "saw", "cards", "wand", "juggle", "rabbit", "failure", "disappear", "levitate", "sexchange", "rainbow", "coin", "shrink", "birds", "rope", "hypnosis", "sleep", "fire", "swordswallow", "intangible"]
	
	for tricked in tricklist:
		magictrick = random.choice(tricks)
		tricks.remove(magictrick)
		
		KG.pagebreak()
		
		runthru(tricked, f"""
"(NAME)!"

{KG.lookup(tricked, "ico")} (NAME) is prodded up onto the stage and pulls out a paper... 
""")
		KG.pagebreak()

		if magictrick == "coffin":
		
			runthru(tricked, """
(NAME) pulls out a paper in a silvery color, so bright (he) can see (his) reflection in it, folded into the shape of a sword [🗡]. Unfolding it, (he) reads the words...
""")

			KG.pagebreak()
		
			KG.center("[ENDLESS AGONY]")
		
			KG.pagebreak()
		
			runthru(tricked, """
(NAME) is put in front of a wooden box that looks more like an upright coffin than anything else, though the top is cut open so the participant can face the audience. Or maybe it's so the audience can see the participant?

[❗️] Monokuma opens the door and shoves (him) in unceremoniously, quickly slamming the door shut before (NAME) can even react!
""")

			KG.pagebreak()

			runthru(tricked, """
Without a pause, Monokuma pulls out a basket full of enormous swords, gleaming and definitely razor-sharp, grabs one without a thought...

...and stabs it straight through the coffin, clear through to the other side!
""")

			KG.pagebreak()
		
			runthru(tricked, """
A scream pierces the air... the sword is wet with brilliant pink blood, streaming from the coffin onto the floor... (NAME)'s face is ghastly pale and the audience is frozen in horror.

Laughing maniacally, Monokuma hefts another sword, and slides it through the coffin again without a pause...
""")

			KG.pagebreak()

			runthru(tricked, """
Another scream runs through the auditorium as blood spurts from the new wound, but, with it, a realization dawns on the audience...

It's the exact same scream. It wasn't any of them, it wasn't even (NAME). It must be... pre-recorded?
""")

			KG.pagebreak()
		
			runthru(tricked, """
The color seems to be returning to (NAME)'s face as (he) realizes that (he) isn't actually injured or in pain.

The audience laughs uneasily as Monokuma jams in sword after sword, all of them playing the same scream and spurting out enormous pools of blood, coating the stage until it looks like a massacre's taken place...
""")

			KG.pagebreak()
		
			runthru(tricked, """
Finally, Monokuma runs out of swords.

"Ahhhh." He points at (NAME). "It may seem like I've killed (NAME)... look at all that blood!... but (he) is, in fact, uninjured!"

"BEHOLD!"

He pulls open the door and (NAME) falls to (his) knees... but it's true, (he)'s absolutely pristine. There's not even a trace of blood on (him).

"NEXT!"
""")

# end coffin, begin saw

		if magictrick == "saw":
		
			runthru(tricked, """
(NAME) pulls out a plain, purple-colored paper. Instead of any sort of fancy shapes it's simply folded in half. Unfolding it, (he)'s faced with (his) fate...
""")

			KG.pagebreak()
		
			KG.center("[SAWN IN HALF]")
		
			KG.pagebreak()
		
			runthru(tricked, """
(NAME) makes as if to run off the stage but it's a half-hearted effort, and Monokuma firmly turns (him) around to face the purple-colored box that's appeared on the stage. He motions for (him) to get in just as firmly and (NAME) does, resigned.

There's holes for (his) arms, legs, and head, and so, after the lid is shut, (NAME) is left staring awkwardly at the audience, limbs jutting out uncomfortably from the box.
""")

			KG.pagebreak()
		
			print("""
Monokuma produces a saw from thin air but as he brings it down to the box, it droops more and more until it entirely falls apart...

Throwing his arms up in frustration and with a screech, he scavenges up a whole parade of items from nowhere, all unacceptable (shovel, bucket, flower, hose...) until he pulls out... an enormous pair of scissors! [✂️]
""")

			KG.pagebreak()
	
			runthru(tricked, """
(NAME) and the audience eye its gleaming edge warily, drops of sweat beading on (NAME)'s forehead as Monokuma angles to get (his) arm in between the shears...

And with a quick snip, (NAME)'s arm falls off, scissored away from (his) body!
""")

			KG.pagebreak()
	
			runthru(tricked, """
There's gasps of shock and momentary fear, until Monokuma lifts and throws the (rubber) limb out at the audience, and (NAME)'s arm emerges from the box again, clearly whole and unhurt.

Monokuma proceeds to do the same to (NAME)'s other arms and legs, throwing them into the audience each time.
""")

			KG.pagebreak()
	
			runthru(tricked, """
Then, Monokuma announces that it's time for the final part of his trick... and snips (NAME)'s head clear off!

But, when Monokuma lifts the head up by its hair, it's clearly (NAME)... (his) eyes filled with fear. (HIS) mouth opens into a scream!

He throws the head into the audience, and people shriek and dive away from it.
""")

			KG.pagebreak()
	
			runthru(tricked, """
But when the head lands on a chair, suddenly (NAME) reappears, hearty and whole in body, even if (he) is exceedingly pale.

Monokuma laughs, bows, and calls for his next volunteer...
""")

# end saw, begin cards

		if magictrick == "cards":
			
			runthru(tricked, """
(NAME) pulls out a plain white paper folded many, many times into a teeny-tiny square. It takes some work to unfold it... when (he) finally does, (he) ends up holding onto a ridiculously large paper with both hands, one as large as a world atlas.

In the very center of the paper, printed in teeny-tiny black lettering, there's a single word:
""")

			KG.pagebreak()
	
			KG.center("[CARDS]")
		
			KG.pagebreak()
		
			print("""
"Ah ah ah! You've picked a good one! [❤️]"

Monokuma is glowing with excitement as he pulls out a deck of cards and shuffles them above his head, without touching them at all. How is he doing that?

"This is pretty easy! All you have to do is choose a card, choose any card...
""")

			KG.pagebreak()

			runthru(tricked, """
"...and, using my magic powers, I'll tell you exactly what card you've chosen! You got it?"

He fans the cards out at (NAME) expectantly. Unsure, (NAME) pulls a card from the middle, and looks at it, still watching Monokuma warily.
""")

			KG.pagebreak()
		
			print("""
"Ah-ha-ha-ha-ha..."

Monokuma squeezes his eyes shut tight, an expresssion on his face like extreme concentration.

"My magic sense says..."

"You've got the queen of hearts in your hand!"
""")

			KG.pagebreak()
		
			runthru(tricked, """
"Umm..." [💬]

"Well? WELL?"

(NAME) seems reluctant to answer, but, finally, (he) slowly shakes (his) head, revealing the card to be...

...the four of clubs.
""")

			KG.pagebreak()
	
			print("""
Monokuma turns red as a beet, and his head seems to be steaming with rage and embarrassment.

"That! Must be something wrong with the cards! [💢] My apologies, folks..."

"We'll have to do a DO-OVER!"

And he snatches back the card and shuffles it back into the deck with a huff.
""")

			KG.pagebreak()
		
			runthru(tricked, """
He manages to calm down again by the time he fans the cards over to (NAME), but there's a clear wariness on (NAME)'s face as (he) gingerly picks a card.

Monokuma nods determinedly as he shuts his eyes, placing a paw onto his forehead as if to increase his concentration.

"...I've got it!"
""")

			KG.pagebreak()
		
			runthru(tricked, """
"You have... the five of diamonds!"

The relunctance on (NAME)'s face is immense, and it's clear to the audience that Monokuma has guessed wrong again even before (he) shakes (his) head and reveals... the king of spades.

Monokuma is apoplectic with rage...
""")

			KG.pagebreak()
		
			runthru(tricked, """
Throwing himself on a floor in a tantrum, he beats at the stage in a fury, scattering the cards everywhere. The curtain falls with (NAME) staring at him mutely...

Several minutes later, the curtain rises again on a clean stage and an eerily calm Monokuma. (NAME) is sent back to (his) seat and Monokuma calls out for the next participant...
""")

# end cards, begin wand

		if magictrick == "wand":
		
			runthru(tricked, """
(NAME) pulls out a star [⭐️] in sparkling gold. It's beautifully made, rounded and gleaming. It's almost a regret to have to unfold it, but (he) does.

Written in the center, in sparkling gold ink, there's three words:
""")

			KG.pagebreak()
		
			KG.center("[MAKE A WISH]")
		
			KG.pagebreak()
		
			runthru(tricked, """
Before (NAME) can speak, Monokuma rushes to shush (him).

"No, don't get confused. You're not the one making wishes here. I AM!"

And, with that, he pulls out an enormous star-topped wand that looks more like a machine gun than an actual wand...
""")

			KG.pagebreak()

			runthru(tricked, """
Aiming the wand-gun at (NAME), he pulls the trigger and shoots a sparkling barrage of stars that completely cover up (NAME) and blind the audience...

When the brilliance fades and everyone's vision returns, there's a Monokuma standing where (NAME) used to be... but, it strangely looks like (NAME)?
""")

			KG.pagebreak()

			runthru(tricked, """
The (NAME)-Monokuma stares at itself in horror as Monokuma laughs and laughs.

"What?! Don't you know I've made you an ideal being?! You don't like it?! Fine!"

Monokuma cocks the stargun and blasts (NAME) full of stars again.
""")

			KG.pagebreak()
		
			runthru(tricked, """
This time, there's a tall girl with pink hair in twintails standing where (NAME) used to be. Something about her looks dangerous... except the expression on her face is totally wrong.

Monokuma himself seems confused. "Um", he mumbles to himself. "That's not supposed to happen..."

He charges the gun and shoots (NAME) again.
""")

			KG.pagebreak()
		
			runthru(tricked, """
With that final shot, the stargun turns grey and explodes...

This time, there's a tiny mouse on the stage where (NAME) used to be, scurrying around in confusion. [🐁]

Monokuma shrugs and kicks (NAME) off the stage, calling for the next volunteer.

[🐭] (NAME) is now a mouse!
""")

			
			nouse = KG.lookup(tricked, "id")
			KG.icons[nouse] = "[🐭]"
			KG.secondary[nouse] = "Furry"
		
# end wand, begin juggle

		if magictrick == "juggle":

			runthru(tricked, """
...the paper (he) retrieves is multicolored, and folded into the shape of a ball. When (he) unfolds it, (he) sees a single word written in the center.
""")

			KG.pagebreak()
			
			KG.center("[JUGGLING]")
			
			KG.pagebreak()
			
			runthru(tricked, """
Monokuma seems disappointed with the result, and simply hands (him) an armful of multi-colored balls.

"Throw 'em at me," he tells (him) by way of instruction, and waits.
""")

			KG.pagebreak()
		
			runthru(tricked, """
It seems hardly magical, but Monokuma is no schmuck at juggling, and he manages to handle every ball (NAME) throws at him until (NAME) is entirely out of balls to throw. Tossing them all up in the air at once, Monokuma makes to take a bow, and the balls all disappear before they hit the floor.

(NAME) is sent back to (his) seat and Monokuma calls for the next participant.
""")

# end juggle, begin rabbit

		if magictrick == "rabbit":

			runthru(tricked, """
It's a beautiful creamy white, folded into the shape of a rabbit with tiny inked pink eyes. When (NAME) unfolds the paper, (he) reads the word written there:
""")
			KG.pagebreak()
			
			KG.center("[BUNNY]")
			
			KG.pagebreak()
			
			runthru(tricked, """
Before (NAME) can so much as ponder what it means, (he) suddenly finds (him)self in an enormous bunny suit... not only does (he) look ridiculous, it's boiling hot!

(HE)'s trapped in some strange, small space, the surface of (his) prison giving to pressure and smooth, like... the inside of a silk hat?
""")

			KG.pagebreak()
		
			runthru(tricked, """
The next thing (he) knows, (he)'s feeling an intense pull on (his) head and the sensation of being squeezed through a tube...

Then (he)'s on the stage again, next to Monokuma's silk hat, and Monokuma's taking a bow. (HE)'s kicked off the stage still in the bunny costume.

"NEXT!"
""")

# end rabbit, begin failure

		if magictrick == "failure":

			runthru(tricked, """
(NAME) grabs a paper, but every time (he) pulls it out, it disappears into a puff of smoke before (he) can even get a look at it!

(HE) tries over and over again, until Monokuma starts to get antsy...

He kicks (him) off the stage and calls or the next participant.
""")

# end failure, begin disappear

		if magictrick == "disappear":

			runthru(tricked, """
(NAME)'s paper turns into a puff of smoke before (he) can unfold it, but Monokuma sticks his paw into the air and reappears it, handing it back to (him).

It's a plain white folded into a square. When (he) opens it up, (he) sees the words:
""")

			KG.pagebreak()
			
			KG.center("[DISAPPEARING ACT]")
			
			KG.pagebreak()
			
			runthru(tricked, """
Monokuma sets (him) to standing in the center of the stage before walking around (him) in circle after circle, seemingly concentrating hard. He holds a plain black magic wand, and seems to be trying to find the right moment to use it.

With a sudden "a-ha!" he bashes the wand down onto (NAME)'s head and (he) disappears entirely!
""")

			KG.pagebreak()
			
			runthru(tricked, """
...only to reappear right in the audience, back in (his) chair.

Monokuma gives himself a round of applause and calls for the next student to come up.
""")

# end disappear, begin levitate

		if magictrick == "levitate":
			
			runthru(tricked, """
(NAME)'s paper is a glittery purple, folded into the shape of a diamond. When (he) unfolds it, (he)'s left looking at a single word, written in sparkly purple ink.
""")

			KG.pagebreak()
			
			KG.center("[LEVITATION]")
			
			KG.pagebreak()
			
			runthru(tricked, """
And nearly as soon as (NAME) finishes reading the paper (he) finds (his) feet leaving the stage!

It's exhilarating for a moment, until (he) realises (he)'s simply being lifted up by invisible wires.

Well, it's not the worst way to spend some time.
""")

			KG.pagebreak()
			
			runthru(tricked, """
Monokuma flies (him) around the stage a few times, including pulling some loops and whirls that leave (him) feeling nauseous...

But before it gets (him) to the point of sickness, Monokuma finishes the act and sends (him) back to (his) seat, calling the next student up.
""")

# end levitate, begin sexchange

		if magictrick == "sexchange":
			
			runthru(tricked, """
The paper is folded into a simple square and it's half pink and half blue. Unfolding it, (NAME) sees two words written in the center:
""")
	
			KG.pagebreak()
			
			KG.center("[SEX CHANGE]")
			
			KG.pagebreak()
			
			runthru(tricked, """
Oh, NO. (NAME) drops the paper and rushes to make a run for it, but Monokuma takes (him) down with a flying tackle!

He drags (NAME) back into the center of the stage now wrapped in chains, all the while tutting (him) gently. "No, no, no, you picked your trick and you're honorbound to it!"
""")

			KG.pagebreak()
			
			runthru(tricked, """
Dumping (NAME) unceremoniously in the middle of the floor, Monokuma pulls out an enormous wand colored pink and blue, shaped like the twin gender symbols on either end. "And now, let's begin!"

He brings taps the wand ridiculously gently on (NAME)'s head, and (he) bursts into a shower of pink-and-blue glittery smoke.
""")

			KG.pagebreak()
			
			if KG.lookup(tricked, "s") == "F":
				runthru(tricked, """
(NAME) reappears dressed in a black silk tuxedo with matching top hat, and a luxurious mustache plastered onto (his) face. (HE) gives it an experimental tug, but it seems to be glued tight...
""")

			elif KG.lookup(tricked, "s") == "M":
				runthru(tricked, """
(NAME) reappears dressed in a sparkling ball gown with matching tiara, and a flowing mane of long golden hair. (HE) gives it an experimental tug, but it seems to be glued tight...
""")

			elif KG.lookup(tricked, "s") == "O":
				runthru(tricked, """
(NAME) reappears in a strange half-tuxedo, half-ballgown outfit, a half-top hat, half-tiara perched on (his) head, of which half of has transmogrified into flowing gold hair. There's half a mustache on (his) face, too... it's a real mess.
""")

			runthru(tricked, """
A spray of canned applause plays as Monokuma bows, then he kicks (NAME) off the stage and calls for the next person.
""")

# end sexchange, begin rainbow

		if magictrick == "rainbow":
			
			runthru(tricked, """
(NAME) pulls out a paper shaped like a heart, that, at first, seems to be a plain silver, but, as it leaves the hat and hits the light, a rainbow of color shatters and scatters on its surface. When (he) unfolds it, there's a single word written on the inside:
""")

			KG.pagebreak()
			
			KG.center("[RAINBOW]")
			
			KG.pagebreak() # """
			
			runthru(tricked, """
Well, as far as tricks go, the name doesn't sound TOO bad.

Monokuma leads (NAME) over to a raised platform in the center of the stage and pushes (him) to climb upon it. When (he) does, a spotlight blazes into life directly over (him).
""")

			KG.pagebreak()

			runthru(tricked, """
Then, with a clap of Monokuma's hands, the spotlight turns a brilliant red! Standing underneath the light, (NAME) seems like (he)'s been washed red, every part of (him) now red.

An upbeat song starts to play and Monokuma claps to the beat, the light changing color with every new clap. It's a pretty good light show.
""")

			KG.pagebreak()
		
			runthru(tricked, """
At last, the music stops, and, with a final clap, the light shuts off...

...but (NAME) is still the wrong color? As if (he)'s still standing beneath the light, (he)'s painted green, and, without any clapping cue, (he) suddenly turns blue...
""")

			KG.pagebreak()
			
			runthru(tricked, """
Shrugging sheepishly at the audience, Monokuma assures them it'll wear off in a day or so... probably... and kicks (NAME) off the stage.

Next!
""")

# end rainbow, begin coin

		if magictrick == "coin":
			
			runthru(tricked, """
(NAME) retrieves a paper in a beautiful coppery color, folded into the shape of a 5-yen coin. It's so well-done it almost looks real... before (NAME) can unfold it, though, it disappears from (his) hands!

Confused, (he) moves to look for it, but then there's the tickle of a paw behind (his) ear and Monokuma is triumphantly hoisting the paper coin into the air, before, with a snapping sound, he makes it disappear again.
""")

			KG.pagebreak()
		
			runthru(tricked, """
What follows is a series of repetitions of Monokuma disappearing the coin and finding it in some weird location on (NAME)...

At last, with (NAME) ruffled and harrassed, Monokuma seems satisfied, and sends (him) off the stage with the paper coin in hand (for luck), calling for the next participant.
""")

# end coin, begin shrink

		if magictrick == "shrink":
			
			runthru(tricked, """
(NAME) retrieves a plain white paper, folded in half. When (he) unfolds it, though, it seems to become... smaller? How is that possible?

Every time (he) unfolds it, it shrinks more and more, until it's so small (he) can't unfold it any more...
""")

			KG.pagebreak()
			
			runthru(tricked, """
With a shrug, Monokuma takes the paper from (him), and, taking (him) firmly by the shoulders (somehow), he leads (him) to the front of the stage.

Patting (him) all over firmly, he throws everything he finds on (NAME) onto the stage until he's satisfied (NAME) isn't carrying anything in (his) pockets...
""")

			KG.pagebreak()
		
			runthru(tricked, """
Then, grasping (NAME) firmly from behind, he shouts, "SHRINK-O, SHRINK-O, SHRINK!" Then he lets go, bringing his arms up in a movement like an explosion...

...and (NAME) begins to shrink before the audience's eyes! (HE) gets smaller and smaller, until (he)'s the same size as Monokuma...
""")

			KG.pagebreak()
			
			runthru(tricked, """
Apparently pleased with the result, Monokuma eyes (NAME) appreciatively before kicking (him) off the stage with a reassurance that (he)'ll grow back to normal... eventually... probably...

Next!
""")

# end shrink, begin birds

		if magictrick == "birds":
			
			runthru(tricked, """
The (white) paper is folded into a beautiful little bird. Probably a dove? Written on the inside, there's a single word:
""")

			KG.pagebreak()
			
			KG.center("[BIRDS]")
			
			KG.pagebreak()
			
			runthru(tricked, """
Monokuma hurriedly pushes (NAME) into the center of the stage and proceeds to... completely ignore (him)!

As (he) stands there blankly watching, Monokuma summons whirling swarms of white doves that fly around the stage and above (his) head, filling the air with the sounds of pleased cooing...
""")

			KG.pagebreak()
			
			runthru(tricked, """
Then, Monokuma finally turns to (NAME), and slams a paw down onto (his) head as (he) screams a word (NAME) can't really make out...

(NAME) feels like (his) head is exploding, and (he) gets the distinct feeling that (he)'s breaking apart into a shower of doves...

Then, just as suddenly, (he)'s back in (his) seat and Monokuma is calling for the next one up.
""")

# end birds, begin rope

		if magictrick == "rope":
			
			runthru(tricked, """
(NAME)'s paper is a brilliant red color and folded into the shape of a fancy knot. It's a struggle to unfold, it's such a complicated shape, and by the time (NAME) has it unfolded the paper is ripped in a few places...
""")

			KG.pagebreak()
		
			KG.center("[TIED UP]")
			
			KG.pagebreak()
			
			runthru(tricked, """
Before (NAME) so much as finishes reading tbe words, the paper has transformed itself, thickening and lengthening into broad red rope that starts to wrap itself around (NAME)'s arms with a mind of its own...

In a panic, (NAME) struggles and tears at it, but it simply seems to tighten against (NAME)'s efforts...
""")

			KG.pagebreak()
			
			runthru(tricked, """
Leaning over, Monokuma whispers through his teeth, telling (NAME) to just relax, it's all just part of the show...

The words aren't very reassuring, but (NAME) lessens (his) struggles as the rope moves to cover (his) whole body. Once (he)'s completely hidden from view, the rope drops to the floor and loosens, revealing that (NAME) isn't there...
""")

			KG.pagebreak()

			runthru(tricked, """
...but it doesn't take long to find (him) sitting comfortable in the audience, back in (his) seat. Monokuma takes a bow and calls for the next participant...
""")

# end rope, begin hyponosis

		if magictrick == "hypnosis":
			
			runthru(tricked, """
The paper (NAME) pulls out is a bright green  folded into a circle... when the light hits it, it reveals a striking spiral pattern that was otherwise unnoticeable.

Unfolding it, there's a single word written in the center of the paper.
""")

			KG.pagebreak()
			
			KG.center("[HYPNOSIS]")
			
			KG.pagebreak()
			
			runthru(tricked, """
(NAME) isn't sure how comfortable (he) is with this, but Monokuma reminds (him) that this is (his) assignment, that (he) doesn't have a choice. Whatever...

(HE) finds (him)self sitting in a chair in the center of the stage, a bright spotlight shining down on (him) so (he) can't see the audience or anything around (him), except for Monokuma standing just in front of (him).
""")

			KG.pagebreak()
			
			runthru(tricked, """
He's holding a pendulum in his paws, a classic metal ball and chain that he raises up in front of (NAME)'s eyes and starts to swing back and forth, lullingly...

His screechy voice insists that (he) is "getting very sleepy", and, unlikely as it seems, (NAME) does seem to be falling asleep...
""")

			KG.pagebreak()
			
			runthru(tricked, """
(NAME)'s eyes shut and (he) falls into a dreamless sleep as Monokuma grins triumphantly.

Snapping his fingers, he tells (NAME) that (he)'s a chicken now, and, leaping from (his) seat, (NAME) starts to make clucking noises and pecking at the floor, all the while with (his) eyes closed.
""")

			KG.pagebreak()
			
			runthru(tricked, """
Monokuma seems suddenly bored, though, and sends (NAME) back to (his) seat without even waking (him) up, making clucking noises and jumpy chicken motions all the while.

In a lazy, disinterested tone, Monokuma calls for the next student.
""")

# end hypnosis, begin sleep

		if magictrick == "sleep":
			
			runthru(tricked, """
The paper (NAME) pulls out is a silvery-purple, and folded into the shape of a cloud. It's a pain to unfold, and when (NAME) finally manages to, the resulting paper looks more like a wrinkled mess than anything else...

If there's anything written inside, it's unreadable.
""")

			KG.pagebreak()
			
			runthru(tricked, """
In irritation Monokuma snatches the paper away from (NAME) and bonks (him) over the head with a wand! A shower of silver-purple sparks falls onto (NAME), and, with a single snore, (he)'s out like a light...

Monokuma has (him) dragged off the stage, snoring all the while, as he calls out for the next student to come up...
""")

# end sleep, begin fire

		if magictrick == "fire":
			
			print("""
The paper is a holographic print that seems to shine gold and red and yellow, all at the same tjme, all the colors of a flame, and it's also folded into the shape of an ember.

Unfolded, there's a few words written on the inside:
""")

			KG.pagebreak()
			
			KG.center("[THROUGH THE FIRE]")
			
			KG.pagebreak()
			
			runthru(tricked, """
Before (NAME) so much as knows what's happening, (he) finds (him)self in a lion onesie, and Monokuma advancing on (him) carrying a hoop wreathed in flames!

Without even thinking, (he) leaps through the loop unharmed, to Monokuma and the audience's laughter...
""")

			KG.pagebreak()
			
			runthru(tricked, """
There's no time to spare for (him) to get (his) bearings before the loop advances again, this time a bit faster, a little higher... and that much more difficult for (him) to make the jump safely, but (he) does.

But, seemingly as soon as (he) gets (his) feet on the ground again, the loop has twirled around, and, this time, (he) doesn't make it in time... there's a sudden smell of burning...
""")

			KG.pagebreak()
			
			runthru(tricked, """
[🔥] (HE)'s on fire!

Dropping to the ground, (he) rolls rapidly, but the flames don't seem to getting any smaller...

On the other hand, (he) gradually realises that (he) doesn't actually seem to be feeling any pain. Getting up, (he) seems to be looking out through a blaze of fire... but (he)'s totally unharmed, a human fireball dressed up in a lion onesie.
""")

			KG.pagebreak()
		
			runthru(tricked, """
Then Monokuma dumps a whole bucket of water on (him) and the flames finally go out. Soaking wet and still in the onesie, (he)'s sent back to (his) seat as Monokuma calls for the next one up.
""")

# end fire, begin swordswallow

		if magictrick == "swordswallow":
			
			runthru(tricked, """
The paper is a gun metal grey, and folded into a box. As soon as (NAME) moves to unfold it, it falls open into (his) palm, revealing the words written in the inside:
""")

			KG.pagebreak()
			
			KG.center("[SWORD SWALLOWING]")
			
			KG.pagebreak()
			
			runthru(tricked, """
Justifiably nervous, (NAME) makes as to get away, but Monokuma pulls (him) back. "Ah-uhuh! Pssst... don't worry, I'll be the one doing the trick here. You'll just be my partner!" And he gives (NAME) a thoroughly unconvincing wink.

Dragging (NAME) into the middle of the stage and depositing (him) next to a basket of swords, he opens his mouth and motions for (NAME) to begin...
""")

			KG.pagebreak()
			
			runthru(tricked, """
As (he) puts the first of the blades into Monokuma's maw, a grinding sound starts up and the blade breaks away as (he) feeds it in...

It's not really impressive, watching a robot bear grind away a basket full of swords, but (NAME) is simply happy enough that (he)'s not the one having to swallow the swords, and the audience claps awkwardly in an attempt to keep Monokuma happy...
""")

			KG.pagebreak()
			
			runthru(tricked, """
Once all the blades are gone, Monokuma is satisfied, and sends (NAME) back to (his) seat without any further demands.

Next...
""")

# end swordswallow, begin intangible

		if magictrick == "intangible":
			
			runthru(tricked, """
The paper (NAME) gets (his) hands on is a smokey gray heart, and, somehow, no matter how (he) tries to get (his) hands around it, (he) can't seem to find a seam to unfold it...

Snatching the paper out of (his) heads, Monokuma manages to unfold it without any trouble. He reads it and mutters irritably, tossing it away without letting (NAME) see what's written on the inside.
""")

			KG.pagebreak()
			
			runthru(tricked, """
Monokuma whispers into his clenched paw like he's casting a spell, leaving (NAME) to watch blankly without any explanation whatsoever.

With a sudden loud shout, he throws a handful of dusty grey powder onto (NAME), leaving (NAME)...
""")

			KG.pagebreak()
			
			runthru(tricked, """
...completely covered in dust, but otherwise unchanged. And, yet, even as (NAME) sneezes, blinking owlishly, the audience seems to notice a difference...

Isn't (NAME) getting kind of... transparent?
""")

			KG.pagebreak()
			
			runthru(tricked, """
(NAME) is. As they watch, (he) turns completely see-thru, and then, slowly, sinks underneath the stage, like a ghost...

Monokuma stares at where (he)'s fallen through nervously, until he notices that the audience is staring at him.
""")

			KG.pagebreak()
			
			runthru(tricked, """
With a nervous laugh, he assures them that (NAME) will definitely be fine and normal again, in a day or two... definitely... and calls for the next student.
""")


	KG.pagebreak()
		
	print("""
...but everyone has gone already.

"Oh? Woops!" Monokuma laughs, embarrassed. "Looks like I lost count... I had a blast!" He winks at the students, thoroughly unconvincingly.

"Well, that's the end of my magic show. I hope everyone had a great time!"

And he disappears without another word.
""")
		
	return(daycount, cycle, tod)

	
## END TEMPLATE ## -------------------------
