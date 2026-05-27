import pickle
import os

pkl_file = "c:\\Users\\Administrator\\code\\test\\paper\\dataset\\WESAD\\S2\\S2.pkl"
with open(pkl_file, 'rb') as f:
    data = pickle.load(f, encoding='latin1')

print("Keys in pickle:")
print(data.keys())

print("\nSubject:")
print(data['subject'])

print("\nLabel shape:")
print(data['label'].shape)

print("\nChest signals:")
for k, v in data['signal']['chest'].items():
    print(f"  {k}: shape {v.shape}")

print("\nWrist signals:")
for k, v in data['signal']['wrist'].items():
    print(f"  {k}: shape {v.shape}")
