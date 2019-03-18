from flask import Flask, render_template, request, redirect, jsonify, url_for,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'
db = SQLAlchemy(app)
from database_setup import Restaurant, MenuItem





db.create_all()

def lotsofmenus():
    # Menu for UrbanBurger
    restaurant1 = Restaurant(name="Urban Burger")

    db.session.add(restaurant1)
    db.session.commit()

    menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.50", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()


    menuItem1 = MenuItem(name="French Fries", description="with garlic and parmesan",
                     price="$2.99", course="Appetizer", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit()

    menuItem2 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="$5.50", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()
    
    menuItem3 = MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="$3.99", course="Dessert", restaurant=restaurant1)

    db.session.add(menuItem3)
    db.session.commit()

    menuItem4 = MenuItem(name="Sirloin Burger", description="Made with grade A beef",
                     price="$7.99", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem4)
    db.session.commit()

    menuItem5 = MenuItem(name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

    db.session.add(menuItem5)
    db.session.commit()

    menuItem6 = MenuItem(name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", restaurant=restaurant1)

    db.session.add(menuItem6)
    db.session.commit()

    menuItem7 = MenuItem(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                     price="$3.49", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem7)
    db.session.commit()

    menuItem8 = MenuItem(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     price="$5.99", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem8)
    db.session.commit()


# Menu for Super Stir Fry
    restaurant2 = Restaurant(name="Super Stir Fry")

    db.session.add(restaurant2)
    db.session.commit()


    menuItem1 = MenuItem(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     price="$7.99", course="Entree", restaurant=restaurant2)

    db.session.add(menuItem1)
    db.session.commit()

    menuItem2 = MenuItem(
    name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", course="Entree", restaurant=restaurant2)

    db.session.add(menuItem2)
    db.session.commit()

    menuItem3 = MenuItem(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="15", course="Entree", restaurant=restaurant2)

    db.session.add(menuItem3)
    db.session.commit()

    menuItem4 = MenuItem(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="12", course="Entree", restaurant=restaurant2)

    db.session.add(menuItem4)
    db.session.commit()

    menuItem5 = MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="14", course="Entree", restaurant=restaurant2)

    db.session.add(menuItem5)
    db.session.commit()

    menuItem6 = MenuItem(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="12", course="Entree", restaurant=restaurant2)

    db.session.add(menuItem6)
    db.session.commit()


# Menu for Panda Garden
    restaurant1 = Restaurant(name="Panda Garden")

    db.session.add(restaurant1)
    db.session.commit()


    menuItem1 = MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="$8.99", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit()

    menuItem2 = MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="$6.99", course="Appetizer", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()

    menuItem3 = MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                     price="$9.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem3)
    db.session.commit()

    menuItem4 = MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$6.99", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem4)
    db.session.commit()
    
    menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()


# Menu for Thyme for that
    restaurant1 = Restaurant(name="Thyme for That Vegetarian Cuisine ")

    db.session.add(restaurant1)
    db.session.commit()


    menuItem1 = MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                         price="$2.99", course="Dessert", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit()

    menuItem2 = MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                         price="$5.99", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()

    menuItem3 = MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                         price="$4.50", course="Dessert", restaurant=restaurant1)

    db.session.add(menuItem3)
    db.session.commit()

    menuItem4 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                         price="$6.95", course="Appetizer", restaurant=restaurant1)

    db.session.add(menuItem4)
    db.session.commit()

    menuItem5 = MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                         price="$7.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem5)
    db.session.commit()

    menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                         price="$6.80", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()


    # Menu for Tony's Bistro
    restaurant1 = Restaurant(name="Tony\'s Bistro ")

    db.session.add(restaurant1)
    db.session.commit()


    menuItem1 = MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                         price="$13.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit()

    menuItem2 = MenuItem(name="Chicken and Rice", description="Chicken... and rice",
                         price="$4.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()

    menuItem3 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                         price="$6.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem3)
    db.session.commit()

    menuItem4 = MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                         description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course="Dessert", restaurant=restaurant1)

    db.session.add(menuItem4)
    db.session.commit()

    menuItem5 = MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                         price="$7.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem5)
    db.session.commit()


    # Menu for Andala's
    restaurant1 = Restaurant(name="Andala\'s")

    db.session.add(restaurant1)
    db.session.commit()


    menuItem1 = MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                         price="$9.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit()

    menuItem2 = MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                         price="$7.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()

    menuItem3 = MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                         price="$6.50", course="Appetizer", restaurant=restaurant1)

    db.session.add(menuItem3)
    db.session.commit()

    menuItem4 = MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                         price="$6.75", course="Appetizer", restaurant=restaurant1)

    db.session.add(menuItem4)
    db.session.commit()

    menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                         price="$7.00", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()


    # Menu for Auntie Ann's
    restaurant1 = Restaurant(name="Auntie Ann\'s Diner' ")

    db.session.add(restaurant1)
    db.session.commit()

    menuItem9 = MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                         price="$8.99", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem9)
    db.session.commit()


    menuItem1 = MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                         price="$2.99", course="Dessert", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit()

    menuItem2 = MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                         price="$10.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()

    menuItem3 = MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                         price="$7.50", course="Appetizer", restaurant=restaurant1)

    db.session.add(menuItem3)
    db.session.commit()

    menuItem4 = MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                         price="$8.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem4)
    db.session.commit()

    menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                         price="$9.50", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()

    menuItem10 = MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                          price="$1.99", course="Dessert", restaurant=restaurant1)

    db.session.add(menuItem10)
    db.session.commit()


    # Menu for Cocina Y Amor
    restaurant1 = Restaurant(name="Cocina Y Amor ")

    db.session.add(restaurant1)
    db.session.commit()


    menuItem1 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                         price="$5.95", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit()

    menuItem2 = MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                         price="$7.99", course="Entree", restaurant=restaurant1)

    db.session.add(menuItem2)
    db.session.commit()


    restaurant1 = Restaurant(name="State Bird Provisions")
    db.session.add(restaurant1)
    db.session.commit()

    menuItem1 = MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                         price="$5.95", course="Appetizer", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit

    menuItem1 = MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                         price="$6.95", course="Dessert", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit()


    menuItem1 = MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                         price="$4.25", course="Dessert", restaurant=restaurant1)

    db.session.add(menuItem1)
    db.session.commit()


    print "added menu items!"

