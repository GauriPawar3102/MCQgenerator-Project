from transformers import TFPreTrainedModel
from tensorflow import keras

model.save_weights("some_folder/tf_model.h5")
model = TFPreTrainedModel.from_pretrained("some_folder")


#file has been successfully updated
