"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME=40


def bake_time_remaining(n):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_remaning = 40 - n
    return time_remaning

def bake_time_in_minutes(baking_time_started,baking_time_current):
  """Return the elapsed baking time based on start and current time."""
  elapsed_bake_time = baking_time_current - baking_time_started
  return elapsed_bake_time
print(bake_time_in_minutes)
    



# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes."""
    time_spent=2
    return number_of_layers*time_spent



# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes (number_of_layers,elapsed_bake_time):
  """Calculate total elapsed cooking time (prep + bake)."""
  return (preparation_time_in_minutes(number_of_layers) + elapsed_bake_time)