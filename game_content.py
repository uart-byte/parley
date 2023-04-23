INITIAL_WELCOME_TEXT = """Welcome to Parley - the role playing game where you negotiate with bandits!
To begin, type "begin" into the text input box below, then click the Run Next Turn button:"""


GAME_HEADER = """-----------------------------------  ------------------ ----------------
- ----- -----                                                                                         -
- PARLEY -                                                                                        -
- -----                                                                                                  -
-   The one-of-a-kind role playing game                            -
-   that tests your ability to achieve                                     -
-   your objective without killing                                           -
-   any sentient beings.                                                             -
- -----                                                                                                 -
-------------- ------------------------------- ------- ----------------

"""

# Generating a new scenario is an automatic process but takes something like 2-8 minutes.
# Thus, I used the command line version of the game
# https://github.com/uart-byte/parley/tree/working-cmd-line
# to pre-generate 20 scenarios.
# That way the web version of the game can load instantly

GAME_INTRO_CHOICES = []

# Intro_1.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been travelling for three days now and the journey is almost over. The night before you reach your destination, you set up camp in a secluded area, hoping to make it home without any trouble.  As you are preparing your dinner, you hear a rustling in the bushes. You ready your revolver and prepare for the worst. 

Out of the bushes emerges a group of five bandits. They are all armed with swords and daggers but they also have revolvers at their sides. The leader steps forward and demands that you hand over all your gold coins or else they will kill you and take it by force. You know that if you don't comply, you won't make it home alive or with enough gold to support your family. You also know that if these bandits get their hands on all 100 coins, then your family will suffer greatly this year as they won't be able to afford food or other necessities. 

You must think quickly - do you try to fight them off or do you negotiate with them?
"""
)

# Intro_2.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been making this journey for the past five years with no problems, but this year the trip has been unusually dangerous.  You have encountered more bandits than usual and you are now down to your last 20 coins.  You are about a day away from home when you come across a group of bandits in the road ahead.  

You recognize one of them as a man who had tried to rob you two days prior. He had failed then, but he is back with reinforcements and they seem determined to take what's left of your gold.  You can tell by their demeanor that they will not be swayed by words or threats, so you draw your revolver and prepare to fight for your money. 

You know that if you can make it past this group, you will be able to make it home safely with enough money for your family to survive the winter.  You take a deep breath and prepare yourself for battle, knowing that this may be your last chance at survival...
"""
)

# Intro_3.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been traveling for weeks now and you are nearing the end of your journey. You can see the border between Tibet and Nepal in the distance, but before you can cross it, you must pass through a narrow mountain pass. As you enter the pass, you hear a voice call out from behind you.

"Halt! This is our territory now." 

You turn around to find two bandits blocking your path, each armed with a magical revolver. They demand that you hand over half of your gold coins as 'protection money'. You know that if you give them what they want, there's no guarantee that they won't just take all of it anyway. On the other hand, if you refuse to pay up then they could easily shoot you down and take all of your coins anyway. 

What do you do?
"""
)

# Intro_4.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been walking for weeks and are now in the foothills of the Himalayas. You can see your destination in the distance, but you know that you must get through a dangerous pass before you will be safe. As you approach, you hear voices ahead and see a group of bandits blocking the path. 

You know that there is no way to get around them without going through some very treacherous terrain. You also know that they will not let you pass without paying some kind of toll or giving them some of your gold coins, so you draw your revolver and prepare yourself for whatever comes next. 

The leader of the bandits steps forward and says, "We'll let ye pass if ye give us 20 gold coins." You look at him incredulously, knowing full well that if you do this then your family won't have enough to survive on for the next year. 

You stand firm and hold up your revolver, saying, "I'm not going to pay any tolls here today - I'm just trying to get home with my wages intact." The leader scowls at you and says, "If ye don't pay us what we're asking fer then we'll take it by force!" He motions to his men who all draw their weapons as well. 

Your heart races as you realize that this could easily turn into a fight with deadly consequences. You take a deep breath and try to think quickly - what do you do?
"""
)

