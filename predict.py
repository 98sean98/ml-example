import os
import math
import typing
import json

import torch

from model import Model, generate_features


base_directory = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(base_directory, "artifacts", "model.pt")

model = Model()
model.load_state_dict(torch.load(model_path))
model.eval()


def predict(i: typing.List[float]):
    # turn input into a tensor, and generate faetures
    x = torch.Tensor(i)
    xx = generate_features(x)

    # run prediction
    y = model(xx)

    # convert to list of scalars
    output = y.tolist()

    return output

if __name__ == "__main__":
    i = [math.pi/4, math.pi*3/4]
    print("input: {}".format(i))
    output = predict(i)
    print("output: {}".format(output))
