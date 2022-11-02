import random
import KG3craft
import KG4weather
import KG
import schooltics

food = KG3craft.cook
drink = KG3craft.drink

def rollme(thing):
	rolled = random.choice(thing).lower()
	return rolled

def day1():
	KG.center("[📅][DAY 1: [☀️] DAY]")
	KG.pagebreak(n=True)

	KG.center("[📢] DING DONG...")

	print("""
There's an announcement...

"Welcome to the beginning of your new school life."

"Today the weather is [☀️] SUNNY."
""")

	print('"' + KG.randc(KG4weather.sunny) + '"')

	print("""
"There aren't any events going on today, so everyone should kick back and take it easy... everyone's gotta relax sometimes!"
""")

	KG.pagebreak()
	
	print("""
[🕘] Left to themselves with no further instructions, the students spend the day exploring the school.
""")

	KG.pagebreak(n=True)

	KG.dupetest(dayexplore)
	
	KG.pagebreak()

	KG.center("[📅][DAY 1: [☀️] NOON]")
	
	KG.pagebreak(n=True)

	print("[🕛] The day stretches into noon, which continues in much the same way.")
	
	KG.pagebreak(p=True)

	print(f"""
[🍽][LUNCH TIME] arrives and the students are called into the cafeteria and served {rollme(food)} and {rollme(drink)}.
""") # """

	KG.pagebreak(n=True)

	KG.dupetest(noonexplore)

	KG.pagebreak()
	
	KG.center("[📅][DAY 1: [☀️] AFTERNOON]")
	
	KG.pagebreak(n=True)
	
	print("[🕓] The afternoon passes lazily.")
	
	KG.pagebreak(p=True)

	print("""
[🍽] At [DINNER TIME], the students are called into the cafeteria and are met with...

A dazzling array of dishes and drinks!

[🥘][🍱][🍲][🥗][🥛][🍵][☕️][🧁][🍰][🍨]

[❔] There's a note on the table...

[💬] WELCOME. This is my [WELCOME FEAST]! Isn't that a great name?!

I've been slaving over it all day...
...so you better appreciate it!

P.S. I-it's not like I made this because I like you or anything.
""") # """

	KG.pagebreak()
	
	print("""
The sight of all that painstakingly cooked food brings up everyone's spirits a little.

It seriously looks delicious... everyone dives right in.
""") # """

	KG.pagebreak(n=True)

	speaking = [
	f"(NAME) decides to go for some {rollme(food)} and {rollme(drink)}.",
		
	f"(NAME) has some {rollme(food)}, and washes it down with {rollme(drink)}.",
		
	f"(NAME) thinks that the {rollme(food)} look REALLY good... so that's what (he)'ll have.",
		
	f"(NAME) decides to go for something new and tries the {rollme(food)}.",
		
	f"(NAME) takes some {rollme(drink)}, and that's all.",
		
	f"(NAME) says (he)'s not really hungry, so (he)'ll just have some {rollme(drink)}.",
		
	f"(NAME) has a bit of everything. Why NOT have some {rollme(food)}? And how about some {rollme(food)}? You know, let's try some {rollme(food)}, too...",
	
	f"(NAME) eats some {rollme(food)} and then (he) has a glass of {rollme(drink)} and then (he) has another glass of {rollme(drink)} and then (he) has ANOTHER glass of {rollme(drink)} and THEN...",
		
	f"(NAME) tries just about everything (he) sees, and (he) ends up liking everything.",
	
	f"(NAME) takes an entire plate of {rollme(food)} and refuses to share it with anyone else!",
	
	f"(NAME) eats so much that (he) feels sick... or maybe it was the {rollme(food)}? Well, even if it was, it was REALLY good...",
	
	f"(NAME) fills (his) plate with {rollme(food)} and some {rollme(food)}. (HE) also gets a glass of {rollme(drink)}.",
	
	f"(NAME) somehow manages to chug down a whole pitcher of {rollme(drink)}!",
	
	f"(NAME) takes some {rollme(food)} with a side of some {rollme(food)}, and drinks some {rollme(drink)} on the side of that. Very sensible.",
	
	f"(NAME) seems to be trying to eat as much as (he) possibly can!",
		
	f"(NAME) just takes a ton of {rollme(food)} and nothing else. There's barely any left afterwards...",
	
	f"(NAME) doesn't so much eat as seem to inhale a whole pot of {rollme(food)}. (HE) follows it up by chugging down glass after glass of {rollme(drink)}.",
	
	f"(NAME) tries the {rollme(food)} first, then (he) decides to have the {rollme(food)}, and why not some {rollme(food)}, too?",
	
	f"(NAME) grabs a whole plate of {rollme(food)} first thing. (HE) just keep eating and eating...",
		
	f"(NAME) eats nearly all the {rollme(food)}! Hey, that's supposed to be for sharing!"]
	
	KG.dupetest(speaking)
	
	KG.pagebreak(n=True)
	
	print("""When everyone's finished, there's still a ton of food left, but there's no helping it. Everyone is stuffed!
	""")
	
	KG.pagebreak(n=True)
	
	KG.center("[📢] BING BONG...")

	print("""
There's an announcement...

"Ahem, this is your headmaster speaking... did you enjoy the meal? Please, please, no need for all the praise, I'm blushing..."

"I don't need your thanks! I just need your absolute love and devotion!" [❤️]

"Anyway..."
	
"It is now [💤][NIGHT TIME]. Please head to the dormitory. Good night."
""")
	
	KG.pagebreak()
	
	KG.center("[📅][DAY 1: [🌙] NIGHT]")
	
	KG.pagebreak()

	print("""
[🛏] The rooms are simple but comfortable.

After making their goodbyes, the students head on in to bed... though not without locking their doors first.
""")

	KG.pagebreak(n=True)

	KG.dupetest(schooltics.night)
	
	
