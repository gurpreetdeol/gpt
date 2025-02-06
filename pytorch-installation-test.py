import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))  # 0 corresponds to the first GPU
x = torch.rand(5, 3)
print(x)