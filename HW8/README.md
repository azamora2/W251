# Homework 8: 
Part 1 Questions : 
1.	In the time allowed, how many images did you annotate? 384
2.	Home many instances of the Millennium Falcon did you annotate?  How many TIE Fighters? 308 instances of the Millenium Falcon and 287 instances of Tie fighters
3.	Based on this experience,  how would you handle the annotation of large image data set? I would try to automate the process as much as possible, and would divide
the annotation process so that sevral people would do it if there was no other way to do it as opposed to manually
4.	Think about image augmentation?  How would augmentations such as flip, rotation, scale, cropping, and translation effect the annotations?
Yes flip, rotation, scale, cropping, and translation would affect the annotation by being able to generate more images yeilding a larger data set to train models with

Part 2 Questions: 
1. Describe the following augmentations in your own words
-	Flip: make a mirror image of the image with respect to the specified axis
- 	Rotation: rotate the image about it's center a specified amount of degrees
-	Scale: make the image bigger or smaller in terms of pixels
-	Crop: cut a specified part of an image
-	Translation: move the image up or down and only saved the desired amount of x and y direction that the image was moved
-	Noise: add random bits of colored pixels throughout the image at random points to ensure that the image changes but the general picture that the image is portraying or at least its label is still visible and distinguishable by the human eye

Part 3 Questions: 
1.	Image annotations require the coordinates of the objects and their classes; in your option, what is needed for an audio annotation? 
in my opinion to classify audio you need to be able to classify sound waves in the form of time series data of the sound wave that is heard. You also need to be able to add noise and add as much variation into the audio that you want to classiy in the training set so that it is able to generalize well when deployed. If you need to cut certain portions of audio recordings to build your training set you must be able to specify where you want this segmentation to be made and come up with a protocol that ensures that all audio is segmented in a similar manner. You also need to teach your model to read in the same audio at different intervals within the test data so that it is able to distinguish the audio classification once it has started so that your model is able to segment the audio properly.
