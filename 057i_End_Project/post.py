class Post:
    def __init__(self, blog):
        self.posts = {post['id']: post for post in blog}
