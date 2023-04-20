#! /usr/bin/env python3

on_screen_transcript = ""


def Faction:
  def __init__(name, cannons_per_broadside=0, n_boarding_grapples_expendable=1, loot_carried_aboard_gold_coins=0, loot_carried_aboard_medicine_equiv_value_in_gold_coins=0)


HEAVILY_ARMED_FRIENDLY = Faction("Friendly", cannons_per_broadside=10, n_boarding_grapples_expendable=1, loot_carried_aboard_gold_coins=10_000, loot_carried_aboard_medicine_equiv_value_in_gold_coins=10)
FRIENDLY_MEDICAL_VESSEL = Faction("Friendly Medical Vessel", cannons_per_broadside=0, n_boarding_grapples_expendable=0, loot_carried_aboard_gold_coins=100, loot_carried_aboard_medicine_equiv_value_in_gold_coins=10_000)
PIRATE = Faction("Pirate", cannons_per_broadside=4, n_boarding_grapples_expendable=90, loot_carried_aboard_gold_coins=1_500, loot_carried_aboard_medicine_equiv_value_in_gold_coins=2)

# Conversion rate for the monetary value of medicine:
# 1 gold coin's worth of medicine (at prices available ASHORE, and only to a licensed doctor) can treat 1 hp worth of disease
# At sea or in black markets, that same 1 hp's worth of medicine might be worth 100 gold coins or so.

def Character:
  # pct = percent, i.e. range is 0 thru 100
  # max hp for most characters is 100
  def __init__(name, faction, rank, hp=100, playable=False, tendency_to_disobey_orders_pct=1, desperation_to_finish_and_get_paid_for_this_job_pct=10, money_gold_coins=0, untreated_treatable_diseases_penalty_to_hp=0):
    self.name = name
    self.faction = faction
    self.rank = rank
    self.hp = hp
    self.playable = playable
    self.tendency_to_disobey_orders_pct = tendency_to_disobey_orders_pct
    self.desperation_to_finish_and_get_paid_for_this_job_pct = desperation_to_finish_and_get_paid_for_this_job_pct

characters = [
  Character("Able Adams", HEAVILY_ARMED_FRIENDLY, "Captain", hp=75, playable=True, money_gold_coins=10, desperation_to_get_paid_for_this_job_pct=95),
  Character("Ben Berger", HEAVILY_ARMED_FRIENDLY, "Sailor", hp=50, desperation_to_get_paid_for_this_job_pct=35),
  Character("Cassandra Casado", HEAVILY_ARMED_FRIENDLY, "1st Mate", tendency_to_disobey_orders_pct=10, desperation_to_get_paid_for_this_job_pct=25),
  Character("Daniel Davidson", HEAVILY_ARMED_FRIENDLY, "Sailor", desperation_to_get_paid_for_this_job_pct=35),
  Character("Eduardo Eth", HEAVILY_ARMED_FRIENDLY, "Sailor", tendency_to_disobey_orders_percent=25, desperation_to_get_paid_for_this_job_pct=80),

  Character("Paul Peters", PIRATE, "Captain", money_gold_coins=15, untreated_treatable_diseases_penalty_to_hp=25),
  Character("Quincy Quill", PIRATE, "Sailor", money_gold_coins=3, tendency_to_disobey_orders_percent=50, untreated_treatable_diseases_penalty_to_hp=2),
  Character("Roberta Rogers", PIRATE, "1st Mate", tendency_to_disobey_orders_percent=5),
  Character("Samuel Samson", PIRATE, "Sailor", untreated_treatable_diseases_penalty_to_hp=35),
  Character("Travis O'Toole", PIRATE, "Sailor", tendency_to_disobey_orders_percent=25, desperation_to_get_paid_for_this_job_pct=100),
  Character("Ulysses Umberto", PIRATE, "Sailor", tendency_to_disobey_orders_percent=55, untreated_treatable_diseases_penalty_to_hp=20),
  Character("Victoria Vickessen", PIRATE, "Sailor", tendency_to_disobey_orders_percent=60, untreated_treatable_diseases_penalty_to_hp=5),

  Character("Georgette Greggors", FRIENDLY_MEDICAL_VESSEL, "Captain", hp=105, playable=True, money_gold_coins=3, desperation_to_get_paid_for_this_job_pct=50),
  Character("Henry Hildberger", FRIENDLY_MEDICAL_VESSEL, "Doctor", hp=95, desperation_to_get_paid_for_this_job_pct=0),
  Character("Ignacio Imperator", FRIENDLY_MEDICAL_VESSEL, "Doctor", tendency_to_disobey_orders_pct=10, desperation_to_get_paid_for_this_job_pct=25),
  Character("Daniel Davidson", FRIENDLY_MEDICAL_VESSEL, "Sailor", desperation_to_get_paid_for_this_job_pct=35),
  Character("Edward Eth", FRIENDLY_MEDICAL_VESSEL, "Sailor", tendency_to_disobey_orders_percent=25, desperation_to_get_paid_for_this_job_pct=80),
]

def p(s):
  print(s)
  on_screen_transcript += s + "\n"


if __name__ == "__main__":
