from keyword import iskeyword


def contains_keyword(*words):
    return any([w for w in words if iskeyword(w)])


print(contains_keyword("def", "goodbye"))