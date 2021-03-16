from collections import Counter

_str = "sdlfnlfvjnslfvkjnsldfkvnsldfkjvnslfjkvndfljvkn"

print(str(Counter(_str).most_common()).replace("', ", " = ").replace("), ('", " \n").replace("[('", "").replace(")]", ' '))