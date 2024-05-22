from src.Data import * 
from src.prox import *


cp = 0 
ok = 0


def tunggu(t):
  for x in range(t+1):
    print('\r[*] [OK:%s][CP:%s] Tunggu %s detik            '%(ok,cp,str(t)), end='')
    sys.stdout.flush()
    t -= 1
    if t == 0: break 
    else: time.sleep(1)
 # print('\r' + ' ' * 50 + '\r', end="")  # Clear the countdown line after completion
user = open('ua.txt','r').read().splitlines()

def clear():
  os.system("clear")
  

def Username():
  dev = log()
  mail ,ses = Mail()
  name = Names()
  ua = random.choice(user)
  Post = POST(ua)
  try:
    data = {
      'email': '',
      'first_name': name,
      'client_id': dev,
      'seamless_login_enabled': '1',
      'opt_into_one_tap': 'false',
    }
    pos = requests.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", data=data, headers=Post).text 
    js = json.loads(pos)
    if "username_suggestions" in js:
      respon = js["username_suggestions"]
      step1(mail,name,respon,dev,Post,ua,ses)
    else:
      sys.exit(1)
  except Exception as e:
    print(e)
  
def step1(mail,name,respon,dev,Post,ua,ses):
  pas = pw()
  try:
    
    data = {
      'enc_password': '#PWD_INSTAGRAM_BROWSER:0:%s:%s'%(round(time.time()),pas),
      'email': mail,
      'first_name': name,
      'username': respon[0],
      'client_id': dev,
      'seamless_login_enabled': '1',
      'opt_into_one_tap': 'false',
    }
    pos = requests.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",headers=Post,data=data, allow_redirects=False).text 
    js = json.loads(pos)
  except Exception as e:
    print(e)
  ttl(mail,name,respon,dev,pas,Post,ua,ses)

def ttl(mail,name,respon,dev,pas,Post,ua,ses):
  day  = random.randint(1,29)
  bln = random.randint(1,12)
  thn = random.choice(['2000','2001','2002','2003','2004'])
  try:
    data = {
      'day': day,
      'month': bln,
      'year': thn
    }
    pr = requests.post('https://www.instagram.com/api/v1/web/consent/check_age_eligibility/',headers=Post, data=data).text 
    jsk = json.loads(pr)
  except Exception as e:
    print(e)
  Code(mail,name,respon,dev,pas,day,bln,thn,Post,ua,ses)
def Code(mail,name,respon,dev,pas,day,bln,thn,Post,ua,ses):
  try:
    data = {
      'device_id': dev,
      'email': mail
    }
    ps = requests.post("https://www.instagram.com/api/v1/accounts/send_verify_email/",headers=Post,data=data).text 
    jsb = json.loads(ps)
    #print("\n[*] Email: %s"%(mail))
    #print("[*] sedang mengirim kode"); time.sleep(0.01)
    while True:
      mass=Email(ses).inbox()
      if mass:
        topic = mass['topic'].split()[0]
        #print("[*] Kode: %s"%(topic))
        break
  except Exception as e:
    print(e)
  confirm(mail,name,respon,topic,dev,pas,day,bln,thn,Post,ua)
  
  
def confirm(mail,name,respon,topic,dev,pas,day,bln,thn,Post,ua):
  try:
    
    data = {
      'code': topic,
      'device_id': dev,
      'email': mail
    }
    pk = requests.post("https://www.instagram.com/api/v1/accounts/check_confirmation_code/",headers=Post, data=data).text 
    jh = json.loads(pk)
    
    if 'signup_code' in jh:
      sign_up = jh["signup_code"]
      Create(mail,name,respon,sign_up,dev,pas,day,bln,thn,Post,ua)
    else: 
      sys.exit(1)
  except Exception as e:
    print(e)
  
def Create(mail,name,respon,sign_up,dev,pas,day,bln,thn,Post,ua):
  global ok, cp
  usernam = respon[0]
  data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:%s:%s'%(round(time.time()),pas),
    'day': day,
    'email': mail,
    'first_name': name,
    'month': bln,
    'username': usernam,
    'year': thn,
    'client_id': dev, 
    'seamless_login_enabled': '1',
    'tos_version': 'row',
    'force_sign_up_code': sign_up
  }
  
  pos = requests.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/",headers=Post, data=data,allow_redirects=True)
  if 'user_id' in str(pos.text):
    cok = str(pos.cookies)
    tok = re.findall('csrftoken=([^ ]+)',cok)[0]
    cokie = re.findall(r'<Cookie ([^=]+)=([^ ]+) for .instagram.com/>', cok)
    coki = '; '.join([f"{name}={value}" for name, value in cokie])
    up = posting(tok,coki)
    if "https://www.instagram.com/accounts/suspended/" in str(up):
      print(f"\r[*] Username: {usernam}\n[*] Password: {pas}\n[*] UserAgent: {ua}\n[*] Cookies: {coki}")
      print("[?] Akun Di Nonaktifkan\n")
      
    else:
      print("[*] CREATE AKUN SUKSES             ")
      print(f"\r[*] Username: {usernam}\n[*] Password: {pas}\n[*] UserAgent: {ua}\n[*] Cookies: {coki}")
      print("[+] Berhasil Upload Photo\n")
      open("ok.txt","a").write(usernam+"|"+pas+"|"+coki+"\n")
    ok+=1
  else: 
    print("\r[*] Create Checkpoint             ")
    print("[*] Username: %s\n[*] Password: %s\n[*] UserAgent: %s\n"%(usernam,pas,ua))
    open("cp.txt","a").write(usernam+"|"+pas+"\n")
    cp+=1
  tunggu(10)

def posting(tok,coki):
  global img
  try:
    p_pic = img# ganti sama alamat file foto yang mau di unggah
    p_pic_s = os.path.getsize(p_pic)
    headers = {
      "Host": "www.instagram.com",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
      "Accept": "/",
      "Accept-Language": "en-US,en;q=0.5",
      "Accept-Encoding": "gzip, deflate, br",
      "Referer": "https://www.instagram.com",
      "X-CSRFToken": '%s'%(tok), # ganti csrftoken sesuai cookie yang valid
      "X-Instagram-AJAX": "1013618137",
      "X-Requested-With": "XMLHttpRequest",
      "Content-Length": str(p_pic_s),
      "DNT": "1",
      "Connection": "keep-alive",
    }
    files = {'profile_pic': open(p_pic,'rb')}
    values = {
      "Content-Disposition": "form-data",
      "name": "profile_pic",
      "filename":"profilepic.jpg",
      "Content-Type": "image/jpeg"
      }

    r = requests.post('https://www.instagram.com/accounts/web_change_profile_picture/', files=files, data=values, headers=headers, cookies={'cookie':coki}).text
    return r
    #  open('Create/ok.txt','a').write(usernam+'|'+pas+'|'+coki+"\n")
  except Exception as e:
    print(e)
