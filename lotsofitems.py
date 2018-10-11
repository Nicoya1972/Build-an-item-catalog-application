from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

engine = create_engine('sqlite:///catalogs.db')
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


# Create test user
User1 = User(name="Hello None", email="test.xyzk@gmail.com")
session.add(User1)
session.commit()

# Create category of Soccer
category1 = Categories(user_id=1, name="Soccer")
session.add(category1)
session.commit()


# Create category of Basketball
category2 = Categories(user_id=1, name="Basketball")
session.add(category2)
session.commit()

# Create category of Surf
category3 = Categories(user_id=1, name="Surf")
session.add(category3)
session.commit()

# Create category of Yoga
category4 = Categories(user_id=1, name="Yoga")
session.add(category4)
session.commit()

# Create category of Running
category5 = Categories(user_id=1, name="Running")
session.add(category5)
session.commit()

# Create category of Skating
category6 = Categories(user_id=1, name="Skating")
session.add(category6)
session.commit()

# Create category of Swimming
category7 = Categories(user_id=1, name="Swimming")
session.add(category7)
session.commit()

# Create category of Rock Climbing
category8 = Categories(user_id=1, name="Rock Climbing")
session.add(category8)
session.commit()

# Create category of Pilates
category9 = Categories(user_id=1, name="Pilates")
session.add(category9)
session.commit()

# Create category of Hockey
category10 = Categories(user_id=1, name="Hockey")
session.add(category10)
session.commit()

# Create category of Snowboarding
category11 = Categories(user_id=1, name="Snowboarding")
session.add(category11)
session.commit()


# Add Items into categories
item1 = CategoryItem(user_id=1, name="Socker Boots",
                             description="Shoes to play socker",
                             categories=category1)
session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1, name="Basket ball",
                             description="A ball to play basket",
                             categories=category2)
session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1, name="Surf board",
                             description="Board to surf",
                             categories=category3)
session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1, name="Jogging pant",
                             description="A very confortable pant for practising yoga ",
                             categories=category4)
session.add(item4)
session.commit()

item5 = CategoryItem(user_id=1, name="Running shoes",
                             description="Shoes adapted for the running",
                             categories=category5)
session.add(item5)
session.commit()

item6 = CategoryItem(user_id=1, name="Skate board",
                             description="Very light board for skating everywhere",
                             categories=category6)
session.add(item6)
session.commit()

item7 = CategoryItem(user_id=1, name="Swim suit",
                             description="A swim suit for swimming with all the confort",
                             categories=category7)
session.add(item7)
session.commit()

item8 = CategoryItem(user_id=1, name="Harnesses",
                             description="To practice rock climbing",
                             categories=category8)
session.add(item8)
session.commit()

item9 = CategoryItem(user_id=1, name="Pilates ball",
                             description="To practice pilates at home",
                             categories=category9)
session.add(item9)
session.commit()

item10 = CategoryItem(user_id=1, name="Hockey stick",
                             description="A quality wood hockey stick to practice this sport",
                             categories=category10)
session.add(item10)
session.commit()

item11 = CategoryItem(user_id=1, name="Snow board",
                             description="To practice this sport",
                             categories=category11)
session.add(item11)
session.commit()


print "added category items!"
