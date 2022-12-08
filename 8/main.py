import numpy as np

with open('input.txt', 'r') as f:
    forest = []
    while line := f.readline():
        forest.append(list(line.strip()))

    forest = np.array(forest).astype(np.uint8)



# Keep track of visible trees
is_visible = np.zeros_like(forest)
scenic_score = np.zeros_like(forest).astype(np.uint32)

# Bordering trees are all visible
is_visible[0,:] = 1
is_visible[:,0] = 1
is_visible[-1,:] = 1
is_visible[:,-1] = 1

# Iterate over every tree
for y in range(1, forest.shape[0] - 1):
    for x in range(1, forest.shape[1] - 1):
        # Get list of trees in each direction
        tree = forest[y, x]
        top = np.flip(forest[:y, x].flatten())
        bot = forest[y + 1:, x].flatten()
        right = forest[y, x + 1:].flatten()
        left = np.flip(forest[y, :x].flatten())

        # Check if the tree is visible
        if (top < tree).all():
            is_visible[y, x] = 1
        elif (bot < tree).all():
            is_visible[y, x] = 1
        elif (right < tree).all():
            is_visible[y, x] = 1
        elif (left < tree).all():
            is_visible[y, x] = 1

        # Calculate the scenic score
        score = 1
        if (top >= tree).any():
            score *= np.argmax(top >= tree) + 1
        else:
            score *= len(top)
        if (bot >= tree).any():
            score *= np.argmax(bot >= tree) + 1
        else:
            score *= len(bot)
        if (right >= tree).any():
            score *= np.argmax(right >= tree) + 1
        else:
            score *= len(right)
        if (left >= tree).any():
            score *= np.argmax(left >= tree) + 1
        else:
            score *= len(left)
        scenic_score[y, x] = score

print(f'(1) Number of visible trees {np.count_nonzero(is_visible)}')
print(f'(2) Total scenic score: {np.max(scenic_score)}')
