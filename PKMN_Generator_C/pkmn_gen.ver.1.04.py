import random
import time
import sys
import colorama
from colorama import Fore, Style
sys.stdout.reconfigure(encoding='utf-8')
colorama.init()
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BLACK = '\033[30m'
    DARK_RED = '\033[31m'
    DARK_GREEN = '\033[32m'
    DARK_YELLOW = '\033[33m'
    DARK_BLUE = '\033[34m'
    DARK_MAGENTA = '\033[35m'
    DARK_CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    RESET = '\033[0m'
type_colors = {
    "Normal": colors.WHITE,
    "Fire": colors.RED,
    "Water": colors.BLUE,
    "Grass": colors.GREEN,
    "Fighting": colors.DARK_RED,
    "Flying": colors.LIGHT_BLUE,
    "Poison": colors.DARK_MAGENTA,
    "Electric": colors.YELLOW,
    "Ground": colors.LIGHT_YELLOW,
    "Psychic": colors.MAGENTA,
    "Rock": colors.DARK_YELLOW,
    "Ice": colors.CYAN,
    "Bug": colors.LIGHT_GREEN,
    "Dragon": colors.DARK_BLUE,
    "Ghost": colors.LIGHT_MAGENTA,
    "Dark": colors.DARK_GRAY,
    "Steel": colors.LIGHT_GRAY
}

# Print the type with color
def print_colored_type(type_name):
    color_code = type_colors.get(type_name, colors.RESET)
    print(f"{color_code}{type_name}{colors.RESET}", end=" ")

def loading_animation1():
    print("-Generating", end="")
    for _ in range(3):  # Repeat the animation 5 times
        for _ in range(3):  # Print dots
            print(".", end="", flush=True)
            time.sleep(0.5)  # Wait for 0.5 seconds
        print("\b\b\b   \b\b\b", end="", flush=True)  # Clear the dots
    print(" Done!-\n")
def loading_animation2():
    print("-Hmmmm...\n", end="")
    time.sleep(1.0)
    for _ in range(1):  # Repeat the animation 5 times
        for word in ["Eeny, ", "meeny, ", "miny, "]:  # Print "Eeny, meeny, miny, moe,"
            print(word, end="", flush=True)
            time.sleep(0.9)  # Wait for 0.9 seconds
        print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b", end="", flush=True)  # Clear the words
    print("Eeny, meeny, miny, moe!-")
    time.sleep(0.7)
def loading_animation3():
    print("-Now, what to pick.", end="")
    for _ in range(3):  # Repeat the animation 5 times
        for _ in range(3):  # Print dots
            print(".", end="", flush=True)
            time.sleep(0.5)  # Wait for 0.5 seconds
        print("\b\b\b   \b\b\b", end="", flush=True)  # Clear the dots
    print("\nGot it-!\n")
    time.sleep(0.5)

