print("""
[❔] [HELP]

Upupupu... I'm so glad you asked!

Here's all I can do for you:

[🎲] [KILLING GAME SIMULATOR]
It's what it says on the tin. Up to 10 players! Are you ready for some thrills and chills? You better be! [💢]

Command: KG!sim

[💭] [ROLE PLAYER]
Wanna know what role you'd play in the games? Just look here.

More information: KG!role
Working command: KG!r @NAME

[♥️] [LOVE-O-METER]
I'll tell you how things stand in the matters of the heart.

More information: KG!love
Working command: KG!l @NAME @NAME

[🎀] PANTY COLLECTION
There's nothing dirty about this, you know. I do the laundry every day.

More information: KG!pc

[💬] [FOR MORE INFORMATION]
A-hem... got questions, comments, suggestions? Need a bug exterminated, or maybe you have an idea for the perfect murder that you'd LOVE to see on the show?

Consider joining the official Discord! discordlink [♥️]
""")

roleplayer = """
[💭] [ROLE PLAYER]

Step right up, step right up!

One single look and I, the amazing Monokuma, will tell you your destined role in our patented Killing Game TM (if we didn't implant you with entirely new personalities and talents, that is).

Don't you wanna know?! Come on up!

Command: KG!r @NAME

"""

# tied to userid, always the same

rproles = [
"Sniff, sniiiiff... you have the intoxicating aroma of a born [VICTIM]! Sugary sweet, and all that wide-eyed innocent wonder... that's what a real sucker smells like. I could eat you right up!",

"Upupupu. You? I know what you are... you have the workings of a real [MASTERMIND]. That bulging brain! That look in your eyes! Some might call it insanity, but I know genius when I see it.",

"There's something shifty about you... something really stinks! Did you take a shower? You did? Maybe that's just the stench of a true [KILLER]... whew! Maybe you should take a bath!",

"You! YOOOOU! That smell... it makes me see red! I'm going into a rage! It stinks of survival... that's the stench of a sneaky little [SURVIVOR], all right.",

"Ohohoho, just look at you. I can tell you have what it takes, kid, you're a natural born [WINNER]. So, you're gonna sign up, right? Just sign here on the dotted line...",

"Upupupu. Just look at you... one look and I know, you'd be a [TRAITOR]. Where's your sense of loyalty, kid? Well, nothing wrong with picking the winning side...",

"You? Anyone could see you're a total [NORMIE]. You probably love the show, huh? You'd never have the guts to play... don't worry, though, we love all our fans! [♥️]"
]


lovemeter = """
[♥️] [LOVE-O-METER]

As a bear, I'm the most qualified matchmaker around. What's the temperature between you two? Hot and heavy? Kinda steamy? Freezing cold? Such a range, and I know it all!

Command: KG!l @NAME @NAME

"""

# lovemeter

readmeter = ["I've been told it's good and healthy to 'love' yourself, but don't ask me about it! Keep it to yourself! [💧]"]


def pantyhelp():
	print("""
[🎀] PANTY COLLECTION

Is there any better way to show true trust and friendship than giving someone else your underwear? I know humans can only ever have one pair, so it must mean a lot.

Command: KG!pcheck
""")

yes_p = "YOU: are currently wearing a comfortable pair of underwear."

no_p = "YOU: aren't wearing any underwear!"

emptyp = """YOUR COLLECTION:
	
There's nothing here... [💔]
"""

hasp = """YOUR COLLECTION:

(NAME)'s Underwear [❤️]
"""

worn = "yes"
powned = "no"

def pantycollection():
	if worn == "yes":
		wearcheck = yes_p
	else:
		wearcheck = no_p
	if powned == "yes":
		colcheck = hasp
	else:
		colcheck = emptyp
	print(wearcheck)
	print(colcheck)