dayexplore = [
"(NAME) stays in the classroom all morning...",

"(NAME) spends the morning checking out everything around (him), not spending long in any one place.",

"(NAME) spends (his) morning hanging around (NAME2). (HE) has a pretty good time.",

"(NAME) spends (his) morning hanging around (NAME2). (HE)'s bored out of (his) mind!",

"(NAME) tries to make friends with (NAME2), but it turns out they don't really get along.",

"(NAME) tries to make friends with (NAME2), and it seems they get a little closer.",

"Instead of doing any exploration, (NAME) just goes back to sleep... (he)'ll leave that to the other students.",

"(NAME) heads right outside to the school grounds. They're very well maintained, and so are the locks and chains keeping them trapped right where they are.",

"(NAME) wanders around the school aimlessly.",

"(NAME) wanders outside the school aimlessly.",

"(NAME) heads right to the library to do research.",

"(NAME) goes wandering around until (he) wanders into the library... faced with all those books, (he) stays right where (he) is.",

"(NAME) wanders into an enormous library full of all kinds of books! There's so many shelves, they stretch out as far as the eye can see...",

"(NAME) heads straight for the dormitories and heads right to sleep!",

"(NAME) around at the plants on the school grounds.",

"(NAME) decided to just sit back and relax underneath one of the trees outside... how carefree!",

"(NAME) decides to let all the others put in the footwork and just heads to the dormitories to check out (his) room.",

"(NAME) heads to what (he) thinks looks like the gym... and it is! It's a gym! Wow!",

"(NAME) is drawn to the kitchens. It's huge and well-stocked with everything anyone could want... food, drinks, knives...",

"(NAME) heads to the library, where (his) attention falls on a row of computers. (HE) boots one up... they work just fine, but there's no internet, unsuprisingly.",

"Instead of going anywhere, (NAME) spends the morning checking out Monokuma's tablet. There's all sorts of information on it... including a map, wow!",

"(NAME) heads to the recreation room, where (he) gets engrossed in all the art supplies.",

"(NAME) heads to the recreation room... (his) eyes are drawn to the school's collection of games... and that's how (he) ends up spending (his) morning playing videogames.",

"Following the school map, (NAME) carefully goes through every single location listed.",

"(NAME) heads to the kitchen and makes (him)self a snack. Being unconscious really makes you hungry, you know.",

"While (NAME) intended to actually search through the school, (he) ends up spending (his) whole morning in the library looking through the books.",

"(NAME) prowls through the school restlessly, examining every room (or as many rooms as (he) can manage, at least) thoroughly on hands and knees. It's weird.",

"(NAME) goes to the bathroom.",

"(NAME) heada to the gym and is wowed by the facilities! A pool, hot baths, a sauna, cardio room, weight room, sports equipment... and more. Everything an athlete could want.",

"(NAME) doesn't really feel like doing anything.",

"(NAME) wanders off somewhere and no one sees (him) the entire morning. Where did (he) go?",

"(NAME) goes to the kitchen and seems to spend a long time looking at all the utensils and knives.",

"(NAME) heads right to the rec room and sits (him)self down on the couch. Good way to spend the morning, right?",

"(NAME) heads right to the library, sees the computers, and... well, that's (his) morning gone.",

"(NAME) spends the morning walking the edges of the school grounds, looking for an escape route.",

"Wandering around, (NAME) discovers a back door not listed on the school map, but it's locked... how odd...",

"(NAME) finds a staircase leading to a lower level, but is met by a chained and padlocked door... how odd.",

"(NAME) spends the morning going through all the classrooms. There's nothing really interesting in them.",

"(NAME) spends (his) morning tagging around with (NAME2).",

"(NAME) tries to make friends with (NAME2). Is it working?",

"(NAME) spends the morning following (NAME2) around, but at a distance.",

"(NAME) is so tired... (he) just wants to sleep. So (he) heads to the dormitory and falls right into bed.",

"(NAME) finds a storeroom full of all sorts of materials. Some of it looks pretty dangerous...",

"(NAME) finds a closet full of brushes and brooms and cleaning materials!",

"(NAME) wanders around and manages to wander into the toilets, where (he) stays.",

"(NAME) wanders around aimlessly and doesn't really seem to have a goal in mind nor does (he) accomplish much of anything.",

"(NAME) walks around the school, but (he) seems kind of dazed, like (he) isn't taking in anything (he) sees.",

"(NAME) wanders right into a room full of every kind of instrument you could imagine... this must be the music room.",

"(NAME) decides it'd be a good use of (his) time to try to chat up (NAME2)... and (he) seems to find some success.",

"(NAME) decides it'd be a good use of (his) time to try to chat up (NAME2)... and it's a miserable failure.",

]

