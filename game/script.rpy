# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "The pot bubbled."

    "It was a small thing. A tinny thing, scorched and burnt by the uneven flames of a half-working oven."

    "It was a small pot in a small kitchen, in a small studio in a city too large for its own good."

    "The paint had long since flaked off the cupboard doors."

    "Various cans sat inside, their labels occasionally highlighted by a flash of lightning outside."

    menu:

        "There were small boxes, too. Pasta."

        "Spaghetti.":
            $ pasta = "spaghetti"
            jump studio

        "Fettucine.":
            $ pasta = "fettucine"
            jump studio

label studio:

    "It's a small place. The neighborhood is rough, but nice enough. The couple across the hall isn't fighting, for once."

    "It's been some time since you moved in."

    "Yesterday, it didn't seem any different. A studio with clothes across the floor, a bed perpetually unmade, and a sink full of dirty dishes."

    "This evening, it's a little more civilized."

    if pasta == "spaghetti":
        "You thought it'd be nice to make some spaghetti tonight."

    if pasta == "fettucine":
        "You thought it'd be nice to make some fettucine tonight."

    "Dinner for two."

    "Another burner flickers as the pot and its contents continue to stew."

    "A saucepan. A little more oil."

    menu:

        "The steam from the pot drifts into the air, into your nostrils. The vent isn't working. The window fogs up, ever so slightly."

        "Marinara.":
            $ sauce = "marinara"
            jump marinara

        "Alfredo.":
            $ sauce = "alfredo"
            jump alfredo

label marinara:

    "The red of the sauce melts into the black of the small pan. It bubbles, but only a little bit."

    "Something tangy fills the air. You stir, and turn off the heat."

    jump phone

label alfredo:

    "The cream clashes with the iron. It bubbles slightly."

    "Something sweet mingles with the steam from the pot."

    "There's a wooden spoon to keep the sauce from burning, and a dial to turn the fire off."

    jump phone

label phone:

    "The phone rings."

    "You hesitate."

    "The phone rings."

    "The pot boils."

    menu:

        "The phone keeps ringing."

        "Maybe it's the police.":
            jump answer
        "Maybe it's the mob.":
            jump answer

label answer:

    "The voice on the other end soothes your nerves. Good news, for once, even if it isn't."

    "They'll be a little late. Traffic."

    menu:

        "The rain can be felt through the walls. The window strains, but it's stronger than it looks."

        "Set the table.":
            jump table

label table:

    "The tablecloth is clean. It drapes evenly over the sides of a very small dining table, right outside the kitchen."

    "It's large enough for three. The other chair is beside the bed."

    "There's an opaque vase in the center of the table, adorned with something picked up at the florist's after work."

    "The plates are clean. You place silverware neatly beside them. The scent of food wafts into the rest of your home."

    menu:

        "There's a bag with wine in the corner, beside to the table."

        "Red.":
            jump wine

        "White.":
            jump wine

label wine:

    "A bottle of wine on the table, and two empty glasses."

    "You check the time. You remember the voice on the phone."

    "You strain the pasta, and watch the starchy water swirl down the drain."

    "The doorbell rings."

    "Dinner for two."

    # This ends the game.

    return
