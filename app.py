import re

init = "Bob is a Bird... Bob is a Plane... Bob is Superman!"
changed = re.sub(r"Bob is", "It's", init) # Noncompliant
changed = re.sub(r"\.\.\.", ";", changed) # Noncompliant

print('Hellooo World !!') 