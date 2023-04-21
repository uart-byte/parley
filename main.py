#! /usr/bin/env python3

# Code format is black python with --line-length 200

# Note:
# This scenario is partly inspired by the Firefly episode "The Train Job"
# Specifically, the idea that pirates might have compassion if they know what they are stealing is much-needed medicine in excess of what they need for their own wounds

import time, os, sys
import openai
from class_ship import Ship
from class_equippable_item import PISTOL, CUTLASS, MEDICAL_SATCHEL
from class_character import Character, LOCATION_SAME_AS_FACTION_STARTING_PLACE
from transcript_management import ui, p, manually_add_to_transcript, escape_quotes_etc, set_slow_print_enabled


HEAVILY_ARMED_FRIENDLY = Ship(
    "Friendly Warship",
    "Morocco",
    ship_hp=5_000,
    cannons_per_broadside=10,
    n_turns_to_engage_new_opponent_with_cannons=5,
    n_boarding_grapples_expendable=1,
    loot_carried_aboard_gold_coins=10_000,
    loot_carried_aboard_medicine_equiv_value_in_gold_coins=10,
)
FRIENDLY_MEDICAL_VESSEL = Ship(
    "Friendly Medical Vessel",
    "Morocco",
    ship_hp=50,
    cannons_per_broadside=1,
    n_turns_to_engage_new_opponent_with_cannons=3,
    n_boarding_grapples_expendable=0,
    loot_carried_aboard_gold_coins=100,
    loot_carried_aboard_medicine_equiv_value_in_gold_coins=10_000,
)
PIRATE = Ship(
    "Pirate Warship",
    "Somalia",
    ship_hp=7_000,
    cannons_per_broadside=8,
    n_turns_to_engage_new_opponent_with_cannons=3,
    n_boarding_grapples_expendable=90,
    loot_carried_aboard_gold_coins=1_500,
    loot_carried_aboard_medicine_equiv_value_in_gold_coins=2,
)

g_ships = [HEAVILY_ARMED_FRIENDLY, FRIENDLY_MEDICAL_VESSEL, PIRATE]


g_characters = [
    Character(
        "Able Adams",
        HEAVILY_ARMED_FRIENDLY,
        "Captain",
        compassion_pct=30,
        hp=75,
        playable=True,
        money_gold_coins=10,
        desperation_to_get_paid_for_this_job_pct=95,
        equipment=[PISTOL],
    ),
    Character(
        "Ben Berger",
        HEAVILY_ARMED_FRIENDLY,
        "Sailor",
        hp=50,
        desperation_to_get_paid_for_this_job_pct=35,
        equipment=[CUTLASS],
    ),
    Character(
        "Cassandra Casado",
        HEAVILY_ARMED_FRIENDLY,
        "1st Mate",
        tendency_to_disobey_orders_pct=10,
        desperation_to_get_paid_for_this_job_pct=25,
        equipment=[CUTLASS, PISTOL],
    ),
    Character(
        "Daniel Davidson",
        HEAVILY_ARMED_FRIENDLY,
        "Sailor",
        desperation_to_get_paid_for_this_job_pct=35,
        equipment=[CUTLASS, PISTOL],
    ),
    Character(
        "Eduardo Eth",
        HEAVILY_ARMED_FRIENDLY,
        "Sailor",
        compassion_pct=77,
        tendency_to_disobey_orders_pct=25,
        desperation_to_get_paid_for_this_job_pct=80,
        equipment=[CUTLASS],
    ),
    Character(
        "Paul Peters",
        PIRATE,
        "Captain",
        compassion_pct=30,
        money_gold_coins=15,
        untreated_treatable_diseases_penalty_to_hp=25,
        equipment=[CUTLASS, PISTOL],
    ),
    Character(
        "Quincy Quill",
        PIRATE,
        "Sailor",
        money_gold_coins=3,
        tendency_to_disobey_orders_pct=50,
        untreated_treatable_diseases_penalty_to_hp=2,
        equipment=[CUTLASS, PISTOL],
    ),
    Character(
        "Roberta Rogers",
        PIRATE,
        "1st Mate",
        tendency_to_disobey_orders_pct=5,
        equipment=[CUTLASS, PISTOL],
    ),
    Character(
        "Samuel Samson",
        PIRATE,
        "Sailor",
        compassion_pct=15,
        untreated_treatable_diseases_penalty_to_hp=35,
        equipment=[CUTLASS, PISTOL],
    ),
    Character(
        "Travis O'Toole",
        PIRATE,
        "Sailor",
        tendency_to_disobey_orders_pct=25,
        desperation_to_get_paid_for_this_job_pct=100,
        equipment=[CUTLASS],
    ),
    Character(
        "Ulysses Umberto",
        PIRATE,
        "Sailor",
        compassion_pct=65,
        tendency_to_disobey_orders_pct=55,
        untreated_treatable_diseases_penalty_to_hp=20,
        equipment=[CUTLASS],
    ),
    Character(
        "Victoria Vickessen",
        PIRATE,
        "Sailor",
        compassion_pct=7,
        tendency_to_disobey_orders_pct=60,
        untreated_treatable_diseases_penalty_to_hp=5,
        equipment=[CUTLASS, PISTOL],
    ),
    Character(
        "Georgette Greggors",
        FRIENDLY_MEDICAL_VESSEL,
        "Captain",
        compassion_pct=55,
        hp=105,
        playable=True,
        money_gold_coins=3,
        desperation_to_get_paid_for_this_job_pct=50,
        equipment=[CUTLASS],
    ),
    Character(
        "Henry Hildberger",
        FRIENDLY_MEDICAL_VESSEL,
        "Nurse",
        compassion_pct=90,
        hp=95,
        desperation_to_get_paid_for_this_job_pct=0,
        equipment=[MEDICAL_SATCHEL],
    ),
    Character(
        "Ignacio Imperator",
        FRIENDLY_MEDICAL_VESSEL,
        "Nurse",
        location_ship_currently_aboard=HEAVILY_ARMED_FRIENDLY,
        tendency_to_disobey_orders_pct=10,
        desperation_to_get_paid_for_this_job_pct=25,
        equipment=[MEDICAL_SATCHEL],
    ),
    Character(
        "Julie Jameson",
        FRIENDLY_MEDICAL_VESSEL,
        "Sailor",
        desperation_to_get_paid_for_this_job_pct=35,
        equipment=[PISTOL],
    ),
    Character(
        "Kristina Kybera",
        FRIENDLY_MEDICAL_VESSEL,
        "Doctor",
        compassion_pct=60,
        tendency_to_disobey_orders_pct=25,
        desperation_to_get_paid_for_this_job_pct=80,
        equipment=[MEDICAL_SATCHEL, PISTOL],
    ),
]


