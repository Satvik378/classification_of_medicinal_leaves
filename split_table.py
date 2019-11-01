# for splitting the dataset into tain,test and validation dataset.
import split_folders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
# split_folders.ratio('/home/satvik/Downloads/major/satu/satu', output="output", seed=1337, ratio=(.8, .1, .1)) # default values

# Split val/test with a fixed number of items e.g. 100 for each set.
# To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
split_folders.fixed('/home/satvik/Downloads/major/satu', output="/home/satvik/Downloads/major/dataset", seed=1337, fixed=(50, 50), oversample=False) # default values
