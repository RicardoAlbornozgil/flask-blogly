import unittest
from app import app, db
from models import User, Post, Tag

class TestAppRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up test database and create some sample data."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_db'
        with app.app_context():
            db.create_all()

            # Create sample users
            user1 = User(first_name='John', last_name='Doe')
            user2 = User(first_name='Jane', last_name='Smith')

            # Create sample posts
            post1 = Post(title='First Post', content='Content of the first post', user=user1)
            post2 = Post(title='Second Post', content='Content of the second post', user=user2)

            # Create sample tags
            tag1 = Tag(name='Technology')
            tag2 = Tag(name='Travel')

            # Add objects to session and commit
            db.session.add_all([user1, user2, post1, post2, tag1, tag2])
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests are finished."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()

    def test_root(self):
        """Test root route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_users_index(self):
        """Test users index route."""
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up test database and create a sample user."""
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db.sqlite'
        with app.app_context():
            db.create_all()

            # Create a sample user
            cls.user = User(first_name='John', last_name='Doe', image_url='test.jpg')
            db.session.add(cls.user)
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests are finished."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_creation(self):
        """Test user creation."""
        with app.app_context():
            user = User.query.filter_by(first_name='John').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.last_name, 'Doe')
            self.assertEqual(user.image_url, 'test.jpg')

    def test_post_creation(self):
        """Test post creation."""
        with app.app_context():
            # Load the user object within the app context
            user = User.query.filter_by(first_name='John').first()
            
            # Create the post object with the loaded user object
            post = Post(title='Test Post', content='This is a test post.', user_id=user.id)
            db.session.add(post)
            db.session.commit()

            retrieved_post = Post.query.filter_by(title='Test Post').first()
            self.assertIsNotNone(retrieved_post)
            self.assertEqual(retrieved_post.content, 'This is a test post.')
            self.assertEqual(retrieved_post.user_id, user.id)


    def test_tag_creation(self):
        """Test tag creation."""
        with app.app_context():
            tag = Tag(name='Test Tag')
            db.session.add(tag)
            db.session.commit()

            retrieved_tag = Tag.query.filter_by(name='Test Tag').first()
            self.assertIsNotNone(retrieved_tag)

    def test_post_tag_association(self):
        """Test association between posts and tags."""
        with app.app_context():
            # Load the user object within the app context
            user = User.query.filter_by(first_name='John').first()
            
            # Create the post object with the loaded user object
            post = Post(title='Associated Post', content='This post is associated with a tag.', user_id=user.id)
            db.session.add(post)

            # Create the tag object
            tag = Tag(name='Associated Tag')
            db.session.add(tag)

            # Commit the changes so that the objects get persisted to the database
            db.session.commit()

            # Associate the post with the tag
            post.tags.append(tag)
            db.session.commit()

            # Now, perform the assertions
            self.assertIn(tag, post.tags)
            self.assertIn(post, tag.posts)


if __name__ == '__main__':
    unittest.main()
