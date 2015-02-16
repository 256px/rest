from flask import Flask
from flask.ext.restful import reqparse, Api, Resource

from app.usecases.get_stories import GetStories
from app.usecases.get_story import GetStory
from app.usecases.remove_story import RemoveStory
from app.usecases.update_story import UpdateStory
from app.usecases.add_story import AddStory

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')


parser = reqparse.RequestParser()
parser.add_argument('story', type=str)


class Story(Resource):
    def get(self, story_id):
        usecase = GetStory()
        return usecase.get_story(story_id)

    def delete(self, story_id):
        usecase = RemoveStory()
        usecase.remove_story(story_id)

        return '', 204

    def put(self, story_id):
        args = parser.parse_args()
        story = {'story': args['story']}

        usecase = UpdateStory()
        story = usecase.update_story(story_id, story)

        return story, 201


class StoriesList(Resource):
    def get(self):
        usecase = GetStories()
        return usecase.get_stories()

    def post(self):
        args = parser.parse_args()

        usecase = AddStory()
        story = usecase.add_story(args['story'])

        return story, 201

#
# Actually setup the Api resource routing here
#
api.add_resource(StoriesList, '/stories')
api.add_resource(Story, '/stories/<string:story_id>')


if __name__ == '__main__':
    app.run()
