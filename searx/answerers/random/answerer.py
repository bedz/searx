import random
import string
from flask_babel import gettext

# required answerer attribute
# specifies which search query keywords triggers this answerer
keywords = ('random',)

random_int_max = 2**31

random_string_letters = string.lowercase + string.digits + string.uppercase


def random_string():
    return u''.join(random.choice(random_string_letters)
                    for _ in range(random.randint(8, 32)))


def random_float():
    return unicode(random.random())


def random_int():
    return unicode(random.randint(-random_int_max, random_int_max))


random_types = {u'string': random_string,
                u'int': random_int,
                u'float': random_float}


# required answerer function
# can return a list of results (any result type) for a given query
def answer(query):
    parts = query.query.split()
    if len(parts) != 2:
        return []

    if parts[1] not in random_types:
        return []

    return [{'answer': random_types[parts[1]]()}]


# required answerer function
# returns information about the answerer
def self_info():
    return {'name': gettext('Random value generator'),
            'description': gettext('Generate different random values'),
            'examples': [u'random {}'.format(x) for x in random_types]}
