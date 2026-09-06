print("Hello, this project is temporary; it will later be transferred to OS-CORE713 as a command: linof, or Links Of. This utility provides official links to services.")

import webbrowser

links = {
    "chatgpt": "https://chatgpt.com",
    "chat gpt": "https://chatgpt.com",
    "chatGPT": "https://chatgpt.com",
    "ChatGPT": "https://chatgpt.com",
    "cHatgpt": "https://chatgpt.com",
    "Chatgpt": "https://chatgpt.com",
    "chAtgpt": "https://chatgpt.com",
    "chaTgpt": "https://chatgpt.com",
    "CHATGPT": "https://chatgpt.com", # pay me for ADS openai 
    "CHATgpt": "https://chatgpt.com",
    "chatGPT": "https://chatgpt.com",
    "c hatgpt": "https://chatgpt.com",
    "ch atgpt": "https://chatgpt.com",
    "cha tgpt": "https://chatgpt.com",
    "C hatgpt": "https://chatgpt.com",
    "Ch atgpt": "https://chatgpt.com",
    "Cha tgpt": "https://chatgpt.com", # i wait.
    "CH atgpt": "https://chatgpt.com",
    "CHA tgpt": "https://chatgpt.com",
    "CHAT gpt": "https://chatgpt.com",
    "CHAT GPT": "https://chatgpt.com",
    "чат бот от openai": "https://chatgpt.com",
    "yt": "https://www.youtube.com",
    "youtube": "https://www.youtube.com",
    "YouTube": "https://www.youtube.com",
    "YT": "https://www.youtube.com",
    "youTube": "https://www.youtube.com",
    "Youtube": "https://www.youtube.com",
    "youtubE": "https://www.youtube.com",
    "yOutube": "https://www.youtube.com",

    "grok": "https://grok.com",
    "Grok": "https://grok.com",
    "GRok": "https://grok.com",  # ilon hiii
    "GROk": "https://grok.com",
    "GROK": "https://grok.com",
    "gRok": "https://grok.com",
    "grOk": "https://grok.com",
    "groK": "https://grok.com",
    
    "google": "https://www.google.com",
    "Google": "https://www.google.com", # google.
    "GOOGLE": "https://www.google.com",
    "gOogle": "https://www.google.com",
    "gOOgle": "https://www.google.com",
    "gOOGle": "https://www.google.com",
    "gOOGLe": "https://www.google.com",
    "goOGLE": "https://www.google.com",
    "gooGLE": "https://www.google.com",
    "googLE": "https://www.google.com",
    "googlE": "https://www.google.com",

    "linux": "https://kernel.org",
    "kernel linux": "https://kernel.org",
    "Linux": "https://kernel.org",
    "LInux": "https://kernel.org",
    "LINux": "https://kernel.org",
    "LINUx": "https://kernel.org",
    "LINUX": "https://kernel.org",
    "Kernel": "https://kernel.org", # There is no such thing as too much Linux.. Linus Torvalds HIIII
    "KErnel": "https://kernel.org",
    "KERnel": "https://kernel.org",
    "KERNel": "https://kernel.org",
    "KERNEl": "https://kernel.org",
    "KERNEL": "https://kernel.org",

    "ubuntu": "https://ubuntu.com",
    "Ubuntu": "https://ubuntu.com",
    "UBuntu": "https://ubuntu.com",
    "UBUntu": "https://ubuntu.com",
    "UBUNtu": "https://ubuntu.com",
    "UBUNTu": "https://ubuntu.com",
    "UBUNTU": "https://ubuntu.com",
    "uBUNTU": "https://ubuntu.com",
    "ubUNTU": "https://ubuntu.com",
    "ubuNTU": "https://ubuntu.com",
    "ubunTU": "https://ubuntu.com",
    "ubuntU": "https://ubuntu.com",
    "ubuntu linux": "https://ubuntu.com",
    "Ubuntu Linux": "https://ubuntu.com",
    "UBuntu Linux": "https://ubuntu.com",
    "UBUntu Linux": "https://ubuntu.com",
    "UBUNtu Linux": "https://ubuntu.com",
    "UBUNTu Linux": "https://ubuntu.com",
    "UBUNTU Linux": "https://ubuntu.com",
    "Ubuntu LInux": "https://ubuntu.com",
    "Ubuntu LINux": "https://ubuntu.com",
    "Ubuntu LINUx": "https://ubuntu.com", # ummm.. Ubuntu, fuck you! And it's joke, lollllll
    "Ubuntu LINUX": "https://ubuntu.com",
    "UBuntu LInux": "https://ubuntu.com",
    "UBUntu LINux": "https://ubuntu.com",
    "UBUNtu LINUx": "https://ubuntu.com",
    "UBUNTu LINUX": "https://ubuntu.com",
    "UBUNTU LINUX": "https://ubuntu.com",
    "ubuntU linuX": "https://ubuntu.com",
    "ubunTU linUX": "https://ubuntu.com",
    "ubuNTU liNUX": "https://ubuntu.com",
    "ubUNTU lINUX": "https://ubuntu.com",
    "uBUNTU LINUX": "https://ubuntu.com",
    "ubuntu linuX": "https://ubuntu.com",
    "ubuntu linUX": "https://ubuntu.com",
    "ubuntu liNUX": "https://ubuntu.com",
    "ubuntu lINUX": "https://ubuntu.com",
    "ubuntu LINUX": "https://ubuntu.com",
    "UBUNTU linux": "https://ubuntu.com",
    "Ubuntu linux": "https://ubuntu.com",
    "Ubuntu1 linux": "https://ubuntu.com",
    "Ubuntu2 linux": "https://ubuntu.com",
    "Ubuntu3 linux": "https://ubuntu.com",
    "Ubuntu4 linux": "https://ubuntu.com",
    "Ubuntu5 linux": "https://ubuntu.com",
    "Ubuntu6 linux": "https://ubuntu.com",
    "Ubuntu8 linux": "https://ubuntu.com",
    "ubuntu9 linux": "https://ubuntu.com",
    "ubuntu10 linux": "https://ubuntu.com",
    "ubuntu1 linuX": "https://ubuntu.com",
    "ubuntu1 linUX": "https://ubuntu.com",
    "ubuntu1 liNUX": "https://ubuntu.com",
    "ubuntu1 lINUX": "https://ubuntu.com",   # PAY FOR ADS FUUUUCK
    "ubuntu1 LINUX": "https://ubuntu.com",
    "ubuntu2 linuX": "https://ubuntu.com",
    "ubuntu2 linUX": "https://ubuntu.com",
    "ubuntu2 liNUX": "https://ubuntu.com",
    "ubuntu2 lINUX": "https://ubuntu.com",
    "ubuntu2 LINUX": "https://ubuntu.com",
    "ubuntu3 linuX": "https://ubuntu.com",
    "ubuntu3 linUX": "https://ubuntu.com",
    "ubuntu3 liNUX": "https://ubuntu.com",
    "ubuntu3 lINUX": "https://ubuntu.com",
    "ubuntu3 LINUX": "https://ubuntu.com",
    "ubuntu4 linuX": "https://ubuntu.com",
    "ubuntu4 linUX": "https://ubuntu.com",
    "ubuntu4 liNUX": "https://ubuntu.com",
    "ubuntu4 lINUX": "https://ubuntu.com",
    "ubuntu4 LINUX": "https://ubuntu.com",    # who read this, ... --- ... loll
    "ubuntu5 linuX": "https://ubuntu.com",
    "ubuntu5 linUX": "https://ubuntu.com",
    "ubuntu5 liNUX": "https://ubuntu.com",
    "ubuntu5 lINUX": "https://ubuntu.com",
    "ubuntu5 LINUX": "https://ubuntu.com",    
    "ubuntu6 linuX": "https://ubuntu.com",
    "ubuntu6 linUX": "https://ubuntu.com",
    "ubuntu6 liNUX": "https://ubuntu.com",
    "ubuntu6 lINUX": "https://ubuntu.com",
    "ubuntu6 LINUX": "https://ubuntu.com",
    "ubuntu7 linuX": "https://ubuntu.com",
    "ubuntu7 linUX": "https://ubuntu.com",
    "ubuntu7 liNUX": "https://ubuntu.com",
    "ubuntu7 lINUX": "https://ubuntu.com",
    "ubuntu7 LINUX": "https://ubuntu.com",
    "ubuntu8 linuX": "https://ubuntu.com",
    "ubuntu8 linUX": "https://ubuntu.com",
    "ubuntu8 liNUX": "https://ubuntu.com",
    "ubuntu8 lINUX": "https://ubuntu.com",
    "ubuntu8 LINUX": "https://ubuntu.com",
    "ubuntu9 linuX": "https://ubuntu.com",
    "ubuntu9 linUX": "https://ubuntu.com", # wow
    "ubuntu9 liNUX": "https://ubuntu.com",
    "ubuntu9 lINUX": "https://ubuntu.com",
    "ubuntu9 LINUX": "https://ubuntu.com",
    "ubuntu10 linuX": "https://ubuntu.com",
    "ubuntu10 linUX": "https://ubuntu.com",
    "ubuntu10 liNUX": "https://ubuntu.com",
    "ubuntu10 lINUX": "https://ubuntu.com",
    "ubuntu10 LINUX": "https://ubuntu.com",


    "@torvalds": "https://github.com/torvalds",
    "torvalds": "https://github.com/torvalds",
    "cooltorvalds.com": "https://github.com/torvalds", # torvalds hellooooooooooooooooo!
    "torvaldsnotcoolbebebe": "no.", # torvalds
    "torvaldsmegacoolyes": "https://github.com/torvalds" # yeees, torvalds hellooooooooooooo

    "i use arch btw": "https://archlinux.org",
    "spotify": "https://spotify.com",
    "tg": "https://telegram.org",
    "telegram": "https://telegram.org",
    "Ну этот который паша": "https://telegram.org",
    "durov": "https://t.me/monk", # durov, durov durov durov 
    "@durov": "https://t.me/monk",
    "@monk": "https://t.me/monk",
    
    "ac713": "https://github.com/OS-AC713", # Oh, this is me, woow
    "@ac713": "https://github.com/OS-AC713",
    "OS-AC713": "https://github.com/OS-AC713",
    "@OS-AC713": "https://github.com/OS-AC713",
    "os-ac713": "https://github.com/OS-AC713",
    "@os-ac713": "https://github.com/OS-AC713", # It's me again, hello Linus Torvalds

    " ": "bro, was the keyboard created for?",
    "if": "else", # logic 
    "openai": "Sorry, I can't give you a link. They didn't pay me money for the advertising ( ads ) .((((((( https://openai.com it's secret",
    "UBUNTU200202020202020": "no. I wait money sorry. (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((( For free ADS, ( secret: https://ubuntu.com )",
    "linof": "linof.",
    "git": "i idk. Hellooo torvaldsssssssss",
    "song": "my favorite song is GIRL HELL 1999 Femtanyl, joost - Kutmuziek, and what will you do with it?",
    "song2": "ok: Dreamcore - pathetic240px, ( torvalds hello ), Seek - LSPLASH, ( torvalds hi ), frutiger aero - amirthettrash, ( torvalds hi ).",
    "torvalds hiii": "bruh, this is my thing😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡"
    

}
while True:
    user_input = input("Enter the service name: ")
    if user_input in links:
        url = links[user_input]
        print(f"official links: {url}")   #
        webbrowser.open(url)
    else:
        print("Not Found. Retry")
