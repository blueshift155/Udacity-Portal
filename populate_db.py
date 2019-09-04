from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Girish Thavai", email="thavai.girish@gmail.com",
             picture='https://freeiconshop.com/wp-content/uploads/edd/person-outline-filled.png')
session.add(User1)
session.commit()
print("User created: " + User1.name)

# Menu for Fusion Kadai
restaurant1 = Restaurant(user_id=1, name="Fusion Kadai")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="French Chat", description="Desi Chat with garlic and parmesan",
                     price="₹150", course="Appetizers", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chaat Papdi", description="Fried papdi mixed with onions, tomatoes, mint, tamarind & yogurt",
                     price="₹100", course="Appetizers", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Paneer Pakora", description="Cottage cheese dipped in chickpea batter and fried",
                     price="₹200", course="Starters", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Coconut Soup", description="Coconut milk, light onion sauce with fresh cream",
                     price="₹250", course="Appetizers", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Gulab Jamun", description="Deep fried milk confection in a sweet syrup",
                     price="₹50", course="Desserts", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Root Beer", description="16oz of refreshing goodness",
                     price="₹150", course="Beverages", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Iced Tea", description="with Lemon",
                     price="₹80", course="Beverages", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Special Dinner", description="Tandoori chicken, shrimp, lamb kabab, seekh kabab, choice of one curry, rice and choice of one bread",
                     price="₹500", course="Main Course", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Pin Cuk
restaurant2 = Restaurant(user_id=1, name="Pin Cuk")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Chicken Stir Fry", description="With your choice of noodles, vegetables and sauces",
                     price="₹300", course="Starters", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook",
                     price="₹750", course="Main Course", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="₹450", course="Main Course", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="₹200", course="Starters", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="₹150", course="Main Course", restaurant=restaurant2)

session.add(menuItem5)
session.commit()


# Menu for South Coast Hotel
restaurant3 = Restaurant(user_id=1, name="South Coast Hotel")

session.add(restaurant3)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Mixed Platter", description="Samosa, vegetables, chicken, paneer, shrimp pakora & papadom",
                     price="₹350", course="Appetizers", restaurant=restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Fish Tikka", description="Marinated seasonal fish served with choice of soup",
                     price="₹250", course="Starters", restaurant=restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Vegetable Green Masala", description="Mixed vegetables in a hot spinach sauce topped with coconut cream",
                     price="₹300", course="Main Course", restaurant=restaurant3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Bread Basket", description="Naan, Garlic Naan, Cheese Naan",
                     price="₹150", course="Main Course", restaurant=restaurant3)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Gajar Halwa", description="Grated carrots cooked in milk and butter",
                     price="₹150", course="Desserts", restaurant=restaurant3)

session.add(menuItem5)
session.commit()


# Menu for Barworks Eatery
restaurant4 = Restaurant(user_id=1, name="Barworks Eatery")
session.add(restaurant4)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="₹350", course="Desserts", restaurant=restaurant4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Mushroom Risotto", description="Mushrooms in a creamy risotto",
                     price="₹250", course="Starters", restaurant=restaurant4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     price="₹150", course="Starters", restaurant=restaurant4)

session.add(menuItem3)
session.commit()


# Menu for The Mint Leaf Kitchen
restaurant5 = Restaurant(user_id=1, name="The Mint Leaf Kitchen")

session.add(restaurant5)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="₹350", course="Starters", restaurant=restaurant5)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="₹350", course="Desserts", restaurant=restaurant5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="₹350", course="Starters", restaurant=restaurant5)

session.add(menuItem3)
session.commit()

restaurants = session.query(Restaurant).all()
for restaurant in restaurants:
    print("Added: " + restaurant.name)
