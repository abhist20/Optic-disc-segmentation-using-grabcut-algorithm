# Optic-disc-segmentation-using-grabcut-algorithm


This project utilizes popular computer vision library cv2 and its subfuction grabcut alogrithm for segmentation and detection of optic disc in a fundus image of eye.

It also implements a popular CNN architecture inception V3 for image quality assesment.


Trained by using transfer learning.



To test on different image
python image_lable.py \
--graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt \
--input_layer=Placeholder \
--output_layer=final_result \
--image="image path"

