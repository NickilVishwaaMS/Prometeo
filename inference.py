import torch
from torchvision import models, transforms
from PIL import Image

# Create an instance of the model
# Updated to use weights=None as per the latest torchvision API
model = models.mobilenet_v2(weights=None)

# Load the state dict into the model
state_dict = torch.load('./models/MobileNetV2_checkpoint.pt')  # Adjust path as needed
model.load_state_dict(state_dict)

model.eval()  # Set the model to evaluation mode

def predict(image_path):
    # Transform the image
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    image = Image.open(image_path)
    image_tensor = transform(image).unsqueeze(0)

    # Predict
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
        return predicted.item()

predicted_class = predict('./Data/Moderate Dementia/OAS1_0308_MR1_mpr-1_101.jpg')
print("Predicted Class:", predicted_class)
