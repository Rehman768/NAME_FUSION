# Function to merge slices of strings from a list of names
def merge_slice_strings(names):
    # List to store unique merged names
    merged_names = []
    
    # Iterate over each name in the list
    for i in range(len(names)):
        # Pair each name with other names in the list
        for j in range(len(names)):
            # Ensure the two indices are not equal
            if i != j:
                # Merge slices of the two names to create a new merged name
                merged_name = names[i][:len(names[i]) // 2] + names[j][len(names[j]) // 2:]
                # Check if the merged name is unique
                if merged_name not in merged_names:
                    # Append unique merged name to the list
                    merged_names.append(merged_name)
    
    # Return the list of unique merged names
    return merged_names

# Get input from the user for the number of names
num_names = int(input("Enter the number of names: "))
names = []

# Get names from the user
for i in range(num_names):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

# Generate and print unique merged slice string names
merged_names = merge_slice_strings(names)
print("Unique Merged Slice String Names:")
for i, merged_name in enumerate(merged_names, start=1):
    print(f"{i}. {merged_name}")
