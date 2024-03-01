import os
import pytz


STATUS=(
    ('active', "Active"),
     ('inactive', "Inactive"),
      ('deleted', "Deleted"),
)

STATUS_DICT= dict(STATUS)

CATEGORIES= (
    ('hot', "HOT"),
    ('cold', "COLD"),
    ('bagel', "BAGEL"),
)

CATEGORIES_DICT= dict(CATEGORIES) 