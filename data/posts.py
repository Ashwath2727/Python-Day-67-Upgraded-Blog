import requests

from models.blog_post import BlogPost


class Post:

    def __init__(self):
        self.post_api = "https://api.npoint.io/00b23b65247a891e7d9e"

    def get_posts(self):
        response = requests.get(self.post_api)

        posts_dict = response.json()

        posts = [
            BlogPost(
                title = post["title"],
                subtitle = post["subtitle"],
                date = post["date"],
                body = post["body"],
                author = post["author"],
                img_url = post["image_url"]
            )
            for post in posts_dict
        ]

        print(f"posts = {posts}")
        return posts