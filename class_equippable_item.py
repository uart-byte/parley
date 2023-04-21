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
