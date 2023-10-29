import random
import math
attributes=[]
attributes.append(int(input("input 1:")))
attributes.append(int(input("input 2:")))
attributes.append(int(input("input 3:")))
threshold_accuracy=(float(input("Threshold accuracy:")))
epochs=(float(input("Epochs:")))

w56=random.random()
w14=random.random()
w15=-(random.random())
w24=random.random()
w25=random.random()
w34=-(random.random())
w35=random.random()
w46=-(random.random())
w15=random.random()

o4=-(random.random())
o5=random.random()
o6=random.random()

weights=[w14,w15,w24,w25,w34,w35,w56,w46]
bias=[o4,o5,o6]

orig_output=1
l=0.8

#input for hidden layer
h_input=[]
for i in range(0,2):
  if i==0:
    h_input.append(attributes[0]*weights[0]+attributes[1]*weights[2]+attributes[2]*weights[4]+bias[0])
  else:
    h_input.append(attributes[0]*weights[1]+attributes[1]*weights[3]+attributes[2]*weights[5]+bias[1])

#output for hidden layer
h_output=[]
h_output.append(1/(1+math.exp(-h_input[0])))
h_output.append(1/(1+math.exp(-h_input[1])))

#input for output layer
o_input=[]
o_input.append(bias[2]+h_output[0]*w46+h_output[1]*weights[6])

#output for output layer
o_output=[]
o_output.append(1/(1+math.exp(-o_input[0])))

print("weights:", len(weights))
print("bias:",len(bias))
print("Hidden layer outputs:",h_output)
print("Hidden layer inputs:",h_input)
print("original output:", orig_output )
print("final output:",o_output)

def update():
  if o_output[0]<=threshold_accuracy:
    while epochs<=6:
      e6=o_output[0]*(1-o_output[0])*(orig_output-o_output[0])
      e5=h_output[1]*(1-h_output[1])*e6*weights[6]
      e4=h_output[0]*(1-h_output[0])*e5*weights[7]
      ew14=l*e4*attributes[0]
      ew15=l*e5*attributes[0]
      ew24=l*e4*attributes[1]
      ew25=l*e5*attributes[1]
      ew34=l*e4*attributes[2]
      ew35=l*e5*attributes[2]
      ew46=l*e6*h_output[0]
      ew56=l*e6*h_output[1]
      eo4=l*e4
      eo5=l*e5
      eo6=l*e6
      weights[7]+=ew56
      weights[0]+=ew14
      weights[1]+=ew15
      weights[2]+=ew24
      weights[3]+=ew25
      weights[4]+=ew34
      weights[5]+=ew35
      weights[6]+=ew46
      bias[0]+=eo4
      bias[1]+=eo5
      bias[2]+=eo6
      epochs+=1
      update()
  else:
    print("Output is good. Nothing to update!")
    print(o_output[0])
update()
