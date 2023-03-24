import clip
import os
from PIL import Image
import numpy as np
import torch

device = 'cpu'
model_path = "weights/ViT-B-32.pt"

model, preprocess = clip.load(model_path)


def get_emb(image_folder):
    image_folder = image_folder
    image_paths = []
    for filename in os.listdir(image_folder):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                    image_path = os.path.join(image_folder, filename)
                    image_paths.append(image_path)
            paths = image_paths
    images = [Image.open(path) for path in image_paths]
    with torch.no_grad():
        features = []
        for image in images:
            image_tensor = preprocess(image).unsqueeze(0).to(device)
            feature = model.encode_image(image_tensor)
            features.append(feature.detach().cpu().numpy())
        features = np.array(features)
    np.save("emb_images.npy", features)
    return features, paths
        
    

            