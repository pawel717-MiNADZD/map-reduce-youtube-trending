#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_category_id = None
current_interactions_count = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    category_id, likes, dislikes, comment_count = line.split('\t')

    # convert to int
    try:
        interactions_count = int(likes) + int(dislikes) + int(comment_count)
    except ValueError:
        # not a number, so silently discard this line
        continue


    if current_category_id == category_id:
        current_interactions_count += interactions_count
    else:
        if current_category_id:
            print '%s\t%s' % (current_category_id, current_interactions_count)
        current_interactions_count = interactions_count
        current_category_id = category_id

if current_category_id == category_id:
    print '%s\t%s' % (current_category_id, current_interactions_count)
