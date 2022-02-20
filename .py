#!/usr/bin/env python3

import socket
import sys

def jls_extract_def():

    # https://twitter.com/Linesecurity7
    
    def banner():
           print("""
    ...................................................
             _nnnn_
            dGGGGMMb
           @p~qp~~qMb
           M|@||@) M|
           @,----.JM|
          JS^\__/  qKL
        dZP        qKRb
       dZP          qKKb    Created by line#0007
       fZP            SMMb
       HZM            MMMM         Port Scan
       FqM            MMMM
     __| ".        |\dS"qML
     |    `.       | `' \Zq
    _)      \.___.,|     .'
    \____   )MMMMMP|   .'
         `-'       `--'
    ...................................................
    """)

    return banner

banner = jls_extract_def()

def scan():

       ports = [21,22,23,25,53,80,88,110,119,137,138,139,143,156,161,389,443,445,512,513,3306,8080]

       print("Port          Service        State\n\n")

       for port in ports:

              client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

              if((client.connect_ex((sys.argv[1],port))) == 0):

                     print(f"{port}              {socket.getservbyport(port)}           open\n")

              else:

                     print(f"{port}              {socket.getservbyport(port)}           closed\n")

       client.close()

try:  

        if(sys.argv == 1):

           print("Usage: python3 scan.py TARGET")

        else:
        
            banner()
            scan()

except KeyboardInterrupt:

       print("Exit...")

       quit()

except socket.gaierror:

        print("Host not found")
