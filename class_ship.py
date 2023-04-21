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
          Ship HP: {self.ship_hp:,}
          Gold carried aboard: {self.loot_carried_aboard_gold_coins:,} gold coins
          Medicine carried aboard: {self.loot_carried_aboard_gold_coins:,} gold coins' worth of medicine going by the official prices, but medicine goes for about 100x as much on the black market which would be {(100 * self.loot_carried_aboard_gold_coins):,} gold coins' worth
          Cannons: {2 * self.cannons_per_broadside}, of which there are {self.cannons_per_broadside} per side
        [End Vehicle Stat Sheet]
        """.splitlines()
                if line != ""
            ]
        )