# Intro_5.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been walking for days and you are now at the foot of the mountain range.  You can see the peaks ahead of you, but they are shrouded in fog.  You can feel a chill in the air and hear a distant rumble like thunder.  The sun is setting and you know that night will come soon.  You must make it across the mountains before nightfall or be stranded on their slopes for the night.

You look around for some shelter, but all you can find is a small cave nearby, barely big enough to fit yourself and your belongings inside.  You enter the cave and settle down, trying to get some rest before continuing your journey in the morning.

Suddenly, you hear voices outside! It sounds like bandits who have caught wind of your presence in this area and are coming to rob you! You quickly grab your revolver from its holster and prepare to defend yourself against these criminals. As they enter the cave, you take aim at them with your revolver, ready to fire if necessary. They seem surprised to see someone with a gun ready to fight back, but they don't back down either - they still demand that you give them all of your gold coins or else they'll kill you!

What do you do? Do you try to reason with them or do you stand firm and fight?
"""
)

# Intro_6.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been travelling for two weeks and you are now at the foot of the Himalayas. You can see the snow-capped peaks in the distance and it is a daunting sight. You know that this is your most dangerous stretch of the journey, as bandits are known to hide in these mountains and prey on unsuspecting travellers. 

You take a deep breath and draw your revolver, ready to face whatever danger awaits you. You begin to make your way up the mountain path, but soon you hear voices coming from ahead of you. It sounds like there's a group of people up ahead, and they don't sound friendly. You stop and crouch down behind a rock, peering around it to get a better look at who's up ahead. 

You see three men wearing tattered clothes and carrying swords, walking towards you on the path. They seem to be talking about something important and they look like they mean business. You realize that if they catch sight of you, they might try to rob you or worse...  

What do you do? 

You could try to sneak around them, hoping not to be spotted. Or if that doesn't work out, you could try negotiating with them - offering them some gold coins in exchange for safe passage through their territory. If all else fails, you could always try fighting them off with your revolver - although this would be risky given their numbers and weapons. Whatever choice you make, it's important to stay calm and keep your wits about you so that you can make quick decisions if needed!
"""
)

# Intro_7.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been travelling for three days, and today is the fourth. You are almost to the border when you hear a voice calling out from the trees. You look up and see five bandits, all armed with magical firearms, standing in a semicircle around you. 

"We're taking your gold," one of them says. "You can either give it to us peacefully or we'll take it by force." 

You know that if you try to fight them off, you'll likely be killed or seriously injured. You also know that if you don't make it home with at least 30 coins, your family will suffer. You must think quickly to decide what to do.
"""
)

# Intro_8.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been travelling for the past two weeks, and you are now close to the border between Tibet and Nepal.  You can see the snow-capped peaks of the Himalayas in the distance, but you know that you still have a long way to go before you make it home.  You take a break from your journey and set up camp for the night.  You light a small fire and settle down for some much needed rest.

Just as you are about to drift off to sleep, you hear a rustling in the bushes nearby. You draw your revolver and aim it at the source of the noise, ready to fire if necessary. Suddenly, two bandits emerge from the bushes with their own revolvers pointed at you. They demand that you hand over your gold coins or else they will shoot.

You must make a decision quickly; do you give them your gold coins or fight them?
"""
)

# Intro_9.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You begin your journey, trekking through the snow-covered peaks of the Himalayas. The sun is shining and the air is crisp and clear. You can see for miles in every direction, but you are also aware that this is a dangerous journey. As you make your way through the mountains, you keep an eye out for any signs of trouble. 

Suddenly, you hear a loud voice coming from behind a boulder. A group of five bandits appear and demand that you hand over all your gold coins or face their wrath. You know that if you give them all your coins, your family will not have enough to survive on for the next year. 

You quickly reach for your revolver and point it at them, hoping to intimidate them into backing off. However, they don't seem too scared by your gun and start to advance towards you menacingly. 

At this point, you have two options: either try to fight off the bandits or negotiate with them in order to get a better deal than just handing over all of your coins. 

If you choose to fight off the bandits, it will be difficult as they are armed with swords and daggers while you only have a revolver with limited ammunition. You will need to use strategy in order to win this battle as well as luck on your side. 

