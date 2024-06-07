#!/usr/bin/env python3
import os
import time
from time import sleep
import sys
from dta import *
import sys
import socket
import subprocess
import webbrowser
import requests
import base64
from time import sleep
os.system(clear)
con= f'{bblue}$ {bblue}Scriptbox{blue}95{purple}@{bgreen}'+f'[{bcyan}'+version+f'{bgreen}]{purple}~{white} '
url = "https://exowiki.space/project/v1/"
token = "sY28Ai8ZKQgOmzsyPyAETJuQatAg7ksbY3mV4gmeTdRYZCe94ratcwIFblCVHYSd6Q5u6k8ECtwUY1gSpvcaSGb3fhBAKscA3jKQkqOS04St7o3hybJ8g958Q0SWmEhk1bbkOyW57VLANahfeVyr8Nb2dcvdhsvoCZuO0wtq7LYD4bceaJCkli8sQWH2ezsRWNLIrSQ1Ax5iLDGkVM5tU9oPxil626raLkN32YtZxKqZVfUoEbdHcEaR39zpbw5EfzUJ90HZStUJfWKgkK8JJ1ONkcW0pQ7yH4gUrsWkLowR"

def api(id, file_name, Script_Code, id1):
    headers = {
    "User-Agent": "project/884938t48y584y5",
    "Authorization": f"Bearer {token}",
    "File-Name": file_name,
    "id" : id1,
    "Script-Code":Script_Code,}
    params = {"id": id}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
      print(con+"Server Cunnection Success!")
      data = response.json()[0]
      return 1, data
    else:
      print(con+"Error:", response.status_code)
      return 0, response.text



def cnt_chk():
    try:
        socket.create_connection(("www.exowiki.space", 80))
        return True
    except OSError:
        pass
    return False

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def save_script_to_file(file_name, script):
    current_script_dir = os.path.abspath(os.path.dirname(__file__))
    tools_dir = os.path.join(current_script_dir, 'tools')
    os.makedirs(tools_dir, exist_ok=True)
    file_path = os.path.join(tools_dir, file_name)
    with open(file_path, 'w') as file:
        file.write(script)

def get_script_by_id(connection, id):
    query = f"SELECT name, script, ver FROM main WHERE id = {id}"
    result = execute_query(connection, query)
    if result:
        name, script, verz = result
        return script, name, verz
    else:
        return None, None, None
    
def chk_f(file_name, folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, file_name)
    
    if os.path.isfile(file_path):
        return "Yes"
    else:
        return "No"

def imp(id):
  if cnt_chk():
    print(con_pls+'ID = '+str(id))
    sdi, responce = api('4','','',str(id))
    if responce == [] :
             return 'non',"0"
    else:
         name = responce[0]['name']
         script = responce[0]['script']
         if script and sdi == 1:
             file_name = str(id)+'.py'
             print(con+'Tool name is '+name)
             file_exist = chk_f(file_name, 'tools')
             if file_exist == 'No':
                 save_script_to_file(file_name, script)
                 print(con+name+' is imported, redy to use.')
             else:
                 print(con+name+' is alredy imported.')
        
             return file_name, "1"
         else:
             return 'non',"0"
  else:
         print(con+"No internet connection, exiting...")
         sys.exit(0)

def conf_usr():
    input(con+"Press Enter key to continue...")

def upload():
   if cnt_chk():
    try:
        file_path = input(con+"Enter the absolute path of the Python file: ")
        
        if not os.path.isabs(file_path):
            print(con_inf+"The provided path is not an absolute path.")
            conf_usr()
            return
        if not os.path.exists(file_path):
            print(con_inf+"The provided path does not exist.")
            conf_usr()
            return
        if not (os.path.isfile(file_path) and file_path.endswith('.py')):
            print(con_inf+"The provided path is not a valid Python file.")
            conf_usr()
            return
        if os.path.getsize(file_path) == 0:
            print(con_inf+"The provided Python file is empty.")
            conf_usr()
            return
        file_name_with_extension = os.path.basename(file_path)
        file_name, file_extension = os.path.splitext(file_name_with_extension)
        with open(file_path, 'r') as file:
            script_code = file.read()
        code = base64.urlsafe_b64encode(script_code.encode())
        print(con_pls+"File is: "+file_name)
        opt = input(con+"You want to cantinue 'y' for yes : ")
        if opt== "y":
            sts,responce = api('2',file_name,code,'non')
            if sts == 1:
                print(con+con_pls+"Your script Id is :"+str(responce))
                print(con+"upload done...")
            elif sts == 0:
                print(con+con_pls+"Server Error"+str(responce))
        else:
            return
    except Exception as e:
        print(con+"An error occurred:", e)
    except KeyboardInterrupt:
              print('\n'+con_inf+"Exiting ..!!!")
              conf_usr()
              return
    conf_usr()
   else:
    print(con+"No internet connection, exiting...")
    sys.exit(0)

