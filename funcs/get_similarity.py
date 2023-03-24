import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
import os
import clip
import numpy as np
import torch.nn.functional as F
import matplotlib.pyplot as plt
import cv2

device = 'cpu'
model_path = "weights/ViT-B-32.pt"

model, preprocess = clip.load('ViT-B/32', device)

def get_similarity_score(text_query, image_features):
    text_tokens = clip.tokenize([text_query]).to(device)
    with torch.no_grad():
        text_features = model.encode_text(text_tokens).squeeze(0)
        text_features= F.normalize(text_features, p=2, dim=-1)
        similarity_score = text_features @ image_features.T * 100.0
        similarity_score = similarity_score.squeeze(0)
    return similarity_score

def create_filelist(path_to_imagefolder):
        image_folder = path_to_imagefolder
        image_paths = []
        for filename in os.listdir(image_folder):
                if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                        image_path = os.path.join(image_folder, filename)
                        image_paths.append(image_path)
                file_paths = image_paths
        return file_paths

def load_embeddings(path_to_emb_file):
    features = np.load(path_to_emb_file)
    features = torch.from_numpy(features)
    return features


def find_matches(image_embeddings, query, image_filenames, n=6):
    text_query = query
    features = image_embeddings
    similarity_scores = []
    for emb in features:
        emb /= emb.norm(dim=-1, keepdim=True)
        similarity_score = get_similarity_score(text_query, emb)
        similarity_scores.append(similarity_score)
    similarity_scores = torch.stack(similarity_scores)
    values, indices = torch.topk(similarity_scores.squeeze(0), 6)
    matches = [image_filenames[idx] for idx in indices]
    return matches