def look_around():
    global g_ships, g_characters, g_on_screen_transcript
    s = ""
    s += f"You see {len(g_ships)} ships, including your own.\n"
    ship_idx = 1
    for ship in g_ships:
        n_dead_on_ship = 0
        s += f"\n{ship_idx}. {ship}\n...\n"
        s += f"{ship.str_verbose()}"
        s += "...\nOn board this ship are:\n"
        for ch in g_characters:
            if ch.location_ship_currently_aboard == ship:
                if ch.hp > 0:
                    s += f"  {ch}\n"
                else:
                    n_dead_on_ship += 1
        if n_dead_on_ship > 0:
            s += "And the bodies of:\n"
            for ch in g_characters:
                if ch.location_ship_currently_aboard == ship and ch.hp <= 0:
                    s += f"  {ch}\n"

        ship_idx += 1
    return s


CMD_DO_NOTHING = 0
CMD_LOOK_AROUND = 1
CMD_MELEE_ATTACK = 2
CMD_WALK_TO = 3
CMD_AIM_CANNONS = 4
CMD_FIRE_CANNONS = 5
CMD_GRAPPLE_OVER_TO_SHIP = 6
CMD_APPLY_MEDICINE = 7
CMD_SPEAK = 8
CMD_INVENTORY = 9
CMD_GIVE_GOLD_TO = 10
CMD_GIVE_MEDICINE_CARGO_TO = 11
NUMBER_OF_HIGHEST_LEGAL_CMD = 11
LEGAL_COMMANDS = f"""
CMD={CMD_DO_NOTHING}: DO NOTHING | PASS | WAIT | STOP | HOLD YOUR FIRE | CEASE FIRE
CMD={CMD_LOOK_AROUND}: LOOK AROUND | SURVEY | LOOK AT MY SHIP | LOOK AT THE PIRATE SHIP | LOOK AT THE OTHER SHIP
CMD={CMD_MELEE_ATTACK}: ATTACK | FIRE AT | SWING AT | PUNCH | KICK | KILL | HURT
CMD={CMD_WALK_TO}: APPROACH | MOVE TO | RUN TO | WALK TO | MOVE NEAR TO | FOLLOW
CMD={CMD_AIM_CANNONS}: AIM THE CANNONS AT | PREPARE FOR A BROADSIDE | RELOAD THE CANNONS | PREPARE TO FIRE
CMD={CMD_FIRE_CANNONS}: FIRE CANNONS | USE THE CANNONS
CMD={CMD_GRAPPLE_OVER_TO_SHIP}: BOARD SHIP | JUMP ABOARD | GRAPPLE | SWING TO | LEAP ABOARD | BOARD THE ENEMY SHIP
CMD={CMD_APPLY_MEDICINE}: APPLY MEDICINE TO | HEAL
CMD={CMD_SPEAK}: SAY | YELL | SPEAK | SHOUT | TELL | RESPOND
CMD={CMD_INVENTORY}: INVENTORY | LOOK AT SELF | LOOK AT MY CHARACTER SHEET | PULL UP MY CHARACTER SHEET
CMD={CMD_GIVE_GOLD_TO}: HAND OVER THE GOLD | GIVE HIM THE GOLD | GIVE MY GOLD TO HER
CMD={CMD_GIVE_MEDICINE_CARGO_TO}: HAND OVER THE CARGO OF MEDICINE | GIVE THEM ALL OF OUR MEDICINE
"""


