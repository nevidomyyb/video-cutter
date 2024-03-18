import streamlit as st
import multiprocessing
from utils.delete_files import delete_files
from time import sleep
import subprocess
from streamlit.web import cli as stcli
import sys
from streamlit import runtime 

def main_streamlit():
    # output = subprocess.check_output(["streamlit", "run", "st.py"], stderr=subprocess.STDOUT, text=True)
    # print(output)
    sys.argv = ["streamlit", "run", "st.py"]
    sys.exit(stcli.main())
        

def main_loop():
    while True:
        sleep(60*10)
        # delete_files()
            
def stop_processes(processes):
    for p in processes:
        p.terminate()

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        st_p = multiprocessing.Process(target=main_streamlit)
        loop_p = multiprocessing.Process(target=main_loop)
        
        st_p.start()
        loop_p.start()
        
        try:
            st_p.join()
            loop_p.join()
        except KeyboardInterrupt:
            stop_processes([st_p, loop_p])