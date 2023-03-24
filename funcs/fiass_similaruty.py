import torch
import numpy as np
import clip
import torch.nn.functional as F
import faiss
import os

device = 'cpu'

model, preprocess = clip.load('ViT-B/32', device)

def load_embeddings(path_to_emb_file):
    features = np.load(path_to_emb_file).astype('float32')
    features = torch.from_numpy(features)
    features = features.squeeze(1)
    features = F.normalize(features, p=2, dim=-1)
    return features

def encode_text(query):
    text = clip.tokenize([query]).to(device)
    text_features = model.encode_text(text).to("cpu")
    text_features= F.normalize(text_features, p=2, dim=-1)
    text_features = text_features.to("cpu").detach().numpy()
    return text_features


def find_matches_fiass(image_embeddings, query, image_filenames, n=5):
    features = image_embeddings
    index = faiss.IndexFlatL2(features.shape[1])
    index.add(features)
    text_features = encode_text(query)
    _, I = index.search(text_features, n)
    matches = [image_filenames[idx] for idx in I.squeeze(0)]
    return matches 

def create_filelist(path_to_imagefolder):
        image_folder = path_to_imagefolder
        image_paths = []
        image_names = os.listdir(image_folder)
        image_names.sort()
        image_names.sort(key=len)
        for filename in image_names:
                if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                        image_path = os.path.join(image_folder, filename)
                        image_paths.append(image_path)
                file_paths = image_paths
        return file_paths