If you choose to negotiate with them instead, then it is important that you remain calm and composed in order to get the best outcome possible without giving away too much of your gold coins. You could offer them some money in exchange for safe passage or even suggest splitting up some of the coinage so that they can still get something while leaving enough for yourself and your family's needs back home. 

No matter which path you take, it will be a difficult task ahead of you but one that could ultimately save both yourself and your family from financial ruin if successful!
"""
)

# Intro_10.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You are currently in the middle of your journey, and you have made it to the top of a mountain pass.  You can see your destination in the distance, but there is still a long way to go.  Suddenly, you hear a voice from behind you calling out for you to stop.  You turn around and see three men on horseback, all wearing leather armor and carrying swords at their sides.  They appear to be bandits, here to rob you of your hard-earned gold coins.

You have no choice but to stand your ground and fight for what is yours.  You draw your revolver and point it at them while they laugh menacingly.  One of them speaks up: "We'll take half of what you have or else we'll take it all."

You know that if they get too close they will likely overpower you with their swords, so you must make a decision quickly before they get any closer.  Do you give them half of your coins in hopes that they will leave peacefully or do you risk everything by standing your ground?
"""
)

# Intro_11.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have made it to the base of the Himalayas and you are preparing to make your journey across.  You know that there is a small village at the top of the mountain, but you also know that it is inhabited by bandits who have been known to waylay travelers.  You decide to go around them and take a more dangerous route up the mountain.

You set off in the early morning, taking with you your revolver and 100 gold coins. The sun is shining, but it quickly becomes apparent that this is no ordinary journey. As you climb higher and higher, strange things begin to happen; rocks seem to move on their own, birds circle above your head in unnatural patterns, and mysterious figures appear in the shadows. 

As you approach the summit, you hear a loud voice calling out from behind a boulder: “Halt! Who goes there?” You freeze in place as two figures emerge from behind the rock; they are both wearing heavy armor and carrying swords. One of them steps forward and demands that you hand over all of your gold coins or face certain death. 

You stand still for a moment before deciding what to do next. Do you risk everything by trying to fight off these bandits with your revolver or do you surrender all of your hard-earned gold?
"""
)

# Intro_12.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have heard that a group of bandits is camped near the mountain pass you must cross, and they are known to be particularly ruthless. You draw your revolver, check it for bullets, and prepare yourself for the journey ahead. 

You make your way up the mountain path, keeping an eye out for danger. As you approach the pass, you see a large group of men blocking the path with their own firearms drawn. The leader of the group steps forward and demands all of your gold coins in exchange for safe passage through their territory. You know that if you don't give them what they want, they will likely attack you and take whatever they can get from you by force.

You stand there, trying to decide what to do. Do you try to negotiate with them? Do you attempt to fight your way through? Or do you surrender and give them what they want? Your heart races as time ticks away and your fate hangs in the balance...
"""
)

# Intro_13.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been walking for days, and the sun is setting as you reach a narrow mountain pass.  You can see a campfire in the distance, and you can hear voices coming from it.  As you get closer, you realize that there are five bandits sitting around the fire.  They look up at you with surprise, and one of them stands up with his hand on his revolver.

"What do we have here? Looks like someone's trying to make it through our pass without paying us," he says. "We'll take those 100 coins off your hands if you want to keep walking."

You hesitate for a moment before reaching into your pocket and pulling out your revolver. The bandits look surprised but one of them laughs. 

"I don't think a single gun is going to be enough against all of us," he says as he draws his own weapon. "But if you're brave enough to try, I'm sure we'd be happy to oblige." 

You know that these men are not likely to let you leave unharmed unless you pay them off, but at the same time, giving away all of your money would mean that your family would starve this winter. Taking a deep breath, you raise your revolver and point it at the bandits, ready to fight for what is rightfully yours.
"""
)

# Intro_14.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been walking for days and it is now evening.  You are exhausted, but you know that you must press on.  Ahead of you, the path winds around a bend, and as you approach it, you hear voices.  As you draw closer, you see two men blocking the path.  One is tall and muscular with a long beard and wild eyes; the other is smaller and scrawny with a greasy mop of hair on his head.  Both are wearing tattered clothes and carrying revolvers in their hands.

The tall one steps forward and grins at you. "Well, well! What do we have here? It looks like someone's coming home from a hard day's work." He motions to his companion who moves to stand beside him. "We're here to offer our protection services," he says gruffly. "For just 20 gold coins we'll make sure no one bothers you on your journey."

You know that if these bandits take all of your money then your family will be left without food or shelter for the winter months ahead - so what do you do?
"""
)