#lotsofmenus()
#engine = create_engine('sqlite:///restaurantmenu.db')
#Base.metadata.bind = engine

#DBSession = sessionmaker(bind=engine)
#session = DBSession()




# Fake Restaurants
# restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

# restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


# Fake Menu Items
# items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
# item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}
# items = []


@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).one()
    items = MenuItem.query.filter_by(
                                              restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    Menu_Item = MenuItem.query.filter_by(id=menu_id).one()
    return jsonify(Menu_Item=Menu_Item.serialize)


@app.route('/restaurant/JSON')
def restaurantsJSON():
    restaurants = Restaurant.query.all()
    return jsonify(restaurants=[r.serialize for r in restaurants])


# Show all restaurants
@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    restaurants = Restaurant.query.all()
    # return "This page will show all my restaurants"
    return render_template('restaurants.html', restaurants=restaurants)


# Create a new restaurant
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        db.session.add(newRestaurant)
        db.session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')
# return "This page will be for making a new restaurant"

# Edit a restaurant


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = Restaurant.query.filter_by(id=restaurant_id).one()
    if request.method == 'POST':
      if request.form['name']:
        editedRestaurant.name = request.form['name']
        db.session.add(editedRestaurant)
        db.session.commit()
        return redirect(url_for('showRestaurants'))
    else:
      return render_template('editRestaurant.html', restaurant=editedRestaurant)

# return 'This page will be for editing restaurant %s' % restaurant_id

# Delete a restaurant


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurantToDelete = Restaurant.query.filter_by(id=restaurant_id).one()
    if request.method == 'POST':
      db.session.delete(restaurantToDelete)
      db.session.commit()
      return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
      return render_template('deleteRestaurant.html', restaurant=restaurantToDelete)
# return 'This page will be for deleting restaurant %s' % restaurant_id


# Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).one()
    items = MenuItem.query.filter_by(
                                              restaurant_id=restaurant_id).all()
    return render_template('menu.html', items=items, restaurant=restaurant)
# return 'This page is the menu for restaurant %s' % restaurant_id

# Create a new menu item


@app.route(
           '/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form['description'], price=request.form['price'], course=request.form['course'], restaurant_id=restaurant_id)
        db.session.add(newItem)
        db.session.commit()
        flash("new menu item created!")
                                                                               
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)
    
    return render_template('newMenuItem.html', restaurant=restaurant)
# return 'This page is for making a new menu item for restaurant %s'
# %restaurant_id

# Edit a menu item


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = MenuItem.query.filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        db.session.add(editedItem)
        db.session.commit()
        flash("menu item edited!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        
        return render_template(
                               'editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)

# return 'This page is for editing menu item %s' % menu_id

# Delete a menu item


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = MenuItem.query.filter_by(id=menu_id).one()
    if request.method == 'POST':
        db.session.delete(itemToDelete)
        db.session.commit()
        flash("menu item deleted!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item=itemToDelete)
# return "This page is for deleting menu item %s" % menu_id


if __name__ == '__main__':
    app.secret_key="super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)




