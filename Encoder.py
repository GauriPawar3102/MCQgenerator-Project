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

#transactions
from django.db import migrations
class Migration(migrations.Migration):
    atomic = False

def error_view(r=HTML.request, e=HTML.exeption):
    defaults.page_not_found(r, e, template_name='404.html')
    if(defaults.page_not_found(r, e, template_name='404.html')==True):
        print("PAGE NOT FOUND")
        print("YOU MIGHT HAVE ENTERED WRONG URL")
class ExceptionLoggingMiddleware(object):
    def process_exception(self, request, exception):
        import traceback
        print traceback.format_exc()
        except Exception,e:
        # Get line
        trace=traceback.extract_tb(sys.exc_info()[0])
        # Add the event to the log
        output ="Error in the server: %s.\n" % (e)
        output+="\tTraceback is:\n"
        for (file,ln=linenumber,a=affected,l=line)  in trace:
            output+="\t> Error at function %s\n" % (a)
            output+="\t  At: %s:%s\n" % (file,ln)
            output+="\t  Source: %s\n" % (l)
        output+="\t> Exception: %s\n" % (e)


def show_error():
    import exception as e
    from django.core.exceptions import ObjectDoesNotExist
    if(django_error_HTML==True):
        try:
            e1=e.exception_server_HTML
    	except ObjectDoesNotExist:
       		print("Object does not exist")



    
           
        







