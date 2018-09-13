############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        if self.pairings == []:
            self.pairings = [pairing]
        else:
            self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code



def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", "1998", "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", "2003", "orange", True, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", "1996", "green", True, False, "Crenshaw")
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType("yw", "2013", "yellow", True, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print("{} pairs with".format(melon.name))
        for pair in melon.pairings:
            print(" - {}".format(pair))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_types_dict = {}

    for melon_type in melon_types:
        melon_types_dict[melon_type.code] = melon_type

    return melon_types_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    harvested_melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    harvested_melons.append(melon1)

    melon2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    harvested_melons.append(melon2)
    
    melon3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    harvested_melons.append(melon3)

    melon4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    harvested_melons.append(melon4)

    melon5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    harvested_melons.append(melon5)

    melon6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    harvested_melons.append(melon6)

    melon7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    harvested_melons.append(melon7)
    
    melon8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    harvested_melons.append(melon8)
    
    melon9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")
    harvested_melons.append(melon9)


    return harvested_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        sellable = "(NOT SELLABLE)"
        if melon.is_sellable:
            sellable = "(CAN BE SOLD)"
        print("Harvested by {} from field {} {}".format(melon.harvester,
            melon.field,sellable))


    # Fill in the rest 

get_sellability_report(make_melons(make_melon_types()))
