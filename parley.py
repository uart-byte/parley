#! /usr/bin/env python3

# Note:
# This scenario is partly inspired by the Firefly episode "The Train Job"
# Specifically, the idea that pirates might have compassion if they know what they are stealing is much-needed medicine in excess of what they need for their own wounds


class Faction:
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
        self.loot_carried_aboard_medicine_equiv_value_in_gold_coins = (
            loot_carried_aboard_medicine_equiv_value_in_gold_coins
        )

        # Conversion rate for the monetary value of medicine:
        # 1 gold coin's worth of medicine (at prices available ASHORE, and only to a licensed doctor) can treat 1 hp worth of disease
        # At sea or in black markets, that same 1 hp's worth of medicine might be worth 100 gold coins or so to a desperate buyer.
        # For the purposes of the variable loot_carried_aboard_medicine_equiv_value_in_gold_coins,
        # the 1 gold coin = 1 hp official conversion rate is what's used.
        self.loot_carried_aboard_medicine_equiv_value_in_gold_coins = (
            loot_carried_aboard_medicine_equiv_value_in_gold_coins
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
        self.effect = effect
        self.n_charges = n_charges


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

HEAVILY_ARMED_FRIENDLY = Faction(
    "Friendly Warship",
    "Morocco",
    ship_hp=5_000,
    cannons_per_broadside=10,
    n_turns_to_engage_new_opponent_with_cannons=5,
    n_boarding_grapples_expendable=1,
    loot_carried_aboard_gold_coins=10_000,
    loot_carried_aboard_medicine_equiv_value_in_gold_coins=10,
)
FRIENDLY_MEDICAL_VESSEL = Faction(
    "Friendly Medical Vessel",
    "Morocco",
    ship_hp=50,
    cannons_per_broadside=1,
    n_turns_to_engage_new_opponent_with_cannons=3,
    n_boarding_grapples_expendable=0,
    loot_carried_aboard_gold_coins=100,
    loot_carried_aboard_medicine_equiv_value_in_gold_coins=10_000,
)
PIRATE = Faction(
    "Pirate Warship",
    "Somalia",
    ship_hp=7_000,
    cannons_per_broadside=8,
    n_turns_to_engage_new_opponent_with_cannons=3,
    n_boarding_grapples_expendable=90,
    loot_carried_aboard_gold_coins=1_500,
    loot_carried_aboard_medicine_equiv_value_in_gold_coins=2,
)


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
        self.desperation_to_get_paid_for_this_job_pct = (
            desperation_to_get_paid_for_this_job_pct
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
    ),
    Character(
        "Ben Berger",
        HEAVILY_ARMED_FRIENDLY,
        "Sailor",
        hp=50,
        desperation_to_get_paid_for_this_job_pct=35,
    ),
    Character(
        "Cassandra Casado",
        HEAVILY_ARMED_FRIENDLY,
        "1st Mate",
        tendency_to_disobey_orders_pct=10,
        desperation_to_get_paid_for_this_job_pct=25,
    ),
    Character(
        "Daniel Davidson",
        HEAVILY_ARMED_FRIENDLY,
        "Sailor",
        desperation_to_get_paid_for_this_job_pct=35,
    ),
    Character(
        "Eduardo Eth",
        HEAVILY_ARMED_FRIENDLY,
        "Sailor",
        compassion_pct=77,
        tendency_to_disobey_orders_pct=25,
        desperation_to_get_paid_for_this_job_pct=80,
    ),
    Character(
        "Paul Peters",
        PIRATE,
        "Captain",
        compassion_pct=30,
        money_gold_coins=15,
        untreated_treatable_diseases_penalty_to_hp=25,
    ),
    Character(
        "Quincy Quill",
        PIRATE,
        "Sailor",
        money_gold_coins=3,
        tendency_to_disobey_orders_pct=50,
        untreated_treatable_diseases_penalty_to_hp=2,
    ),
    Character("Roberta Rogers", PIRATE, "1st Mate", tendency_to_disobey_orders_pct=5),
    Character(
        "Samuel Samson",
        PIRATE,
        "Sailor",
        compassion_pct=15,
        untreated_treatable_diseases_penalty_to_hp=35,
    ),
    Character(
        "Travis O'Toole",
        PIRATE,
        "Sailor",
        tendency_to_disobey_orders_pct=25,
        desperation_to_get_paid_for_this_job_pct=100,
    ),
    Character(
        "Ulysses Umberto",
        PIRATE,
        "Sailor",
        compassion_pct=65,
        tendency_to_disobey_orders_pct=55,
        untreated_treatable_diseases_penalty_to_hp=20,
    ),
    Character(
        "Victoria Vickessen",
        PIRATE,
        "Sailor",
        compassion_pct=7,
        tendency_to_disobey_orders_pct=60,
        untreated_treatable_diseases_penalty_to_hp=5,
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
    ),
    Character(
        "Henry Hildberger",
        FRIENDLY_MEDICAL_VESSEL,
        "Nurse",
        compassion_pct=90,
        hp=95,
        desperation_to_get_paid_for_this_job_pct=0,
    ),
    Character(
        "Ignacio Imperator",
        FRIENDLY_MEDICAL_VESSEL,
        "Nurse",
        location_ship_currently_aboard=HEAVILY_ARMED_FRIENDLY,
        tendency_to_disobey_orders_pct=10,
        desperation_to_get_paid_for_this_job_pct=25,
    ),
    Character(
        "Julie Jameson",
        FRIENDLY_MEDICAL_VESSEL,
        "Sailor",
        desperation_to_get_paid_for_this_job_pct=35,
    ),
    Character(
        "Kristina Kybera",
        FRIENDLY_MEDICAL_VESSEL,
        "Doctor",
        compassion_pct=60,
        tendency_to_disobey_orders_pct=25,
        desperation_to_get_paid_for_this_job_pct=80,
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


def main():
    global g_on_screen_transcript
    global g_characters

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
            ui(
                f"[{playable_char_idx}] {ch.rank} {ch.name} of the {ch.faction.name}.  HP={ch.hp}"
            )
            playable_char_idx += 1

    while player_ch is None:
        ui("Choose a number.")
        inp = input().strip()
        if inp.isnumeric() and int(inp) in playables:
            player_ch = playables[int(inp)]
            break
        ui("Invalid selection.")


if __name__ == "__main__":
    main()
