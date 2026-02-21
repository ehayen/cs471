import tensorflow_datasets as tfds

# setup local path
local_path = "./data"

ds = tfds.load('rock_paper_scissors',
               data_dir=local_path,
               download=True,
               as_supervised=True,
               with_info=True)

print("Download finished.")