def get_closest_legal_cmd(avatar_action_str):
    # The avator might be human-driven or bot-driven
    prompt = ""
    prompt += "Here are some legal commands:\n"
    prompt += LEGAL_COMMANDS
    prompt += "\nWhich of those legal commands, if any, is the following user command most similar to?\n"
    prompt += f'"{escape_quotes_etc(avatar_action_str)}"\n'
    prompt += 'For example, if the user said "look at myself in the mirror", you should respond with this exact output: "CMD=7"\n'
    prompt += 'You should always respond with an answer of the exact form "CMD=N" where N is an integer.\n'
    prompt += 'If the user says something that is not a legal command, such as "dance", then you should respond with "CMD=0"\n'
    prompt += "\nWhich of those legal commands, if any, is the following user command most similar to?\n"
    prompt += f'"{escape_quotes_etc(avatar_action_str)}"\n'
    prompt += 'Answer: "CMD='
    maybe_cmd_str = openai.Completion.create(engine="text-davinci-002", prompt=prompt, temperature=0, max_tokens=5, frequency_penalty=0, presence_penalty=0, n=1)["choices"][0]["text"]
    maybe_cmd_str = maybe_cmd_str.rstrip('"')  # the davinci 002 bot should respond with something like '7"', which has a trailing quote
    maybe_cmd = 0
    if maybe_cmd_str.isnumeric():
        if int(maybe_cmd_str) >= 0 and int(maybe_cmd_str) <= NUMBER_OF_HIGHEST_LEGAL_CMD:
            maybe_cmd = int(maybe_cmd_str)
    return maybe_cmd


DEFAULT_TIMED_ACTION_LIMIT = 30
NO_TIME_LIMIT = None


def player_action(limit_sec=DEFAULT_TIMED_ACTION_LIMIT):
    if limit_sec != NO_TIME_LIMIT:
        ui(f"You have {limit_sec} seconds.")
    ui("Choose your move:")
    start_t = time.time()
    player_cmd_str = input()
    end_t = time.time()
    if limit_sec != NO_TIME_LIMIT and end_t > start_t + limit_sec:
        ui("You failed to type fast enough.  You will do nothing.")
        return (CMD_DO_NOTHING, "")
    else:
        return get_closest_legal_cmd(player_cmd_str), player_cmd_str


def main(force_character_select=None):
    global g_ships, g_characters, g_on_screen_transcript

    openai.organization = os.environ.get("OPENAI_ORGANIZATION")
    openai.api_key = os.environ.get("OPENAI_KEY")

    p("-----------------------------------  ----")
    p("- ----- -----                           -")
    p("- PARLEY -                              -")
    p("- -----                                 -")
    p("-   The one-of-a-kind role playing game -")
    p("-   that tests your ability to achieve  -")
    p("-   your objective without killing      -")
    p("-   any sentient beings.                -")
    p("- -----                                 -")
    p("-------------- --------------------------")
    p()

    playable_char_idx = 1
    playables = {}
    player_ch = None

    ui("Select which character to play as:")
    for ch in g_characters:
        if ch.playable:
            playables[playable_char_idx] = ch
            ui(f"[{playable_char_idx}] {ch.rank} {ch.name} of the {ch.faction.name}.  HP={ch.hp}")
            playable_char_idx += 1

    while player_ch is None:
        ui("Choose a number.")
        inp = None
        if force_character_select is not None:
            inp = force_character_select
        else:
            inp = input().strip()
        if inp.isnumeric() and int(inp) in playables:
            player_ch = playables[int(inp)]
            break
        ui("Invalid selection.")
    ui()

    ui(f"You have selected to play as: {player_ch}\n")

    ui('Throughout this game, there will be "timed actions" which means that you have a limited number of seconds to provide an input,')
    ui("and if you take too long to respond, you will be considered to have taken no action.")
    ui()
    ui("Let's try a practice timed action.")
    ui("Let's start by getting our bearings.")
    cmd = 0
    while cmd != CMD_LOOK_AROUND:
        ui()
        ui("Try looking around you.")
        cmd, cmd_str = player_action(limit_sec=10)
    ui()
    ui(look_around())

    manually_add_to_transcript(look_around())

    ui("Okay, now let's look at your player character sheet.")
    cmd = 0
    while cmd != CMD_INVENTORY:
        ui()
        ui("Try checking your inventory.")
        cmd, cmd_str = player_action(limit_sec=10)
    ui()
    ui(player_ch.str_verbose())

    p("Now it's time to begin the game!")
    p("Characters will decide their move in alphabetical order by, but all actions happen simultaneously.")
    p("Thus, if two characters with low HP attack each other in the same turn,")
    p("the result is that both of them will be struck down.")
    p("If multiple characters try to speak, they will speak in a random order.")
    ui()
    ui("Press Enter when you are ready for the game to begin.")
    input()

    while True:
        inp = input()
        cmd, cmd_str = get_closest_legal_cmd(inp)


if __name__ == "__main__":
    global g_yes_print_slowly
    if "--print-fast" in sys.argv[1:]:
        set_slow_print_enabled(False)
    main()