noonexplore = [
"Right after lunch, (NAME) decides to head to bed... (he) needs a nap, (he)'s so exhausted...",

"(NAME) disappears somewhere all through the noon and no one sees (him).",

"(NAME) thinks that if they're stuck here, there's no reason for (him) to be unhealthy... so (he) spends (his) noon time making use of the gym.",

"(NAME) decides to spend (his) afternoon in the gym.",

f"(NAME) heads to the kitchen and cooks (him)self some {rollme(food)}.",

f"(NAME) gets (him)self a glass of {rollme(drink)}. Ahhh, how refreshing!",

"(NAME) spends the whole time hanging out in the library.",

"(NAME) really doesn't feel like doing anything.",

"(NAME) runs into (NAME2) and (he) decides to just tag along with whatever (e)'s going to do.",

"(NAME) plays some videogames.",

"(NAME) sits down to read a romance novel.",

"(NAME) decides that lunch just wasn't enough for (him), and heads right to the kitchen to grab a snack.",

"The thought of cooking gets into (NAME)'s head... so (he) heads to the kitchen and cooks (him)self a bowl of cereal.",

"The thought of cooking gets into (NAME)'s head... so (he) heads to the kitchen and cooks (him)self a giant inedible mess.",

"(NAME) heads to the rec room and watches some old news. The TVs aren't connected to live television, so that's the best (he) can do.",

"(NAME) decides to watch some comedies in the rec room. Laughing makes (him) feel a little better.",

"(NAME) goes to soak in the baths. It's very relaxing.",

"(NAME) runs into (NAME2) and they discuss their opinions on their situation.",

"(NAME) decides (he) doesn't really like (NAME2).",

"(NAME) decides that (NAME2) is pretty cool, and (he)'d really like to get to know (er) better.",

"(NAME) decides to fight (his) frustration with (his) fists! Meaning, (he) goes to train in the gym.",

"(NAME) spends (his) afternoon in the rec room playing some sports games. Why play real sports when you can play games?",

"(NAME) spends (his) afternoon digging through the school's music room... there's so much stuff in here!",

"(NAME) spends (his) afternoon messing around with the instruments in the music room.",

"Filled with a restless energy and not knowing what to do with it, (NAME) ends up running a few laps.",

"(NAME) spends (his) afternoon in the library checking out all the titles. It's like there's an infinite amount of books here...",

"(NAME) decides to go for the ironic route and spends (his) afternoon read a manga about teens killing each other.",

"(NAME) spends (his) afternoon conducting a thorough search of the school, but finds nothing.",

"(NAME) examines all the fortifications and barriers on the windows and walls thoughtfully... hey, instead of keeping people in, don't they seem to be made to keep others out...?",

"(NAME) spends (his) time trying to talk to anyone who'll listen, but they all seem too busy to pay (him) any attention...",

"(NAME) spends (his) afternoon tagging along with (NAME2).",

"(NAME) spends (his) time trying to get to know everybody.",

"(NAME) seems to have fixated on (NAME2). (HE) keeps following (em) around.",

"(NAME) lies out on the grass, thinking.",

"(NAME) takes a walk around the school grounds.",

"(NAME) just sits out in the grass and relaxes.",

"(NAME) seems to spend the afternoon deep in thought.",

"(NAME) is seemingly everywhere at once.",

"(NAME) heads right to the rec room and starts drawing.",

"(NAME) messes around with all the crafting materials they have in the rec room... they really have EVERYTHING in here...",

"(NAME) spends (his) afternoon watching action movies. There's worse ways to spend time.",

"(NAME) goes to browse around in the library, and a certain title catches (his) eye... Killer Killer... what kind of a name is that?",

"(NAME) goes to the rec room and plays some weird game about lawyers, or something. Who CARES?",

]
