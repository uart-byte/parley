#! /usr/bin/env python3

# Code format is black python with --line-length 200

# Note:
# This scenario is partly inspired by the Firefly episode "The Train Job"
# Specifically, the idea that pirates might have compassion if they know what they are stealing is much-needed medicine in excess of what they need for their own wounds

import time, os, openai

openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_KEY")

def escape_quotes_etc(s):
  return s.replace('"', "'").replace(':', '').replace('\n', ' ').replace('{', '(').replace('}', ')')


class Ship:
    def __init__(
        self,
        name,
        country_of_most_of_crew_citizenship,
        ship_hp=1_000,
        cannons_per_broadside=0,
        n_turns_to_engage_new_opponent_with_cannons=5,
        n_boarding_grapples_expendable=1,
        loot_carried_aboard_gold_coins=0,
        loot_carried_aboard_medicine_equiv_value_in_gold_coins=0,
    ):
        self.name = name
        self.country_of_most_of_crew_citizenship = country_of_most_of_crew_citizenship
        self.ship_hp = ship_hp
        self.cannons_per_broadside = cannons_per_broadside
        self.n_boarding_grapples_expendable = n_boarding_grapples_expendable
        self.loot_carried_aboard_gold_coins = loot_carried_aboard_gold_coins
        self.loot_carried_aboard_medicine_equiv_value_in_gold_coins = loot_carried_aboard_medicine_equiv_value_in_gold_coins

        # Conversion rate for the monetary value of medicine:
        # 1 gold coin's worth of medicine (at prices available ASHORE, and only to a licensed doctor) can treat 1 hp worth of disease
        # At sea or in black markets, that same 1 hp's worth of medicine might be worth 100 gold coins or so to a desperate buyer.
        # For the purposes of the variable loot_carried_aboard_medicine_equiv_value_in_gold_coins,
        # the 1 gold coin = 1 hp official conversion rate is what's used.
        self.loot_carried_aboard_medicine_equiv_value_in_gold_coins = loot_carried_aboard_medicine_equiv_value_in_gold_coins

    def __str__(self):
        return f"The good ship {self.name} sailing from {self.country_of_most_of_crew_citizenship}"

    def str_verbose(self):
        return "\n".join(
            [
                line.replace("        ", "")
                for line in f"""
        [Begin Vehicle Stat Sheet]
          Name: {self.name}
          Nationality: {self.country_of_most_of_crew_citizenship}
          Ship HP: {self.ship_hp}
          Gold carried aboard: {self.loot_carried_aboard_gold_coins} gold coins
          Medicine carried aboard: {self.loot_carried_aboard_gold_coins} gold coins' worth of medicine going by the official prices, but medicine goes for about 100x as much on the black market which would be {100 * self.loot_carried_aboard_gold_coins} gold coins' worth
          Cannons: {2 * self.cannons_per_broadside}, of which there are {self.cannons_per_broadside} per side
        [End Vehicle Stat Sheet]
        """.splitlines() if line != ""
            ]
        )



LOCATION_SAME_AS_FACTION_STARTING_PLACE = "::LOCATION_SAME_AS_FACTION_STARTING_PLACE::"
ITEM_DOES_NOT_NEED_CHARGES = -1


class EquippableItem:
    # pct = percent, i.e. range is 0 thru 100
    def __init__(
        self,
        name,
        requires_close_proximity,
        chance_of_hit_pct,
        effect_on_hp,
        n_charges=ITEM_DOES_NOT_NEED_CHARGES,
        consumes_medicine=False,
    ):
        self.name = name
        self.requires_close_proximity = requires_close_proximity
        self.chance_of_hit_pct = chance_of_hit_pct
        self.effect_on_hp = effect_on_hp
        self.n_charges = n_charges
        self.consumes_medicine = consumes_medicine

    def __str__(self):
        return f"{self.name}"


PISTOL = EquippableItem(
    "Dual-Barrelled Flintlock Pistol",
    requires_close_proximity=False,
    chance_of_hit_pct=20,
    effect_on_hp=-50,
    n_charges=2,
)
CUTLASS = EquippableItem(
    "Cutlass Sword",
    requires_close_proximity=True,
    chance_of_hit_pct=90,
    effect_on_hp=-50,
    n_charges=ITEM_DOES_NOT_NEED_CHARGES,
)
MEDICAL_SATCHEL = EquippableItem(
    "Medical Satchel which allows the user to apply consumable medicines",
    requires_close_proximity=True,
    chance_of_hit_pct=60,
    effect_on_hp=+10,
    n_charges=ITEM_DOES_NOT_NEED_CHARGES,
    consumes_medicine=True,
)

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