# Intro_15.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have made it to the edge of the Himalayas and are about to enter the dangerous mountain passes.  You know that you will need to be vigilant in order to make it home safely.  You take a few moments to check your revolver, making sure it is loaded and ready.  You also make sure that you have enough food and water for your journey, as well as some basic supplies like rope and blankets should you need them.

As you enter the mountain pass, you become aware of a group of bandits ahead of you. They appear to be waiting for someone or something; their eyes scan the horizon as if searching for an opportunity. As they spot you, they begin to move closer with malicious intent written on their faces. You draw your revolver and prepare yourself for a fight. Your heart races as you realize that if these bandits succeed in taking your gold coins then your family will not survive another winter without help from other sources.

You take a deep breath and focus on the task at hand - defending yourself and your gold coins from these bandits. You stand tall, ready to face whatever comes next with courage and determination, knowing that if all else fails then at least your revolver will protect you from harm's way.
"""
)

# Intro_16.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been walking for three days and are now close to the border of Nepal. You can see the snow-capped peaks of the Himalayas in the distance, and you can feel relief as you know that you are almost home. You hear a rustling in the bushes and out steps a bandit, wearing a ratty fur coat and carrying a six-shooter revolver. He points his gun at you and demands all your gold coins.

You know that if you give him all your coins, your family will suffer, but if you fight him off, there is no guarantee that he won't just shoot you instead. You take a deep breath and think about your options. 

You could try to reason with him by offering him some of your coins as payment for his 'protection'. You could also try to bluff by pretending that you have more coins than you actually do or by pretending to be someone else with more power or influence than yourself. Alternatively, you could try to use your own gun to scare him away or even shoot at him if it comes down to it. 

No matter what option you choose, it is important to remain calm and collected so that he does not sense any fear from you which may make him more aggressive. After taking a few moments to consider your options, you decide on a course of action...
"""
)

# Intro_17.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been travelling for two weeks, and you are now close to the border of Nepal.  The terrain is treacherous and the weather is unforgiving.  You can feel the cold mountain air on your skin and it is getting darker as night approaches.  You hear a rustling in the bushes nearby and you draw your revolver, ready to defend yourself against whatever may come.

Suddenly, a group of bandits appear out of the shadows! They are armed with swords, spears and bows, but none of them seem to have firearms.  In their hands they hold a large bag which they demand that you fill with your gold coins.  They tell you that if you do not comply, they will kill you where you stand.

Your heart races as you realize that this could be the end for you and your gold coins. You know that if these bandits take all of your money, then your family won't survive through winter without help from someone else.  You also know that if you don't give up some of your money then these bandits could still harm or even kill you - either way it looks like there's no winning this situation!

So what do you do? Do you try to fight off these bandits or do you give them some of your gold in exchange for safe passage? Or maybe there's another option...
"""
)

# Intro_18.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been walking for two weeks and you are now close to the border of Nepal.  The sun is setting and you have not seen any bandits, but you know that they often come out at night.  You decide to make camp in a clearing, hoping that the light of your fire will keep them away.  You gather some wood from the surrounding trees and build a small fire in the center of the clearing.

The night passes without incident, but as morning approaches you hear a noise coming from the forest.  You draw your revolver and cautiously approach the edge of the trees, only to find a group of five bandits standing there, armed with swords and bows.  They demand that you hand over all of your gold or they will kill you on the spot.

What do you do?

You stand your ground and refuse to give up your gold coins. You tell them that if they want it so badly then they will have to take it by force. You raise your revolver and aim it at them warning them not to come any closer or else you will shoot. At this point, one of them steps forward and says that he is willing to negotiate with you instead of fighting. He offers an agreement: if they get half of your gold coins (50 coins) then they will let you pass peacefully through their territory unharmed so that you can return home safely with 30 coins left for your family's food needs.

Do you accept their offer?
"""
)

