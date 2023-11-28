import re
from collections import Counter

# Define the regex patterns for each mask type
patterns = {
    "?d": r"\d",
    "?l": r"[a-z]",
    "?u": r"[A-Z]",
    "?s": r"[^\w\s]"
}

# Define a function to generate password masks
def generate_mask(password):
    mask = ""
    for char in password:
        for pattern in patterns.values():
            if re.match(pattern, char):
                mask += list(patterns.keys())[list(patterns.values()).index(pattern)]
                break
    return mask

# Read in the passwords file and generate masks for each password
passwords = []
masks = []
with open("passwords.txt", "r") as f:
    for line in f:
        password = line.strip()
        passwords.append(password)
        masks.append(generate_mask(password))

# Count the frequency of each mask and print out the top three most common masks
mask_counts = Counter(masks)
for mask, count in mask_counts.most_common(3):
    print(f"{mask} : {count} ")
