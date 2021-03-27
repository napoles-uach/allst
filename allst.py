import streamlit as st
import os
from pyngrok import ngrok
import subprocess


input_=st.text_input('enter git page')


#st.write(input_)


#with open('test.py', 'w') as f: # opción "a" append
#  if os.stat('test.py').st_size > 0:
#    pass
#  else:
#    f.write('import streamlit as st\n')
#    f.write('st.write("seconda page")')
#  f.write(input_+'\n')
b1=st.button('ngrok?')
if b1:
  public_url = ngrok.connect(port='80')
  st.write(public_url)
#if input_ is not None:
#  st.write(public_url)
#  with open('script.sh', 'w') as f:
#    f.write("#!/bin/bash\n")
#    f.write("git clone -l -s "+input_ +"\n")
#    f.write("OUTPUT=$(basename " +input_+" .git)\n")
#    f.write("cd " +""" $OUTPUT """+"\n")
#    f.write("pip install -r requirements.txt >> outputpip")
#    f.write("echo finish >> outputpip")
#    f.write("streamlit run --server.port 80 app.py >/dev/null")
  
#  subprocess.call("./script.sh")
