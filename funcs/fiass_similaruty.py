import torch
import numpy as np
import clip
import torch.nn.functional as F
import faiss

device = 'cpu'
model_path = "weights/ViT-B-32.pt"

model, preprocess = clip.load('ViT-B/32', device)

def load_embeddings(path_to_emb_file):
    features = np.load(path_to_emb_file)
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