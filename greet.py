import datetime

def checkValidInteger(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False
    
user_name = input("Plz enter your Name:\n")
user_age  = input("Plz enter your Age:\n")

while not checkValidInteger(user_age):
   user_age = input("The number you entered is invalid, Plz enter a valid Age:\n")



current_year = datetime.datetime.now().year
year_to_reach_100 = current_year + (100-int(user_age))

greeting = f"Hello, {user_name}! Nice to meet you."
year_100_msg = f"Did you know, you will turn 100 in year {year_to_reach_100}!."
if int(user_age) >= 100:
    year_100_msg = f"Congratulations on reaching the incredible milestone of living over 100 years! Your resilience and wisdom are truly remarkable, and your legacy will continue to inspire generations to come." 

print(greeting, end="\n")
print(year_100_msg, end="\n")



# Add quotes as an output based on Age to give out a customized greeting

# quotes

# Children (0-19 years old):

# Quote: "Believe in the magic within you, for you are capable of achieving wonderful things."
# Fun Fact: "Did you know that honey never spoils? It's like a jar of magic that lasts forever!"
# Young Adults (20-39 years old):

# Quote: "Life is an adventure waiting to be embraced. Seize the opportunities and create your own path."
# Fun Fact: "Octopuses have three hearts, just like you have a heart full of passion for your adventures."
# Middle-Aged Adults (40-59 years old):

# Quote: "The middle of your journey is not the end. It's a chance for renewal and rediscovery."
# Fun Fact: "As you navigate life's twists and turns, remember that your taste for new experiences can evolve, just like your palate."
# Older Adults (60-79 years old):

# Quote: "The beauty of life is in its continuous evolution. Embrace change and savor the wisdom that comes with age."
# Fun Fact: "Much like the Eiffel Tower, you too can stand tall and proud in any season of life, growing stronger with time."
# Elderly (80+ years old):

# Quote: "Your life is a masterpiece painted with years of experience and memories. Cherish every stroke."
# Fun Fact: "Like the 'immortal jellyfish,' you've experienced the power of renewal, forever young in spirit."