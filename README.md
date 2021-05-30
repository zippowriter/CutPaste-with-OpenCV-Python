# CutPaste-with-OpenCV-Python
This is CutPaste which is one of methods of data augmentation repository.

CutPaste is developed by Google Cloud Ai research team in 2021.

Its paper is here.

[CutPaste: Self-Supervised Learning for Anomaly Detection and Localization](https://arxiv.org/abs/2104.04015)

# How to use
Clone this repository or download code in your root directory of the project.

```bash
git clone https://github.com/zippowriter/CutPaste-with-OpenCV-Python.git CutPaste
```

Then, write in your file as follows.

```Python
import CutPaste
```

Ready!

You can make a cutpaste image as follows.

```Pthon
# cut patch from an original image
patch = cut_patch(sample_img)
# make a cutpaste image
paste = paste_patch(sample_img, patch=patch, rot=60, ratio=1)
```

# Example
### Original Image

