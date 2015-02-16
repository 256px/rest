from app.repository.story import StoryRepository


class UpdateStory:

    def __init__(self, repository=StoryRepository):
        self.repository = repository()

    def update_story(self, id, data):
        return self.repository.update_story(id, data)