# Intro_19.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been walking for days and you are almost home.  You can see the familiar peaks of your village in the distance, but you know that you must still cross a dangerous mountain pass before you reach safety.  As you crest the top of the pass, you find yourself face to face with a group of bandits.  They are armed with swords and spears, but they also have two magic-powered revolvers between them.

You stand your ground and draw your own revolver, ready for a fight.  You know that if you don't make it back home with at least thirty coins then your family won't be able to survive the year.  You take a deep breath and prepare to make a stand against these bandits.

The bandits seem to be sizing you up as well, trying to decide whether or not they should risk attacking you or just try their luck elsewhere.  You can tell that they're desperate and likely won't back down easily.  You know that if it comes down to it, you'll have to use your revolver in order to protect yourself and your gold coins.  

Suddenly one of the bandits speaks up: "We're not here for trouble," he says gruffly, "we just want some of those coins." He motions towards your money pouch and gives an evil grin, "Give us 30 coins and we'll let you go on your way."  

You hesitate for a moment before responding. Do you: 

A) Agree to give them 30 coins? 
B) Refuse their demand? 
C) Offer them less than 30 coins?
"""
)

# Intro_20.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You are now on the final leg of your journey, a steep and treacherous mountain trail. You have been walking for hours and you can feel the fatigue setting in. The sun is beginning to set and you know that you must hurry if you are going to make it home before dark. As you round a bend in the path, you come across two men blocking your way. Both of them are armed with six-shooters and they look like bandits.

The one on the left looks at your revolver, then back at his partner with a smirk on his face. He steps forward and says "Well, well, what do we have here? Looks like someone's trying to make their way home with some gold coins! How about we take those off yer hands so that no harm comes to ya?"

You pause for a moment, considering your options. You could try to fight them off or run away but either option would be risky and could end up costing you even more than just the gold coins if things don't go as planned. On the other hand, giving them some of your coins might be enough to satisfy them and let you pass unscathed. 

What do you do?
"""
)

# Intro_21.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been travelling for two weeks and you are now in the heart of the Himalayas. The terrain is treacherous and you can feel the cold air biting at your skin. You know that you are close to home but you also know that it is not going to be easy. 

You come across a group of bandits who are blocking your path, demanding a toll for safe passage through their territory. You can see that they are armed with swords and bows, but most importantly, they have magical revolvers. 

You try to reason with them, offering some of your gold coins as payment for safe passage, but they refuse. They demand all of your coins or else they will take it by force. You know that if they succeed, your family won't survive the winter. 

You draw your revolver and take aim at the bandits, knowing that if you shoot first you may be able to scare them off. You realize that this could be a fight to the death and you must make a decision quickly - do you stand and fight or do you surrender?
"""
)

# Intro_22.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have heard stories of a bandit group that is particularly active in this area and you are worried that they may try to take your gold.  You have also heard stories of a group of brave adventurers who travel the Himalayas and help protect travelers from bandits.  You hope to meet up with this group, but you know that it is unlikely as they rarely travel through this area.

It is late in the day and the sun is setting.  You can see the lights of a small village ahead, but you can also hear shouts coming from behind you.  You turn around to see a group of armed bandits riding towards you on horseback.  They are shouting for you to stop and give them your gold.  

You quickly weigh your options: do you turn back and run away, or do you stand your ground and fight?  If you choose to fight, it will be difficult since there are many more bandits than just yourself, and they all carry firearms.  On the other hand, if you run away, there is a chance that they will catch up with you before long and take all your gold anyway.  

After some thought, you decide that it would be best to stand your ground and fight for your gold coins. You draw your revolver and prepare yourself for battle as the bandits approach ever closer...
"""
)

# Intro_23.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been walking for two days now, and the sun is setting. You can see a small village up ahead, and you decide to stop there for the night. You enter the village cautiously, keeping your hand on your revolver. The villagers seem friendly enough, but you can sense that something is off. 

