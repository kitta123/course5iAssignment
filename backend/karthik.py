import json
from flask import Flask, request, flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from flask_marshmallow import Marshmallow
# from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '6a7cabb8e92dfc7883c03862336f9624'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///focus.db'
db = SQLAlchemy(app)
# ma = Marshmallow(app)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ListPrice = db.Column(db.String(10))
    DollarsOff = db.Column(db.String(10))
    NetPrice = db.Column(db.String(10))
    Off = db.Column(db.String(10))
    HarmonyCost = db.Column(db.String(10))
    CostConcession = db.Column(db.String(10))
    SpecialCost = db.Column(db.String(10))
    Comments = db.Column(db.String(10))

    def __repr__(self):
        return f"POST('{self.id}','{self.ListPrice}','{self.DollarsOff}','{self.NetPrice}','{self.Off}','{self.HarmonyCost}','{self.CostConcession}','{self.SpecialCost}','{self.Comments}')"


# class PostSchema(ma.Schema):
#     class Meta:
#         fields = ("id","ListPrice", "DollarsOff", "NetPrice","Off","HarmonyCost","CostConcession","SpecialCost","Comments")
#
#
# post_schema = PostSchema()
# posts_schema = PostSchema(many=True)

@app.route("/postprice", methods=['GET','POST'])
def PostListResource():
    if request.method == 'GET':
        list = []
        posts = Post.query.all()
        for post in posts:
            dict = {}
            dict['id'] = post.id
            dict['ListPrice'] = post.ListPrice
            dict['DollarsOff'] = post.DollarsOff
            dict['NetPrice'] = post.NetPrice
            dict['Off'] = post.Off
            dict['HarmonyCost'] = post.HarmonyCost
            dict['CostConcession'] = post.CostConcession
            dict['SpecialCost'] = post.SpecialCost
            dict['Comments'] = post.Comments
            list.append(dict)
        # flash('Succefully get the data')
        # posts = {'id':str(posts.id),'ListPrice':str(posts.ListPrice),"DollarsOff":str(posts.DollarsOff), "NetPrice":str(posts.NetPrice),"Off":str(posts.Off),"HarmonyCost":str(posts.HarmonyCost),"CostConcession":str(posts.CostConcession),"SpecialCost":str(posts.SpecialCost),"Comments":str(posts.Comments)}
        return jsonify(list)

    else:
        data = request.get_json()
        new_post = Post(
        id = data['id'],
        ListPrice=data['ListPrice'],
        DollarsOff=data['DollarsOff'],
        NetPrice=data['NetPrice'],
        Off=data['Off'],
        HarmonyCost=data['HarmonyCost'],
        CostConcession=data['CostConcession'],
        SpecialCost=data['SpecialCost'],
        Comments=data['Comments']
        )
        db.session.add(new_post)
        db.session.commit()
        flash('Succefully post the data')


# class GetResource(Resource):
#     def get(self):
#         post = Post.query.all()
#         return post_schema.dump(post)

    # def get(self):
    #     post = Post.query.all()
    #     return post_schema.dump(post)
    # def patch(self, post_id):
    #     post = Post.query.get_or_404(post_id)
    #
    #     if 'title' in request.json:
    #         post.title = request.json['title']
    #     if 'content' in request.json:
    #         post.content = request.json['content']
    #     if 'content' in request.json:
    #         post.content = request.json['ListPrice']
    #
    #     db.session.commit()
    #     return post_schema.dump(post)
    #
    # def delete(self, post_id):
    #     post = Post.query.get_or_404(post_id)
    #     post.delete()
    #     db.session.commit()
    #     return '', 204


# @app.route('/getlist', methods = ['GET'])
# def index():
#     return jsonify({'price list': PostListResource.query.all()})

# api.add_resource(PostListResource, '/postprice')
# # api.add_resource(PostListResource, '/getlist')
# api.add_resource(GetResource, '/getprice')


if __name__ == '__main__':
    app.run(debug=True)