class Character:
    # max hp for most characters is 100
    def __init__(
        self,
        name,
        faction,
        rank,
        compassion_pct=50,
        location_ship_currently_aboard=LOCATION_SAME_AS_FACTION_STARTING_PLACE,
        hp=100,
        equipment=[],
        playable=False,
        tendency_to_disobey_orders_pct=1,
        desperation_to_get_paid_for_this_job_pct=10,
        money_gold_coins=0,
        untreated_treatable_diseases_penalty_to_hp=0,
        close_to=[],  # TODO make it possible to be close to people, the helm, or the cannons
    ):
        self.name = name
        self.faction = faction
        if location_ship_currently_aboard == LOCATION_SAME_AS_FACTION_STARTING_PLACE:
            self.location_ship_currently_aboard = faction
        else:
            self.location_ship_currently_aboard = location_ship_currently_aboard
        self.rank = rank
        self.hp = hp
        self.equipment = equipment
        self.playable = playable
        self.tendency_to_disobey_orders_pct = tendency_to_disobey_orders_pct
        self.desperation_to_get_paid_for_this_job_pct = desperation_to_get_paid_for_this_job_pct

    def __str__(self):
        return self.name

    def str_verbose(self):
        return "\n".join(
            [
                line.lstrip()
                for line in f"""
        [Begin Character Sheet]
        Name: {self.name}
        HP: {self.hp}
        Inventory: {", ".join([str(item) for item in self.equipment])}
        Location: {self.location_ship_currently_aboard}
        Ship: {self.faction}
        [End Character Sheet]
        """.splitlines() if line != ""
            ]
        )


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


g_on_screen_transcript = ""

# p() means print to screen and transcript
def p(s=""):
    global g_on_screen_transcript
    print(s)
    g_on_screen_transcript += s + "\n"


# ui() means print only to screen
def ui(s=""):
    print(s)


def look_around():
    global g_ships, g_characters, g_on_screen_transcript
    s = ""
    s += f"You see {len(g_ships)} ships, including your own.\n"
    ship_idx = 1
    for ship in g_ships:
        n_dead_on_ship = 0
        s += f"\n{ship_idx}. {ship}\n"
        s += f"{ship.str_verbose()}"
        s += "On board this ship are:\n"
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


DEFAULT_TIMED_ACTION_LIMIT = 30
def timed_action(limit_sec=DEFAULT_TIMED_ACTION_LIMIT):
    ui(f"You have {limit_sec} seconds.")
    ui("Choose your move:")
    start_t = time.time()
    player_cmd = input()
    end_t = time.time()
    if end_t > start_t + limit_sec:
        ui("You failed to type fast enough.  You will do nothing.")
        return None
    else:
        return player_cmd


LEGAL_COMMANDS = """
CMD=0: DO NOTHING | PASS | WAIT
CMD=1: LOOK AROUND | SURVEY | LOOK AT MY SHIP | LOOK AT THE PIRATE SHIP | LOOK AT THE OTHER SHIP
CMD=2: ATTACK | FIRE AT | SWING AT | PUNCH | KICK | KILL | HURT
CMD=3: FIRE CANNON | USE CANNON
CMD=4: BOARD SHIP
CMD=5: APPLY MEDICINE TO | HEAL
CMD=6: SAY | YELL | SPEAK | SHOUT | TELL | RESPOND
CMD=7: INVENTORY | LOOK AT SELF
"""
NUMBER_OF_HIGHEST_LEGAL_CMD = 7

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
    maybe_cmd_str = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=5,
        frequency_penalty=0, presence_penalty=0,
        n=1)["choices"][0]["text"]
    maybe_cmd_str = maybe_cmd_str.rstrip('"')  # the davinci 002 bot should respond with something like '7"', which has a trailing quote
    maybe_cmd = 0
    if maybe_cmd_str.isnumeric():
        if int(maybe_cmd_str) >= 0 and int(maybe_cmd_str) <= NUMBER_OF_HIGHEST_LEGAL_CMD:
            maybe_cmd = int(maybe_cmd_str)
    return maybe_cmd


def main(start_with_practice_turns=True, force_character_select=None):
    global g_ships, g_characters, g_on_screen_transcript

    p("-----------------------------------  ----")
    p("- ----- -----                           -")
    p("- PARLEY -                              -")
    p("- -----                                 -")
    p("-   The one-of-a-kind role playing game -")
    p("-   that tests your ability to achieve  -")
    p("-   your objective without killing      -")
    p("-   any human or sentient enemies.      -")
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

    if start_with_practice_turns:
        ui('Throughout this game, there will be "timed actions" which means that you have a limited number of seconds to provide an input,')
        ui("and if you take too long to respond, you will be considered to have taken no action.")
        ui()
        ui("Let's try a practice timed action.")
        ui("Let's start by getting our bearings.  Try looking around you.")
        for nth in ["1st", "2nd", "3rd", "4th", "5th"]:
            ui()
            ui(f"This is your {nth} practice turn.")
            ui('Try saying "inventory" or "look around".')
            action = timed_action(limit_sec=10)
        ui()

    p("You have selected to play as:\n" + player_ch.str_verbose())
    p(look_around())

    while True:
        inp = input()
        print(get_closest_legal_cmd(inp))

if __name__ == "__main__":
    main(start_with_practice_turns=False, force_character_select="2")
