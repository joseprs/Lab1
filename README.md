#### Josep Reverter Sancho (205571)
# Lab1
Repository for Lab 1

#### 1. Translator from RGB to YUV and YUV to RGB
The code is in scripts/rgb_yuv.py

#### 2. Resize Lenna.png
The command used to resize Lenna.png is shown in images/LennaResize(2).png, and the result is Lenna240x240.png.
If we observe the Lenna.png and Lenna240x240.png, we can see than the second one is smaller in size, that means that it has lower resolution, and obviously, the visualization is not that good.

#### 3. Transform Lenna.png into b/w and compress
The command used to transform Lenna.png into b/w image is shown in images/LennaBW(3).png. It is done with FFMpeg command, setting hue and saturation of the image to 0. We can see the result on images/LennaBW.png. Then, to compress we have done the command that is shown in images/Compression(3).png, and the image is LennaBWC.png.
The b/w compression was a success. We have compressed with the maximum compression (100), and the compression was not very significative, but we can see some compression.

#### 4. Run-Length
Code in scripts/run_lenght.py

#### 5. DCT
Code in scripts/DCT.py


