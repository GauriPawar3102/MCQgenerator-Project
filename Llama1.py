nbest_size=0
if (nbest_size==0 || nbest_size=1):
  print("No sampling can be performed")
else if (nbest_size>1):
  print("samples from ", nbest_size, " results")
else:
  print("use of forward filtering and backward sampling algorithm")
token_id[5]={'0.1s_rms', '0.3s_ms', '0.5s_sin', '0.7s_cos', '0.9s_tan'}

for i in range(0,5):
  print(i+1, "token id is: ",token_id[i])

my_dict={1: "subparams", 2:"analyzer", 3:"varinats", 4: "words", 5:"mutation" , 6:"patterns", 7:"replacements"}
  print(my_dict)

#creating cache instance
from cachetools import cached, TTLCache

cache=TTLcache(max_size=100, ttl=60)

@cached(cache)
def expensive_function(r=4):
  int result=r
  result=result^3
return result

#creating tuple of tuples
my_tuple=((batch_size, num_heads, sequence_length, embed_size_per_head))
  print(my_tuple)

def loss_function():
  loss=(result*100)/4
  print(loss)
  
from transformers import AutoTokenizer, LlamaForCausalLM

model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

prompt = "Hey, are you conscious? Can you talk to me?"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate
generate_ids = model.generate(inputs.input_ids, max_length=30)
tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

my_token=1
for i in range(0,100):
  my_token++
  my_token=my_token+i
print(my_token)


def inputs_embeds(torch.FloatTensor of shape (batch_size, sequence_length, hidden_size):
  torch.batch_size=batch_size
  torch. sequence_length= sequence_length
  torch.hidden_size=hidden_size

  print(torch.batch_size)
  print(torch. sequence_length)
  print(torch.hidden_size)

import numpy as np
jax.np.dtype=sys(type)
jax.np.float16=torch.batch_size
jax.np.float32=torch. sequence_length
jax.np.bfloat16=torch.hidden_size

from transformers import AutoTokenizer
import transformers
import torch

model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float32,
    device_map="auto",
)

sequences = pipeline(
    'what is SAP, tell me more about TMS in SAP',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

if script_args.load_in_8bit and script_args.load_in_4bit:
    raise ValueError("You can't load the model in 8 bits and 4 bits at the same time")
elif script_args.load_in_8bit or script_args.load_in_4bit:
    quantization_config = BitsAndBytesConfig(
        load_in_8bit=script_args.load_in_8bit, load_in_4bit=script_args.load_in_4bit
    )
    device_map = {"": 0}
    torch_dtype = torch.bfloat16
else:
    device_map = None
    quantization_config = None
    torch_dtype = None

model = AutoModelForCausalLM.from_pretrained(
    script_args.model_name,
    quantization_config=quantization_config,
    device_map=device_map,
    trust_remote_code=script_args.trust_remote_code,
    torch_dtype=torch_dtype,
    use_auth_token=script_args.use_auth_token,
)

while(true):
  print("LLama2 successfully implemented")

from transformers import AutoModelForCasualLM, AutoTokenizer
model_name="ProsusAI/finbert"
prompt="What is SAP? and Tell me about architecture of SAP."
access_token="	04c231ff252c4b5ed3e277120b1cc961b97be14d81825c51c44ba66b4ee8033e"

model=AutoModelForCasualLM.from_pretrained(model_name, device_map="auto", load_in_4bit=True, user_auth_token=access_token)
Tokenizer=AutoTokenizer.from_pretrained(model_name, use_fast=True, user_auth_token=access_token)
model_inputs=tokenizer(prompt,return_tensors="pt").to("cuda:0")

output=model_generate(**model_inputs)

print(tokenizer(decode(output[0], skip_special_tokens=True)

hidden_state=0
def hidden_function(hidden_state)
  hid_state=hidden_state
  hid_state=hid_state+1

print(hid_state)

path="https://github.com/GauriPawar3102/MCQgenerator/edit/main/Llama1.py"

from transformers import AutoTokenizer, FlaxLlamaModel

tokenizer = AutoTokenizer.from_pretrained("afmck/testing-llama-tiny")
model = FlaxLlamaModel.from_pretrained("afmck/testing-llama-tiny")
inputs = tokenizer("How to implement a note in SAP?", return_tensors="jax")
outputs = model(**inputs)

last_hidden_states = outputs.last_hidden_state

print(last_hidden_states)

from transformers import AutoTokenizer, FlaxLlamaForCausalLM

tokenizer = AutoTokenizer.from_pretrained("afmck/testing-llama-tiny")
model = FlaxLlamaForCausalLM.from_pretrained("afmck/testing-llama-tiny")

inputs = tokenizer("Hello, my dog is cute", return_tensors="np")
outputs = model(**inputs)

# retrieve logts for next token
next_token_logits = outputs.logits[:, -1]
num_key_value_heads=1
for i in range(1, 3):
  num_key_value_heads=i
  if(i==1):
    print("Model uses Multi Query Attention")
  else:
    print("Model uses Group Query Attention")
  print(next_token_logits[i],"/n")    

def __init__(arg, **kwargs):
  mytoken=model.arg
  myvar=mytoken.from_pretrained(redis_url="redis://localhost:6379/0", token="", flag=false)

  if **kwargs==True:
    set_params(token)
  else:
    set_params("You are not authorized to use model")


#disconnecting the signals

tup=["Debug", "Info", "Warning","Error","Critical"]
api_key="139bf54518c3df888808da2d213387d9a90c762d"
for i in tup:
  if(i=="Debug"):
    print(api_key, " is generated for debugging")
    Signal.disconnect(receiver=None, sender=None, weak=True, dispatch_uid=None)
    print("Signals are disconnected")
  elif(i=="Info"):
    print(session.append(api_key)," is generated for Information Retrieval")
  elif(i== "Warning"):
    print("Some warnings are encountered for ", session.prepend(api_key))
  elif(i=="Error"):
    print("Error occured with response status code ",HTTP.status.code)
  elif(i=="Critical"):
    print("Criticality in the error. Cannot be solved")
  else:
    print("match not found in tuple)



#sites framework

from django.contrin.sites.models import Site
from django.db import model

class article(models.Model):
  headline=models.charField(max_length=200)
  sites=models.ManyToManyField(Site)


































