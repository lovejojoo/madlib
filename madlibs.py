# String concatenation - how to put strings together
# We want to create a string that says "subscribe to ____"
# youtuber = "Letscodewithher"  # This will be a string variable

# To create a string there is a few ways to express string concatenation :
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person")

madLib = f"Computing programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
# strings are string literals that have an f at the beginning and curly braces
# containing expressions that will be replaced with their values.
print(madLib)
