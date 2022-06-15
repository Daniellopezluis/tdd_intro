# Unittest how-to
Information extracted from [here](https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python)

## Defining a `TestCase` Subclass
One of the most important classes provided by the unittest module is named `TestCase`. 
`TestCase` provides the general scaffolding for testing our functions. Let’s consider an example:

```python
import unittest

def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)
```

First we import `unittest` to make the module available to our code. We then define the function we want to test—here it is `add_fish_to_aquarium`.

In this case our `add_fish_to_aquarium` function accepts a list of fish named `fish_list`, and raises an error if `fish_list` has more than 10 elements. The function then returns a dictionary mapping the name of a fish tank "tank_a" to the given `fish_list`.

A class named `TestAddFishToAquarium` is defined as a subclass of `unittest.TestCase`. A method named `test_add_fish_to_aquarium_success` is defined on `TestAddFishToAquarium`. `test_add_fish_to_aquarium_success` calls the `add_fish_to_aquarium` function with a specific input and verifies that the actual returned value matches the value we’d expect to be returned.

Now that we’ve defined a `TestCase` subclass with a test, let’s review how we can execute that test.

## Executing a `TestCase`

In the previous section, we created a `TestCase` subclass named `TestAddFishToAquarium`. From the same directory as the `test_add_fish_to_aquarium.py` file, let’s run that test with the following command:

```sh
$ python -m unittest test_add_fish_to_aquarium.py
```

We invoked the Python library module named `unittest` with `python -m unittest`. Then, we provided the path to our file containing our `TestAddFishToAquarium` `TestCase` as an argument.

After we run this command, we receive output like the following:

```
Output
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

```

## Assertions
Note: `unittest.TestCase` exposes a number of other methods beyond `assertEqual` and `assertRaises` that you can use. The full list of assertion methods can be found in the [documentation](https://docs.python.org/3/library/unittest.html), but a selection are included here:

| Method | Assertion |
| ------ | ------ |
| assertEqual(a, b) | a == b |
| assertNotEqual(a, b) | a != b |
| assertTrue(a)| bool(a) is True |
| assertFalse(a) | bool(a) is False |
| assertIsNone(a | a is None |
| assertIsNotNone(a) | a is not None |
| assertIn(a, b) | a in b |
| assertNotIn(a, b) | a not in b |