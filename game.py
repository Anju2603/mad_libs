def mad_libs():
    print("Welcome to the Mad Libs Game!\n")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb_past = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")
    animal = input("Enter an animal: ")

    story = f"""
    Today I went to the {place}. It was a very {adjective} day.
    I saw a {animal} that {verb_past} {adverb} across the street.
    Everyone around looked {emotion}. Then, I picked up a {noun} and walked away smiling.
    What a day!
    """

    print("\nHere's your Mad Libs story:\n")
    print(story)

mad_libs()