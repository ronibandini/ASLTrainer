# American Sign Language for TI AM62A

American Sign Language trainer with Machine Learning and Texas Instruments AM62A

This project was made to test Edge Impulse BYOM, Bring your own model feature.

1. A model was trained using Google's Teachable Machine
2. The model was exported for Tensor Flor Lite
3. The model was imported to Edge Impulse using BYOM feature
4. The model was deployed to Texas Instruments AM62A
5. A Python script was coded to select random letters and calculate the time to make the signs in front of the camera

# 26 letters

If you want to use 26 letters you should
Clone standalone inferencing linux repo https://github.com/edgeimpulse/example-standalone-inferencing-linux
Download and unzip the TIDL-RT Library (AM62A) from the Studio and place in the top-level directory of the repo (1)
increase EI_CLASSIFIER_MAX_LABELS_COUNT in edge-impulse-sdk/classifier/ei_classifieri_types.h to a number higher than 25.
Build for AM62A
$ APP_EIM=1 TARGET_AM62A=1 make -j

# Demo 

https://www.youtube.com/watch?v=2z3iV9BN94c
