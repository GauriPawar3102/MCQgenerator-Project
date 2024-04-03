import pandas as pd
from datasets import load_dataset
df=load_dataset("hf-internal-testing/librispeech_asr_dummy", split=True)
model=get_model(model_name="microsoft/cvt-13", params=134, verbose=True)


def produce_data(args, queue, filepaths, dataset_indices):
    global_batch_size = args.batch_size*args.nprocs    #Global batch size
    size_per_dataset = int(global_batch_size / args.datasets_per_batch)    #How many datasets per batch
    num_same_dataset = int(size_per_dataset / args.batch_size)
    print("producer", "global_batch_size", global_batch_size)
    print("producer", "size_per_dataset", size_per_dataset)
    print("producer", "num_same_dataset", num_same_dataset)

datasets=[]
for filepath in filepaths:
  if "reddit_" in filepath:
    data_obj=RedditDataset(filepath)
  else:
    data_obj=Dataset(filepath)
  Dataset.append(iter(data_obj))


from django.contrib.redirects.models import Redirect

redirects=RedirectFallbackMiddleware("/https://github.com/GauriPawar3102/MCQgenerator/main/Encoder.py", admin=None)
path="www.github.com/GauriPawar3102/MCQgenerator/main/Encoder.py"
if(path=""):
    print("404 GONE ERROR")
    redirects.color("Red: 255, 0, 0")
else:
    print("Request continues to be processed")
    redirects.color("Yellow:#FFFF00")
