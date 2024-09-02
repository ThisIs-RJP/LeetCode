#!/usr/bin/env python3

from collections import Counter

# Example list of strings
your_list = ["A", "A", "A", "B", "B", "B",]

# Combine the list into a single string
combined_string = ''.join(your_list)

# Get the frequency of each letter
letter_frequencies = Counter(combined_string)

# Print the frequencies
print(letter_frequencies)

k = 2 ### Cooler
accounted = {}
i = 0

while len(accounted) != len(your_list):
    task = your_list[0]

    if your_list[0] not in accounted:
        accounted[your_list[0]] = k
     