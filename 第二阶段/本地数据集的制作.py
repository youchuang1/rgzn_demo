import torch
from torch import nn
from torchvision.io import read_image
from torch.utils.data import Dataset
from PIL import Image
import os


class Mask_dataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None, ):
        self.landmarks_frame = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.landmarks_frame)

    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, self.landmarks_frame.iloc[idx, 0])
        label = self.landmarks_frame.iloc[idx, 1]
        img = Image.open(img_path).convert("RGB")
        if self.transform is not None:
            img = self.transform(img)
        return img, label
