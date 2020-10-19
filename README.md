# ACM_Capstone_Project
Generation of images using cGAN

__________
A deep learning model has been deployed to train a conditional generative
adversarial network(cGAN) to learn a mapping from an input image to an output
image by training the network on a dataset of known images using tensorflow.

**INPUT**: Image with incomplete data like having only the edges and semantic
labeling.

**OUTPUT**: An output image built by completing the missing image data that is
close to reality.

cGAN is an architecture to train conditional networks by making use of generators
and discriminators. Our project uses a U-net generator and a patch GAN based
discriminator. The model was successfully able to train the dataset and produce
complete images.


_______

## Salient Features

1. HED edge detection of dataset instead of canny edge detection. Canny edge
detection is more manual and laborious and consequently results in
imperfect edges. Thus the HED method saved us time and effort.

2. cGAN was employed instead of regular GAN, which makes the training
process swift.

3. U-net generator is used, the dataset is downsampled 7 times and upsampled
8 times, with the smallest sample being of dimension 1x1x512. The bottleneck structure aids the generator to learn the optimal reduced mapping
and not simply memorize the training set.

4. Patch GAN discriminator is used which looks for details and learns upon
them to distinguish between images.


_________

## Results 

