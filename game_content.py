GAME_INTRO_1 = """-----------------------------------  ------------------ ----------------
- ----- -----                                                                                         -
- PARLEY -                                                                                        -
- -----                                                                                                  -
-   The one-of-a-kind role playing game                            -
-   that tests your ability to achieve                                     -
-   your objective without killing                                           -
-   any sentient beings.                                                             -
- -----                                                                                                 -
-------------- ------------------------------- ------- ----------------

The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been travelling for three days now and the journey is almost over. The night before you reach your destination, you set up camp in a secluded area, hoping to make it home without any trouble.  As you are preparing your dinner, you hear a rustling in the bushes. You ready your revolver and prepare for the worst. 

Out of the bushes emerges a group of five bandits. They are all armed with swords and daggers but they also have revolvers at their sides. The leader steps forward and demands that you hand over all your gold coins or else they will kill you and take it by force. You know that if you don't comply, you won't make it home alive or with enough gold to support your family. You also know that if these bandits get their hands on all 100 coins, then your family will suffer greatly this year as they won't be able to afford food or other necessities. 

You must think quickly - do you try to fight them off or do you negotiate with them?
"""

GAME_INTRO_2 = """-----------------------------------  ------------------ ----------------
- ----- -----                                                                                         -
- PARLEY -                                                                                        -
- -----                                                                                                  -
-   The one-of-a-kind role playing game                            -
-   that tests your ability to achieve                                     -
-   your objective without killing                                           -
-   any sentient beings.                                                             -
- -----                                                                                                 -
-------------- ------------------------------- ------- ----------------

The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been making this journey for the past five years with no problems, but this year the trip has been unusually dangerous.  You have encountered more bandits than usual and you are now down to your last 20 coins.  You are about a day away from home when you come across a group of bandits in the road ahead.  

You recognize one of them as a man who had tried to rob you two days prior. He had failed then, but he is back with reinforcements and they seem determined to take what's left of your gold.  You can tell by their demeanor that they will not be swayed by words or threats, so you draw your revolver and prepare to fight for your money. 

You know that if you can make it past this group, you will be able to make it home safely with enough money for your family to survive the winter.  You take a deep breath and prepare yourself for battle, knowing that this may be your last chance at survival...
"""

GAME_INTRO_3 = """-----------------------------------  ------------------ ----------------
- ----- -----                                                                                         -
- PARLEY -                                                                                        -
- -----                                                                                                  -
-   The one-of-a-kind role playing game                            -
-   that tests your ability to achieve                                     -
-   your objective without killing                                           -
-   any sentient beings.                                                             -
- -----                                                                                                 -
-------------- ------------------------------- ------- ----------------

The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been traveling for weeks now and you are nearing the end of your journey. You can see the border between Tibet and Nepal in the distance, but before you can cross it, you must pass through a narrow mountain pass. As you enter the pass, you hear a voice call out from behind you.

"Halt! This is our territory now." 

You turn around to find two bandits blocking your path, each armed with a magical revolver. They demand that you hand over half of your gold coins as 'protection money'. You know that if you give them what they want, there's no guarantee that they won't just take all of it anyway. On the other hand, if you refuse to pay up then they could easily shoot you down and take all of your coins anyway. 

What do you do?
"""

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
