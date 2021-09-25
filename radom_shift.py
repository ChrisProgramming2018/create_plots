import torch
import cv2
import torch.nn as nn
import kornia
import numpy as np

from replay_buffer_depth import ReplayBufferDepth


size= 256
memory = ReplayBufferDepth((size, size), (size,size,3), (size, size, 3), 50, "cuda")
#memory.load_memory("depth_memory5k")
memory.load_memory("real_world_depth_buffer-50")


state = memory.obses[0]
print(state.shape)


#cv2.imshow("surface_image", state[:,:,[2,1,0]])
cv2.waitKey(0)
image_pad = 4
obs_shape = (3, 256, 256)
aug_trans = nn.Sequential(
        nn.ReplicationPad2d(image_pad),
        kornia.augmentation.RandomCrop((obs_shape[-1], obs_shape[-1])))

state = state.transpose(2,0,1)
print("transpos", state.shape)
state = torch.as_tensor(state, device="cuda").float()

print(state.shape)
obs = state.unsqueeze(0)
print(obs.shape)
#obs = memory.obses[[0,1]]
#obs = torch.as_tensor(obs, device="cuda").float()
state = aug_trans(obs)
state = state.cpu().numpy().squeeze(0)
state = state.transpose(1,2,0)
#cv2.imshow("surface_image", state[:,:,[2,1,0]])
print(state[0])
state = np.array(state, dtype=np.uint8)
print(state[0])
cv2.imshow("surface_image", state[:,:,[2,1,0]])
#cv2.imshow("surface_image", state)
cv2.waitKey(0)

print(state.shape)
