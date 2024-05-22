from src.ig import * 




def Logo():
  print("""
  _____             __      _________
 / ___/______ ___ _/ /____ /  _/ ___/
/ /__/ __/ -_) _ `/ __/ -_)/ // (_ / 
\___/_/  \__/\_,_/\__/\__/___/\___/  
                                     
 """)
def Main():
  Logo() 
  print("[1] AUTO CREATE IG\n[2] CHECK RESULT")
  match int(input("[?] Choice: ")):
    case 1:
      img = input("\n[+] Masukan File Gambar Sesuai Tempat Photonya Cth:/sdcard/img.jpg/png\n[+] Input: ")
      
      print( )
      total = int(input("[*] Masukan Jumlah: "))
      print( )
      for _ in range(total):
        Username()
    case 2:
      print("\n[1] Akun Checkpoint\n[2] Akun Live")
      match int(input("[?] Choice: ")):
        case 1:
          print()
          cp = open('cp.txt','r').read().splitlines()
          jum = len(cp)
          for x in cp:
            print(x)
          print("\n[*] Jumlah Akun Checkpoint: %s"%(jum))
    case __:
      Main()
if __name__=="__main__":
  clear()
  Main()
