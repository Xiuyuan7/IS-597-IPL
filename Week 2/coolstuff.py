joke = "Why did the snake cross the road?"
answer = "Just to be a sneaky snakie"

def bad_animal_joke(animal):
  """Provide a species name and this will return a tuple of the joke an answer"""
  assert isinstance(animal, str)
  joke = "Why did the " + animal.lower() + " cross the road?"
  answer = "To get to the " + animal.lower() + " club."
  return (joke, answer)
  