print("\nThis is a random Pokémon generator that will dictate everything about that Pokémon for your team.")
def main():
    include_legendary = input("-Do you want to include" + colors.BLUE + " Legendary " + colors.RESET + "Pokémon? (y/n): ").lower()
    include_mythical = input("-Do you want to include" + colors.YELLOW + " Mythical " + colors.RESET + "Pokémon? (y/n): ").lower()
    input("-We will now generate a Pokémon for you to use. Ready?-\n* ↵/⌤ to continue *")

    type_roll = random.randint(1, 17)
    secondary_type = random.randint(1, 2)
    gender_roll = random.randint(1, 2)
    evolve = random.randint(1, 2)
    ability = []
    ability_desc = []
    pkmn_name = []
    pkmn_num = []
    pkmn_type = []
    line_num = 0
    pkmn_data = [(num, name, types) for num, name, types in zip(pkmn_num, pkmn_name, pkmn_type)]

    # Get the name and dex number of the Pokémon and store them in the above lists.
    #------------------------------------------------------------
    fname = "PokeDexGen5.txt"
    handle = open(fname)

    for line in handle:
        line_num += 1
        line = line.rstrip()
        if line.startswith('#'):
            pkmn_num.append(line)
        elif line and line_num % 4 == 0:
            pkmn_type.append(line)
        elif not line:
            continue
        else:
            pkmn_name.append(line)
    legendary_dex = {'#0144', '#0145', '#0146', '#0150', '#0243', '#0244', '#0245', '#0249', '#0250', '#0377', '#0378',
                     '#0379', '#0380', '#0381', '#0382', '#0383', '#0384', '#0480', '#0481', '#0482', '#0483', '#0484',
                     '#0485', '#0486', '#0487', '#0488', '#0638', '#0639', '#0640', '#0641', '#0642', '#0643', '#0644',
                     '#0645', '#0646'}
    mythical_dex = {'#0151', '#0251', '#0385', '#0386', '#0489', '#0490', '#0491', '#0492', '#0493', '#0494', '#0647',
                    '#0648', '#0649'}
    handle.close()
    #print(pkmn_type)
    #print(pkmn_name)
    #for x in pkmn_num:
        #print(f'"{x}":')
    if include_legendary == 'n':
        pkmn_data = [pkmn for pkmn in pkmn_data if pkmn not in legendary_dex]
    if include_mythical == 'n':
        pkmn_data = [pkmn for pkmn in pkmn_data if pkmn not in mythical_dex]

        # Shuffle the filtered Pokémon data
    random.shuffle(pkmn_data)

    #------------------------------------------------------------

    #This part here will open a text document from Bulbapedia and extract the abilities and their descriptions from gen 3-5 and put them into a list
    #------------------------------------------------------------
    fname2 = "Abilities.txt"
    handle = open(fname2)
    for line in handle:
        parts = line.split('\t')
        if len(parts) >= 3:
            name = parts[1].strip()
            ability.append(parts[1])
        parts2 = line.split('\t')
        if len(parts2) >= 4:
            desc = parts2[2]
            ability_desc.append(parts2[2])

    #print(ability_desc)
    #print(ability)
    #------------------------------------------------------------
    # Combining the lists of the names and the descriptions and putting them into a dictionary.
    ability_dict = dict(zip(ability, ability_desc))
    #print(ability_dict)
    handle.close()
    #------------------------------------------------------------

    #This will determine the type(s).
    #------------------------------------------------------------
    def type_assign(type_roll):
        types = [
            "Normal", "Fire", "Water", "Grass", "Fighting", "Flying",
            "Poison", "Electric", "Ground", "Psychic", "Rock", "Ice",
            "Bug", "Dragon", "Ghost", "Dark", "Steel"
        ]
        if type_roll <= len(types):
            return types[type_roll - 1]
        else:
            return "???"

    # Determine the primary type
    primary_type = type_assign(type_roll)
    # Determines if the combination is valid or not
    def valid_combo(primary_type, secondary_type):
        invalid_combo = [("Normal, Ice"), ("Normal, Bug"), ("Normal, Rock", ("Normal, Steel"), ("Ice, Poison"), ("Bug, Dragon"), ("Rock, Ghost"), ("Normal, Ghost"), ("Fire, Water"), ("Fire, Ice"), ("Fire, Steel"), ("Electric, Psychic"), ("Ice, Steel"), ("Ice, Fairy"), ("Fighting, Rock"), ("Poison, Psychic"), ("Psychic, Ghost"), ("Psychic, Dragon"))]
        return (primary_type, secondary_type) not in invalid_combo

    # This function returns a secondary type that is different from the primary type
    def type_rerun(primary_type):
        types = [
            "Normal", "Fire", "Water", "Grass", "Fighting", "Flying",
            "Poison", "Electric", "Ground", "Psychic", "Rock", "Ice",
            "Bug", "Dragon", "Ghost", "Dark", "Steel"
        ]
        # Remove the primary type from the types list
        if primary_type in types:
            types.remove(primary_type)
        # If secondary_type is 1, return the first type from the modified types list
        if secondary_type == 1:
            secondary = random.choice(types)
            while not valid_combo(primary_type, secondary):
                secondary = random.choice(types)
            return secondary
        else:
            return None

    result_list = [primary_type]
    # Call type_rerun to determine the secondary type
    secondary_type = type_rerun(primary_type)
    if secondary_type:
        result_list.append(secondary_type)

    match = [(num, name, types) for num, name, types in zip(pkmn_num, pkmn_name, pkmn_type) if types == ' · '.join(result_list)]

    # To ensure that the return_list matches exactly whatever is printer at the end.
    while not match:
        type_roll = random.randint(1, len(pkmn_type))
        primary_type = type_assign(type_roll)
        result_list = [primary_type]
        secondary_type = type_rerun(primary_type)
        if secondary_type:
            result_list.append(secondary_type)
        match = [(num, name, types) for num, name, types in zip(pkmn_num, pkmn_name, pkmn_type) if types == ' · '.join(result_list)]

    selection = random.choice(match)
    #------------------------------------------------------------
    # This part will assign the abilities to each roll
    pokedex_abilities = {
    "#0001": ["Overgrow, Chlorophyll"],
    "#0002": ["Overgrow, Chlorophyll"],
    "#0003": ["Overgrow, Chlorophyll"],
    "#0004": ["Blaze, Solar Power"],
    "#0005": ["Blaze, Solar Power"],
    "#0006": ["Blaze, Solar Power"],
    "#0007": ["Torrent, Rain Dish"],
    "#0008": ["Torrent, Rain Dish"],
    "#0009": ["Torrent, Rain Dish"],
    "#0010": ["Shield Dust, Run Away"],
    "#0011": ["Shed Skin"],
    "#0012": ["Compound Eyes, Tinted Lens"],
    "#0013": ["Shield Dust, Run Away"],
    "#0014": ["Shed Skin"],
    "#0015": ["Swarm, Sniper"],
    "#0016": ["Keen Eye, Tangled Feet, Big Pecks"],
    "#0017": ["Keen Eye, Tangled Feet, Big Pecks"],
    "#0018": ["Keen Eye, Tangled Feet, Big Pecks"],
    "#0019": ["Run Away, Guts, Hustle"],
    "#0020": ["Run Away, Guts, Hustle"],
    "#0021": ["Keen Eye, Sniper"],
    "#0022": ["Keen Eye, Sniper"],
    "#0023": ["Intimidate, Shed Skin, Unnerve"],
    "#0024": ["Intimidate, Shed Skin, Unnerve"],
    "#0025": ["Static, Lightning Rod"],
    "#0026": ["Static, Lightning Rod"],
    "#0027": ["Sand Veil, Sand Rush"],
    "#0028": ["Sand Veil, Sand Rush"],
    "#0029": ["Poison Point, Rivalry, Hustle"],
    "#0030": ["Poison Point, Rivalry, Hustle"],
    "#0031": ["Poison Point, Rivalry, Sheer Force"],
    "#0032": ["Poison Point, Rivalry, Hustle"],
    "#0033": ["Poison Point, Rivalry, Hustle"],
    "#0034": ["Poison Point, Rivalry, Sheer Force"],
    "#0035": ["Cute Charm, Magic Guard, Friend Guard"],
    "#0036": ["Cute Charm, Magic Guard, Unaware"],
    "#0037": ["Flash Fire, Drought"],
    "#0038": ["Flash Fire, Drought"],
    "#0039": ["Cute Charm, Competitive, Friend Guard"],
    "#0040": ["Cute Charm, Competitive, Frisk"],
    "#0041": ["Inner Focus, Infiltrator"],
    "#0042": ["Inner Focus, Infiltrator"],
    "#0043": ["Chlorophyll, Run Away"],
    "#0044": ["Chlorophyll, Stench"],
    "#0045": ["Chlorophyll, Effect Spore"],
    "#0046": ["Effect Spore, Dry Skin, Damp"],
    "#0047": ["Effect Spore, Dry Skin, Damp"],
    "#0048": ["Compound Eyes, Tinted Lens, Run Away"],
    "#0049": ["Shield Dust, Tinted Lens, Wonder Skin"],
    "#0050": ["Sand Veil, Arena Trap, Sand Force"],
    "#0051": ["Sand Veil, Arena Trap, Sand Force"],
    "#0052": ["Pickup, Technician, Unnerve"],
    "#0053": ["Limber, Technician, Unnerve"],
    "#0054": ["Damp, Cloud Nine, Swift Swim"],
    "#0055": ["Damp, Cloud Nine, Swift Swim"],
    "#0056": ["Vital Spirit, Anger Point, Defiant"],
    "#0057": ["Vital Spirit, Anger Point, Defiant"],
    "#0058": ["Intimidate, Flash Fire, Justified"],
    "#0059": ["Intimidate, Flash Fire, Justified"],
    "#0060": ["Water Absorb, Damp, Swift Swim"],
    "#0061": ["Water Absorb, Damp, Swift Swim"],
    "#0062": ["Water Absorb, Damp, Swift Swim"],
    "#0063": ["Synchronize, Inner Focus, Magic Guard"],
    "#0064": ["Synchronize, Inner Focus, Magic Guard"],
    "#0065": ["Synchronize, Inner Focus, Magic Guard"],
    "#0066": ["Guts, No Guard, Steadfast"],
    "#0067": ["Guts, No Guard, Steadfast"],
    "#0068": ["Guts, No Guard, Steadfast"],
    "#0069": ["Chlorophyll, Gluttony"],
    "#0070": ["Chlorophyll, Gluttony"],
    "#0071": ["Chlorophyll, Gluttony"],
    "#0072": ["Clear Body, Liquid Ooze, Rain Dish"],
    "#0073": ["Clear Body, Liquid Ooze, Rain Dish"],
    "#0074": ["Rock Head, Sturdy, Sand Veil"],
    "#0075": ["Rock Head, Sturdy, Sand Veil"],
    "#0076": ["Rock Head, Sturdy, Sand Veil"],
    "#0077": ["Run Away, Flash Fire, Flame Body"],
    "#0078": ["Run Away, Flash Fire, Flame Body"],
    "#0079": ["Oblivious, Own Tempo, Regenerator"],
    "#0080": ["Oblivious, Own Tempo, Regenerator"],
    "#0081": ["Magnet Pull, Sturdy, Analytic"],
    "#0082": ["Magnet Pull, Sturdy, Analytic"],
    "#0083": ["Keen Eye, Inner Focus, Defiant"],
    "#0084": ["Run Away, Early Bird, Tangled Feet"],
    "#0085": ["Run Away, Early Bird, Tangled Feet"],
    "#0086": ["Thick Fat, Hydration, Ice Body"],
    "#0087": ["Thick Fat, Hydration, Ice Body"],
    "#0088": ["Stench, Sticky Hold, Poison Touch"],
    "#0089": ["Stench, Sticky Hold, Poison Touch"],
    "#0090": ["Shell Armor, Skill Link, Overcoat"],
    "#0091": ["Shell Armor, Skill Link, Overcoat"],
    "#0092": ["Levitate"],
    "#0093": ["Levitate"],
    "#0094": ["Cursed Body"],
    "#0095": ["Rock Head, Sturdy, Weak Armor"],
    "#0096": ["Insomnia, Forewarn, Inner Focus"],
    "#0097": ["Insomnia, Forewarn, Inner Focus"],
    "#0098": ["Hyper Cutter, Shell Armor, Sheer Force"],
    "#0099": ["Hyper Cutter, Shell Armor, Sheer Force"],
    "#0100": ["Soundproof, Static, Aftermath"],
    "#0101": ["Soundproof, Static, Aftermath"],
    "#0102": ["Chlorophyll, Harvest"],
    "#0103": ["Chlorophyll, Harvest"],
    "#0104": ["Rock Head, Lightning Rod, Battle Armor"],
    "#0105": ["Rock Head, Lightning Rod, Battle Armor"],
    "#0106": ["Limber, Reckless, Unburden"],
    "#0107": ["Keen Eye, Iron Fist, Inner Focus"],
    "#0108": ["Own Tempo, Oblivious, Cloud Nine"],
    "#0109": ["Levitate, Neutralizing Gas, Stench"],
    "#0110": ["Levitate, Neutralizing Gas, Stench"],
    "#0111": ["Lightning Rod, Rock Head, Reckless"],
    "#0112": ["Lightning Rod, Rock Head, Reckless"],
    "#0113": ["Natural Cure, Serene Grace, Healer"],
    "#0114": ["Chlorophyll, Leaf Guard, Regenerator"],
    "#0115": ["Early Bird, Scrappy, Inner Focus"],
    "#0116": ["Swift Swim, Sniper, Damp"],
    "#0117": ["Poison Point, Sniper, Damp"],
    "#0118": ["Swift Swim, Water Veil, Lightning Rod"],
    "#0119": ["Swift Swim, Water Veil, Lightning Rod"],
    "#0120": ["Illuminate, Natural Cure, Analytic"],
    "#0121": ["Illuminate, Natural Cure, Analytic"],
    "#0122": ["Soundproof, Filter, Technician"],
    "#0123": ["Swarm, Technician, Steadfast"],
    "#0124": ["Oblivious, Forewarn, Dry Skin"],
    "#0125": ["Static, Vital Spirit"],
    "#0126": ["Flame Body, Vital Spirit"],
    "#0127": ["Hyper Cutter, Mold Breaker, Moxie"],
    "#0128": ["Intimidate, Anger Point, Sheer Force"],
    "#0129": ["Swift Swim, Rattled"],
    "#0130": ["Intimidate, Moxie"],
    "#0131": ["Water Absorb, Shell Armor, Hydration"],
    "#0132": ["Limber, Impostor"],
    "#0133": ["Run Away, Adaptability, Anticipation"],
    "#0134": ["Water Absorb, Hydration"],
    "#0135": ["Volt Absorb, Quick Feet"],
    "#0136": ["Flash Fire, Guts"],
    "#0137": ["Trace, Download, Analytic"],
    "#0138": ["Swift Swim, Shell Armor, Weak Armor"],
    "#0139": ["Swift Swim, Shell Armor, Weak Armor"],
    "#0140": ["Swift Swim, Battle Armor, Weak Armor"],
    "#0141": ["Swift Swim, Battle Armor, Weak Armor"],
    "#0142": ["Rock Head, Pressure, Unnerve"],
    "#0143": ["Immunity, Thick Fat, Gluttony"],
    "#0144": ["Pressure, Snow Cloak"],
    "#0145": ["Pressure, Static"],
    "#0146": ["Pressure, Flame Body"],
    "#0147": ["Shed Skin, Marvel Scale"],
    "#0148": ["Shed Skin, Marvel Scale"],
    "#0149": ["Inner Focus, Multiscale"],
    "#0150": ["Pressure, Unnerve"],
    "#0151": ["Synchronize"],
    "#0152": ["Overgrow, Leaf Guard"],
    "#0153": ["Overgrow, Leaf Guard"],
    "#0154": ["Overgrow, Leaf Guard"],
    "#0155": ["Blaze, Flash Fire"],
    "#0156": ["Blaze, Flash Fire"],
    "#0157": ["Blaze, Flash Fire"],
    "#0158": ["Torrent, Sheer Force"],
    "#0159": ["Torrent, Sheer Force"],
    "#0160": ["Torrent, Sheer Force"],
    "#0161": ["Run Away, Keen Eye, Frisk"],
    "#0162": ["Run Away, Keen Eye, Frisk"],
    "#0163": ["Insomnia, Keen Eye, Tinted Lens"],
    "#0164": ["Insomnia, Keen Eye, Tinted Lens"],
    "#0165": ["Swarm, Early Bird, Rattled"],
    "#0166": ["Swarm, Early Bird, Iron Fist"],
    "#0167": ["Swarm, Insomnia, Sniper"],
    "#0168": ["Swarm, Insomnia, Sniper"],
    "#0169": ["Inner Focus, Infiltrator"],
    "#0170": ["Volt Absorb, Illuminate, Water Absorb"],
    "#0171": ["Volt Absorb, Illuminate, Water Absorb"],
    "#0172": ["Static, Lightning Rod"],
    "#0173": ["Cute Charm, Magic Guard, Friend Guard"],
    "#0174": ["Cute Charm, Competitive, Friend Guard"],
    "#0175": ["Hustle, Serence Grace, Super Luck"],
    "#0176": ["Hustle, Serence Grace, Super Luck"],
    "#0177": ["Synchronize, Early Bird, Magic Bounce"],
    "#0178": ["Synchronize, Early Bird, Magic Bounce"],
    "#0179": ["Static, Plus"],
    "#0180": ["Static, Plus"],
    "#0181": ["Static, Plus"],
    "#0182": ["Chlorophyll, Healer"],
    "#0183": ["Thick Fat, Huge Power, Sap Sipper"],
    "#0184": ["Thick Fat, Huge Power, Sap Sipper"],
    "#0185": ["Sturdy, Rock Head, Rattled"],
    "#0186": ["Water Absorb, Damp, Drizzle"],
    "#0187": ["Chlorophyll, Leaf Guard, Infiltrator"],
    "#0188": ["Chlorophyll, Leaf Guard, Infiltrator"],
    "#0189": ["Chlorophyll, Leaf Guard, Infiltrator"],
    "#0190": ["Run Away, Pickup, Skill Link"],
    "#0191": ["Chlorophyll, Solar Power, Early Bird"],
    "#0192": ["Chlorophyll, Solar Power, Early Bird"],
    "#0193": ["Speed Boost, Compound Eyes, Frisk"],
    "#0194": ["Damp, Water Absorb, Unaware"],
    "#0195": ["Damp, Water Absorb, Unaware"],
    "#0196": ["Synchronize, Magic Bounce"],
    "#0197": ["Synchronize, Inner Focus"],
    "#0198": ["Insomnia, Super Luck, Prankster"],
    "#0199": ["Oblivious, Own Tempo, Regenerator"],
    "#0200": ["Levitate"],
    "#0201": ["Levitate"],
    "#0202": ["Shadow Tag, Telepathy"],
    "#0203": ["Inner Focus, Early Bird, Sap Sipper"],
    "#0204": ["Sturdy, Overcoat"],
    "#0205": ["Sturdy, Overcoat"],
    "#0206": ["Serence Grace, Run Away, Rattled"],
    "#0207": ["Hyper Cutter, Sand Veil, Immunity"],
    "#0208": ["Rock Head, Sturdy, Sheer Force"],
    "#0209": ["Intimidate, Run Away, Rattled"],
    "#0210": ["Intimidate, Quick Feet, Rattled"],
    "#0211": ["Poison Point, Swift Swim, Intimidate"],
    "#0212": ["Swarm, Technician, Light Metal"],
    "#0213": ["Sturdy, Gluttony, Contrary"],
    "#0214": ["Swarm, Guts, Moxie"],
    "#0215": ["Inner Focus, Keen Eye, Pickpocket"],
    "#0216": ["Pickup, Quick Feet, Honey Gather"],
    "#0217": ["Guts, Quick Feet, Unnerve"],
    "#0218": ["Magma Armor, Flame Body, Weak Armor"],
    "#0219": ["Magma Armor, Flame Body, Weak Armor"],
    "#0220": ["Oblivious, Snow Cloak, Thick Fat"],
    "#0221": ["Oblivious, Snow Cloak, Thick Fat"],
    "#0222": ["Hustle, Natural Cure, Regenerator"],
    "#0223": ["Hustle, Sniper, Moody"],
    "#0224": ["Suction Cups, Sniper, Moody"],
    "#0225": ["Vital Spirit, Hustle, Insomnia"],
    "#0226": ["Swift Swim, Water Absorb, Water Veil"],
    "#0227": ["Keen Eye, Sturdy, Weak Armor"],
    "#0228": ["Early Bird, Flash Fire, Unnerve"],
    "#0229": ["Early Bird, Flash Fire, Unnerve"],
    "#0230": ["Swift Swim, Sniper, Damp"],
    "#0231": ["Pickup, Sand Veil"],
    "#0232": ["Sturdy, Sand Veil"],
    "#0233": ["Trace, Download, Analytic"],
    "#0234": ["Intimidate, Frisk, Sap Sipper"],
    "#0235": ["Own Tempo, Technician, Moody"],
    "#0236": ["Guts, Steadfast, Vital Spirit"],
    "#0237": ["Intimidate, Technician, Steadfast"],
    "#0238": ["Oblivious, Forewarn, Hydration"],
    "#0239": ["Static, Vital Spirit"],
    "#0240": ["Flame Body, Vital Spirit"],
    "#0241": ["Thick Fat, Scrappy, Sap Sipper"],
    "#0242": ["Natural Cure, Serene Grace, Healer"],
    "#0243": ["Pressure, Inner Focus"],
    "#0244": ["Pressure, Inner Focus"],
    "#0245": ["Pressure, Inner Focus"],
    "#0246": ["Guts, Sand Veil"],
    "#0247": ["Shed Skin"],
    "#0248": ["Sand Stream, Unnerve"],
    "#0249": ["Pressure, Multiscale"],
    "#0250": ["Pressure, Regenerator"],
    "#0251": ["Natural Cure"],
    "#0252": ["Overgrow, Unburden"],
    "#0253": ["Overgrow, Unburden"],
    "#0254": ["Overgrow, Unburden"],
    "#0255": ["Blaze, Speed Boost"],
    "#0256": ["Blaze, Speed Boost"],
    "#0257": ["Blaze, Speed Boost"],
    "#0258": ["Torrent, Damp"],
    "#0259": ["Torrent, Damp"],
    "#0260": ["Torrent, Damp"],
    "#0261": ["Run Away, Quick Feet, Rattled"],
    "#0262": ["Intimidate, Quick Feet, Moxie"],
    "#0263": ["Pickup, Gluttony, Quick Feet"],
    "#0264": ["Pickup, Gluttony, Quick Feet"],
    "#0265": ["Shield Dust, Run Away"],
    "#0266": ["Shed Skin"],
    "#0267": ["Swarm, Rivalry"],
    "#0268": ["Shed Skin"],
    "#0269": ["Shield Dust, Compound Eyes"],
    "#0270": ["Swift Swim, Rain Dish, Own Tempo"],
    "#0271": ["Swift Swim, Rain Dish, Own Tempo"],
    "#0272": ["Swift Swim, Rain Dish, Own Tempo"],
    "#0273": ["Chlorophyll, Early Bird, Pickpocket"],
    "#0274": ["Chlorophyll, Early Bird, Pickpocket"],
    "#0275": ["Chlorophyll, Early Bird, Pickpocket"],
    "#0276": ["Guts, Scrappy"],
    "#0277": ["Guts, Scrappy"],
    "#0278": ["Keen Eye, Hydration, Rain Dish"],
    "#0279": ["Keen Eye, Drizzle, Rain Dish"],
    "#0280": ["Synchronize, Trace, Telepathy"],
    "#0281": ["Synchronize, Trace, Telepathy"],
    "#0282": ["Synchronize, Trace, Telepathy"],
    "#0283": ["Swift Swim, Rain Dish"],
    "#0284": ["Intimidate, Unnerve"],
    "#0285": ["Effect Spore, Poison Heal, Quick Feet"],
    "#0286": ["Effect Spore, Poison Heal, Technician"],
    "#0287": ["Truant"],
    "#0288": ["Vital Spirit"],
    "#0289": ["Truant"],
    "#0290": ["Compoung Eyes, Run Away"],
    "#0291": ["Speed Boost, Infiltrator"],
    "#0292": ["Wonder Guard"],
    "#0293": ["Soundproof, Rattled"],
    "#0294": ["Soundproof, Scrappy"],
    "#0295": ["Soundproof, Scrappy"],
    "#0296": ["Thick Fat, Guts, Sheer Force"],
    "#0297": ["Thick Fat, Guts, Sheer Force"],
    "#0298": ["Thick Fat, Huge Power, Sap Sipper"],
    "#0299": ["Sturdy, Magnet Pull, Sand Force"],
    "#0300": ["Cute Charm, Normalize, Wonder Skin"],
    "#0301": ["Cute Charm, Normalize, Wonder Skin"],
    "#0302": ["Keen Eye, Stall, Prankster"],
    "#0303": ["Hyper Cutter, Intimidate, Sheer Force"],
    "#0304": ["Sturdy, Rock Head, Heavy Metal"],
    "#0305": ["Sturdy, Rock Head, Heavy Metal"],
    "#0306": ["Sturdy, Rock Head, Heavy Metal"],
    "#0307": ["Pure Power. Telepathy"],
    "#0308": ["Pure Power. Telepathy"],
    "#0309": ["Static, Lightning  Rod, Minus"],
    "#0310": ["Static, Lightning  Rod, Minus"],
    "#0311": ["Plus, Lightning Rod"],
    "#0312": ["Minus, Volt Absorb"],
    "#0313": ["Illuminate, Swarm, Prankster"],
    "#0314": ["Oblivious, Tinted Lens, Prankster"],
    "#0315": ["Natural Cure, Poison Point, Leaf Guard"],
    "#0316": ["Liquid Ooze, Sticky Hold, Gluttony"],
    "#0317": ["Liquid Ooze, Sticky Hold, Gluttony"],
    "#0318": ["Rough Skin, Speed Boost"],
    "#0319": ["Rough Skin, Speed Boost"],
    "#0320": ["Water Veil, Oblivious, Pressure"],
    "#0321": ["Water Veil, Oblivious, Pressure"],
    "#0322": ["Oblivious, Simple, Own Tempo"],
    "#0323": ["Magma Armor, Solid Rock, Anger Point"],
    "#0324": ["White Smoke, Drought, Shell Armor"],
    "#0325": ["Thick Fat, Own Tempo, Gluttony"],
    "#0326": ["Thick Fat, Own Tempo, Gluttony"],
    "#0327": ["Own Tempo, Tangled Feet, Contrary"],
    "#0328": ["Hyper Cutter, Arena Trap, Sheer Force"],
    "#0329": ["Levitate"],
    "#0330": ["Levitate"],
    "#0331": ["Sand Veil, Water Absorb"],
    "#0332": ["Sand Veil, Water Absorb"],
    "#0333": ["Natural Cure, Cloud Nine"],
    "#0334": ["Natural Cure, Cloud Nine"],
    "#0335": ["Immunity, Toxic Boost"],
    "#0336": ["Shed Skin, Infiltrator"],
    "#0337": ["Levitate"],
    "#0338": ["Levitate"],
    "#0339": ["Oblivious, Anticipation, Hydration"],
    "#0340": ["Oblivious, Anticipation, Hydration"],
    "#0341": ["Hyper Cutter, Shell Armor, Adaptability"],
    "#0342": ["Hyper Cutter, Shell Armor, Adaptability"],
    "#0343": ["Levitate"],
    "#0344": ["Levitate"],
    "#0345": ["Suction Cups, Storm Drain"],
    "#0346": ["Suction Cups, Storm Drain"],
    "#0347": ["Battle Armor, Swift Swim"],
    "#0348": ["Battle Armor, Swift Swim"],
    "#0349": ["Swift Swim, Oblivious, Adaptability"],
    "#0350": ["Marvel Scale, Competitive, Cute Charm"],
    "#0351": ["Forecast"],
    "#0352": ["Color Change, Protean"],
    "#0353": ["Insomnia, Frisk, Cursed Body"],
    "#0354": ["Insomnia, Frisk, Cursed Body"],
    "#0355": ["Levitate, Frisk"],
    "#0356": ["Pressure, Frisk"],
    "#0357": ["Chlorophyll, Solar Power, Harvest"],
    "#0358": ["Levitate"],
    "#0359": ["Pressure, Super Luck, Justified"],
    "#0360": ["Shadow Tag, Telepathy"],
    "#0361": ["Inner Focus, Ice Body, Moody"],
    "#0362": ["Inner Focus, Ice Body, Moody"],
    "#0363": ["Thick Fat, Ice Body, Oblivious"],
    "#0364": ["Thick Fat, Ice Body, Oblivious"],
    "#0365": ["Thick Fat, Ice Body, Oblivious"],
    "#0366": ["Shell Armor, Rattled"],
    "#0367": ["Swift Swim, Water Veil"],
    "#0368": ["Swift Swim, Hydration"],
    "#0369": ["Swift Swim, Rock Head, Sturdy"],
    "#0370": ["Swift Swim, Hydration"],
    "#0371": ["Rock Head, Sheer Force"],
    "#0372": ["Rock Head, Overcoat"],
    "#0373": ["Intimidate, Moxie"],
    "#0374": ["Clear Body, Light Metal"],
    "#0375": ["Clear Body, Light Metal"],
    "#0376": ["Clear Body, Light Metal"],
    "#0377": ["Clear Body, Sturdy"],
    "#0378": ["Clear Body, Ice Body"],
    "#0379": ["Clear Body, Light Metal"],
    "#0380": ["Levitate"],
    "#0381": ["Levitate"],
    "#0382": ["Drizzle"],
    "#0383": ["Drought"],
    "#0384": ["Air Lock"],
    "#0385": ["Serene Grace"],
    "#0386": ["Pressure"],
    "#0387": ["Overgrow, Shell Armor"],
    "#0388": ["Overgrow, Shell Armor"],
    "#0389": ["Overgrow, Shell Armor"],
    "#0390": ["Blaze, Iron Fist"],
    "#0391": ["Blaze, Iron Fist"],
    "#0392": ["Blaze, Iron Fist"],
    "#0393": ["Torrent, Defiant"],
    "#0394": ["Torrent, Defiant"],
    "#0395": ["Torrent, Defiant"],
    "#0396": ["Keen Eye, Reckless"],
    "#0397": ["Intimidate, Reckless"],
    "#0398": ["Intimidate, Reckless"],
    "#0399": ["Simple, Unaware, Moody"],
    "#0400": ["Simple, Unaware, Moody"],
    "#0401": ["Shed SKin, Run Away"],
    "#0402": ["Swarm, Technician"],
    "#0403": ["Rivalry, Intimidate, Guts"],
    "#0404": ["Rivalry, Intimidate, Guts"],
    "#0405": ["Rivalry, Intimidate, Guts"],
    "#0406": ["Natural Cure, Poison Point, Leaf Guard"],
    "#0407": ["Natural Cure, Poison Point, Technician"],
    "#0408": ["Mold Breaker, Sheer Force"],
    "#0409": ["Mold Breaker, Sheer Force"],
    "#0410": ["Sturdy, Soundproof"],
    "#0411": ["Sturdy, Soundproof"],
    "#0412": ["Shed Skin, Overcoat"],
    "#0413": ["Anticipation, Overcoat"],
    "#0414": ["Swarm, Tinted Lens"],
    "#0415": ["Honey Gather, Hustle"],
    "#0416": ["Pressure, Unnerve"],
    "#0417": ["Run Away, Pickup, Volt Absorb"],
    "#0418": ["Swift Swim, Water Veil"],
    "#0419": ["Swift Swim, Water Veil"],
    "#0420": ["Chlorophyll"],
    "#0421": ["Flower Gift"],
    "#0422": ["Sticky Hold, Storm Drain, Sand Force"],
    "#0423": ["Sticky Hold, Storm Drain, Sand Force"],
    "#0424": ["Technician, Pickup, Skill Link"],
    "#0425": ["Aftermath, Unburden, Flare Boost"],
    "#0426": ["Aftermath, Unburden, Flare Boost"],
    "#0427": ["Run Away, Klutz, Limber"],
    "#0428": ["Cute Charm, Klutz, Limber"],
    "#0429": ["Levitate"],
    "#0430": ["Insomnia, Super Luck, Moxie"],
    "#0431": ["Limber, Own Tempo, Keen Eye"],
    "#0432": ["Thick Fat, Own Tempo, Defiant"],
    "#0433": ["Levitate"],
    "#0434": ["Stench, Aftermath, Keen Eye"],
    "#0435": ["Stench, Aftermath, Keen Eye"],
    "#0436": ["Levitate, Heatproof, Heavy Metal"],
    "#0437": ["Levitate, Heatproof, Heavy Metal"],
    "#0438": ["Sturdy, Rock Head, Rattled"],
    "#0439": ["Soundproof, Filter, Technician"],
    "#0440": ["Natural Cure, Serene Grace, Friend Guard"],
    "#0441": ["Keen Eye, Tangled Feet, Big Pecks"],
    "#0442": ["Pressure, Infiltrator"],
    "#0443": ["Sand Veil, Rough Skin"],
    "#0444": ["Sand Veil, Rough Skin"],
    "#0445": ["Sand Veil, Rough Skin"],
    "#0446": ["Pickup, Thick Fat, Gluttony"],
    "#0447": ["Steadfast, Inner Focus, Prankster"],
    "#0448": ["Steadfast, Inner Focus, Justified"],
    "#0449": ["Sand Stream, Sand Force"],
    "#0450": ["Sand Stream, Sand Force"],
    "#0451": ["Battle Armor, Sniper, Keen Eye"],
    "#0452": ["Battle Armor, Sniper, Keen Eye"],
    "#0453": ["Anticipation, Dry Skin, Poison Touch"],
    "#0454": ["Anticipation, Dry Skin, Poison Touch"],
    "#0455": ["Levitate"],
    "#0456": ["Swift Swim, Storm Drain, Water Veil"],
    "#0457": ["Swift Swim, Storm Drain, Water Veil"],
    "#0458": ["Swift Swim, Water Absorb, Water Veil"],
    "#0459": ["Snow Warning, Soundproof"],
    "#0460": ["Snow Warning, Soundproof"],
    "#0461": ["Pressure, Pickpocket"],
    "#0462": ["Magnet Pull, Sturdy, Analytic"],
    "#0463": ["Own Tempo, Oblivious, Cloud Nine"],
    "#0464": ["Lightning Rod, Solid Rock, Reckless"],
    "#0465": ["Chlorophyll, Leaf Guard, Regenerator"],
    "#0466": ["Motor Drive, Vital Spirit"],
    "#0467": ["Flame Body, Vital Spirit"],
    "#0468": ["Hustle, Serene Grace, Super Luck"],
    "#0469": ["Speed Boost, Tinted Lens, Frisk"],
    "#0470": ["Leaf Guard, Chlorophyll"],
    "#0471": ["Snow Cloak, Ice Body"],
    "#0472": ["Hyper Cutter, Sand Veil, Poison Heal"],
    "#0473": ["Oblivious, Snow Cloak, Thick Fat"],
    "#0474": ["Adaptability, Download, Analytic"],
    "#0475": ["Steadfast, Sharpness, Justified"],
    "#0476": ["Sturdy, Magnet Pull, Sand Force"],
    "#0477": ["Pressure, Frisk"],
    "#0478": ["Snow Cloak, Cursed Body"],
    "#0479": ["Levitate"],
    "#0480": ["Levitate"],
    "#0481": ["Levitate"],
    "#0482": ["Levitate"],
    "#0483": ["Pressure, Telepathy"],
    "#0484": ["Pressure, Telepathy"],
    "#0485": ["Flash Fire, Flame Body"],
    "#0486": ["Slow Start"],
    "#0487": ["Pressure, Telepathy"],
    "#0488": ["Levitate"],
    "#0489": ["Hydration"],
    "#0490": ["Hydration"],
    "#0491": ["Bad Dreams"],
    "#0492": ["Natural Cure"],
    "#0493": ["Multitype"],
    "#0494": ["Victory Star"],
    "#0495": ["Overgrow, Contrary"],
    "#0496": ["Overgrow, Contrary"],
    "#0497": ["Overgrow, Contrary"],
    "#0498": ["Blaze, Thick Fat"],
    "#0499": ["Blaze, Thick Fat"],
    "#0500": ["Blaze, Reckless"],
    "#0501": ["Torrent, Shell Armor"],
    "#0502": ["Torrent, Shell Armor"],
    "#0503": ["Torrent, Shell Armor"],
    "#0504": ["Run Away, Keen Eye, Analytic"],
    "#0505": ["Run Away, Keen Eye, Analytic"],
    "#0506": ["Vital Spirit, Pickup, Run Away"],
    "#0507": ["Intimidate, Sand Rush, Scrappy"],
    "#0508": ["Intimidate, Sand Rush, Scrappy"],
    "#0509": ["Limber, Unburden, Prankster"],
    "#0510": ["Limber, Unburden, Prankster"],
    "#0511": ["Gluttony, Overgrow"],
    "#0512": ["Gluttony, Overgrow"],
    "#0513": ["Gluttony, Blaze"],
    "#0514": ["Gluttony, Blaze"],
    "#0515": ["Gluttony, Torrent"],
    "#0516": ["Gluttony, Torrent"],
    "#0517": ["Forewarn, Synchronize, Telepathy"],
    "#0518": ["Forewarn, Synchronize, Telepathy"],
    "#0519": ["Big Pecks, Super Luck. Rivalry"],
    "#0520": ["Big Pecks, Super Luck. Rivalry"],
    "#0521": ["Big Pecks, Super Luck. Rivalry"],
    "#0522": ["Lightning Rod, Motor Drive, Sap Sipper"],
    "#0523": ["Lightning Rod, Motor Drive, Sap Sipper"],
    "#0524": ["Sturdy, Weak Armor, Sand Force"],
    "#0525": ["Sturdy, Weak Armor, Sand Force"],
    "#0526": ["Sturdy, Weak Armor, Sand Force"],
    "#0527": ["Unaware, Klutz, Simple"],
    "#0528": ["Unaware, Klutz, Simple"],
    "#0529": ["Sand Rush, Sand Force, Mold Breaker"],
    "#0530": ["Sand Rush, Sand Force, Mold Breaker"],
    "#0531": ["Healer, Regenerator, Klutz"],
    "#0532": ["Guts, Sheer Force, Iron Fist"],
    "#0533": ["Guts, Sheer Force, Iron Fist"],
    "#0534": ["Guts, Sheer Force, Iron Fist"],
    "#0535": ["Swift Swim, Hydration, Water Absorb"],
    "#0536": ["Swift Swim, Hydration, Water Absorb"],
    "#0537": ["Swift Swim, Hydration, Water Absorb"],
    "#0538": ["Guts, Inner Focus, Mold Breaker"],
    "#0539": ["Guts, Inner Focus, Mold Breaker"],
    "#0540": ["Swarm, Chlorophyll, Overcoat"],
    "#0541": ["Leaf Guard, Chlorophyll, Overcoat"],
    "#0542": ["Swarm, Chlorophyll, Overcoat"],
    "#0543": ["Poison Point, Swarm, Speed Boost"],
    "#0544": ["Poison Point, Swarm, Speed Boost"],
    "#0545": ["Poison Point, Swarm, Speed Boost"],
    "#0546": ["Prankster, Infiltrator, Chlorophyll"],
    "#0547": ["Prankster, Infiltrator, Chlorophyll"],
    "#0548": ["Chlorophyll, Own Tempo, Leaf guard"],
    "#0549": ["Chlorophyll, Own Tempo, Leaf guard"],
    "#0550": ["Reckless, Adaptability, Mold Breaker"],
    "#0551": ["Intimidate, Moxie, Anger Point"],
    "#0552": ["Intimidate, Moxie, Anger Point"],
    "#0553": ["Intimidate, Moxie, Anger Point"],
    "#0554": ["Hustle, Inner Focus"],
    "#0555": ["Sheer Force, Zen Mode"],
    "#0556": ["Water Absorb, Chlorophyll, Storm Drain"],
    "#0557": ["Sturdy, Shell Armor, Weak Armor"],
    "#0558": ["Sturdy, Shell Armor, Weak Armor"],
    "#0559": ["Shed Skin, Moxie, Intimidate"],
    "#0560": ["Shed Skin, Moxie, Intimidate"],
    "#0561": ["Wonder Skin, Magic Guard, Tinted Lens"],
    "#0562": ["Mummy"],
    "#0563": ["Mummy"],
    "#0564": ["Solid Rock, Sturdy, Swift Swim"],
    "#0565": ["Solid Rock, Sturdy, Swift Swim"],
    "#0566": ["Defeatist"],
    "#0567": ["Defeatist"],
    "#0568": ["Stench, Sticky Hold, Aftermath"],
    "#0569": ["Stench, Weak Armor, Aftermath"],
    "#0570": ["Illusion"],
    "#0571": ["Illusion"],
    "#0572": ["Cute Charm, Technician, Skill Link"],
    "#0573": ["Cute Charm, Technician, Skill Link"],
    "#0574": ["Frisk, Competitive, Shadow Tag"],
    "#0575": ["Frisk, Competitive, Shadow Tag"],
    "#0576": ["Frisk, Competitive, Shadow Tag"],
    "#0577": ["Overcoat, Magic Guard, Regenerator"],
    "#0578": ["Overcoat, Magic Guard, Regenerator"],
    "#0579": ["Overcoat, Magic Guard, Regenerator"],
    "#0580": ["Keen Eye, Big Pecks, Hydration"],
    "#0581": ["Keen Eye, Big Pecks, Hydration"],
    "#0582": ["Ice Body, Snow Cloak, Weak Armor"],
    "#0583": ["Ice Body, Snow Cloak, Weak Armor"],
    "#0584": ["Ice Body, Snow Warning, Weak Armor"],
    "#0585": ["Chlorophyll, Sap Sipper, Serene Grace"],
    "#0586": ["Chlorophyll, Sap Sipper, Serene Grace"],
    "#0587": ["Static, Motor Drive"],
    "#0588": ["Swarm, Shed Skin, No Guard"],
    "#0589": ["Swarm, Shell Armor, Overcoat"],
    "#0590": ["Effect Spore, Regenerator"],
    "#0591": ["Effect Spore, Regenerator"],
    "#0592": ["Water Absorb, Cursed Body, Damp"],
    "#0593": ["Water Absorb, Cursed Body, Damp"],
    "#0594": ["Helaer, Hydration, Regenerator"],
    "#0595": ["Compound Eyes, Unnerve, Swarm"],
    "#0596": ["Compound Eyes, Unnerve, Swarm"],
    "#0597": ["Iron Barbs, Anticipation"],
    "#0598": ["Iron Barbs, Anticipation"],
    "#0599": ["Plus, Minus, Clear Body"],
    "#0600": ["Plus, Minus, Clear Body"],
    "#0601": ["Plus, Minus, Clear Body"],
    "#0602": ["Levitate"],
    "#0603": ["Levitate"],
    "#0604": ["Levitate"],
    "#0605": ["Telepathy, Synchronize, Analytic"],
    "#0606": ["Telepathy, Synchronize, Analytic"],
    "#0607": ["Flash Fire, Flame Body, Infiltrator"],
    "#0608": ["Flash Fire, Flame Body, Infiltrator"],
    "#0609": ["Flash Fire, Flame Body, Infiltrator"],
    "#0610": ["Rivalry, Mold Breaker, Unnerve"],
    "#0611": ["Rivalry, Mold Breaker, Unnerve"],
    "#0612": ["Rivalry, Mold Breaker, Unnerve"],
    "#0613": ["Snow Cloak, Slush Rush, Rattled"],
    "#0614": ["Snow Cloak, Slush Rush, Swift Swim"],
    "#0615": ["Levitate"],
    "#0616": ["Hydration, Shell Armor, Overcoat"],
    "#0617": ["Hydration, Sticky Hold, Unburden"],
    "#0618": ["Static, Limber, Sand Veil"],
    "#0619": ["Inner Focus, Regenerator, Reckless"],
    "#0620": ["Inner Focus, Regenerator, Reckless"],
    "#0621": ["Rough Skin, Sheer Force, Mold Breaker"],
    "#0622": ["Iron Fist, Klutz, No Guard"],
    "#0623": ["Iron Fist, Klutz, No Guard"],
    "#0624": ["Defiant, Inner Focus, Pressure"],
    "#0625": ["Defiant, Inner Focus, Pressure"],
    "#0626": ["Reckless, Sap Sipper, Soundproof"],
    "#0627": ["Keen Eye, Sheer Force, Hustle"],
    "#0628": ["Keen Eye, Sheer Force, Defiant"],
    "#0629": ["Big Pecks, Overcoat, Weak Armor"],
    "#0630": ["Big Pecks, Overcoat, Weak Armor"],
    "#0631": ["Gluttony, Flash Fire, White Smoke"],
    "#0632": ["Swarm, Hustle, Truant"],
    "#0633": ["Hustle"],
    "#0634": ["Hustle"],
    "#0635": ["Levitate"],
    "#0636": ["Flame Body, Swarm"],
    "#0637": ["Flame Body, Swarm"],
    "#0638": ["Justified"],
    "#0639": ["Justified"],
    "#0640": ["Justified"],
    "#0641": ["Prankster, Defiant"],
    "#0642": ["Prankster, Defiant"],
    "#0643": ["Turboblaze"],
    "#0644": ["Teravolt"],
    "#0645": ["Sand Force, Sheer Force"],
    "#0646": ["Pressure"],
    "#0647": ["Justified"],
    "#0648": ["Serene Grace"],
    "#0649": ["Download"]

    }

    selection_num = selection[0]

    #------------------------------------------------------------
    # Randomly select one ability to go with your Pokémon
    selected_ability = random.choice(pokedex_abilities[selection_num])
    if ', ' in selected_ability:
        selected_ability = random.choice(selected_ability.split(', '))

    ability_description = ability_dict.get(selected_ability)

    #------------------------------------------------------------
    loading_animation1()
    print(end="")
    for t in result_list:
        print_colored_type(t)
    input("\n-This is your type!-\n* ↵/⌤ to continue *\n")
    loading_animation3()
    #------------------------------------------------------------

    print("PokéDex Number:  ", selection[0])
    if selection[0] in legendary_dex:
        print(colors.BLUE + "* Legendary *" + colors.RESET)
    elif selection[0] in mythical_dex:
        print(colors.YELLOW + "* Mythical *" + colors.RESET)
    print("Name:  ", selection[1])
    print("Type:  ", end="")
    for type_name in selection[2].split(" · "):
        print_colored_type(type_name)
        print(" ", end="")
    print("\nAbilities:   ", ", ".join(pokedex_abilities[selection_num]))
    input("\n-This is your Pokémon. Next step is to pick out what Ability it will have!-\n* ↵/⌤ to continue *\n")
    loading_animation2()
    print('\n-You will have to use this Ability with it!-\n', selected_ability, '-', ability_description, '\n* ↵/⌤ to continue *\n')


    q1 = input("\n-What's the gender?- * If it has one *   (y/n).\n")
    if q1 == "n":
        print("-" + colors.RED + "N" + colors.DARK_YELLOW + "o" + colors.YELLOW + "n" + colors.RESET + "-" +colors.GREEN + "B" + colors.CYAN + "i" + colors.LIGHT_BLUE + "n" + colors.BLUE + "a" + colors.DARK_MAGENTA + "r" + colors.MAGENTA + "y" + colors.RESET + "!")
    elif gender_roll == 1:
        print(colors.BLUE + "-Male!-" + colors.RESET)
    else:
        print(colors.MAGENTA + "-Female!-" + colors.RESET)

    input("\n-Can it evolve, if applicable?-\n* ↵/⌤ to continue *\n")
    if evolve == 1:
        print(colors.YELLOW + "-Sure!-\n" + colors.RESET)
    else:
        print(colors.RED + "-Nope!-\n" + colors.RESET)

    random_number = random.randint(1, 5)
    if random_number == 1:
      answer = '-Yup! This is definitely the one to carry you. Treat it with respect.-'
    elif random_number == 2:
      answer = "-Not gonna lie boss, this was a dogshit pull. I'm not sorry.-"
    elif random_number == 3:
      answer = "-Without a doubt, this is the most mid Pokémon you could've gotten. Purely because of its gender-"
    elif random_number == 4:
      answer = "-Mmmm, I'm not sure how to feel about this one. But, you'll make it work.-"
    elif random_number == 5:
      answer = "-You think you can make this work? Me personally... Doubtful.-"
    time.sleep(2.0)
    print(answer)

if __name__ == "__main__":
    while True:
        main()
        run_again = input("\nDo you want to generate another? (y/n)\n").strip().lower()
        if run_again != "y":
            print("Goodbye!")
            time.sleep(1.0)
            break