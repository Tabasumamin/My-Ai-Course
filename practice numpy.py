import numpy as np

brokered_by, status,price,bed = np.genfromtxt(
    'My-Ai-Course/RealEstate-USA.csv',
    delimiter=",",
    usecols=(0,1,2,3),
    unpack=True,
    dtype=None,
    skip_header=1
    )
print(brokered_by)
print(status)
print(price)
print(bed)
# Statistics operations
print('RealEstate-USA mean:' , np.mean(price))
print('RealEstate-USA median:' , np.median(price))
print("RealEstate-USA min:" , np.min(price))
print("RealEstate-USA max:", np.max(price))
print("RealEstate-USA sum:", np.sum(price))
print("RealEstate-USA std:" , np.std(price))

# Perform basic arithmetic operations
print
