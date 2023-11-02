from flask_restful import fields

post_serlizer = {
  "id": fields.Integer,
  "title": fields.String,
  "body": fields.String,
  "image": fields.String,
  "category_id": fields.Integer,
}