import torch


def generate_features(x):
    # Prepare the input tensor (x, x^2, x^3).
    p = torch.tensor([1, 2, 3])
    return x.unsqueeze(-1).pow(p)


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(3, 1)
        self.flatten = torch.nn.Flatten(0, 1)

    def forward(self, x):
        x = self.linear(x)
        return self.flatten(x)
