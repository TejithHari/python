def play_mad_libs():
    story = "Once upon a time, there was a {noun} who loved to {verb} in the {place}."
    print("Let's play Mad Libs!")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    print("Here's your story:")
    print(story.format(noun=noun, verb=verb, place=place))

# Play the game
play_mad_libs()
