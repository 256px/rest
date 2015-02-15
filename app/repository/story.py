class StoryRepository:

    def __init__(self):
        self.stories = {
            '1': {'task': 'build an API'},
            '2': {'task': '?????'},
            '3': {'task': 'profit!'},
        }

    def get_stories(self):
        return self.stories

    def get_story_by_id(self, id):
        return self.stories[id]

    def remove_story_by_id(self, id):
        del self.stories[id]

    def update_story(self, id, story):
        pass

    def add_story(self, story):
        pass

    def get_stories_by_user(self, user):
        pass

    def delete_story_by_id(self, id):
        pass