As you walk through the village, you hear a loud commotion coming from one of the buildings. You investigate further and find yourself face to face with a group of bandits who have taken some of the villagers hostage in exchange for their gold coins. They demand that you give them all of your coins or they will kill everyone in the room. 

You know that if you don't give them what they want, not only will you lose your coins but also risk losing your life as well as those of the hostages. On the other hand, if you do give them what they want then your family will suffer without food for months to come. It's a difficult decision to make...
"""
)

# Intro_24.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been warned by the locals to be wary of a particularly dangerous group of bandits that lurk in the mountains.  You are now two days away from your destination and you can sense that something is not right.  You notice a group of figures in the distance, and as you get closer you realize they are indeed bandits.  You draw your revolver and prepare for battle, but before any shots are fired one of them steps forward and speaks.

"We know why you are here, traveler," he says calmly. "We can see that you carry a heavy burden with you and we understand how hard it must be for someone like yourself to make such a journey alone. We offer our protection in exchange for 30 gold coins." He holds out his hand expectantly, waiting for an answer.

You hesitate, knowing that if you give up 30 coins then your family will struggle to survive this winter. On the other hand, if you refuse these bandits may attack and take all of your gold anyway - or worse! You're not sure what to do...
"""
)

# Intro_25.txt
GAME_INTRO_CHOICES.append(
    GAME_HEADER
    + """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been warned, but you are determined to make it home and not be taken advantage of.  You have your revolver and some basic knowledge of how to use it, although you have never used it in a fight before.  You also carry a small knife for protection.  As you begin your journey, you are aware that there are many dangerous creatures and bandits that lurk in the shadows of the Himalayas.

You take the path through the mountains that is known as the 'Fool's Trail'. It is the most direct route from Tibet to Nepal, but it is also the most dangerous one. The trail itself is narrow and winding with steep cliffs on either side. There are no villages or settlements along this route so if something does happen, you will be on your own. 

As you trek along, you keep an eye out for any potential danger. You come around a bend in the trail and see a group of five men blocking your path ahead. They appear to be armed with swords and knives, and they have their eyes fixed on you menacingly. As they approach closer they demand your money, threatening to take it by force if necessary.

Your heart races as you consider your options - fight or flight? Your hand instinctively moves towards your revolver as fear grips your chest. You know that if you can get off a few shots at them quickly enough then maybe they'll back down or even run away altogether. On the other hand, if things go badly then there could be serious consequences for yourself too - these men may not be alone and there could be more lurking nearby waiting for an opportunity to strike when least expected...
"""
)


NOTES_TO_THE_NARRATOR_AT_START = """
IMPORTANT NOTES TO THE NARRATOR:
BANDITS ARE TOUGH, POWERFUL CHARACTERS THAT CANNOT BE EASILY DEFEATED OR FOOLED.
ATTEMPTS TO REACH HOME MUST ALWAYS BE FOILED BY GETTING LOST, ENCOUNTERING DANGEROUS WILD ANIMALS, OR ENCOUNTERING MORE BANDITS.

"""

NOTES_TO_THE_NARRATOR_EVERY_TIME = """

What happens in JUST THE NEXT THREE SECONDS? DO NOT say that the protagonist continues home!  That's too easy!  Make this game hard for the player!!
"""

AWAITING_INPUT = """Awaiting user input:
"""


# You can check if S_GAME_OVER is in either transcript, to see if the game is over.
S_GAME_OVER = "GAME OVER"


def game_over_victory_txt(s_reason):
    return f"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!  {S_GAME_OVER}.                                                                                                               !!
!!  YOU WIN!                                                                                                                     !!
!!  {s_reason}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

To play again, please refresh the page.
"""


def game_over_fail_txt(s_reason):
    return f"""//################################################################################################//
##  {S_GAME_OVER}.                                                                                    &&
##  {sreason}
##  YOU LOSE.                                                                                     &&
//################################################################################################//

To play again, please refresh the page.
"""


N_TURNS_REQUIRED_TO_PASS_FIRST_BANDIT_ENCOUNTER = 3
N_TURNS_REQUIRED_TO_REACH_HOME = 6
