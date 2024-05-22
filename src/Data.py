from src.module import *



def Names():
  rr = str(random.choice(["emmawilliams","danielthomas","olivialopez","matthewmiller","graceharris","lucasjackson","ameliasmith","williamtaylor","emilyhall","josephwilson","chloejones","andrewroberts","sarahmartinez","jamesclark","audreyadams","michaelrodriguez","elizabethlee","nathangreen","sophiamartin","davidmitchell","abigailjohnson","jacksonhernandez","victoriasmith","ethandavis","charlotteperez","christopherturner","madisonwalker","oliverharris","emilyking","nathansanchez","victoriawilliams","lucasmartinez","hannahroberts","williammiller","ellieperez","josephwilson","emilymoore","danielgarcia","olivialopez","sophiawhite","jacksondavis","audreythompson","michaelmartinez","elizabethhall","benjaminwilson","gracemartin","dylanthomas","abigailjackson","lucasrobinson","sarahjohnson","jamesclark","oliviamartin","andrewwilson","nathansmith","chloewilliams","victoriaadams","ethanjones","ameliamiller","christophertaylor","charlotteharris","matthewwalker","emilydavis","josephroberts","lucassmith","sophiadavis","masonclark","elizabethmartin","danieljones","audreymoore","jacksonmiller","abigailturner","williamrodriguez","victoriamartinez","gracewilson","hannahrodriguez","nathanclark","sarahperez","jamesdavis","oliviaroberts","lucasjohnson","davidthomas","elizabethmiller","chloeturner","andrewmitchell","sophiaclark","michaelhall","ethanjones"]))
  return rr

# =========HEADERS POST=========== #
uas = random.choice(["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36","Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"])
def GET():
  Get= {'Host': 'www.instagram.com','user-agent': str(uas),'content-type': 'application/x-www-form-urlencoded','origin': 'https://www.instagram.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.instagram.com/accounts','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
  return Get
def POST(ua):
  Post = {'Host': 'www.instagram.com','x-ig-www-claim': '0','x-csrftoken': 'n0wjkJkEsoUkP5dFFrgHEzsepxh74sPE','x-ig-app-id': '936619743392459','x-instagram-ajax': '1013522313','user-agent': str(ua),'content-type': 'application/x-www-form-urlencoded','accept': '*/*','x-asbd-id': '129477','origin': 'https://www.instagram.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.instagram.com/accounts/login/','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
  return Post

def pw():
  pk = random.choice(["123","1234","12345@"])
  pss = Names()+pk 
  return pss
  
def Mail():
  create = Email().Mail()
  email = create['mail']
  ses = create['session']
  return(email,ses) 
  
def log():
  r = requests.Session()
  req = r.get("https://www.instagram.com/accounts/login/",headers=GET()).text 
  client = re.search('"machine_id":"(.*?)"',str(req)).group(1)
  return(client)
  
  
  
