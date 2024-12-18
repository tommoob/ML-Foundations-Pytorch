import torch
import torch.nn as nn
import torch.nn.functional as F

class MNISTTwoLayerModel(nn.Module):
    def __init__(self):
        super(MNISTTwoLayerModel, self).__init__()
        self.fc1 = nn.Linear(784, 128) 
        self.fc2 = nn.Linear(128, 64) 
        self.fc3 = nn.Linear(64, 10)  

    def forward(self, x):
        x = x.view(-1, 784)
        
        x = F.relu(self.fc1(x))
        
        x = F.relu(self.fc2(x))
        
        x = F.log_softmax(self.fc3(x), dim=1)
        
        return x