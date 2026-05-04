from app import app, db
from models import Post, User

with app.app_context():
    posts = Post.query.all()
    print(f"Total posts: {len(posts)}")
    for post in posts:
        print(f"Post ID: {post.id}, Title: {post.title}, Author: {post.author}")
        if post.author is None:
            print(f"WARNING: Post {post.id} has no author! This will cause a 500 error in the template.")
    
    users = User.query.all()
    print(f"Total users: {len(users)}")
    for user in users:
        print(f"User ID: {user.id}, Username: {user.username}")