def run_py(py_name, folder_name):
    tool_folder = os.path.join(os.getcwd(), folder_name)
    os.chdir(tool_folder)

    py_path = os.path.join(tool_folder, py_name)
    subprocess.run(['python3', py_path])
    os.chdir('..')
    print(con+"exiting program...")
    time.sleep(2)
    main()


def search_name_in_db(name):
    print(con+'searching..')
    try:
       sts,responce = api('3',name,'','')
       if sts == 1:
           if responce:
                print(con+"Result Found..")
                prt_dta(responce)
           elif responce == []:
               print(con+"No Result Found..")
    except:
        print(con+"Server Error")


def fch_dta():
    sts,responce = api('1','','','')
    if sts == 1:
        return responce
    elif sts == 0:
        print(con+"Server Error - "+responce)
def prt_dta(records):
    for row in records:
        print(f"ID: {row['id']}, Name: {row['name']}")

def prt_m_dta():
 if __name__ == "__main__":
     prt_dta(records)

def handle_user_input():
    while True:
        try:
            user_option = (input("\n"+con_pls+"Enter Tool ID You Want To Import\n"+con_inf+"Import on your own risk, Press 'a' for About me \n"+con_pls+"Press 's' For Search, 'u' For Upload Your Python script\n"+con_pls+"Enter Your Value :"))
            return user_option
        except ValueError:
            print(con_inf+"Error: Please enter an integer.")
            time.sleep(2)
            main()
            """sys.exit(1)"""
        except KeyboardInterrupt:
            print('\n'+con_inf+"Exiting ..!!!")
            sleep(2)
            sys.exit()

def main():
    os.system(clear)
    print(go)
    print(con+"Select An Option..")
    prt_m_dta()
    id1 = handle_user_input()
    if id1  == "s":
        os.system(clear)
        print(go)
        user_input = input(con_inf+"Enter the name to search: ")
        if not user_input:
            print(con+"No any input")
            conf_usr()
            main()
        else:
           try:
             search_name_in_db(user_input)
             conf_usr()
             main()
           except KeyboardInterrupt:
              print('\n'+con_inf+"Exiting ..!!!")
              main()
    elif id1 == "a":
        webbrowser.open("divyansh.exowiki.space")
        main()
    elif id1 == "u":
        upload()
        main()
    try:
        id=int(id1)
    except ValueError:
            print(con_inf+"Error: Please enter an integer.")
            time.sleep(2)
            main() 
    py_name, sts=imp(id)
    try:
        if sts == '0':
            print(con_inf+"The ID you entered is not valid. Try again")
            time.sleep(2)
            main()
        elif sts == '1':
            run_py(py_name, 'tools')
        
    except KeyboardInterrupt:
            print('\n'+con_inf+"Exiting ..!!!")
            sleep(2)
            sys.exit()

def load():
    '''os.system(clear)
    print(con_inf+"Loading [1%]")
    time.sleep(2)
    os.system(clear)
    print(con_inf+"Loading [10%]")
    time.sleep(1)
    os.system(clear)
    print(con_inf+"Loading [35%]")
    time.sleep(0.5)
    os.system(clear)
    print(con_inf+"Loading [40%]")
    time.sleep(0.5)
    os.system(clear)
    print(con_inf+"Loading [56%]")
    time.sleep(0.5)
    os.system(clear)
    print(con_inf+"Loading [61%]")
    time.sleep(0.5)
    os.system(clear)
    print(con_inf+"Loading [79%]")
    time.sleep(0.5)
    os.system(clear)
    print(con_inf+"Loading [91%]")
    time.sleep(0.5)
    os.system(clear)
    print(con_inf+"Loading [100%]")
    time.sleep(2)'''
    os.system(clear)
    print(con+"Chacking internet cunnection...")
    if cnt_chk():
       print(con+"Internet is cunnected...")
       global records 
       records = fch_dta()
       time.sleep(2)
       main()
    else:
      print(con+"No internet connection, exiting...")
      sys.exit(0)


load()
