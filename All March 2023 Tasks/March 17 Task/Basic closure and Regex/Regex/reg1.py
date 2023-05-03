# Regualr Expressions is a declarative mechanism to represent a group of Strings accroding to
# particular format/pattern
import re
pattern = re.compile("ab")      # compile() function to compile a pattern into RegexObject.
print(pattern)
print(type(pattern))