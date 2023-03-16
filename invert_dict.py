def invert_dict_with_lists(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for val in val:
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
    return inverse


gear_sets = {
    "dungeon_set": ["Helm of the Mountain", "Soulforge Breastplate", "Bloodforged Legplates"],
    "raid_set": ["Helmet of Ten Storms", "Breastplate of Wrath", "Legplates of Wrath", "Gauntlets of Wrath",
                 "Sabatons of Wrath"],
    "pvp_set": ["Grand Marshal's Lamellar Helm", "Grand Marshal's Lamellar Breastplate",
                "Grand Marshal's Lamellar Legplates"]
}

inverted_gear_sets = invert_dict_with_lists(gear_sets)


def main():
    print("Original gear sets:", gear_sets)
    print("Inverted gear sets:", inverted_gear_sets)


if __name__ == "__main__":
    main()

# Output: Original gear sets: {'dungeon_set': ['Helm of the Mountain', 'Soulforge Breastplate', 'Bloodforged
# Legplates'], 'raid_set': ['Helmet of Ten Storms', 'Breastplate of Wrath', 'Legplates of Wrath', 'Gauntlets of
# Wrath', 'Sabatons of Wrath'], 'pvp_set': ['Grand Marshal's Lamellar Helm', 'Grand Marshal's Lamellar Breastplate',
# 'Grand Marshal's Lamellar Legplates']}

#Inverted gear sets: {'Helm of the Mountain': ['dungeon_set'], 'Soulforge
# Breastplate': ['dungeon_set'], 'Bloodforged Legplates': ['dungeon_set'], 'Helmet of Ten Storms': ['raid_set'],
# 'Breastplate of Wrath': ['raid_set'], 'Legplates of Wrath': ['raid_set'], 'Gauntlets of Wrath': ['raid_set'],
# 'Sabatons of Wrath': ['raid_set'], "Grand Marshal's Lamellar Helm": ['pvp_set'], "Grand Marshal's Lamellar
# Breastplate": ['pvp_set'], "Grand Marshal's Lamellar Legplates": ['pvp_set']}

# Suppose you are a player in World of Warcraft and you have a collection of gear sets. You want to be able to
# quickly find out which gear sets contain a particular item. You can use the invert_dict_with_lists function to
# create a dictionary that maps each item to a list of gear sets that contain it. The invert_dict_with_lists
# function takes a dictionary that maps gear sets to a list of items and returns a dictionary that maps each item
# to a list of gear sets that contain it. The invert_dict_with_lists function uses a nested for loop to iterate
# through the items in the original dictionary. The outer for loop iterates through the keys in the original
# dictionary. The inner for loop iterates through the items in the list of items associated with each key. The
# inner for loop checks whether the item is already a key in the inverted dictionary. If it is not, the item is
# added as a key in the inverted dictionary and the gear set is added to the list of gear sets associated with
# that item. If the item is already a key in the inverted dictionary, the gear set is added to the list of gear
# sets associated with that item. The invert_dict_with_lists function returns the inverted dictionary.
