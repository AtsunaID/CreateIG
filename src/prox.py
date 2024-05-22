from src.module import * 



def proxy():
  req = requests.get("https://github.com/TheSpeedX/PROXY-List/blob/master/socks5.txt")
  pr = re.findall('"rawlines":"(.*?)"',str(req))
  print(pr)