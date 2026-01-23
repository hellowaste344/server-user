import torch 
from torch.utils.data import Dataset, DataLoader, TensorDataset, RandomSampler, SequentialSampler, Sampler
x = torch.tensor([1.0, 2.0, 3.0])
print("1D Tensor: \n", x)

y = torch.zeros((3,3))
print("2D Tensor: \n", y)

# operations on tensors
a = torch.tensor([1.0, 2.0])
b = torch.tensor([3.0, 4.0])
print("Element wise addition of a & b: \n", a+b)
# .view(r,c) always creates a 2D tensor with 'r' rows and 'c' columns
print("matrix multiplication of a & b: \n", torch.matmul(a.view(2,1), b.view(1,2)))

t = torch.tensor([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
print("Reshaping")
print(t.reshape(6,2))

print("\nResizing")
print(t.view(2,6))

print("\nTransposing")
print(t.transpose(0,1)) #swap rows and columns


#autograd and computational graphs
x = torch.tensor(2.0, requires_grad=True)
y = x.pow(2).sum()
y.backward() #compute ∂y/∂x
print(x.grad) #implement the value 
#output tensor(4.)

# building neural networks in pytorch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        #Call the parent class’s method
        super(NeuralNetwork, self).__init__()
        # we created 3 fully connected (dense) layer
        self.fc1 = nn.Linear(10,16)
        self.fc2 = nn.Linear(16,8)
        self.fc3 = nn.Linear(8,1)
    # define how data flows through the network   
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = NeuralNetwork() #predicts
print(model)

criterion = nn.BCEWithLogitsLoss() #measures errors, expects datatype to be float32 
optimizer = torch.optim.Adam(model.parameters(), lr=0.001) #learns

inputs = torch.randn((100,10)) #100 batches, 10 labels
targets = torch.randint(0,2,(100,1)).float() #100 labels(0 or 1)
epochs = 20

for epoch in range(epochs):
    #clears old gradients before new computation
    optimizer.zero_grad()
    #produces predictions
    outputs = model(inputs)
    #compares predictions vs true labels
    loss = criterion(outputs, targets)
    #stores gradients in param.grad
    loss.backward()
    #reads param.grad uses lr
    optimizer.step()
    
    if (epoch+1) % 5 == 0:
        #loss.item() converts tensor into python number(float) 
        #.4f gets 4 digits after the decimal
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
     
#PyTorch DataLoader
from torchvision import datasets, transforms

# sample dummy image tensors
image_data = torch.randn(1000, 3, 64, 64)
labels = torch.randint(0,10,(1000,)) #1D tensor

dataset = TensorDataset(image_data, labels)

# split into batches
batch_size = 32
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# to view only first iterated batch
for i ,(batch_images, batch_labels) in enumerate(dataloader):
    print(f"Batch shape: {batch_images.shape}, Labels: {batch_labels}")
    if i == 0:
        break   
# MNIST Dataset->loads one simple at a time, dynamic & scalable
train_loader = DataLoader(datasets.MNIST('data', train=True, download=True,
                                         transform=transforms.Compose([
                                             transforms.ToTensor(),
                                             transforms.Normalize((0.1307,), (0.3081,))
                                         ])),
                          batch_size=64, shuffle=True)


# TensorDataset->loads everyting at once, manual & static
# create a synthetic dataset of integers from 0 to 99
data = torch.arange(0, 100) #arange(start, stop, step)
# create dummy targets (just for the sake of having them)
targets = torch.zeros(100)
 
# create a TensorDataset
dataset = TensorDataset(data, targets)

# DataLoader with shuffle=True
dataloader_shuffle = DataLoader(dataset, batch_size=10, shuffle=True)

# DataLoader with shuffle=False
dataloader_noshuffle = DataLoader(dataset, batch_size=10, shuffle=False)

# function to print the first batch of the dataloader
def print_first_batch(dataloader, shuffle_status):
    for batch in dataloader:
        data, _ = batch
        print(f"First batch with shuffle={shuffle_status}: {data}")
        break
# print the first batch of each DataLoader to compare
print_first_batch(dataloader_shuffle, shuffle_status=True)
print_first_batch(dataloader_noshuffle, shuffle_status=False)
#
# Alternative approaches for shuffling with samplers
#

# Random Sampler
t = transforms.ToTensor()
mnist_dataset = datasets.MNIST(root='./data',train=False,download=True,transform=t)
random_sampler = RandomSampler(mnist_dataset)
random_loader = DataLoader(mnist_dataset, batch_size=32, sampler=random_sampler)
x, y = next(iter(random_loader))
print(x)
print(y)
for x, y in random_loader:
    print("x shape:", x.shape)
    print("y shape: ", y.shape)
    break
    
# Sequential Sampler 
sequential_sampler = SequentialSampler(mnist_dataset)
sequential_loader = DataLoader(mnist_dataset, batch_size=32, sampler=sequential_sampler)
for batch_idx, (x,y) in enumerate(sequential_loader):
    print(f"Batch: {batch_idx}")
    print("x:", x)
    print("y:", y)
    break
    
import random
# Custom Sampler
class CustomSampler(Sampler):
    def __init__(self, data_source):
        self.data_source = data_source
        self.indices = list(range(len(data_source)))
    
    def __iter__(self):
        random.shuffle(self.indices)
        return iter(self.indices)
    
    def __len__(self):
        return len(self.indices)
    
custom_sampler = CustomSampler(mnist_dataset)
custom_loader = DataLoader(mnist_dataset, batch_size=32, sampler=custom_sampler)
for x, y in custom_loader:
    print("First sample:", x[0], y[0])
    break


# Processing Data
import matplotlib.pyplot as plt
#preprocess - transform as tensor
transform = transforms.Compose([
    transforms.RandomResizedCrop(224), #resizes it to 224x224
    transforms.RandomHorizontalFlip(), #makes model invariant
    transforms.ToTensor(), #PIL Image->PyTorch Tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

#labels data
train_dataset = datasets.CIFAR10(root='./data', train=True, 
                                 download=True, transform=transform)

#to describe train
#each item(image_tensor, label)
train_dataset

#turns raw data into mini-batches
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

#utilizing collate function for batch-level processing
#Batching variable-length data requires custom logic
from torch.nn.utils.rnn import pad_sequence

class CustomDataset(Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]
    
def custom_collate(batch):
    inputs = [item[0] for item in batch]
    labels = [item[1] for item in batch]
    
    inputs_padded = pad_sequence(inputs, batch_first=True, padding_value=0)
    
    #Dataloader expects tensors 
    #Labels must also be attached
    return inputs_padded, torch.tensor(labels)

# If DataLoader uses workers → always use if __name__ == "__main__":
if __name__ == "__main__":
    # example usage
    data = [(torch.tensor([1,2,3]), 0),
            (torch.tensor([4,5]), 1),
            (torch.tensor([6,7,8,9]), 0)]

    custom_dataset = CustomDataset(data)

    # using worker threads allows multiple samples to be loaded concurrently
    custom_loader = DataLoader(custom_dataset, batch_size=2, collate_fn=custom_collate, num_workers=4)

    for batch_inputs, batch_labels in custom_loader:
        print("Batch Inputs:", batch_inputs)
        print("Batch labels:", batch_labels)
        

# packing the tensors with variable
a = torch.tensor([5.,4.], requires_grad=True)
b = torch.tensor([6.,8.])

# polynomial function with a,b as variable
y = ((a**2)+(5*b))
z = y.mean()
print("Z value is:", z)

# dy/da=2*a=10,8
# dy/db=5

# computing gradient
z.backward()

#printing out
print("Gradient of a", a.grad)
print("Gradient of b", b.grad)
print("Loss:", z.item())

# input (no gradient needed)
x = torch.randn(1, 10)

# parameters (learnable)
w = torch.randn(10, 1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

# target
y = torch.tensor([[0.822]])

# forward pass
y_pred = x @ w + b

# loss (Mean Squared Error)
loss = (y_pred - y).pow(2)
print("Loss:", loss.item())

# backward pass (compute gradients)
loss.backward()

print("Gradient of w:\n", w.grad)
print("Gradient of b:\n", b.grad)

# learning rate
lr = 0.001

# parameter update (gradient descent)
with torch.no_grad():
    w -= lr * w.grad
    b -= lr * b.grad

    # reset gradients after update
    w.grad.zero_()
    b.grad.zero_()

print("Updated weights:\n", w)