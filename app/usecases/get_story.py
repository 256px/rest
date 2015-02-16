from app.repository.story import StoryRepository


class GetStory:

    def __init__(self, repository=StoryRepository):
        self.repository = repository()

    def get_story(self, id):
        return self.repository.get_story_by_id(id)
