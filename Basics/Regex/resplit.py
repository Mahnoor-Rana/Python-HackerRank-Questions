
import re
regex_pattern = r"(?<=\d)[.,](?=\d)"  # match one or more commas or digits
print("\n".join(re.split(regex_pattern, input())))