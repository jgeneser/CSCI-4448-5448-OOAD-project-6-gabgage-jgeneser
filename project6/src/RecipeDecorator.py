#The recipeDecorator class demonstrates the decorator pattern
#The decorator takes in a recipe object and decocorates it with either a comment or review depending on what the user inputs

class RecipeDecorator:
    def __init__(self, recipe):
        self.recipe = recipe

class ReviewDecorator(RecipeDecorator):
    def __init__(self, recipe, review):
        super().__init__(recipe)
        self.review = review

    def display(self, review):
        print("Review: " + review)


class CommentDecorator(RecipeDecorator):
    def __init__(self, recipe, comment):
        super().__init__(recipe)
        self.comment = comment

    def display(self, comment):
        print("Comment: " + comment)