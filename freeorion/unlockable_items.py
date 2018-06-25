from enum import IntEnum


class UnlockableItemType(IntEnum):
    INVALID = -1  # unlockableItemType(-1, "invalid")
    BUILDING = 0  # unlockableItemType(0, "building")
    SHIP_PART = 1  # unlockableItemType(1, "shipPart")
    SHIP_HULL = 2  # unlockableItemType(2, "shipHull")
    SHIP_DESIGN = 3  # unlockableItemType(3, "shipDesign")
    TECH = 4  # unlockableItemType(4, "tech")
