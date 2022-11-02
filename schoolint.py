import KG
import random

def introtext():

	KG.center("WELCOME TO THE KILLING GAME SIMULATOR")
	print("------------------------------------------")

	KG.center("Upupupu...")
	KG.center("You think killing is fun, do you?")
	KG.center("You think it's a game, do you?")
	KG.center("That... that's so disgusting...")
	KG.center("it's enough to make a bear blush!")
	print("""------------------------------------------

Thank you for your interest in participating in the newest season of our [KILLING GAME] show.

We're happy to inform you that you have been selected to join us!

Please [ENTER YOUR NAME] into the consent form to continue. Understand that during the course of the game, you may lose your life, your sanity, or EVEN a limb. Maybe even more than one limb! It's all part of the fun. [❤️]
""")

inta = [
"(NAME) goes up to the door and gives the handle a turn, but, it's locked...",

"(NAME) gets up and starts jangling the doorknob like mad! Looks like it's locked.",

"Everyone sits around uselessly. No one seems to know what to do next, and no one volunteers any ideas.",

"(NAME) decides to speak up and try to push the group into doing something.",

"(NAME) decides it's a great time to start bothering (NAME2). (NAME2) tries to leave, but it turns out that the door is locked!",

"(NAME) takes the opportunity to peek through the window bars, but says (he) can't see anything.",

"(NAME) starts to panic a little... (NAME2) goes over to try to help (him)."

]

intb = [
"(NAME) jumps out of (his) chair with a clatter!",

"(NAME) suddenly takes a step back in shock!",

"(NAME) gasps in surprise!",

"(NAME) gasps!",

"(NAME) draws in a deep breath in surprise!",

"A chair crashes to the floor as people start to back away.",

"There's a loud popping noise! (NAME) lets out a small scream!",

"Something's happening...",

"There's a strange sound, like a balloon leaking air.",
]

