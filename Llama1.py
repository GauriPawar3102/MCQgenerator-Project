nbest_size=0
if (nbest_size==0 || nbest_size=1)
  print("No sampling can be performed")
else if (nbest_size>1)
  print("samples from ", nbest_size, " results")
else 
  print("use of forward filtering and backward sampling algorithm")
token_id[5]={'0.1s_rms', '0.3s_ms', '0.5s_sin', '0.7s_cos', '0.9s_tan'}

for i in range(0,5):
  print(i+1, "token id is: ",token_id[i])

my_dict={1: "subparams", 2:"analyzer", 3:"varinats", 4: "words", 5:"mutation" , 6:"patterns", 7:"replacements"}
  print(my_dict)
