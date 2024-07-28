"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        [
    {
        "input": [20.0],
        "answer": (68.0, "Ameno")
    },
    {
        "input": [-500.0],
        "answer": "Temperatura não realista"
    },
    {
        "input": [10.0],
        "answer": (50.0, "Frio")
    },
    {
        "input": [85.0],
        "answer": (185.0, "Quente")
    }
]
    ]
}
