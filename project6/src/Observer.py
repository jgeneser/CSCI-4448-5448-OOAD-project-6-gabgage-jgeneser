from Recipe import Recipe  # Import the display_recipes function

# Observer interface
class RecipeObserver():
    def update(self, recipe):
        pass


# Concrete Observer
class RecipePrinter(RecipeObserver):
    def update(self, recipe):
        print()
        print("Recipe Updated!")
        print()
        print("==== " + recipe + " ====")


# Subject
class RecipeManager:
    def __init__(self):
        self._observers = set()
        self._recipes = set()

    def add_observer(self, observer):
        self._observers.add(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, recipe):
        for observer in self._observers:
            observer.update(recipe)

    def update_recipe(self, recipe):
        self.notify_observers(recipe)

