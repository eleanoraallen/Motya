# Definitions ---------------------------------------------------
init python:
    # Character Stats
    class CharStats:
        def __init__(self, hunger, thirst, health, morale, alive):
            self.hunger = hunger
            self.thirst = thirst
            self.health = health
            self.morale = morale
            self.alive = alive

    Player = CharStats(5, 3, 10, 10, True)
    Partner = CharStats(5, 3, 10, 10, True)
    Child1 = CharStats(5, 3, 10, 10, True)
    Child2 = CharStats(5, 3, 10, 10, True)

    # Places visited
    visited = []

    # Invnetory
    Money = 0
    Food = 0
    Water = 0
    Wine = 0
    Medicine = 0
    Fishing = 5

    # Store Prices
    FoodPrice = 10
    WaterPrice = 1
    WinePrice = 50
    MedicinePrice = 200
    FishingPrice = 25

    # Has Boat
    HasBoat = True
    
    # Can Leave
    CanLeave = False

    # Taken Food
    NotTakenFood = True

    # Update Stats
    def updateStats(c1):
        c1.hunger = c1.hunger - 1
        c1.thirst = c1.thirst - 1
        if (c1.hunger < 4):
            c1.health - 1
        if (c1.thirst < 3):
            c1.health - 1
        if (c1.hunger >= 4 and c1.thirst == 3 and (c1.health < 10)):
            c1.health = c1.health + 1
        if (c1.hunger == 5 and c1.thirst == 3 and (c1.morale < 10)):
            c1.morale = c1.morale + 1
        if (c1.hunger < 3 or c1.thirst < 2 or c1.health < 6):
            c1.morale = c1.morale - 1
        if (c1.health < 1 or c1.thirst < 1 or c1.health < 1 or c1.morale < 1):
            c1.alive = False
        return c1

# Game Start

