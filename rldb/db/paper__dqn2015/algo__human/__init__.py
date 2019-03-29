from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Human",
    "algo-nickname": "Human",

    # HYPERPARAMETERS
    "algo-frames": 0,  # TODO Unsure
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49