from app.repository.story import StoryRepository


class AddStory:

    def __init__(self, repository=StoryRepository):
        self.repository = repository()

    def add_story(self, data):
        return self.repository.add_story(data)