label start:

    # Starting Scene ----------------------------------------------------------
    scene home
    with dissolve
    "Hello and welcome to Motya, an interactive fiction game about life on an island in the ancient world."
    "In this game you will play the role of a citizen of the Punic colony of Motya around the year 398BCE."
    "You are between twenty-five and thirty years old. You have a Partner and two Children, one about seven and the other about two. You make your living fishing using a small boat that you own."
    "Every day you will be able to explore the city by going to a total of three locations. These locations are:"
    "The Cothon, the city’s harbor where you store your boat."
    "The Market where you can buy and sell things."
    "The Residential Quarter where you live and can gossip with your neighbors."
    "The Cappiddazzu, the city’s religious and cultural center."
    "The Artisan’s Quarter where the city’s artisans live and work."
    "The Causeway that connects the city to the mainland."
    "The Tophet, the oldest ritual site in the city."
    "The Necropolis, the city’s graveyard." 
    "And The Barracks, where the city’s protectors live."
    "Keep in mind that you can only go to three locations per day, and you can’t go to the same location twice, so plan your days accordingly!"
    "In order to survive you and each member of your family must eat and drink regularly."
    "Each of you has four stats that track your overall well being. Hunger, Thirst, Health, and Morale." 
    "Hunger and Thirst decrease if a character doesn’t eat or drink. Health and Morale may also decrease if a character is hungry or dehydrated, but can also be affected by other events in the world."
    "At the end of each day, you will be prompted to divide up your resources for the day amongst your family, so make sure you have enough resources to keep them and yourself alive!"
    "You can purchase food and water at the market, or get them through events at other locations."
    "You can also by wine and medicine, which increase morale and health respectively, though using these items does have some tradeoffs."
    "And that’s more or less everything. Without further ado, let the game begin!"

    jump Day1

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 1
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    label Day1:
        scene home
        with dissolve

        "Day 1:"
        "It’s still dark when you wake up."
        "You are in your home, a medium sized apartment in the city of Motya."
        "Your apartment is located in the southern part of the island’s central Residential District."
        "With space on the island limited the buildings in this area have been expanded again and again, so that now many of them are five or six stories high, their flat, earth covered roofs looming higher the city walls."
        "Beside you, your Partner is still asleep. In the next room your two Children are quiet. You thank every god you know of that the youngest managed to sleep through the night."
        "You quietly get out of bed and tip toe out the door, determined not to wake the rest of your sleeping family."
        "Fish are more likely to bite in the morning, so you know you should probably head to The Cothon right away, then to The Market to buy food with the money you earn."
        "However, there is nothing forcing you to do so. You can go anywhere you’d like. The day is yours."

        jump NavigationDay1
        

    # Cothon ------------------------------------------------------------------
    label CothonDay1:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon, a rectangular artificial harbor on the Southwestern shore of the island."
        "The harbor is busy, with traders and fishermen transporting their wares in handcarts or waiting for their turns to navigate their boats through the channel that connects the harbor to the lagoon beyond."
        "You expertly navigate through the crowd, ignoring the hawkers and hangers on, until you reach your boat, a small wooden dinghy with oars and a small square sail."
        "You’re pretty sure you have some fishing supplies left, though you’ll need to remember to buy more when you’re next at The Market."

        "You currently have %(Fishing)d Fishing Supplies."
        "Would you like to go fishing?"
        menu:
            "Yes":
                if (Fishing >= 10):
                    $ Fishing -= 10
                    $ Money += 1000
                    "You clamber into your boat and take up the oars."
                    "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                    "For hours you cast your nets and let out your lines."
                    "You have good luck today! You manage to catch and sell 1000 shekels worth of fish using a total of 10 Fishing Supplies."
                    "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                else:
                    if (Fishing > 0):
                        $ profit = 50 * Fishing
                        $ Money += profit
                        "You clamber into your boat and take up the oars."
                        "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                        "For hours you cast your nets and let out your lines."
                        "Your luck is ok today. You manage to catch and sell %(profit)d shekels worth of fish using a total of %(Fishing)d Fishing Supplies."
                        $ Fishing = 0
                        "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                    else:
                        "You didn't bring any Fishing Supplies with you."
                        "You give it your best shot but, predictably, you don't catch anything."  
                        "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
            "No":
                "You decide not to go fishing today and do something else." 
        jump NavigationDay1
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay1:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter, the sprawling, slightly disorganized area at the center of the island where most of the city’s residents live."
        "About you is the hustle and bustle of daily life. In the streets are full of men pushing handcarts and children and dogs running about."
        "Neighbors lean out their windows to talk to each other and laundry hangs to dry on lines running between the apartment buildings."

        jump NavigationDay1

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay1:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu, the great three tiered temple that stands at the city’s heart."
        "Built from great blocks of stone, it’s materials had to be brought by boat to the island from quarries far inland."
        "Around you, priests, officials, and the city’s elite move about their tasks."
        "You feel somewhat out of place in your simple clothes, but everyone seems to be ignoring you."

        jump NavigationDay1

    # Market ------------------------------------------------------------------
    label MarketDay1:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way through the city’s narrow streets to The Market, a square where shops compete with vendors with carts or tents or sometimes just tables laid with their wares."
        "The sounds of vendor’s yelling, customers haggling, and animals being slaughtered fills the air."
        "You hold your purse a bit tighter in the crowd, hoping you have enough money to buy whatever it is your family needs for today."

        jump StoreDay1

    # Store ------------------------------------------------------------------
    label StoreDay1:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay1
            else:
                "You don't have enough money for food."
                jump StoreDay1
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay1
            else:
                "You don't have enough money for water."
                jump StoreDay1
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay1
            else:
                "You don't have enough money for wine."
                jump StoreDay1
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay1
            else:
                "You don't have enough money for medicine."
                jump StoreDay1
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay1
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay1
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay1

    # Causeway ------------------------------------------------------------------
    label CausewayDay1:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway, a semi-submerged road that connects the island’s northern shore to the mainland."
        "As usual, there isn’t much going on here. Most travel and transport to and from the city is done by boat."

        jump NavigationDay1

    # Tophet ------------------------------------------------------------------
    label TophetDay1:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay1

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay1:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        jump NavigationDay1

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay1:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
        
        "You head to The Artisan's Quarter, a section of the city towards the northern end of the island where the city’s craftspeople make their homes in apartments above their workshops."
        "This part of the city is alive with industry. Potters form small handled “Phoenician style” amphora from rough uncleaned clay and sculptures mold stone with chisels in the Greek style."
        "Chandlers weave rope and blacksmiths pound out nails for ships, and porters run to and fro, carrying orders or instructions that you don’t know enough about to follow."

        jump NavigationDay1

    # Barracks ------------------------------------------------------------------
    label BarracksDay1:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks the area that houses the city’s garrison."
        "The Barracks is actually made up of several buildings in the southernmost part of the city, near the Cothon, and you can see soldiers moving busily about the area on one errand or another."

        jump NavigationDay1
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay1:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay1
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay1
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay1
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay1
                else:
                    "You decide to head to the Market."
                    jump MarketDay1
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay1
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay1
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay1
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay1
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay1
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay1
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay1
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay1
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay1
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay1
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay1
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay1
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay1
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay1

    # Home ------------------------------------------------------------------
    label HomeDay1:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day2

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 2
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 10
    $ WaterPrice = 1
    $ WinePrice = 50
    $ MedicinePrice = 100
    $ FishingPrice = 25


    # Starting Scene  ------------------------------------------------------------------
    label Day2:
        scene home
        with dissolve

        "Day 2:"
        "You wake up in your home early in the morning"
        "You can now go anywhere and do anything you’d like. The day is yours."

        jump NavigationDay2
        

    # Cothon ------------------------------------------------------------------
    label CothonDay2:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon, a rectangular artificial harbor on the Southwestern shore of the island."
        "The harbor is busy, with traders and fishermen transporting their wares in handcarts or waiting for their turns to navigate their boats through the channel that connects the harbor to the sea."

        # Merchant Event
        "When you get to your boat you find that there is already someone there."
        "A man in well cut clothes made from fine material is looking over your boat with an appraising eye."
        "Noticing you as you approach he turns to you, and a huge smile covers his face, though you notice it doesn’t quite seem to reach his eyes."
        "“Hello my friend,” he booms. “Would you happen to be the owner of this fine boat?”"
        "You answer guardedly that you are and his smile widens."
        "“Splendid,” he says happily, “This is wonderful as I just so happen to want to buy your boat here, how does 3,000 shekels sound?”"
        "You look at him to see if he’s joking. 3,000 shekels is a lot of money, but this boat is your livelihood."
        "“So, my friend,” says the man who doesn’t seem to be joking, “what’ll it be?”"

        menu:
            "Reject his offer.":
                "The man smiles,"
                "“A poor choice my friend…”"
                "“But no matter. I don’t suppose you can’t be blamed for it.”"
                "“Good day!”"
                "And with that he turns on his heal and walks away, disappearing into the harbor crowds."
                "You shake your head and get back to work. You feel like this is going to be a weird day."

            "Accept his offer.":
                "The man smiles,"
                "“Excellent choice my friend! Between you and me, that boat probably wasn’t going to be of much use to you anyway.”"
                "Before you can ask him what he meant by this he shoves a bag of money into your arms."
                "It’s very heavy."
                "“Be sure to save it.” The man winks. “You never know when you’ll need a little something tucked away!”"
                "With that he bustles off, leaving a taciturn servant to prep the boat for what appears to be a journey of some length."
                "Turning away you shake your head. You feel like this is going to be a weird day."
                $ HasBoat = False
                $ Money += 3000

        if (HasBoat): 
            "You currently have %(Fishing)d Fishing Supplies."
            "Would you like to go fishing?"
            menu:
                "Yes":
                    if (Fishing >= 10):
                        $ Fishing -= 10
                        $ Money += 1000
                        "You clamber into your boat and take up the oars."
                        "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                        "For hours you cast your nets and let out your lines."
                        "You have good luck today! You manage to catch and sell 1000 shekels worth of fish using a total of 10 Fishing Supplies."
                        "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                    else:
                        if (Fishing > 0):
                            $ profit = 50 * Fishing
                            $ Money += profit
                            "You clamber into your boat and take up the oars."
                            "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                            "For hours you cast your nets and let out your lines."
                            "Your luck is ok today. You manage to catch and sell %(profit)d shekels worth of fish using a total of %(Fishing)d Fishing Supplies."
                            $ Fishing = 0
                            "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                        else:
                            "You didn't bring any Fishing Supplies with you."
                            "You give it your best shot but, predictably, you don't catch anything."  
                            "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                "No":
                    "You decide not to go fishing today and do something else." 
        else:
            "You don't have a boat and so you can't go fishing."

        jump NavigationDay2
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay2:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter, the sprawling, slightly disorganized area at the center of the island where most of the city’s residents live."
        "About you is the hustle and bustle of daily life. In the streets are full of men pushing handcarts and children and dogs running about."
        "Neighbors lean out their windows to talk to each other and laundry hangs to dry on lines running between the apartment buildings."

        jump NavigationDay2

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay2:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu, the great three tiered temple that stands at the city’s heart."
        "Built from great blocks of stone, it’s materials had to be brought by boat to the island from quarries far inland."
        "Around you, priests, officials, and the city’s elite move about their tasks."
        "You feel somewhat out of place in your simple clothes, but everyone seems to be ignoring you."


        jump NavigationDay2

    # Market ------------------------------------------------------------------
    label MarketDay2:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way through the city’s narrow streets to The Market, a square where shops compete with vendors with carts or tents or sometimes just tables laid with their wares."
        "The sounds of vendor’s yelling, customers haggling, and animals being slaughtered fills the air."

        jump StoreDay2

    # Store ------------------------------------------------------------------
    label StoreDay2:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay2
            else:
                "You don't have enough money for food."
                jump StoreDay2
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay2
            else:
                "You don't have enough money for water."
                jump StoreDay2
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay2
            else:
                "You don't have enough money for wine."
                jump StoreDay2
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay2
            else:
                "You don't have enough money for medicine."
                jump StoreDay2
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay2
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay2
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay2

    # Causeway ------------------------------------------------------------------
    label CausewayDay2:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway, a semi-submerged road that connects the island’s northern shore to the mainland."
        "As usual, there isn’t much going on here. Most travel and transport to and from the city is done by boat."

        jump NavigationDay2

    # Tophet ------------------------------------------------------------------
    label TophetDay2:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay2

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay2:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        jump NavigationDay2

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay2:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
        
        "You head to The Artisan's Quarter, a section of the city towards the northern end of the island where the city’s craftspeople make their homes in apartments above their workshops."
        "This part of the city is alive with industry. Potters form small handled “Phoenician style” amphora from rough uncleaned clay and sculptures mold stone with chisels in the Greek style."
        "Chandlers weave rope and blacksmiths pound out nails for ships, and porters run to and fro, carrying orders or instructions that you don’t know enough about to follow."

        jump NavigationDay2

    # Barracks ------------------------------------------------------------------
    label BarracksDay2:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks the area that houses the city’s garrison."
        "The Barracks is actually made up of several buildings in the southernmost part of the city, near the Cothon, and you can see soldiers moving busily about the area on one errand or another."

        jump NavigationDay2
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay2:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay2
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay2
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay2
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay2
                else:
                    "You decide to head to the Market."
                    jump MarketDay2
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay2
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay2
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay2
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay2
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay2
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay2
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay2
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay2
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay2
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay2
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay2
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay2
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay2
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay2

    # Home ------------------------------------------------------------------
    label HomeDay2:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day3


    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 3
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 12
    $ WaterPrice = 1
    $ WinePrice = 55
    $ MedicinePrice = 120
    $ FishingPrice = 30


    # Starting Scene  ------------------------------------------------------------------
    label Day3:
        scene home
        with dissolve

        "Day 3:"
        "You wake up in your home early in the morning"
        "You can now go anywhere and do anything you’d like. The day is yours."

        jump NavigationDay3
        

    # Cothon ------------------------------------------------------------------
    label CothonDay3:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon, a rectangular artificial harbor on the Southwestern shore of the island."
        "The harbor is busy, with traders and fishermen transporting their wares in handcarts or waiting for their turns to navigate their boats through the channel that connects the harbor to the sea."

        # Merchant Event 2
        "When you get to your boat you find that there is already a strange man in fine clothes standing in front of it. someone there."
        "“Ah, my friend.” The man says. “I wanted to buy your boat yesterday but, I’m afraid, that did not work out.”"
        "“Still, I’m willing to let bygones be bygones.”"
        "“Yesterday I would have paid you 3,000 shekels for your boat, today, I would pay 2,000, plus a little extra, a tip of sorts.”"
        "“Believe me, this is the best offer you’re likely to get in your life, so, what do you say?”"
        "You look at him. He’s now offering you less money for the boat that is still your livelihood! Is this man insane?"

        menu:
            "Reject his offer.":
                "The man smiles,"
                "“A poor choice my friend…”"
                "“You will suffer for it, I'm afraid, but such, I suppose, is the lot of mortals.”"
                "And with that he turns on his heal and walks away, disappearing into the harbor crowds."
                "You shake your head and get back to work. What was that about?"

            "Accept his offer.":
                "The man smiles,"
                "“Excellent choice my friend!”"
                "You look at him blankly, surprised by your answer as much as his ridiculous offer."
                "“Ah yes.” He says. “Your payment!”"
                "He shoves a bag of money into your arms and then leans down to your ear."
                "“Now for your tip.” he whispers."
                "His breath smells of olives and garum."
                "“Take this money, gather your family, if you have one, and get off this rock as fast as you can. Don’t tell anyone where you’re going. Don't take anything you don’t need.”"
                "“Just. Run.”"
                "He leans back, gives you one last toothy grin, and then bustles off without another word, leaving a taciturn servant to prep the boat for what appears to be a journey of some length."
                "You shake your head in bewilderment. What could he have meant by that?"
                $ HasBoat = False
                $ CanLeave = True
                $ Money += 2000

        if (HasBoat): 
            "You currently have %(Fishing)d Fishing Supplies."
            "Would you like to go fishing?"
            menu:
                "Yes":
                    if (Fishing >= 10):
                        $ Fishing -= 10
                        $ Money += 1000
                        "You clamber into your boat and take up the oars."
                        "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                        "For hours you cast your nets and let out your lines."
                        "You have good luck today! You manage to catch and sell 1000 shekels worth of fish using a total of 10 Fishing Supplies."
                        "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                    else:
                        if (Fishing > 0):
                            $ profit = 50 * Fishing
                            $ Money += profit
                            "You clamber into your boat and take up the oars."
                            "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                            "For hours you cast your nets and let out your lines."
                            "Your luck is ok today. You manage to catch and sell %(profit)d shekels worth of fish using a total of %(Fishing)d Fishing Supplies."
                            $ Fishing = 0
                            "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                        else:
                            "You didn't bring any Fishing Supplies with you."
                            "You give it your best shot but, predictably, you don't catch anything."  
                            "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                "No":
                    "You decide not to go fishing today and do something else." 
        else:
            "You don't have a boat and so you can't go fishing."

        jump NavigationDay3
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay3:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter, the sprawling, slightly disorganized area at the center of the island where most of the city’s residents live."
        "About you is the hustle and bustle of daily life. In the streets are full of men pushing handcarts and children and dogs running about."
        "Neighbors lean out their windows to talk to each other and laundry hangs to dry on lines running between the apartment buildings."

        jump NavigationDay3

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay3:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu, the great three tiered temple that stands at the city’s heart."
        "Built from great blocks of stone, it’s materials had to be brought by boat to the island from quarries far inland."
        "Around you, priests, officials, and the city’s elite move about their tasks."
        "You feel somewhat out of place in your simple clothes, but everyone seems to be ignoring you."

        # Cap event 1

        "You notice that some of the people around you seem more nervous for some reason."
        "The chatter less lively and the couriers more determined."
        "You can’t put your finger on it, but the city’s elite seem to know something that you don’t."


        jump NavigationDay3

    # Market ------------------------------------------------------------------
    label MarketDay3:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way through the city’s narrow streets to The Market, a square where shops compete with vendors with carts or tents or sometimes just tables laid with their wares."
        "The sounds of vendor’s yelling, customers haggling, and animals being slaughtered fills the air."

        jump StoreDay3

    # Store ------------------------------------------------------------------
    label StoreDay3:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay3
            else:
                "You don't have enough money for food."
                jump StoreDay3
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay3
            else:
                "You don't have enough money for water."
                jump StoreDay3
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay3
            else:
                "You don't have enough money for wine."
                jump StoreDay3
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay3
            else:
                "You don't have enough money for medicine."
                jump StoreDay3
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay3
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay3
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay3

    # Causeway ------------------------------------------------------------------
    label CausewayDay3:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway, a semi-submerged road that connects the island’s northern shore to the mainland."
        "As usual, there isn’t much going on here. Most travel and transport to and from the city is done by boat."

        # Leave Event
        if CanLeave:
            "You can’t help but remember the words of the strange man who bought your boat."
            "“Get off this rock.” “Just. Run.”"
            "Your whole life is here, your friends, your family, your livelihood. Surely you couldn’t just leave on the advice of some strange old man…"
            menu:
                "Leave Motya.":
                    "Despite any and all logic, you can’t help but believe him, and follow his instructions."
                    "For the rest of the day you gather supplies, purchase transportation, and gather your family."
                    "Your partner and children are shocked and upset, but somehow, you convince them to come with you."
                    "You leave Motya on a pleasant afternoon, crossing the semi-submerged causeway and into the Sicilian countryside."
                    "Despite the insanity of your decision, you can’t help but feel like you were somehow right to make it, as though you were able, somehow, to avoid some terrible fate, a great calamity which you had been destined to experience."
                    "You feel this way right up until you run into a Syricusian army that had been marching through Sicily to attack Motya."
                    "Your family captured and sold into slavery."
                    "You aren’t so lucky. You are killed by a Greek soldier as you try to escape."
                    "Bad End"
                    return
                "Don't leave Motya.":
                    "Yeah, that would have been really stupid."

        jump NavigationDay3

    # Tophet ------------------------------------------------------------------
    label TophetDay3:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay3

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay3:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        jump NavigationDay3

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay3:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
        
        "You head to The Artisan's Quarter, a section of the city towards the northern end of the island where the city’s craftspeople make their homes in apartments above their workshops."
        "This part of the city is alive with industry. Potters form small handled “Phoenician style” amphora from rough uncleaned clay and sculptures mold stone with chisels in the Greek style."
        "Chandlers weave rope and blacksmiths pound out nails for ships, and porters run to and fro, carrying orders or instructions that you don’t know enough about to follow."

        jump NavigationDay3

    # Barracks ------------------------------------------------------------------
    label BarracksDay3:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks the area that houses the city’s garrison."
        "The Barracks is actually made up of several buildings in the southernmost part of the city, near the Cothon, and you can see soldiers moving busily about the area on one errand or another."

        jump NavigationDay3
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay3:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay3
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay3
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay3
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay3
                else:
                    "You decide to head to the Market."
                    jump MarketDay3
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay3
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay3
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay3
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay3
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay3
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay3
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay3
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay3
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay3
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay3
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay3
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay3
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay3
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay3

    # Home ------------------------------------------------------------------
    label HomeDay3:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day4


    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 4
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 15
    $ WaterPrice = 2
    $ WinePrice = 60
    $ MedicinePrice = 130
    $ FishingPrice = 30


    # Starting Scene  ------------------------------------------------------------------
    label Day4:
        scene home
        with dissolve

        "Day 4:"
        "You wake up in your home early in the morning"
        "You can now go anywhere and do anything you’d like. The day is yours."

        jump NavigationDay4
        
    # Cothon ------------------------------------------------------------------
    label CothonDay4:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon, a rectangular artificial harbor on the Southwestern shore of the island."
        "The harbor is busy, with traders and fishermen transporting their wares in handcarts or waiting for their turns to navigate their boats through the channel that connects the harbor to the sea."

        if (HasBoat): 
            "You currently have %(Fishing)d Fishing Supplies."
            "Would you like to go fishing?"
            menu:
                "Yes":
                    if (Fishing >= 10):
                        $ Fishing -= 10
                        $ Money += 1000
                        "You clamber into your boat and take up the oars."
                        "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                        "For hours you cast your nets and let out your lines."
                        "You have good luck today! You manage to catch and sell 1000 shekels worth of fish using a total of 10 Fishing Supplies."
                        "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                    else:
                        if (Fishing > 0):
                            $ profit = 50 * Fishing
                            $ Money += profit
                            "You clamber into your boat and take up the oars."
                            "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                            "For hours you cast your nets and let out your lines."
                            "Your luck is ok today. You manage to catch and sell %(profit)d shekels worth of fish using a total of %(Fishing)d Fishing Supplies."
                            $ Fishing = 0
                            "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                        else:
                            "You didn't bring any Fishing Supplies with you."
                            "You give it your best shot but, predictably, you don't catch anything."  
                            "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                "No":
                    "You decide not to go fishing today and do something else." 
        else:
            "You don't have a boat and so you can't go fishing."

        jump NavigationDay4
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay4:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter, the sprawling, slightly disorganized area at the center of the island where most of the city’s residents live."
        "About you is the hustle and bustle of daily life. In the streets are full of men pushing handcarts and children and dogs running about."
        "Neighbors lean out their windows to talk to each other and laundry hangs to dry on lines running between the apartment buildings."

        # Res Event 1
        "The people here seem worried."
        "They say an army is approaching the city."
        "No one’s sure exactly who, but the going theory is that Dionysius, tyrant of Syracuse is it’s leader, or perhaps one of his subordinates."
        "He recently laid siege to Segesta, though that city doesn’t seem to have fallen."
        "You aren’t sure how much credence to give these rumors, but they make you worry."
        "Why they would invest your city when so many cities inland haven’t fallen is anyone’s guess."

        jump NavigationDay4

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay4:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu, the great three tiered temple that stands at the city’s heart."
        "Built from great blocks of stone, it’s materials had to be brought by boat to the island from quarries far inland."
        "Around you, priests, officials, and the city’s elite move about their tasks."
        "You feel somewhat out of place in your simple clothes, but everyone seems to be ignoring you."

        # Cap event 2

        "The people in the city’s richest quarter are abuzz with the news of the war."
        "A Greek army has been spotted marching up the coast, presumably with the intention of attacking Motya."
        "Why they would invest your city when so many cities inland haven’t fallen is anyone’s guess."
        "How strong the Greek army is, how far away it is, and whether or not it constitutes a real threat is, apparently, something of an open question."
        "Word has been sent to Carthage for reinforcements, but no one knows when or even if these will come."

        jump NavigationDay4

    # Market ------------------------------------------------------------------
    label MarketDay4:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way through the city’s narrow streets to The Market, a square where shops compete with vendors with carts or tents or sometimes just tables laid with their wares."
        "The sounds of vendor’s yelling, customers haggling, and animals being slaughtered fills the air."

        jump StoreDay4

    # Store ------------------------------------------------------------------
    label StoreDay4:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay4
            else:
                "You don't have enough money for food."
                jump StoreDay4
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay4
            else:
                "You don't have enough money for water."
                jump StoreDay4
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay4
            else:
                "You don't have enough money for wine."
                jump StoreDay4
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay4
            else:
                "You don't have enough money for medicine."
                jump StoreDay4
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay4
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay4
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay4

    # Causeway ------------------------------------------------------------------
    label CausewayDay4:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway, a semi-submerged road that connects the island’s northern shore to the mainland."
        "As usual, there isn’t much going on here. Most travel and transport to and from the city is done by boat."

        # Leave Event
        if CanLeave:
            "You can’t help but remember the words of the strange man who bought your boat."
            "“Get off this rock.” “Just. Run.”"
            "Your whole life is here, your friends, your family, your livelihood. Surely you couldn’t just leave on the advice of some strange old man…"
            menu:
                "Leave Motya.":
                    "Despite any and all logic, you can’t help but believe him, and follow his instructions."
                    "For the rest of the day you gather supplies, purchase transportation, and gather your family."
                    "Your partner and children are shocked and upset, but somehow, you convince them to come with you."
                    "You leave Motya on a pleasant afternoon, crossing the semi-submerged causeway and into the Sicilian countryside."
                    "Despite the insanity of your decision, you can’t help but feel like you were somehow right to make it, as though you were able, somehow, to avoid some terrible fate, a great calamity which you had been destined to experience."
                    "You feel this way right up until you run into a Syricusian army that had been marching through Sicily to attack Motya."
                    "Your family captured and sold into slavery."
                    "You aren’t so lucky. You are killed by a Greek soldier as you try to escape."
                    "Bad End"
                    return
                "Don't leave Motya.":
                    "Yeah, that would have been really stupid."

        jump NavigationDay4

    # Tophet ------------------------------------------------------------------
    label TophetDay4:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay4

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay4:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        jump NavigationDay4

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay4:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
        
        "You head to The Artisan's Quarter, a section of the city towards the northern end of the island where the city’s craftspeople make their homes in apartments above their workshops."
        "While many of the city’s craftspeople are engaged with their usual work, you notice a few seem to be making what appear to be weapons."
        "… odd."

        jump NavigationDay4

    # Barracks ------------------------------------------------------------------
    label BarracksDay4:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks the area that houses the city’s garrison."
        "The Barracks is actually made up of several buildings in the southernmost part of the city, near the Cothon, and you can see soldiers moving busily about the area on one errand or another."

        # Barracks Event
        "The men of the city’s guard seem to have been thrown into a frenzy of activity. Sharpening weapons, fixing armor, storing arrows and sling bullets along the city walls." 
        "Though you aren’t allowed to approach the area openly (which is odd), you can tell that something is definitely going on."
        "Or at least, these people think so."

        jump NavigationDay4
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay4:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay4
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay4
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay4
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay4
                else:
                    "You decide to head to the Market."
                    jump MarketDay4
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay4
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay4
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay4
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay4
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay4
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay4
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay4
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay4
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay4
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay4
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay4
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay4
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay4
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay4

    # Home ------------------------------------------------------------------
    label HomeDay4:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day5    
    
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 5
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 20
    $ WaterPrice = 3
    $ WinePrice = 80
    $ MedicinePrice = 150
    $ FishingPrice = 10


    # Starting Scene  ------------------------------------------------------------------
    label Day5:
        scene home
        with dissolve

        "Day 5:"
        "You wake up in your home early in the morning"
        "You can now go anywhere and do anything you’d like. The day is yours."

        jump NavigationDay5
        
    # Cothon ------------------------------------------------------------------
    label CothonDay5:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon, a rectangular artificial harbor on the Southwestern shore of the island."
        "The harbor is busy, with traders and fishermen transporting their wares in handcarts or waiting for their turns to navigate their boats through the channel that connects the harbor to the sea."

        if (HasBoat): 
            "You currently have %(Fishing)d Fishing Supplies."
            "Would you like to go fishing?"
            menu:
                "Yes":
                    if (Fishing >= 10):
                        $ Fishing -= 10
                        $ Money += 1000
                        "You clamber into your boat and take up the oars."
                        "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                        "For hours you cast your nets and let out your lines."
                        "You have good luck today! You manage to catch and sell 1000 shekels worth of fish using a total of 10 Fishing Supplies."
                        "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                    else:
                        if (Fishing > 0):
                            $ profit = 50 * Fishing
                            $ Money += profit
                            "You clamber into your boat and take up the oars."
                            "With a master's skill you guide your little dingy out of the Cothon and into the sea, setting course for your favorite fishing spot."
                            "For hours you cast your nets and let out your lines."
                            "Your luck is ok today. You manage to catch and sell %(profit)d shekels worth of fish using a total of %(Fishing)d Fishing Supplies."
                            $ Fishing = 0
                            "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                        else:
                            "You didn't bring any Fishing Supplies with you."
                            "You give it your best shot but, predictably, you don't catch anything."  
                            "You now have %(Money)d shekels and %(Fishing)d Fishing Supplies."
                "No":
                    "You decide not to go fishing today and do something else." 
        else:
            "You don't have a boat and so you can't go fishing."

        jump NavigationDay5
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay5:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter, the sprawling, slightly disorganized area at the center of the island where most of the city’s residents live."
        "About you is the hustle and bustle of daily life. In the streets are full of men pushing handcarts and children and dogs running about."
        "Neighbors lean out their windows to talk to each other and laundry hangs to dry on lines running between the apartment buildings."

        # Res Event 1
        "The people here seem worried."
        "They say an army is approaching the city."
        "No one’s sure exactly who, but the going theory is that Dionysius, tyrant of Syracuse is it’s leader, or perhaps one of his subordinates."
        "He recently laid siege to Segesta, though that city doesn’t seem to have fallen."
        "You aren’t sure how much credence to give these rumors, but they make you worry."
        "Why they would invest your city when so many cities inland haven’t fallen is anyone’s guess."

        jump NavigationDay5

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay5:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu, the great three tiered temple that stands at the city’s heart."
        "Built from great blocks of stone, it’s materials had to be brought by boat to the island from quarries far inland."
        "Around you, priests, officials, and the city’s elite move about their tasks."
        "You feel somewhat out of place in your simple clothes, but everyone seems to be ignoring you."

        # Cap event 2

        "The people in the city’s richest quarter are abuzz with the news of the war."
        "A Greek army has been spotted marching up the coast, presumably with the intention of attacking Motya."
        "Why they would invest your city when so many cities inland haven’t fallen is anyone’s guess."
        "How strong the Greek army is, how far away it is, and whether or not it constitutes a real threat is, apparently, something of an open question."
        "Word has been sent to Carthage for reinforcements, but no one knows when or even if these will come."

        jump NavigationDay5

    # Market ------------------------------------------------------------------
    label MarketDay5:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way through the city’s narrow streets to The Market, a square where shops compete with vendors with carts or tents or sometimes just tables laid with their wares."
        "The sounds of vendor’s yelling, customers haggling, and animals being slaughtered fills the air."

        jump StoreDay5

    # Store ------------------------------------------------------------------
    label StoreDay5:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay5
            else:
                "You don't have enough money for food."
                jump StoreDay5
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay5
            else:
                "You don't have enough money for water."
                jump StoreDay5
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay5
            else:
                "You don't have enough money for wine."
                jump StoreDay5
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay5
            else:
                "You don't have enough money for medicine."
                jump StoreDay5
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay5
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay5
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay5

    # Causeway ------------------------------------------------------------------
    label CausewayDay5:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "About half way along the causeway’s length, you see engineers knocking out the road, disconnecting the island from the mainland."
        "Soon, there will be now way for anyone to get into or out of Motya by land."
        "You aren’t sure whether your comforted or scared by this."

        jump NavigationDay5

    # Tophet ------------------------------------------------------------------
    label TophetDay5:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay5

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay5:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        jump NavigationDay5

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay5:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
        
        "You head to The Artisan's Quarter, a section of the city towards the northern end of the island where the city’s craftspeople make their homes in apartments above their workshops."
        "While many of the city’s craftspeople are engaged with their usual work, you notice a few seem to be making what appear to be weapons."
        "… odd."

        jump NavigationDay5

    # Barracks ------------------------------------------------------------------
    label BarracksDay5:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."


        jump NavigationDay5
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay5:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay5
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay5
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay5
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay5
                else:
                    "You decide to head to the Market."
                    jump MarketDay5
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay5
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay5
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay5
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay5
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay5
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay5
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay5
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay5
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay5
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay5
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay5
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay5
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay5
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay5

    # Home ------------------------------------------------------------------
    label HomeDay5:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day6
    
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 6
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 25
    $ WaterPrice = 5
    $ WinePrice = 100
    $ MedicinePrice = 180
    $ FishingPrice = 1



    # Starting Scene  ------------------------------------------------------------------
    label Day6:
        scene home
        with dissolve

        "In the night, a Greek army besieges the city"

        jump Day6Intro

    label Day6Intro:
        scene home
        with dissolve

        "Day 6:"
        "You wake up in your home early in the morning."
        "A strange dread fills the air."

        jump NavigationDay6
        
    # Cothon ------------------------------------------------------------------
    label CothonDay6:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay6
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay6:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s quieter here than usual, people don’t seem to be hanging out outside as much."
        "In the street, there are a few people begging, probably put out of work by the siege."

        jump NavigationDay6

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay6:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu."
        "The city’s elite seem to have flown into a panic."
        "Soldiers and couriers rush about, delivering messages and orders who knows where and in the corners, men in fine clothes talk urgently in low tones."


        jump NavigationDay6

    # Market ------------------------------------------------------------------
    label MarketDay6:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "It’s quieter than usual. Fewer vendors line the streets and the grumbling of customers is more serious." 
        "Times are tight, prices are rising, and here in The Market, the strain is beginning to show."

        jump StoreDay6

    # Store ------------------------------------------------------------------
    label StoreDay6:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay6
            else:
                "You don't have enough money for food."
                jump StoreDay6
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay6
            else:
                "You don't have enough money for water."
                jump StoreDay6
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay6
            else:
                "You don't have enough money for wine."
                jump StoreDay6
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay6
            else:
                "You don't have enough money for medicine."
                jump StoreDay6
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay6
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay6
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay6

    # Causeway ------------------------------------------------------------------
    label CausewayDay6:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "The causeway has been all but destroyed, making it entirely impassible."
        "On the far shore, you see the fires, tents, and ships of the army of Syracuse and her allies."
        "As things stand now they won’t be getting into the city over the causeway, but perhaps they don't have to."

        jump NavigationDay6

    # Tophet ------------------------------------------------------------------
    label TophetDay6:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay6

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay6:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        jump NavigationDay6

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay6:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "The section seems to have been given over entirely to the production of weapons."
        "Blacksmiths pound out spear and arrowheads, woodworkers make shields, spear and arrow shafts, and tanners cut stinking strips of cured hides into armor."
        "Around the edges, loiterers seem to be watching them, hoping to find work in the city’s new arms industry."

        if (len(visited) == 1):
            "As you stand, idly watching the weapon makers at their work, a man yells to you."
            "“Hey, you lookin for work?”"
            "The man in question is large, strong, and clearly a blacksmith."
            "Soot coats his face and apron."
            "“I need someone to work the bellows. It’s hard work, but you seem up to it, and it’s what needs to be done to defend the city.”"
            "“Plus, I’ll pay you 100 shekels for your time.”"
            "“Keep in mind though, if you do accept my offer I’ll need you until the end of the afternoon. You’ll only have the evening to yourself.”"
            "“So if you have more than one other thing you’d like to do today, this might not be for you.”"
            "“So do we have a deal?”"
            "You take a moment to mull his offer over."
            menu:
                "Accept his offer.":
                    "“Wonderful!” Says the man."
                    "“What with all these orders for weapons everyone here’s short handed.”"
                    "“If you’re ever in need of work, come here in the morning. As long as the siege is on I’m sure someone will need something done.”"
                    "“Now to work!”"
                    "What follows is hours of the most back breakingly difficult work you’ve ever experienced."
                    "You’re used to fishing on the open sea. You aren't a stranger to hard work."
                    "However, the boring, repetitive, and difficult task of working the blacksmith’s bellows for hours on end is something else entirely."
                    "As the sun begins to set and the day begins to end, you are given your money and sent on your way."
                    "You’re barely able to stand from exhaustion."
                    $ money += 100
                    $ visited.append("Trans Rights!")
                "Reject his offer.":
                    "The man shrugs."
                    "“Suit yourself, but work’s hard to come by these days.”"
                    "“If you ever change your mind come round here in the morning, I’m sure you’d find something.”"
                    "The man turns and walks away and you continue on your way."
                    "You’re desperate, but not that desperate."

        else:
            "You notice that the number of people here is significantly higher than usual."
            "Untrained hands have been pressed into doing the hard, repetitive, labor that comes with so much activity."
            "You notice some people you recognize as former fishermen working a blacksmith’s bellows."
            "It seems that there is still work to be found in this city, though you’ll likely have to be a bit earlier to get it." 

        jump NavigationDay6

    # Barracks ------------------------------------------------------------------
    label BarracksDay6:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay6
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay6:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay6
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay6
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay6
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay6
                else:
                    "You decide to head to the Market."
                    jump MarketDay6
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay6
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay6
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay6
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay6
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay6
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay6
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay6
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay6
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay6
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay6
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay6
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay6
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay6
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay6

    # Home ------------------------------------------------------------------
    label HomeDay6:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day7
    
        # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 7
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 30
    $ WaterPrice = 8
    $ WinePrice = 100
    $ MedicinePrice = 180
    $ FishingPrice = 1


    # Starting Scene  ------------------------------------------------------------------
    label Day7:
        scene home
        with dissolve

        "Day 7:"
        "You wake up in your home early in the morning."
        "A strange dread fills the air."

        jump NavigationDay7
        
    # Cothon ------------------------------------------------------------------
    label CothonDay7:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay7
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay7:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s quieter here than usual, people don’t seem to be hanging out outside as much."
        "In the street, there are a few people begging, probably put out of work by the siege."

        # Resi riot event
        "The residences, always the site of conversation and gossip, seem more active even than usual."
        "People are grumbling about high prices in the market, merchants hoarding food and supplies, and raising prices to squeeze the most out of them in this time of hardship."
        "As you watch, the rumblings take on more focus."
        "Leaders come to the fore, suggesting that they go to the market tomorrow and demand to be sold food at a reasonable price."
        "They don’t want to steal from the merchants. However, with the price of food more than double what it was a week ago, they have to do something."
        "You listen, and then continue on your way."
        "Something will come of this, though whether you’re excited or worried only you know."
        "What is sure, is that something will happen at the market tomorrow."
        "Exactly what is anyone’s guess."

        jump NavigationDay7

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay7:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu."
        "The city’s elite seem to have flown into a panic."
        "Soldiers and couriers rush about, delivering messages and orders who knows where and in the corners, men in fine clothes talk urgently in low tones."


        jump NavigationDay7

    # Market ------------------------------------------------------------------
    label MarketDay7:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "It’s quieter than usual. Fewer vendors line the streets and the grumbling of customers is more serious." 
        "Times are tight, prices are rising, and here in The Market, the strain is beginning to show."

        jump StoreDay7

    # Store ------------------------------------------------------------------
    label StoreDay7:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay7
            else:
                "You don't have enough money for food."
                jump StoreDay7
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay7
            else:
                "You don't have enough money for water."
                jump StoreDay7
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay7
            else:
                "You don't have enough money for wine."
                jump StoreDay7
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay7
            else:
                "You don't have enough money for medicine."
                jump StoreDay7
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay7
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay7
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay7

    # Causeway ------------------------------------------------------------------
    label CausewayDay7:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "The causeway has been all but destroyed, making it entirely impassible."
        "On the far shore, you see the fires, tents, and ships of the army of Syracuse and her allies."
        "As things stand now they won’t be getting into the city over the causeway, but perhaps they don't have to."

        jump NavigationDay7

    # Tophet ------------------------------------------------------------------
    label TophetDay7:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay7

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay7:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        jump NavigationDay7

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay7:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "The section seems to have been given over entirely to the production of weapons."
        "Blacksmiths pound out spear and arrowheads, woodworkers make shields, spear and arrow shafts, and tanners cut stinking strips of cured hides into armor."
        "Around the edges, loiterers seem to be watching them, hoping to find work in the city’s new arms industry."

        if (len(visited) == 1):
            "As you stand, idly watching the weapon makers at their work, a man yells to you."
            "“Hey, you lookin for work?”"
            "The man in question is large, strong, and clearly a blacksmith."
            "Soot coats his face and apron."
            "“I need someone to work the bellows. It’s hard work, but you seem up to it, and it’s what needs to be done to defend the city.”"
            "“Plus, I’ll pay you 100 shekels for your time.”"
            "“Keep in mind though, if you do accept my offer I’ll need you until the end of the afternoon. You’ll only have the evening to yourself.”"
            "“So if you have more than one other thing you’d like to do today, this might not be for you.”"
            "“So do we have a deal?”"
            "You take a moment to mull his offer over."
            menu:
                "Accept his offer.":
                    "“Wonderful!” Says the man."
                    "“What with all these orders for weapons everyone here’s short handed.”"
                    "“If you’re ever in need of work, come here in the morning. As long as the siege is on I’m sure someone will need something done.”"
                    "“Now to work!”"
                    "What follows is hours of the most back breakingly difficult work you’ve ever experienced."
                    "You’re used to fishing on the open sea. You aren't a stranger to hard work."
                    "However, the boring, repetitive, and difficult task of working the blacksmith’s bellows for hours on end is something else entirely."
                    "As the sun begins to set and the day begins to end, you are given your money and sent on your way."
                    "You’re barely able to stand from exhaustion."
                    $ money += 100
                    $ visited.appen("Trans Rights!")
                "Reject his offer.":
                    "The man shrugs."
                    "“Suit yourself, but work’s hard to come by these days.”"
                    "“If you ever change your mind come round here in the morning, I’m sure you’d find something.”"
                    "The man turns and walks away and you continue on your way."
                    "You’re desperate, but not that desperate."

        else:
            "You notice that the number of people here is significantly higher than usual."
            "Untrained hands have been pressed into doing the hard, repetitive, labor that comes with so much activity."
            "You notice some people you recognize as former fishermen working a blacksmith’s bellows."
            "It seems that there is still work to be found in this city, though you’ll likely have to be a bit earlier to get it." 

        jump NavigationDay7

    # Barracks ------------------------------------------------------------------
    label BarracksDay7:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay7
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay7:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay7
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay7
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay7
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay7
                else:
                    "You decide to head to the Market."
                    jump MarketDay7
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay7
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay7
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay7
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay7
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay7
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay7
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay7
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay7
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay7
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay7
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay7
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay7
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay7
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay7

    # Home ------------------------------------------------------------------
    label HomeDay7:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day8
    
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 8
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # # Update Store Prices
    # $ FoodPrice = 30
    # $ WaterPrice = 8
    # $ WinePrice = 100
    # $ MedicinePrice = 180
    # $ FishingPrice = 1


    # Starting Scene  ------------------------------------------------------------------
    label Day8:
        scene home
        with dissolve

        "Day 8:"
        "You wake up in your home early in the morning."
        "A strange dread fills the air."

        jump NavigationDay8
        
    # Cothon ------------------------------------------------------------------
    label CothonDay8:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay8
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay8:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s quieter here than usual, people don’t seem to be hanging out outside as much."
        "In the street, there are a few people begging, probably put out of work by the siege."

        jump NavigationDay8

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay8:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu."
        "The city’s elite seem to have flown into a panic."
        "Soldiers and couriers rush about, delivering messages and orders who knows where and in the corners, men in fine clothes talk urgently in low tones."


        jump NavigationDay8

    # Market ------------------------------------------------------------------
    label MarketDay8:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "It’s quieter than usual. Fewer vendors line the streets and the grumbling of customers is more serious." 
        "Times are tight, prices are rising, and here in The Market, the strain is beginning to show."

        #Price Riot 1
        "When you arrive at the market it’s clear that something big has just taken place."
        "Tents and stalls have been trampled into the ground, tables of wares overturned, amphorae broken, their contents strewn about the streets."
        "However, what catches our eye immediately is the blood."
        "The ground around the center of the market is stained red with it."
        "You notice several soldiers dragging the corpse of an old man into a side street, an arrow stuck in his chest."
        "There are a lot of soldiers around actually, cleaning up after what appears to have been a fairly major riot."
        "Neither the rioters nor the merchants seem to have come out of this very well."
        "You notice that, amongst the carnage, there is still food and wine and medicine."
        "There are soldiers all around, but they all seem occupied."
        "You could try to grab some for yourself, but it would be dangerous, and a crime."
        "You take a moment to think about what you’ll do."

        menu: 
            "Try and take some stuff.":
                "You furtively edge over to an overturned table and, when you’re sure no one’s looking, scoop up as much as you can carry and run."
                "You hear shouts coming after you in the distance, but you zig-zag through the city’s streets until you’re sure you’re no longer being pursued."
                "You’ve just stolen a lot of stuff from someone, though times were desperate, and whether or not you feel guilty only you know."
                "You look over your haul."
                "You gained (x2) Medicine, (x3) Wine), (x3) Food!"
                $ Food += 3
                $ Wine += 3
                $ Medicine += 3

            "Dont Risk it.":
                "You decide not to risk it." 
                "The soldiers, on edge from violently suppressing a riot, would be unlikely to miss your theft, or do anything short of killing you when the noticed."

        jump NavigationDay8
        
        # jump StoreDay8

    # Store ------------------------------------------------------------------
    label StoreDay8:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay8
            else:
                "You don't have enough money for food."
                jump StoreDay8
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay8
            else:
                "You don't have enough money for water."
                jump StoreDay8
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay8
            else:
                "You don't have enough money for wine."
                jump StoreDay8
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay8
            else:
                "You don't have enough money for medicine."
                jump StoreDay8
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay8
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay8
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay8

    # Causeway ------------------------------------------------------------------
    label CausewayDay8:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "The causeway has been all but destroyed, making it entirely impassible."
        "On the far shore, you see the fires, tents, and ships of the army of Syracuse and her allies."
        "As things stand now they won’t be getting into the city over the causeway, but perhaps they don't have to."

        jump NavigationDay8

    # Tophet ------------------------------------------------------------------
    label TophetDay8:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay8

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay8:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        jump NavigationDay8

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay8:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "The section seems to have been given over entirely to the production of weapons."
        "Blacksmiths pound out spear and arrowheads, woodworkers make shields, spear and arrow shafts, and tanners cut stinking strips of cured hides into armor."
        "Around the edges, loiterers seem to be watching them, hoping to find work in the city’s new arms industry."

        if (len(visited) == 1):
            "As you stand, idly watching the weapon makers at their work, a man yells to you."
            "“Hey, you lookin for work?”"
            "The man in question is large, strong, and clearly a blacksmith."
            "Soot coats his face and apron."
            "“I need someone to work the bellows. It’s hard work, but you seem up to it, and it’s what needs to be done to defend the city.”"
            "“Plus, I’ll pay you 100 shekels for your time.”"
            "“Keep in mind though, if you do accept my offer I’ll need you until the end of the afternoon. You’ll only have the evening to yourself.”"
            "“So if you have more than one other thing you’d like to do today, this might not be for you.”"
            "“So do we have a deal?”"
            "You take a moment to mull his offer over."
            menu:
                "Accept his offer.":
                    "“Wonderful!” Says the man."
                    "“What with all these orders for weapons everyone here’s short handed.”"
                    "“If you’re ever in need of work, come here in the morning. As long as the siege is on I’m sure someone will need something done.”"
                    "“Now to work!”"
                    "What follows is hours of the most back breakingly difficult work you’ve ever experienced."
                    "You’re used to fishing on the open sea. You aren't a stranger to hard work."
                    "However, the boring, repetitive, and difficult task of working the blacksmith’s bellows for hours on end is something else entirely."
                    "As the sun begins to set and the day begins to end, you are given your money and sent on your way."
                    "You’re barely able to stand from exhaustion."
                    $ money += 100
                    $ visited.append("Trans Rights!")
                "Reject his offer.":
                    "The man shrugs."
                    "“Suit yourself, but work’s hard to come by these days.”"
                    "“If you ever change your mind come round here in the morning, I’m sure you’d find something.”"
                    "The man turns and walks away and you continue on your way."
                    "You’re desperate, but not that desperate."

        else:
            "You notice that the number of people here is significantly higher than usual."
            "Untrained hands have been pressed into doing the hard, repetitive, labor that comes with so much activity."
            "You notice some people you recognize as former fishermen working a blacksmith’s bellows."
            "It seems that there is still work to be found in this city, though you’ll likely have to be a bit earlier to get it." 

        jump NavigationDay8

    # Barracks ------------------------------------------------------------------
    label BarracksDay8:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay8
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay8:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay8
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay8
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay8
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay8
                else:
                    "You decide to head to the Market."
                    jump MarketDay8
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay8
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay8
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay8
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay8
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay8
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay8
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay8
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay8
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay8
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay8
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay8
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay8
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay8
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay8

    # Home ------------------------------------------------------------------
    label HomeDay8:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day9

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 9
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 15
    $ WaterPrice = 2
    $ WinePrice = 80
    $ MedicinePrice = 120
    $ FishingPrice = 15


    # Starting Scene  ------------------------------------------------------------------
    label Day9:
        scene home
        with dissolve

        "Day 9:"
        "You wake up in your home early in the morning."
        "A strange dread fills the air."

        jump NavigationDay9
        
    # Cothon ------------------------------------------------------------------
    label CothonDay9:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay9
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay9:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s quieter here than usual, people don’t seem to be hanging out outside as much."
        "In the street, there are a few people begging, probably put out of work by the siege."

        jump NavigationDay9

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay9:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu."
        "The city’s elite seem to have flown into a panic."
        "Soldiers and couriers rush about, delivering messages and orders who knows where and in the corners, men in fine clothes talk urgently in low tones."


        jump NavigationDay9

    # Market ------------------------------------------------------------------
    label MarketDay9:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "It’s quieter than usual. Fewer vendors line the streets and the grumbling of customers is more serious." 
        "Times are tight, prices are rising, and here in The Market, the strain is beginning to show."
        "Yesterday's riot clearly had some effect..."
        
        jump StoreDay9

    # Store ------------------------------------------------------------------
    label StoreDay9:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay9
            else:
                "You don't have enough money for food."
                jump StoreDay9
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay9
            else:
                "You don't have enough money for water."
                jump StoreDay9
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay9
            else:
                "You don't have enough money for wine."
                jump StoreDay9
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay9
            else:
                "You don't have enough money for medicine."
                jump StoreDay9
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay9
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay9
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay9

    # Causeway ------------------------------------------------------------------
    label CausewayDay9:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "The causeway has been all but destroyed, making it entirely impassible."
        "On the far shore, you see the fires, tents, and ships of the army of Syracuse and her allies."
        "As things stand now they won’t be getting into the city over the causeway, but perhaps they don't have to."

        jump NavigationDay9

    # Tophet ------------------------------------------------------------------
    label TophetDay9:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay9

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay9:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        # "You take a moment to reflect..."

        # Necropolis event 1
        "There are more people here than usual, and soon you see why."
        "The battered bodies of about two dozen people are being buried in rock-cut tombs."
        "The families of the dead, almost all lower class and seemingly on the brink of starvation, stand in quiet clusters, shivering in the warmth of the Mediterranean sun." 

        jump NavigationDay9

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay9:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "The section seems to have been given over entirely to the production of weapons."
        "Blacksmiths pound out spear and arrowheads, woodworkers make shields, spear and arrow shafts, and tanners cut stinking strips of cured hides into armor."
        "Around the edges, loiterers seem to be watching them, hoping to find work in the city’s new arms industry."

        if (len(visited) == 1):
            "It’s quite early in the morning, but there are already a lot of people passing through this area."
            "Many are artisans of course, but there are also a lot of people who look to be out of work and looking for odd jobs to do."
            "You look around a bit until you come across a tanner, who seems to be willing to hire you, in a manner of speaking."
            "“I can’t pay you money.” he says."
            "“Don’t have it and even if I did, I doubt it would be worth it, what with prices and the riots and all.”"
            "“However, if I find your work satisfactory, I can give you three portions of food and three portions of water.”"
            "“That seems more than fair to me, and if you don't’ take it I’m sure someone else will.”"
            "He gestures around, to where you see at least two people listening in on your conversation. You can see the hunger in their eyes."
            "“So do we have a deal?” the tanner asks."
            "You take a moment to mull his offer over."
            menu:
                "Accept his offer.":
                    "“Excellent, let's get to work.”"
                    "Your work at the tannery is deeply unpleasant."
                    "The smell is overwhelming and the work, scraping the hair from the fermenting skins of what you think may once have been goats, is exhausting."
                    "By the end of the day your hands are stained and your arms are seized up and you feel deeply nauseous."
                    "As the sun begins to set and the day begins to end, you are given your rations and sent on your way."
                    "You reek of tanning solution, and you’re barely able to stand from exhaustion."
                    $ Food += 3
                    $ Water += 3
                    $ visited.append("Trans Rights!")
                "Reject his offer.":
                    "The man shrugs."
                    "“Your loss.”"
                    "As you continue on your way the two people who had been watching your conversation converge on the man, arguing over who should take the job you just refused."

        else:
            "You notice that the number of people here is significantly higher than usual."
            "Untrained hands have been pressed into doing the hard, repetitive, labor that comes with so much activity."
            "You notice some people you recognize as former fishermen working a blacksmith’s bellows."
            "It seems that there is still work to be found in this city, though you’ll likely have to be a bit earlier to get it." 

        jump NavigationDay9

    # Barracks ------------------------------------------------------------------
    label BarracksDay9:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay9
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay9:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay9
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay9
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay9
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay9
                else:
                    "You decide to head to the Market."
                    jump MarketDay9
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay9
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay9
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay9
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay9
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay9
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay9
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay9
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay9
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay9
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay9
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay9
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay9
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay9
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay9

    # Home ------------------------------------------------------------------
    label HomeDay9:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day10


    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 10
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 15
    $ WaterPrice = 2
    $ WinePrice = 60
    $ MedicinePrice = 110
    $ FishingPrice = 20


    # Starting Scene  ------------------------------------------------------------------
    label Day10:
        scene home
        with dissolve

        "Day 10:"
        "You wake up in your home early in the morning."
        "A strange dread fills the air."

        jump NavigationDay10
        
    # Cothon ------------------------------------------------------------------
    label CothonDay10:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay10
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay10:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s quieter here than usual, people don’t seem to be hanging out outside as much."
        "In the street, there are a few people begging, probably put out of work by the siege."

        # Resi Event

        "The people here seem excited."
        "Despite the high prices in the market and the riots, things seem to be looking up."
        "The Greeks have been unable to reach the city across the lagoon, despite their siege the island has held firm."
        "Furthermore, it is said that a Carthaginian fleet has been sent from North Africa to relive the city and should be arriving soon."
        "Despite everything, it seems as though your ordeal may be over soon."
        "Somehow, you feel less sure of this."

        jump NavigationDay10

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay10:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "You make your way to The Cappiddazzu."
        "The city’s elite seem to have flown into a panic."
        "Soldiers and couriers rush about, delivering messages and orders who knows where and in the corners, men in fine clothes talk urgently in low tones."


        jump NavigationDay10

    # Market ------------------------------------------------------------------
    label MarketDay10:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "It’s quieter than usual. Fewer vendors line the streets and the grumbling of customers is more serious." 
        "Times are tight, prices are rising, and here in The Market, the strain is beginning to show."
        
        jump StoreDay10

    # Store ------------------------------------------------------------------
    label StoreDay10:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay10
            else:
                "You don't have enough money for food."
                jump StoreDay10
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay10
            else:
                "You don't have enough money for water."
                jump StoreDay10
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay10
            else:
                "You don't have enough money for wine."
                jump StoreDay10
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay10
            else:
                "You don't have enough money for medicine."
                jump StoreDay10
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay10
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay10
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay10

    # Causeway ------------------------------------------------------------------
    label CausewayDay10:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "The causeway has been all but destroyed, making it entirely impassible."
        "On the far shore, you see the fires, tents, and ships of the army of Syracuse and her allies."
        "As things stand now they won’t be getting into the city over the causeway, but perhaps they don't have to."

        jump NavigationDay10

    # Tophet ------------------------------------------------------------------
    label TophetDay10:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."

        jump NavigationDay10

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay10:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        jump NavigationDay10

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay10:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "The section seems to have been given over entirely to the production of weapons."
        "Blacksmiths pound out spear and arrowheads, woodworkers make shields, spear and arrow shafts, and tanners cut stinking strips of cured hides into armor."
        "Around the edges, loiterers seem to be watching them, hoping to find work in the city’s new arms industry."

        if (len(visited) == 1):
            "It’s quite early in the morning, but there are already a lot of people passing through this area."
            "Many are artisans of course, but there are also a lot of people who look to be out of work and looking for odd jobs to do."
            "You look around a bit until you come across a tanner, who seems to be willing to hire you, in a manner of speaking."
            "“I can’t pay you money.” he says."
            "“Don’t have it and even if I did, I doubt it would be worth it, what with prices and the riots and all.”"
            "“However, if I find your work satisfactory, I can give you three portions of food and three portions of water.”"
            "“That seems more than fair to me, and if you don't’ take it I’m sure someone else will.”"
            "He gestures around, to where you see at least two people listening in on your conversation. You can see the hunger in their eyes."
            "“So do we have a deal?” the tanner asks."
            "You take a moment to mull his offer over."
            menu:
                "Accept his offer.":
                    "“Excellent, let's get to work.”"
                    "Your work at the tannery is deeply unpleasant."
                    "The smell is overwhelming and the work, scraping the hair from the fermenting skins of what you think may once have been goats, is exhausting."
                    "By the end of the day your hands are stained and your arms are seized up and you feel deeply nauseous."
                    "As the sun begins to set and the day begins to end, you are given your rations and sent on your way."
                    "You reek of tanning solution, and you’re barely able to stand from exhaustion."
                    $ Food += 3
                    $ Water += 3
                    $ visited.append("Trans Rights!")
                "Reject his offer.":
                    "The man shrugs."
                    "“Your loss.”"
                    "As you continue on your way the two people who had been watching your conversation converge on the man, arguing over who should take the job you just refused."

        else:
            "You notice that the number of people here is significantly higher than usual."
            "Untrained hands have been pressed into doing the hard, repetitive, labor that comes with so much activity."
            "You notice some people you recognize as former fishermen working a blacksmith’s bellows."
            "It seems that there is still work to be found in this city, though you’ll likely have to be a bit earlier to get it." 

        jump NavigationDay10

    # Barracks ------------------------------------------------------------------
    label BarracksDay10:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay10
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay10:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay10
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay10
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay10
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay10
                else:
                    "You decide to head to the Market."
                    jump MarketDay10
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay10
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay10
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay10
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay10
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay10
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay10
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay10
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay10
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay10
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay10
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay10
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay10
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay10
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay10

    # Home ------------------------------------------------------------------
    label HomeDay10:
        scene home
        with dissolve
        $ visited = []

        "On your way home you are distracted by shouts coming from the Causeway."
        "The battle for Motya’s future is being fought in the lagoon, and you’re missing it!"
        "You run towards the causeway to join the throngs of people who crowd the shore to watch as the Carthaginian ships are driven against the rocks and destroyed."
        "The rowers and marines jump overboard and swim towards the shore only to be cut down by the soldiers who have drawn up along the coast facing them."
        "Within an hour, the relief fleet has been entirely destroyed or put to flight."
        "You stand there in bleak amazement."
        "Eventually, the crowd begins to disperse in ones and twos."
        "In a haze you make your way back to your home, unsure of what could come next."

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day11


            # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 11
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 60
    $ WaterPrice = 25
    $ WinePrice = 180
    $ MedicinePrice = 420
    $ FishingPrice = 1

    # Decrese Morale
    $ Child2.morale -= 1
    $ Child1.morale -= 1
    $ Partner.morale -= 5
    $ Player.morale -= 5


    # Starting Scene  ------------------------------------------------------------------
    label Day11:
        scene home
        with dissolve

        "Day 11:"
        "You wake up in your home early in the morning."
        "It's quiet."

        jump NavigationDay11
        
    # Cothon ------------------------------------------------------------------
    label CothonDay11:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay11
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay11:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s eerily quiet. No one seems to be out in the street."
        "Many of the buildings are boarded up."
        "In the streets, beggars and mangey starving dogs lie up against the walls."
        "Those with the strength to beg tug weekly at your clothing."
        "You hope that the others are sleeping, but in some cases, you doubt it."

        jump NavigationDay11

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay11:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "There are significantly fewer people here than usual."
        "Those who remain are clearly nervous, going about their business and quickly scuttling away."
        "It seems as though no one wants to be seen here for long."

        jump NavigationDay11

    # Market ------------------------------------------------------------------
    label MarketDay11:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "The streets are almost empty. No one seems to be buying anything." 
        "The destitute linger in side streets and alleys, eyeing what few merchants remain with desperate, angry, or hungry eyes."
        
        jump StoreDay11

    # Store ------------------------------------------------------------------
    label StoreDay11:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay11
            else:
                "You don't have enough money for food."
                jump StoreDay11
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay11
            else:
                "You don't have enough money for water."
                jump StoreDay11
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay11
            else:
                "You don't have enough money for wine."
                jump StoreDay11
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay11
            else:
                "You don't have enough money for medicine."
                jump StoreDay11
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay11
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay11
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay11

    # Causeway ------------------------------------------------------------------
    label CausewayDay11:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "At the far end you see soldiers and labourers from the Greek camp dumping rubble on top of the remains of the causeway."
        "They’re slowly building it back up, and with no one to stop them they’ll reach the walls sooner or later."


        jump NavigationDay11

    # Tophet ------------------------------------------------------------------
    label TophetDay11:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."
        
        if Child2.alive:
            "..."

            "The Tophet is the oldest and most important ritual site on the island of Motya. In the most desperate of times, this is it’s inhabitant’s last refuge."
            "You think of the siege, of the mole that grows ever closer along the causeway, of hunger and disease that even now rack the city."
            "Since this city’s foundation, in times of great hardship a Molk, the ritual sacrifice and cremation of a human infant, has been performed."
            "Your youngest child is the correct age for this type of offering."
            menu:
                "Preform a molk.":
                    "What happens next does not bear describing."
                    "You kill and cremate your youngest child."
                    "In the hours that follow, your neighbors, impressed and perhaps given some measure of hope by your piety, bring you what food and water they can to help you get through the day."
                    "You gained (x3) Food and (x3 water)."
                    $ Food += 3
                    $ Water += 3
                    $ Child2.alive = False
                "Don't.":
                    "Yo do not preform the molk today."

        jump NavigationDay11

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay11:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        if NotTakenFood:
            "You notice that there are still a few food offerings left for the souls of the departed."
            "Some stale porridge prepared in the indigenous style set out in a decorated red-slip vessel."
            "Will you steel the food offerings from the graves?"
            menu:
                "Yes":
                    "Furtively, you grab the bowl of porridge off the grave. You feel bad about it, to do so is sacrilege after all, but whoever this was left for won’t need it anymore."
                    "You got (x1) portion of food."
                    $ Food += 1
                    $ NotTakenFood = False
                "No":
                    "No. You aren’t that desperate."
                    "Not yet."

        jump NavigationDay11

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay11:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "This is one of the few sections of the city that still seems active."
        "Everywhere, grim faced craftspeople assemble the tools of war."
        "There are also many more loiterers than usual. Most of them look very disappointed."

        if (len(visited) == 1):
            "It’s quite early in the morning, but there are already a lot of people passing through this area."
            "Many are artisans of course, but there are also a lot of people who look to be out of work and looking for odd jobs to do."
            "You look around a bit until you come across a tanner, who may have offered you work before."
            "“Not only can I not pay you in money,” he says, “but I can’t even give you as much food as I would have a few days ago.”"
            "“Times are tight and food is scarce. Two portions of food and two portions of water are all I can spare.”"
            "“It’s not a lot, but if you don't’ take it one of these will.”"
            "He gestures around, to where you see half a dozen people listening in on your conversation. You can see the hunger and desperation in their eyes."
            "“So do we have a deal?” the tanner asks."
            "You take a moment to mull his offer over."
            menu:
                "Accept his offer.":
                    "“Right, lets go.” he says."
                    "Your work at the tannery is deeply unpleasant."
                    "The smell is overwhelming and the work, scraping the hair from the fermenting skins of what you think may once have been goats, is exhausting."
                    "By the end of the day your hands are stained and your arms are seized up and you feel deeply nauseous."
                    "As the sun begins to set and the day begins to end, you are given your rations and sent on your way."
                    "You reek of tanning solution, and you’re barely able to stand from exhaustion."
                    $ Food += 2
                    $ Water += 2
                    $ visited.append("Trans Rights!")
                "Reject his offer.":
                    "The man shrugs."
                    "“Your funeral”"
                    "As you continue on your way people who had been watching your conversation descend upon the man, arguing loudly and trying to undercut each other."
                    "You won’t be getting another opportunity like that today."

        else:
            "You notice that the number of people here is significantly higher than usual."
            "Untrained hands have been pressed into doing the hard, repetitive, labor that comes with so much activity."
            "You notice some people you recognize as former fishermen working a blacksmith’s bellows."
            "It seems that there is still work to be found in this city, though you’ll likely have to be a bit earlier to get it." 

        jump NavigationDay11

    # Barracks ------------------------------------------------------------------
    label BarracksDay11:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay11
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay11:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay11
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay11
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay11
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay11
                else:
                    "You decide to head to the Market."
                    jump MarketDay11
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay11
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay11
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay11
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay11
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay11
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay11
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay11
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay11
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay11
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay11
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay11
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay11
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay11
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay11

    # Home ------------------------------------------------------------------
    label HomeDay11:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day12

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 12
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 75
    $ WaterPrice = 30
    $ WinePrice = 200
    $ MedicinePrice = 450
    $ FishingPrice = 1

    # Decrese Morale
    $ Partner.morale -= 1
    $ Player.morale -= 1


    # Starting Scene  ------------------------------------------------------------------
    label Day12:
        scene home
        with dissolve

        "Day 12:"
        "You wake up in your home early in the morning."
        "It's quiet."

        jump NavigationDay12
        
    # Cothon ------------------------------------------------------------------
    label CothonDay12:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay12
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay12:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s eerily quiet. No one seems to be out in the street."
        "Many of the buildings are boarded up."
        "In the streets, beggars and mangey starving dogs lie up against the walls."
        "Those with the strength to beg tug weekly at your clothing."
        "You hope that the others are sleeping, but in some cases, you doubt it."

        # Res event
        "What few people remain outside here are angry."
        "Sullen talk about the price of food, the defeat of the relief force, and the way the last riot was handled turns quickly to calls for a new riot."
        "If their leaders won’t save them and the merchants won’t let them buy food, then they’ll have to take matters into their own hands."
        "You listen, and then continue on your way."
        "Something will come of this, though whether you’re excited or worried only you know."
        "What is sure, is that something will happen at the market tomorrow."
        "Exactly what is anyone’s guess."

        jump NavigationDay12

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay12:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "There are significantly fewer people here than usual."
        "Those who remain are clearly nervous, going about their business and quickly scuttling away."
        "It seems as though no one wants to be seen here for long."

        jump NavigationDay12

    # Market ------------------------------------------------------------------
    label MarketDay12:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "The streets are almost empty. No one seems to be buying anything." 
        "The destitute linger in side streets and alleys, eyeing what few merchants remain with desperate, angry, or hungry eyes."
        
        jump StoreDay12

    # Store ------------------------------------------------------------------
    label StoreDay12:

    "You currently have %(Money)d shekels."
    "You also have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, %(Medicine)d Medicine, and %(Fishing)d Fishing Supplies."
    "Is there anything you'd like to purchase at the market?"
    menu:
        "Buy One (1) portion of Food for %(FoodPrice)d shekels.":
            if (FoodPrice <= Money):
                $ Money -= FoodPrice
                $ Food += 1
                "You purchesed one portion of food."
                jump StoreDay12
            else:
                "You don't have enough money for food."
                jump StoreDay12
        "Buy One (1) portion of Water for %(WaterPrice)d shekels.":
            if (WaterPrice <= Money):
                $ Money -= WaterPrice
                $ Water += 1
                "You purchesed one portion of water."
                jump StoreDay12
            else:
                "You don't have enough money for water."
                jump StoreDay12
        "Buy One (1) portion of Wine for %(WinePrice)d shekels.":
            if (WinePrice <= Money):
                $ Money -= WinePrice
                $ Wine += 1
                "You purchesed one portion of wine."
                jump StoreDay12
            else:
                "You don't have enough money for wine."
                jump StoreDay12
        "Buy One (1) portion of Medicine for %(MedicinePrice)d shekels.":
            if (MedicinePrice <= Money):
                $ Money -= MedicinePrice
                $ Medicine += 1
                "You purchesed one portion of medicine."
                jump StoreDay12
            else:
                "You don't have enough money for medicine."
                jump StoreDay12
        "Buy One (1) set of Fishing Supplies for %(FishingPrice)d shekels.":
            if (FishingPrice <= Money):
                $ Money -= FishingPrice
                $ Fishing += 1
                "You purchesed one set of fishing supplies."
                jump StoreDay12
            else:
                "You don't have enough money for fishing supplies."
                jump StoreDay12
        "No, I'm good.":
            "You decide to leave the market."
            jump NavigationDay12

    # Causeway ------------------------------------------------------------------
    label CausewayDay12:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "At the far end you see soldiers and labourers from the Greek camp dumping rubble on top of the remains of the causeway."
        "They’re slowly building it back up, and with no one to stop them they’ll reach the walls sooner or later."


        jump NavigationDay12

    # Tophet ------------------------------------------------------------------
    label TophetDay12:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."
        
        if Child2.alive:
            "..."

            "The Tophet is the oldest and most important ritual site on the island of Motya. In the most desperate of times, this is it’s inhabitant’s last refuge."
            "You think of the siege, of the mole that grows ever closer along the causeway, of hunger and disease that even now rack the city."
            "Since this city’s foundation, in times of great hardship a Molk, the ritual sacrifice and cremation of a human infant, has been performed."
            "Your youngest child is the correct age for this type of offering."
            menu:
                "Preform a molk.":
                    "What happens next does not bear describing."
                    "You kill and cremate your youngest child."
                    "In the hours that follow, your neighbors, impressed and perhaps given some measure of hope by your piety, bring you what food and water they can to help you get through the day."
                    "You gained (x3) Food and (x3 water)."
                    $ Food += 3
                    $ Water += 3
                    $ Child2.alive = False
                "Don't.":
                    "Yo do not preform the molk today."

        jump NavigationDay12

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay12:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        if NotTakenFood:
            "You notice that there are still a few food offerings left for the souls of the departed."
            "Some stale porridge prepared in the indigenous style set out in a decorated red-slip vessel."
            "Will you steel the food offerings from the graves?"
            menu:
                "Yes":
                    "Furtively, you grab the bowl of porridge off the grave. You feel bad about it, to do so is sacrilege after all, but whoever this was left for won’t need it anymore."
                    "You got (x1) portion of food."
                    $ Food += 1
                    $ NotTakenFood = False
                "No":
                    "No. You aren’t that desperate."
                    "Not yet."

        jump NavigationDay12

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay12:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "This is one of the few sections of the city that still seems active."
        "Everywhere, grim faced craftspeople assemble the tools of war."
        "There are also many more loiterers than usual. Most of them look very disappointed."

        if (len(visited) == 1):
            "It’s quite early in the morning, but there are already a lot of people passing through this area."
            "Many are artisans of course, but there are also a lot of people who look to be out of work and looking for odd jobs to do."
            "You look around a bit until you come across a tanner, who may have offered you work before."
            "“Not only can I not pay you in money,” he says, “but I can’t even give you as much food as I would have a few days ago.”"
            "“Times are tight and food is scarce. Two portions of food and two portions of water are all I can spare.”"
            "“It’s not a lot, but if you don't’ take it one of these will.”"
            "He gestures around, to where you see half a dozen people listening in on your conversation. You can see the hunger and desperation in their eyes."
            "“So do we have a deal?” the tanner asks."
            "You take a moment to mull his offer over."
            menu:
                "Accept his offer.":
                    "“Right, lets go.” he says."
                    "Your work at the tannery is deeply unpleasant."
                    "The smell is overwhelming and the work, scraping the hair from the fermenting skins of what you think may once have been goats, is exhausting."
                    "By the end of the day your hands are stained and your arms are seized up and you feel deeply nauseous."
                    "As the sun begins to set and the day begins to end, you are given your rations and sent on your way."
                    "You reek of tanning solution, and you’re barely able to stand from exhaustion."
                    $ Food += 2
                    $ Water += 2
                    $ visited.append("Trans Rights!")
                "Reject his offer.":
                    "The man shrugs."
                    "“Your funeral”"
                    "As you continue on your way people who had been watching your conversation descend upon the man, arguing loudly and trying to undercut each other."
                    "You won’t be getting another opportunity like that today."

        else:
            "You notice that the number of people here is significantly higher than usual."
            "Untrained hands have been pressed into doing the hard, repetitive, labor that comes with so much activity."
            "You notice some people you recognize as former fishermen working a blacksmith’s bellows."
            "It seems that there is still work to be found in this city, though you’ll likely have to be a bit earlier to get it." 

        jump NavigationDay12

    # Barracks ------------------------------------------------------------------
    label BarracksDay12:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay12
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay12:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay12
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay12
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay12
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay12
                else:
                    "You decide to head to the Market."
                    jump MarketDay12
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay12
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay12
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay12
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay12
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay12
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay12
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay12
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay12
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay12
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay12
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay12
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay12
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay12
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay12

    # Home ------------------------------------------------------------------
    label HomeDay12:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day13

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 13
    # -----------------------------------------------------------------------------------------------------------------------------------------
    
    # Update Store Prices
    $ FoodPrice = 75
    $ WaterPrice = 30
    $ WinePrice = 200
    $ MedicinePrice = 450
    $ FishingPrice = 1

    # Decrese Morale
    $ Partner.morale -= 1
    $ Player.morale -= 1


    # Starting Scene  ------------------------------------------------------------------
    label Day13:
        scene home
        with dissolve

        "Day 13:"
        "You wake up in your home early in the morning."
        "It's quiet."

        jump NavigationDay13
        
    # Cothon ------------------------------------------------------------------
    label CothonDay13:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay13
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay13:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s eerily quiet. No one seems to be out in the street."
        "Many of the buildings are boarded up."
        "In the streets, beggars and mangey starving dogs lie up against the walls."
        "Those with the strength to beg tug weekly at your clothing."
        "You hope that the others are sleeping, but in some cases, you doubt it."

        jump NavigationDay13

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay13:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "There are significantly fewer people here than usual."
        "Those who remain are clearly nervous, going about their business and quickly scuttling away."
        "It seems as though no one wants to be seen here for long."

        jump NavigationDay13

    # Market ------------------------------------------------------------------
    label MarketDay13:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "The streets are almost empty. No one seems to be buying anything." 
        "The destitute linger in side streets and alleys, eyeing what few merchants remain with desperate, angry, or hungry eyes."

        #market event
        "When you arrive at the market it’s clear that a tragedy has just taken place." 
        "Stalls have been smashed to bits, buildings smolder, and the bodies of the dead litter the street."
        "Soldiers, maybe a hundred in all, patrol the area, stopping anyone who comes their way, the tips of their spears still bloody."
        "You could try and slip by them to loot what remains of the market, but to do so would be very dangerous."
        "You take a moment to think about what you’ll do."
        menu:
            "Try to take some stuff.":
                "You sneak down an ally and, pressing your body against the wall, edge out into the market area."
                "You are seen by a soldier almost immediately and shot down."
                return
            "Dont risk it.":
                "You decide not to risk it."
                "To do so would have been certain death."

        jump NavigationDay13

    # Causeway ------------------------------------------------------------------
    label CausewayDay13:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "At the far end you see soldiers and labourers from the Greek camp dumping rubble on top of the remains of the causeway."
        "They’re slowly building it back up, and with no one to stop them they’ll reach the walls sooner or later."


        jump NavigationDay13

    # Tophet ------------------------------------------------------------------
    label TophetDay13:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."
        
        if Child2.alive:
            "..."

            "The Tophet is the oldest and most important ritual site on the island of Motya. In the most desperate of times, this is it’s inhabitant’s last refuge."
            "You think of the siege, of the mole that grows ever closer along the causeway, of hunger and disease that even now rack the city."
            "Since this city’s foundation, in times of great hardship a Molk, the ritual sacrifice and cremation of a human infant, has been performed."
            "Your youngest child is the correct age for this type of offering."
            menu:
                "Preform a molk.":
                    "What happens next does not bear describing."
                    "You kill and cremate your youngest child."
                    "In the hours that follow, your neighbors, impressed and perhaps given some measure of hope by your piety, bring you what food and water they can to help you get through the day."
                    "You gained (x3) Food and (x3 water)."
                    $ Food += 3
                    $ Water += 3
                    $ Child2.alive = False
                "Don't.":
                    "Yo do not preform the molk today."

        jump NavigationDay13

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay13:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        "You take a moment to reflect..."

        if NotTakenFood:
            "You notice that there are still a few food offerings left for the souls of the departed."
            "Some stale porridge prepared in the indigenous style set out in a decorated red-slip vessel."
            "Will you steel the food offerings from the graves?"
            menu:
                "Yes":
                    "Furtively, you grab the bowl of porridge off the grave. You feel bad about it, to do so is sacrilege after all, but whoever this was left for won’t need it anymore."
                    "You got (x1) portion of food."
                    $ Food += 1
                    $ NotTakenFood = False
                "No":
                    "No. You aren’t that desperate."
                    "Not yet."

        jump NavigationDay13

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay13:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "This is one of the few sections of the city that still seems active."
        "Everywhere, grim faced craftspeople assemble the tools of war."
        "There are also many more loiterers than usual. Most of them look very disappointed."

        if (len(visited) == 1):
            "It’s very early in the morning when you make your way to the artisan’s quarter."
            "You pick your way through the dark streets only to find the area swarming with people, all looking for work."
            "You search for about an hour, but everyone seems to have already hired the help they need."
            "However, just when you’re about to give up hope, you run into a potter who offers you work cleaning clay."
            "“I’m afraid I don’t have much left to pay you with. But if you help me I’ll give you one portion of food and one portion of water.”"
            "You look at the potter."
            "His ribs are beginning to show through his bare chest. It’s unlikely he’s been able to sell many pots recently."
            "Will you take his offer?"
            menu:
                "Accept his offer.":
                    "Out of desperation, or pity, you take him up on his offer."
                    "You spend the day cleaning clay, straining and working out impurities until the clay."
                    "It’s surprisingly pleasant work, not to strenuous and surprisingly calming."
                    "All the while the potter works next to you, working on what seems to be an intricate statue of some time."
                    "In all the time your working he manages to finish only a small portion of the work."
                    "Absently you wonder why he bothers, there’s no way anyone’s buying fine art pieces now."
                    "At the end of the day, the potter gives you your food and sends you on your way with a smile."
                    "Several of his teeth are missing."
                    $ Food += 1
                    $ Water += 1
                    $ visited.append("Trans Rights!")
                "Reject his offer.":
                   "“Understandable.” The man says." 
                   "“I realize it’s not enough.”"

        else:
            "You notice that the number of people here is significantly higher than usual."
            "Untrained hands have been pressed into doing the hard, repetitive, labor that comes with so much activity."
            "Many people still loiter about the streets, waiting to jump on any opportunity that presents itself."
            "You feel as though getting work here will be difficult, even if you arrived first thing in the morning."

        jump NavigationDay13

    # Barracks ------------------------------------------------------------------
    label BarracksDay13:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay13
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay13:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay13
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay13
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay13
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay13
                else:
                    "You decide to head to the Market."
                    jump MarketDay13
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay13
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay13
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay13
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay13
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay13
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay13
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay13
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay13
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay13
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay13
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay13
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay13
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay13
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay13

    # Home ------------------------------------------------------------------
    label HomeDay13:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day14

            # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 14
    # -----------------------------------------------------------------------------------------------------------------------------------------
    

    # Decrese Morale
    $ Partner.morale -= 1
    $ Player.morale -= 1


    # Starting Scene  ------------------------------------------------------------------
    label Day14:
        scene home
        with dissolve

        "Day 14:"
        "You wake up in your home early in the morning."
        "It's quiet."

        jump NavigationDay14
        
    # Cothon ------------------------------------------------------------------
    label CothonDay14:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay14
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay14:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s eerily quiet. No one seems to be out in the street."
        "Many of the buildings are boarded up."
        "In the streets, beggars and mangey starving dogs lie up against the walls."
        "Those with the strength to beg tug weekly at your clothing."
        "You hope that the others are sleeping, but in some cases, you doubt it."

        jump NavigationDay14

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay14:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "There are significantly fewer people here than usual."
        "Those who remain are clearly nervous, going about their business and quickly scuttling away."
        "It seems as though no one wants to be seen here for long."

        jump NavigationDay14

    # Market ------------------------------------------------------------------
    label MarketDay14:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "The streets are entirely empty."
        "The Market has been destroyed."
        "There is nothing for you here."

        jump NavigationDay14

    # Causeway ------------------------------------------------------------------
    label CausewayDay14:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "At the far end you see soldiers and labourers from the Greek camp dumping rubble on top of the remains of the causeway."
        "They’re slowly building it back up, and with no one to stop them they’ll reach the walls sooner or later."
        "It looks like it'll be done in a day or two..."


        jump NavigationDay14

    # Tophet ------------------------------------------------------------------
    label TophetDay14:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."
        
        if Child2.alive:
            "..."

            "The Tophet is the oldest and most important ritual site on the island of Motya. In the most desperate of times, this is it’s inhabitant’s last refuge."
            "You think of the siege, of the mole that grows ever closer along the causeway, of hunger and disease that even now rack the city."
            "Since this city’s foundation, in times of great hardship a Molk, the ritual sacrifice and cremation of a human infant, has been performed."
            "Your youngest child is the correct age for this type of offering."
            menu:
                "Preform a molk.":
                    "What happens next does not bear describing."
                    "You kill and cremate your youngest child."
                    "In the hours that follow, your neighbors, impressed and perhaps given some measure of hope by your piety, bring you what food and water they can to help you get through the day."
                    "You gained (x3) Food and (x3 water)."
                    $ Food += 3
                    $ Water += 3
                    $ Child2.alive = False
                "Don't.":
                    "Yo do not preform the molk today."

        jump NavigationDay14

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay14:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        
        "A mass grave is being dug at the necropolis." 
        "The bodies of those who died in yesterday’s riots are being thrown into a large pit by hollow eyed soldiers."
        "Spectators, weather the families of the deceased or just onlookers drawn by the activity, watch the spectacle in a hollow sounding silence."


        jump NavigationDay14

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay14:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "This is one of the few sections of the city that still seems active."
        "Everywhere, grim faced craftspeople assemble the tools of war."
        "There are also many more loiterers than usual. Most of them look very disappointed."

        "This district swarms with people, all of them looking for work."
        "However, many of the workshops seem to have closed down, their windows boarded up and the apartments above quiet."
        "You search for hours, but no one is willing to give you any work."

        jump NavigationDay14

    # Barracks ------------------------------------------------------------------
    label BarracksDay14:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay14
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay14:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay14
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay14
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay14
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay14
                else:
                    "You decide to head to the Market."
                    jump MarketDay14
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay14
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay14
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay14
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay14
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay14
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay14
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay14
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay14
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay14
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay14
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay14
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay14
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay14
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay14

    # Home ------------------------------------------------------------------
    label HomeDay14:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Day15

            # -----------------------------------------------------------------------------------------------------------------------------------------
    # Day 15
    # -----------------------------------------------------------------------------------------------------------------------------------------
    

    # Decrese Morale
    $ Partner.morale -= 1
    $ Player.morale -= 1


    # Starting Scene  ------------------------------------------------------------------
    label Day15:
        scene home
        with dissolve

        "Day 15:"
        "You wake up in your home early in the morning."
        "It's quiet."

        jump NavigationDay15
        
    # Cothon ------------------------------------------------------------------
    label CothonDay15:
        scene cothon1
        with dissolve
        $ visited.append("Cothon")

        "You arrive at The Cothon."
        "However, the harbor is quiet and no one’s around."
        "Blockships have been sunk to protect the mouth of the harbor and no one’s allowed in or out."
        "In the distance you can see Greek ships patrolling the lagoon, their masts removed, ready for combat."
        "The eyes painted on their prows are unsettling, even from so far away."

        jump NavigationDay15
    
    # Residences ------------------------------------------------------------------
    label ResidencesDay15:
        scene residences
        with dissolve
        $ visited.append("Residences")

        "You make your way to The Residential Quarter."
        "It’s eerily quiet. No one seems to be out in the street."
        "Many of the buildings are boarded up."
        "In the streets, beggars and mangey starving dogs lie up against the walls."
        "Those with the strength to beg tug weekly at your clothing."
        "You hope that the others are sleeping, but in some cases, you doubt it."

        jump NavigationDay15

    # Cappiddazzu ------------------------------------------------------------------
    label CappiddazzuDay15:
        scene cappidazzu
        with dissolve
        $ visited.append("Cappiddazzu")

        "There are significantly fewer people here than usual."
        "Those who remain are clearly nervous, going about their business and quickly scuttling away."
        "It seems as though no one wants to be seen here for long."

        jump NavigationDay15

    # Market ------------------------------------------------------------------
    label MarketDay15:
        scene market
        with dissolve
        $ visited.append("Market")

        "You make your way to The Market."
        "The streets are entirely empty."
        "The Market has been destroyed."
        "There is nothing for you here."

        jump NavigationDay15

    # Causeway ------------------------------------------------------------------
    label CausewayDay15:
        scene causeway1
        with dissolve
        $ visited.append("Causeway")

        "You make your way to The Causeway."
        "At the far end you see soldiers and labourers from the Greek camp dumping rubble on top of the remains of the causeway."
        "They’re slowly building it back up, and with no one to stop them they’ll reach the walls sooner or later."
        "Its almost done..."


        jump NavigationDay15

    # Tophet ------------------------------------------------------------------
    label TophetDay15:
        scene tophet
        with dissolve
        $ visited.append("Tophet")
        
        "You make your way to The Tophet, on undeveloped patch of rocky land along the island’s Northwestern coast."
        "This is the oldest ritual site in the city, established with its foundation. Even now it remains quiet and mostly desolate but for the occasional contemplative."
        "You survey the urns with their sacrificial ashes. Laid out amongst the rocks and steele erected to commemorate rituals long passed."
        "The urns mostly contain the bones of animals…"
        "mostly."
        
        if Child2.alive:
            "..."

            "The Tophet is the oldest and most important ritual site on the island of Motya. In the most desperate of times, this is it’s inhabitant’s last refuge."
            "You think of the siege, of the mole that grows ever closer along the causeway, of hunger and disease that even now rack the city."
            "Since this city’s foundation, in times of great hardship a Molk, the ritual sacrifice and cremation of a human infant, has been performed."
            "Your youngest child is the correct age for this type of offering."
            menu:
                "Preform a molk.":
                    "What happens next does not bear describing."
                    "You kill and cremate your youngest child."
                    "In the hours that follow, your neighbors, impressed and perhaps given some measure of hope by your piety, bring you what food and water they can to help you get through the day."
                    "You gained (x3) Food and (x3 water)."
                    $ Food += 3
                    $ Water += 3
                    $ Child2.alive = False
                "Don't.":
                    "Yo do not preform the molk today."

        jump NavigationDay15

    # Necropolis ------------------------------------------------------------------
    label NecropolisDay15:
        scene necropolis1
        with dissolve
        $ visited.append("Necropolis")
        
        "You make your way to The Necropolis, the city’s graveyard that lies on the island’s northern coast."
        "This graveyard has been in use for centuries, and the methods of burial reflect this history."
        "You note a mix of cremation burials and inhumations, with bodies interred in simple rock cut tombs."
        
        if NotTakenFood:
            "Someone has raided the Necropolis and taken what offerings remain at the graves."

        jump NavigationDay15

    # ArtisinsQuarter ------------------------------------------------------------------
    label ArtisinsQuarterDay15:
        scene artisinsquarters
        with dissolve
        $ visited.append("ArtisinsQuarter")
   
        "You head to The Artisan's Quarter."
        "This is one of the few sections of the city that still seems active."
        "Everywhere, grim faced craftspeople assemble the tools of war."
        "There are also many more loiterers than usual. Most of them look very disappointed."

        "This district swarms with people, all of them looking for work."
        "However, many of the workshops seem to have closed down, their windows boarded up and the apartments above quiet."
        "You search for hours, but no one is willing to give you any work."

        jump NavigationDay15

    # Barracks ------------------------------------------------------------------
    label BarracksDay15:
        scene barracks1
        with dissolve
        $ visited.append("Barracks")

        "You make your way to The Barracks."
        "Soldiers block your path."
        "However, you are turned away before you can even get close."

        jump NavigationDay15
    
    # Navigation ------------------------------------------------------------------
    label NavigationDay15:
    if (len(visited) > 2):
        "It's getting late, time to go home."
        jump HomeDay15
    else:
        "Where would you like to head next?"
        menu:
            "Go to the Cothon":
                if ("Cothon" in visited):
                    "You've already visited the Cothon today, no point going twice."
                    jump NavigationDay15
                else:
                    "You decide to head to the Cothon."
                    jump CothonDay15
            "Go to the Market":
                if ("Market" in visited):
                    "You've already visited the Market today, no point going twice."
                    jump NavigationDay15
                else:
                    "You decide to head to the Market."
                    jump MarketDay15
            "Go to the Residential Quarter":
                if ("Residences" in visited):
                    "You've already visited the Residential Quarter today, no point going twice."
                    jump NavigationDay15
                else:
                    "You decide to head to the Residential Quarter."
                    jump ResidencesDay15
            "Go to the Cappiddazzu":
                if ("Cappiddazzu" in visited):
                    "You've already visited the Cappiddazzu today, no point going twice."
                    jump NavigationDay15
                else:
                    "You decide to head to the Cappiddazzu."
                    jump CappiddazzuDay15
            "Go to the Artisan's Quarter":
                if ("ArtisinsQuarter" in visited):
                    "You've already visited the Artisan's Quarter today, no point going twice."
                    jump NavigationDay15
                else:
                    "You decide to head to the Artisan's Quarter."
                    jump ArtisinsQuarterDay15
            "Go to the Causeway":
                if ("Causeway" in visited):
                    "You've already visited the Causeway today, no point going twice."
                    jump NavigationDay15
                else:
                    "You decide to head to the Causeway."
                    jump CausewayDay15
            "Go to the Tophet":
                if ("Tophet" in visited):
                    "You've already visited the Tophet today, no point going twice."
                    jump NavigationDay15
                else:
                    "You decide to head to the Tophet."
                    jump TophetDay15
            "Go to the Necropolis":
                if ("Necropolis" in visited):
                    "You've already visited the Necropolis today, no point going twice."
                    jump NavigationDay15
                else:
                    "You decide to head to the Necropolis."
                    jump NecropolisDay15
            "Go to the Barracks":
                if ("Barracks" in visited):
                    "You've already visited the Barracks today, no point going twice."
                    jump NavigationDay15
                else:
                    "You decide to head to the Barracks."
                    jump BarracksDay15

    # Home ------------------------------------------------------------------
    label HomeDay15:
        scene home
        with dissolve
        $ visited = []

        "You must now divide your supplies amongst your family."
        
        # Child2
        if (Child2.alive):

            "First, you will decide what to give your youngest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."

            # Food
            $ i = Child2.hunger
            "Your youngest child currently has %(i)d/5 Hunger."
            "How much food will you give your youngest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your youngest child one portion of food for the day."
                        $ Child2.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your youngest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your youngest child two portions of food for the day."
                        if (Child2.hunger < 5):
                            $ Child2.hunger += 2
                        else:
                            $ Child2.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your youngest child one portion instead."
                            $ Child2.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your youngest child."
                "No food.":
                    "You choose not to give your youngest child any food."

            # Water
            $ i = Child2.thirst
            "Your youngest child currently has %(i)d/3 Thirst."
            "How much water will you give your youngest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your youngest child one portion of water for the day."
                        $ Child2.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your youngest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your youngest child two portions of water for the day."
                        if (Child2.thirst < 3):
                            $ Child2.thirst += 2
                        else:
                            $ Child2.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your youngest child one portion instead."
                            $ Child2.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your youngest child."
                "No water.":
                    "You choose not to give your youngest child any water."
            # Wine
            $ i = Child2.morale
            "Your youngest child currently has %(i)d/10 Morale."
            "Will you give your youngest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your youngest child one portion of wine."
                        $ Child2.thirst += 1
                        $ Child2.morale += 1
                        $ Child2.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any wine."
            # Medicine
            $ i = Child2.health
            "Your youngest child currently has %(i)d/10 Health."
            "Will you give your youngest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your youngest child one portion of medicine."
                        $ Child2.morale -= 1
                        $ Child2.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your youngest child."
                "No.":
                    "You choose not to give your youngest child any medicine."
        else:
            "Your youngest child is dead."


         # Child1
        if (Child1.alive):

            "Now, you will decide what to give your oldest child."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Child1.hunger
            "Your oldest child currently has %(i)d/5 Hunger."
            "How much food will you give your oldest child?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your oldest child one portion of food for the day."
                        $ Child1.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your oldest child."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your oldest child two portions of food for the day."
                        if (Child1.hunger < 5):
                            $ Child1.hunger += 2
                        else:
                            $ Child1.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your oldest child one portion instead."
                            $ Child1.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your oldest child."
                "No food.":
                    "You choose not to give your oldest child any food."

            # Water
            $ i = Child1.thirst
            "Your oldest child currently has %(i)d/3 Thirst."
            "How much water will you give your oldest child?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your oldest child one portion of water for the day."
                        $ Child1.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your oldest child."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your oldest child two portions of water for the day."
                        if (Child1.thirst < 3):
                            $ Child1.thirst += 2
                        else:
                            $ Child1.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your oldest child one portion instead."
                            $ Child1.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your oldest child."
                "No water.":
                    "You choose not to give your oldest child any water."
            # Wine
            $ i = Child1.morale
            "Your oldest child currently has %(i)d/10 Morale."
            "Will you give your oldest child some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your oldest child one portion of wine."
                        $ Child1.thirst += 1
                        $ Child1.morale += 1
                        $ Child1.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any wine."
            # Medicine
            $ i = Child1.health
            "Your oldest child currently has %(i)d/10 Health."
            "Will you give your oldest child medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your oldest child one portion of medicine."
                        $ Child1.morale -= 1
                        $ Child1.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your oldest child."
                "No.":
                    "You choose not to give your oldest child any medicine."
        else:
            "Your oldest child is dead."
        

         # Partner
        if (Partner.alive):

            "Now, you will decide what to give your partner."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Partner.hunger
            "Your partner currently has %(i)d/5 Hunger."
            "How much food will you give your partner?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You give your partner one portion of food for the day."
                        $ Partner.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food to give your partner."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You give your partner two portions of food for the day."
                        if (Partner.hunger < 5):
                            $ Partner.hunger += 2
                        else:
                            $ Partner.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you give your partner one portion instead."
                            $ Partner.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food to give your partner."
                "No food.":
                    "You choose not to give your partner any food."

            # Water
            $ i = Partner.thirst
            "Your partner currently has %(i)d/3 Thirst."
            "How much water will you give your partner?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You give your partner one portion of water for the day."
                        $ Partner.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water to give your partner."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You give your partner two portions of water for the day."
                        if (Partner.thirst < 3):
                            $ Partner.thirst += 2
                        else:
                            $ Partner.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you give your partner one portion instead."
                            $ Partner.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water to give your partner."
                "No water.":
                    "You choose not to give your partner any water."
            # Wine
            $ i = Partner.morale
            "Your partner currently has %(i)d/10 Morale."
            "Will you give your partner some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You give your partner one portion of wine."
                        $ Partner.thirst += 1
                        $ Partner.morale += 1
                        $ Partner.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine to give your partner."
                "No.":
                    "You choose not to give your partner any wine."
            # Medicine
            $ i = Partner.health
            "Your partner currently has %(i)d/10 Health."
            "Will you give your partner medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You give your partner one portion of medicine."
                        $ Partner.morale -= 1
                        $ Partner.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine to give your partner."
                "No.":
                    "You choose not to give your partner any medicine."
        else:
            "Your partner is dead."
        
        
        # Player
        if (Player.alive):

            "Now, you will decide what to take for to yourself."
            "You currently have: %(Food)d Food, %(Water)d Water, %(Wine)d Wine, and %(Medicine)d Medicine."
            
            # Food
            $ i = Player.hunger
            "You currently have %(i)d/5 Hunger."
            "How much food will you take?"
            menu: 
                "One Portion of food.":
                    if (Food >= 1):
                        "You take one portion of food for the day."
                        $ Player.hunger += 1
                        $ Food -= 1
                    else:
                        "You do not have any food."
                "Two Portions of food.":
                    if (Food >= 2):
                        "You take two portions of food for the day."
                        if (Player.hunger < 5):
                            $ Player.hunger += 2
                        else:
                            $ Player.hunger = 6
                        $ Food -= 2
                    else:
                        if (Food > 0):
                            "You don't have two portions of food, so you take one portion instead."
                            $ Player.hunger += 1
                            $ Food -= 1
                        else:
                            "You do not have any food."
                "No food.":
                    "You choose not to take any food."

            # Water
            $ i = Player.thirst
            "You currently have %(i)d/3 Thirst."
            "How much water will you take?"
            menu: 
                "One Portion of water.":
                    if (Water >= 1):
                        "You take one portion of water for the day."
                        $ Player.thirst += 1
                        $ Water -= 1
                    else:
                        "You do not have any water."
                "Two Portions of water.":
                    if (Water >= 2):
                        "You take two portions of water for the day."
                        if (Player.thirst < 3):
                            $ Player.thirst += 2
                        else:
                            $ Player.thirst = 6
                        $ Water -= 2
                    else:
                        if (Water > 0):
                            "You don't have two portions of water, so you take one portion instead."
                            $ Player.thirst += 1
                            $ Water -= 1
                        else:
                            "You do not have any water."
                "No water.":
                    "You choose not to take any water."
            # Wine
            $ i = Player.morale
            "You currently have %(i)d/10 Morale."
            "Will you take some wine?"
            menu: 
                "Yes.":
                    if (Wine >= 1):
                        "You take one portion of wine."
                        $ Player.thirst += 1
                        $ Player.morale += 1
                        $ Player.health -= 1
                        $ Wine -= 1
                    else:
                        "You do not have any wine."
                "No.":
                    "You choose not to take any wine."
            # Medicine
            $ i = Player.health
            "You currently have %(i)d/10 Health."
            "Will you take any medicine?"
            menu: 
                "Yes.":
                    if (Medicine >= 1):
                        "You take one portion of medicine."
                        $ Player.morale -= 1
                        $ Player.health += 1
                        $ Medicine -= 1
                    else:
                        "You do not have any medicine."
                "No.":
                    "You choose not to take any medicine."
        else:
            "You are dead and also the game is broken because you shouldn't be able to see this!"
        

        "You finish dividing up your supplies and go to bed for the night."

        # Updated stats:
        $ Child2 = updateStats(Child2)
        $ Child1 = updateStats(Child1)
        $ Partner = updateStats(Partner)
        $ Player = updateStats(Player)

        jump Endgame

    label Endgame:
        scene home
        with dissolve

        "In the morning, the Greek forces reach the end of the causeway."
        "The people of Motya give their lives dearly."
        "Fighting rages for nearly the entire day, as the Greeks are forced to fight for every street and every building." 
        "However, the end result is never in doubt."
        "The city is eventually razed to the ground."
        "It is never rebuilt."
        "The city’s population was, for the most part, killed in the struggle, though a few may have survived to found the city of Lilybaeum nearby."
        "The conflict of which the sack of Motya was a part was eventually indecisive, with both Carthage and Syricuse retaining power in their respective spheres of influence."
        "What happened to you and whatever family you had left when the city fell is unknown."
        "The End"

    return