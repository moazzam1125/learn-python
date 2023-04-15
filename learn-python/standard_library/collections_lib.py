import collections

# OrderedDict
''' Dictionary that remembers insertion order '''

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['sector'] = 'OrderedDict'
ordered_dict['module'] = 'collections'

for key, value in ordered_dict.items():
    print(key + " of " + value)