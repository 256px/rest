from app.repository.story import StoryRepository


class RemoveStory:

    def __init__(self, repository=StoryRepository):
        self.repository = repository()

    def remove_story(self, id):
        return self.repository.delete_story_by_id(id)
