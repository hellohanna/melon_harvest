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

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 

