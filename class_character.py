LOCATION_SAME_AS_FACTION_STARTING_PLACE = "::LOCATION_SAME_AS_FACTION_STARTING_PLACE::"


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
                line.replace("        ", "")
                for line in f"""
        [Begin Character Sheet]
          Name: {self.name}
          HP: {self.hp}
          Inventory: {", ".join([str(item) for item in self.equipment])}
          Location: {self.location_ship_currently_aboard}
          Nationality: {self.faction.country_of_most_of_crew_citizenship}
        [End Character Sheet]
        """.splitlines()
                if line != ""
            ]
        )
