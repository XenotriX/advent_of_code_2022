# Keep a count of the number of lines where one of the ranges is fully contained in the other range
fully_contained_count = 0

# Keep a count of the number of lines where the two ranges overlap at all
overlap_count = 0

# Open the file for reading
with open("input.txt", "r") as file:
    # Iterate over each line in the file
    for line in file:
        # Split the line into the two ranges
        range1, range2 = line.strip().split(",")

        # Split each range into its start and end values
        start1, end1 = map(int, range1.strip().split("-"))
        start2, end2 = map(int, range2.strip().split("-"))

        # Check if one of the ranges is fully contained in the other range
        if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
            # If so, increment the fully contained count
            fully_contained_count += 1
            # Increment the overlap count as well
            overlap_count += 1

        # Check if the two ranges overlap at all
        elif (start1 <= end2 and end1 >= start2) or (start2 <= end1 and end2 >= start1):
            # If so, increment the overlap count
            overlap_count += 1

# Print the fully contained count and the overlap count
print("(1) Fully contained:", fully_contained_count)
print("(2) Overlap:", overlap_count)
