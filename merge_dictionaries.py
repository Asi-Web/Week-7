## Asiwome Agbleze
## Trinity Washington University
## CSMS 11/1 - Michael Agee
## March 17, 2026

# Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merge dict1 and dict2 into a new dictionary.
# If a key appears in both, dict2's value will override dict1's value.
merged_dict = dict1.copy()
merged_dict.update(dict2)

# Print the merged dictionary
print(merged_dict)