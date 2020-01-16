from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(255))
    ListPrice = db.Column(db.String(50))
    # DollarsOff = db.Column(db.String(50))
    # NetPrice = db.Column(db.String(50))
    # Off = db.Column(db.String(50))
    # HarmonyCost = db.Column(db.String(50))
    # CostConcession = db.Column(db.String(50))
    # SpecialCost = db.Column(db.String(50))
    # Comments = db.Column(db.String(255))

    def __repr__(self):
        return '<Post %s>' % self.title


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title","content","ListPrice")
        # , "DollarsOff", "NetPrice","Off","HarmonyCost","CostConcession","SpecialCost","Comments")


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)

    def post(self):
        new_post = Post(
            title=request.json['title'],
            content=request.json['content'],
            ListPrice=request.json['ListPrice'],
            # DollarsOff=request.json['DollarsOff'],
            # NetPrice=request.json['NetPrice'],
            # Off=request.json['Off'],
            # HarmonyCost=request.json['HarmonyCost'],
            # CostConcession=request.json['CostConcession'],
            # SpecialCost=request.json['SpecialCost'],
            # Comments=request.json['Comments']
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)


class PostResource(Resource):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post_schema.dump(post)

    def patch(self, post_id):
        post = Post.query.get_or_404(post_id)

        if 'title' in request.json:
            post.title = request.json['title']
        if 'content' in request.json:
            post.content = request.json['content']

        db.session.commit()
        return post_schema.dump(post)

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        post.delete()
        db.session.commit()
        return '', 204


api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')


if __name__ == '__main__':
    app.run(debug=True)
