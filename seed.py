from app import app, db
from models import User, Tag, Post

def drop_database():
    with app.app_context():
        db.drop_all()

def seed_database():
    # Drop the existing Database
    drop_database()
    
    # Create all database tables
    with app.app_context():
        db.create_all()

        # Create users if they do not exist
        users_data = [
            {'first_name': 'Adam', 'last_name': 'Smith', 'image_url': 'https://th.bing.com/th?id=OSK.HEROZjgOPNis7uZ9MYqG2r9c6OHWZoxnTprhlcQZRvT7eUk&w=472&h=280&c=13&rs=2&o=6&pid=SANGAM'},
            {'first_name': 'Anne', 'last_name': 'Conway', 'image_url': 'https://th.bing.com/th?id=ODL.e72ca37004ccf32c3da5802c94ac3186&w=207&h=280&c=10&rs=1&qlt=99&o=6&pid=13.1'},
            {'first_name': 'Alan', 'last_name': 'Turing', 'image_url': 'https://th.bing.com/th?id=ODL.8d35af708d319ec5b81ba3645a6d0896&w=180&h=183&c=10&rs=1&qlt=99&o=6&pid=13.1'},
            {'first_name': 'Ada', 'last_name': 'Lovelace', 'image_url': 'https://th.bing.com/th?id=OSK.HERO6pWim_axaD5Z0Z0u24V1KBVi6H6R6PpVvomRv5EF8Tk&w=472&h=280&c=13&rs=2&o=6&oif=webp&pid=SANGAM'}
        ]

        users = []
        for user_data in users_data:
            existing_user = User.query.filter_by(first_name=user_data['first_name'], last_name=user_data['last_name'], image_url=user_data['image_url']).first()
            if not existing_user:
                new_user = User(**user_data)
                db.session.add(new_user)
                users.append(new_user)
            else:
                users.append(existing_user)

        db.session.commit()

        # Create tags if they do not exist
        tag_names = ['Economics', 'Computer Science', 'Programming', 'Philosophy']
        tags = []
        for name in tag_names:
            existing_tag = Tag.query.filter_by(name=name).first()
            if not existing_tag:
                tag = Tag(name=name)
                tags.append(tag)
                db.session.add(tag)
            else:
                tags.append(existing_tag)

        db.session.commit()

        # Create some posts
        post1 = Post(title='The Wealth of Nations', content='Adam Smith\'s seminal work, "The Wealth of Nations," laid the foundation for modern economics, introducing key concepts such as the invisible hand and division of labor.', user=users[0], tags=[tags[0]])
        post2 = Post(title='An Inquiry into the Nature and Causes of the Wealth of Nations', content='Adam Smith\'s "An Inquiry into the Nature and Causes of the Wealth of Nations" revolutionized economic thought, advocating for free markets and minimal government intervention.', user=users[0], tags=[tags[0]])
        post3 = Post(title='The Conway Criterion', content='Anne Conway\'s philosophical work introduced the "Conway Criterion," a principle of causality that posits that everything must have a cause, laying the groundwork for her holistic metaphysics.', user=users[1], tags=[tags[3]])
        post4 = Post(title='Conway\'s Metaphysical Musings', content='Anne Conway delved into the realm of metaphysics with her intricate philosophical treatises, exploring the nature of substance, essence, and existence.', user=users[1], tags=[tags[3]])
        post5 = Post(title="Ada's Algorithmic Insights", content="Ada Lovelace, often regarded as the world's first computer programmer, made significant contributions to computing with her visionary insights into algorithms and computation.", user=users[3], tags=[tags[1], tags[2], tags[3]])
        post6 = Post(title="Breaking the Enigma Code", content="Alan Turing's groundbreaking work at Bletchley Park during World War II, where he played a pivotal role in breaking the German Enigma code, helped shorten the war and save countless lives.", user=users[2], tags=[tags[1], tags[2]])
        post7 = Post(title="The Analytical Engine and Beyond", content="Ada Lovelace's collaboration with Charles Babbage on the Analytical Engine laid the foundation for modern computing, demonstrating her pioneering vision of what machines could achieve.", user=users[3], tags=[tags[1], tags[2], tags[3]])

        db.session.add_all([post1, post2, post3, post4, post5, post6, post7])
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_database()
