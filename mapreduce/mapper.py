#!/usr/bin/env python
"""mapper.py"""

import sys
import re
import csv

input = sys.stdin
csv_reader = csv.reader(input)

# skip first line in file which is header describing data columns
csv_reader.next()
labels = ["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time",
          "tags", "views", "likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled",
          "ratings_disabled", "video_error_or_removed", "description"]
labels_indices = dict(zip(labels, range(len(labels))))

for data_row in csv_reader:
	# extract informations that are important
    print '%s\t%s\t%s\t%s' % (data_row[labels_indices['category_id']],
                          data_row[labels_indices['likes']],
                          data_row[labels_indices['dislikes']],
                          data_row[labels_indices['comment_count']])
