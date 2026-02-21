import torch
import torchvision.models as models

model = models.squeezenet1_1(pretrained=True)
model.eval()

print(f"PyTorch version: {torch.__version__}")
print("Model ready.")