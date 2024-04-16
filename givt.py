import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as p

# pip install rich
# pip install selenium

p("""

                 ,  ,
              #▄▓██████▀
            "▀███████████▄L
           ▄R████████████▄▄
            ▄▀█████████▓▀▀N
             ' ▀█▀███▀█ ▀
                ' ▀█▌"
                   ▐█
                   ██
                   ██
    ""▀▀▀██▄▄   ▄▄▄██▄a▄▄   ,▄▄██▀▀""
           "▀██▄⌠▀▀▀▀▀'¡▄██▀"
               ▀██▄  ▄██▀`
                  ████"
               ▄▄█▌▀╙██▄▄
          ██▄▄██▀█    █▀███▀█▌

""")
p(Panel("""
     [ Made By GIVT . ]
     [ + ] Telegram : givtt
     [ + ] Instagram : we62
     [ ! ] You are not entitled to sell the Tool [ ! ]
"""), )

class LordGivt:
    def __init__(self, username):
        self.username = username
        self.driver = self.select_driver()
        self.get_info()

    @staticmethod
    def select_driver():
        chrome_options = Options()
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
        return webdriver.Chrome(options=chrome_options)

    def get_info(self):
        try:
            self.driver.get(f"https://api.tellonym.me/profiles/name/{self.username}?previousRouteName=ScreenProfileSharing&isClickedInSearch=true&sourceElement=Search%20Result&adExpId=91&limit=16")
            self.driver.implicitly_wait(5)
            response = self.driver.find_element(By.TAG_NAME, "pre")


            if "The entry you were looking for could not be found." in response.text:
                input("[X] Error : User Not Found")
                exit()
            elif "This account is banned." in response.text:
                input("[X] Error : This account is banned.")
                exit()

            else:
                json_data = json.loads(response.text)
                avatar = f"https://userimg.tellonym.me/lg-v2/{json_data['avatarFileName']}"
                followers = json_data.get("followerCount", "Unknown")
                anonymousFollowerCount = json_data.get("anonymousFollowerCount", "Unknown")
                following = json_data.get("followingCount", "Unknown")
                account_id = json_data.get("id", "Unknown")
                name = json_data.get("displayName", "Unknown")
                username = json_data.get("username", "Unknown")
                aboutMe = json_data.get("aboutMe", "Unknown")
                likesCount = json_data.get("likesCount", "Unknown")
                answerCount = json_data.get("answerCount", "Unknown")
                tellCount = json_data.get("tellCount", "Unknown")
                isAbleToComment = json_data.get("isAbleToComment", "Unknown")
                isVerified = json_data.get("isVerified", "Unknown")
                countryCode = json_data.get("countryCode", "Unknown")
                isActive = json_data.get("isActive", "Unknown")
                RealFollowers = followers - anonymousFollowerCount or "0"
                table = Table(title=f"Getting @{username} info ..")

                table.add_column("Key", no_wrap=True)
                table.add_column("info")

                table.add_row("Account ID", str(account_id))
                table.add_row("Username", str(username))
                table.add_row("Name", str(name))
                table.add_row("Bio", str(aboutMe))
                table.add_row("Following", str(following))
                table.add_row("Followers", str(followers))
                table.add_row("Anonymous Followers", str(anonymousFollowerCount))
                table.add_row("Real Followers", str(RealFollowers))
                table.add_row("Likes", str(likesCount))
                table.add_row("Answers count", str(answerCount))
                table.add_row("Tells count", str(tellCount))
                table.add_row("is Verified Account", "Yes" if isVerified else "No")
                table.add_row("isAbleToComment", "Yes" if isAbleToComment else "No")
                table.add_row("Account Country", str(countryCode))
                table.add_row("is Active now", "Yes" if isActive else "No")
                table.add_row("Avatar Link", str(avatar))
                Console().print(table, justify="center")

                self.driver.quit()
                input("\n[+] Done Sir.")
                exit()
        except Exception as e:
            self.driver.quit()
            input(f"[X] Error -> {str(e)}")
            exit()


username = input("\n| [?] Enter Username : ")
LordGivt(username)