from app.repository.story import StoryRepository


class GetStories:

    def __init__(self, repository=StoryRepository):
        self.repository = repository()

    def get_stories(self):
        return self.repository.get_stories()
