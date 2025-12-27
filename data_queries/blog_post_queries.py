from models.blog_post import BlogPost
from models.result_message import ResultMessage
from extensions import db


class BlogPostQueries:

    def add_cafe(self, post):
        try:
            print("=============> adding post to DB")
            present_post = self.get_post_by_title(post.title)
            print(f"present_post ==========> {present_post}")

            if present_post.get("result") == "":
                print("=========> adding")
                db.session.add(post)
                db.session.commit()

                print("=============> finished adding post to DB")

                message = ResultMessage("", "success", f"post '{post.title}' successfully added", 200)
                print(message.message)
                return message.get_message()

            else:
                message = ResultMessage("", "info", f"post '{post.title}' already exists", 403)
                print(message.message)
                return message.get_message()



        except Exception as e:
            message = ResultMessage("","error", f"Error adding post into DB: {e}", 500)
            print(message.message)
            return message.get_message()


    def get_post_by_title(self, title):

        try:
            print("=============> getting post from DB")

            post = BlogPost.query.filter_by(title=title).all()
            print(f"post ==========> {post}")

            if len(post) == 0:
                message = ResultMessage("", "error", f"No such post is present", 403)
                print("=============> finished getting post from DB")
                return message.get_message()

            else:
                message = ResultMessage(post[0], "success", f"post '{title}' successfully fetched", 200)
                print("=============> finished getting post from DB")
                print(f"result =========> {message.result}")
                return message.get_message()



        except Exception as e:
            message = ResultMessage("", "error", f"Error getting post from DB: {e}", 500)
            print(message.message)
            return message.get_message()


    def get_all_posts(self):
        try:
            print("=============> getting all posts from DB")

            posts = BlogPost.query.all()
            print(f"posts ==========> {posts}")

            print("=============> finished getting all posts from DB")

            message = ResultMessage(posts, "success", f"all posts fetched", 200)

            return message.get_message()

        except Exception as e:
            message = ResultMessage("", "error", f"Error getting posts from DB: {e}", 500)
            print(message.message)
            return message.get_message()


    def get_post_by_id(self, post_id):
        try:
            print("=============> getting post by id from DB")

            post = BlogPost.query.filter_by(id=post_id).all()

            if len(post) == 0:
                message = ResultMessage("", "error", f"No such post is present", 403)
                print("=============> finished getting post by id from DB")
                return message.get_message()
            else:
                print(f"post ==========> {post}")
                message = ResultMessage(post[0], "success", f"post '{post[0].title}' successfully fetched", 200)
                print("=============> finished getting post from DB")
                return message.get_message()

        except Exception as e:
            message = ResultMessage("", "error", f"Error getting post by id from DB: {e}", 500)
            print(message.message)
            return message.get_message()


    def update_post(self, edited_post, requested_post):
        try:
            print("=============> updating post")

            requested_post.title = edited_post.title
            requested_post.subtitle = edited_post.subtitle
            requested_post.author = edited_post.author
            requested_post.body = edited_post.body
            requested_post.img_url = edited_post.img_url

            db.session.add(requested_post)
            db.session.commit()


            print("=============> finished updating post")

        except Exception as e:
            message = ResultMessage("", "error", f"Error updating post: {e}", 500)
            print(message.message)
            return message.get_message()

    def delete_post(self, post_id):
        try:
            print("=============> deleting post")

            post_to_delete = self.get_post_by_id(post_id)["result"]
            print(f"post_to_delete======> {post_to_delete}")

            db.session.delete(post_to_delete)
            db.session.commit()

            print("=============> finished deleting post")

            message = ResultMessage("", "success", f"post '{post_to_delete.title}' successfully deleted", 200)
            print(f"error =============> {message.message}")
            return message.get_message()


        except Exception as e:
            message = ResultMessage("", "error", f"Error deleting post: {e}", 500)
            print(message.message)
            return message.get_message()