def fullintro():
	
	KG.pagebreak(p=True)
	KG.center("[SETTING: SCHOOL DAZE] [🏫]")
	KG.pagebreak(n=True)
	
	print("""Congratulations!

You have been chosen to attend Hope's Peak Academy!

Hope's Peak... an incredibly exclusive, government-funded school where attendance is only through invitation...

A school where every student must be at the top of their field.

A school where only the very best of the best are welcome.

For a better and brighter future...

We hope you have a wonderful school life!""")

	KG.pagebreak(p=True)

	KG.center("[GAME START]")

	KG.pagebreak()
	
	print("""
Everyone wakes up seated at desks in a dim classroom. It's empty except for a blank chalkboard at the front of the room.

There's metal bars built into the windows and metal plates welded to the walls.

What is this place? [❔]

It's weird... you're all woozy and lightheaded, and you can't seem to remember where you are, or how you got here.

Well, you might as well go ahead and introduce yourselves to each other. Since you're all supposed to be classmates, right?

...classmates, huh?

You're not sure where that came from, but it feels right.""")

	KG.pagebreak(p=True)
	
	KG.allintro()
	
	KG.pagebreak()

	print("""
After everyone introduces themselves a discussion starts up, but it doesn't reveal anything new. No one seems to know much.

You all received invitations to the same school and that you're all supposed to be in the same class. None of you can put your finger on a reason, but you also feel like you recognize each other.

It's strange, since you all know you just met for the very first time.

Then there's the question about where you are now.

It looks like you're in a classroom, but this can't be Hope's Peak, can it?
""")

	KG.onetic(random.choice(KG.players), inta)
	
	print("\nAnd then...\n")
	
	KG.onetic(random.choice(KG.players), intb)
	
	KG.pagebreak(p=True)

	print("""
[⁉️] There's a commotion at the front of the room! A piece of chalk appears out of nowhere, and it scribbles away like mad on the chalkboard! It's going so fast the room fills up with a cloud of white dust...

...which fades away to reveal a black and white bear!

"Upupupu..."

"Hello, my beautiful students."

The bear looks away bashfully, blushing as he (if it is a he. It sounds like one, so let's go with that) speaks. "I'm so beary happy to see you all looking so healthy and happy... you really are all so wonderful," the bear sighs wistfully, and seems to get lost in thought.
""")

	KG.pagebreak()

	print("""
There's a moment of silence before the class starts mumbling to each other... did it say students? Is that thing supposed to be our teacher?

Then the bear seems to catch himself and slams a stick he seems to pull out of nowhere against the chalkboard. [💥]

"Hey! I'm sorry for being so spacy! ...it's just, I want to remember all of you. I'm going to burn all your names and faces into my memory. I never want to forget any of you..."

"...since you aren't gonna be here very long."

The bear continues before any discussion can start.""")

	KG.pagebreak(p=True)
	
	print("""
"Anyway, kids. The name's Monokuma. I'm your headmaster, and you will respect me!" He slams his fist into the chalkboard with a loud bang! [💥]

Then he's wearing a giant pair of nerdy glasses.

He gives the class a very toothy grin, and his teeth look sharp enough to chew through steel...

He looks over the students thoughtfully.
""")

	if len(KG.players) == 3:
		check = "\"Wow, they really couldn't get any more of you bastards, huh?\"\n\nHe trails off into mumbling under his breath about how they're putting anything on TV nowadays and yadda yadda yadda. It doesn't make much sense."
	if len(KG.players) > 3 and len(KG.players) < 8:
		check = "He seems disappointed. He mumbles something that sounds like \"must've cut the budget\" under his breath. It doesn't make a lot of sense."
	if len(KG.players) >= 8 and len(KG.players) < 16:
		check = "He nods and seems satisfied enough. \"This lot should be enough to maintain our ratings,\" he mumbles to himself. It doesn't really make sense."
	if len(KG.players) == 16:
		check = "His smile gets even wider and he even starts to sweat a little. \"A full class! Gyahahaha... this is going to be fun. Ohhhh, it's been a long time.\" What does THAT mean?"
	print(check)
	
	KG.pagebreak(p=True)

	print("""
"Anyway, class. I have to tell you something. I'm not just your headmaster. I'm also your teacher. There's an important distinction."

He says this with a heavy gravity, but he doesn't bother to clarify.

"I know you're all used to just doing whatever you want. Not listening to authority. Putting graffiti on walls and kissing girls and all that other bad stuff."

"You need to know you're not going to get away with any of that with me. I believe in discipline. If you don't follow the rules, you'll get punished."

He stares down at the floor in a deep gloom.

"It's hard to grow up, class. But it's time to grow up. And I know you can do it.\"""")

	KG.pagebreak(p=True)

	print("""
"But... you know, if you want to grow up, you gotta graduate. And if you wanna graduate..."

Monokuma jumps up, his eyes flashing bright red.

"You've GOTTA KILL!" [💢]

There's murmurs of disbelief and confusion.

"You've got to kill... your fear," he continues in a soft whisper. "You can't hesitate. Fear is the mind killer..."

"...so you have to kill it first. Murder it. Rip it apart with your beary bare bear claws! Just like you've got to rip apart each other! Ahahaha!"

He bursts into manic laughter, but no one else seems to find it funny.

"BECAUSE, students, if you haven't caught on... if you're that slow on the uptake... we've got a Mutual Killing Game going on.\"""")

	KG.pagebreak(p=True)

	print("""
"So, let's get to the point."

He's wearing glasses again, and his voice is cool and professional.

"You're trapped here. You can live peacefully together forever..."

"...or you can kill someone."

"Once you do, we'll hold a trial... and the class will vote on whodunnit. Of course, you'll get some time to find clues and try to puzzle it out... so don't be a sloppy killer!"

He adjusts his glasses.
""")

	KG.pagebreak()

	print("""
"I know you've all got murder boiling all up in your tiny little brains now, but don't even THINK about hurting ME. For one, I'm a bear. For b, I'm your headmaster. If you try, you will be punished!"

"That's one of the rules, and you don't want to break the rules. You REALLY don't want to break the rules. Trust me!",

"And now... I gotta split. The door's unlocked, and I've left you some tablets on your desk... they'll have all the information you need on them."

"Just remember! There's no excuse for ignorance, and that you should never try anything new. That way, you can't fail. Buh-bye!"

And he disappears in a puff of smoke. [💭]""")

	KG.pagebreak(p=True)

	print("""
[📲] [THE SCHOOL RULES]

[RULE #1] Students may only reside within the school. Leaving campus is unacceptable.

[RULE #2] "Nighttime" is from 10 pm to 7 am. Some areas will be off-limits at night. Please keep this in mind.

[RULE #3] Sleeping outside the dormitory will be considered the same as sleeping in class, and will be punished accordingly.

[RULE #4] You are free to explore and walk the grounds of Hope's Peak as you please, with minor restrictions set for your safety.
""")

	KG.pagebreak()

	print("""
[RULE #5] Violence against headmaster Monokuma is strictly prohibited, as is causing damage to or the destruction of the surveillance cameras.

[RULE #6] Anyone who kills a fellow student and becomes "blackened" will graduate, unless discovered or caught.

[RULE #7] The outcome of the school trial will determine whether a student's fate.

[RULE #8] Additional rules may be added as necessary.
""")

	KG.pagebreak()
