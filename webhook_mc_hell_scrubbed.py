import random
import time
import requests
import threading
import tkinter as tk
import asyncio

clock=0
loop=True
exitloop=False
message=""
i=0

timer_min = 900
timer_max = 1800



####DO NOT TOUCH URLS FOR THE WEBHOOKS####

discord_webhook_url_MC_hell = ''

#messages for MC hell

connor_1="<@364875753940058113> oooooh you want to shave your legs and wear thigh highs oooooooh"

connor_2="this man <@364875753940058113> owns 10 fur suits and is in crippling debt trying to manage them"

suket_2="<@264786926404370434> quarantined bitch"

suket_3="<@264786926404370434> would you like to join the fabulous website pen island? (penisland.com)"

suket_4="<@264786926404370434> fuck you"

h4ck3r_1="<@&698723998489378898> shit programmer fuck you"

xi_1="<@&698734917747605524> 动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet 六四天安門事件 The Tiananmen Square protests of 1989 天安門大屠殺 The Tiananmen Square Massacre 反右派鬥爭 The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward 文化大革命 The Great Proletarian Cultural Revolution 人權 Human Rights 民運 Democratization 自由 Freedom 獨立 Independence 多黨制 Multi-party system 台灣 臺灣 Taiwan Formosa 中華民國 Republic of China 西藏 土伯特 唐古特 Tibet 達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區 The Xinjiang Uyghur Autonomous Region 諾貝爾和平獎 Nobel Peace Prize 劉暁波 Liu Xiaobo 民主 言論 思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口 遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 Winnie the Pooh 劉曉波动态网自由门"

alex_jones_1="I will, I'll do it right now. I'll get in the ring with you and I will break your jaw, I will knock your teeth out, I will break your nose, and I will break your neck. You coward, you think you're tough guy, messing with little cameramen people. You want to sit there and defame me and the president? Get in the ring with me, I will break your jaw in seconds. I will smash your nose into a bloody pulp, and I will whack your teeth out. My fists are going to bleeding with your teeth marks all over em. You frickin' bully, you coward. I hate you"

eric_2="<@251788258529378304> died to a fucking baby magma cube imagine being this guy"

zohal_1="<@446333426296160266>"

marine_1="What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."

madzia_2="According to all known :speaking_head: laws :hammer: :writing_hand: of aviation :airplane:, there is no :x: way that a bee :bee: should be able :heavy_check_mark: to fly :butterfly: :bee: . Its wings :wind_blowing_face: are too small :white_small_square: to get its fat :busts_in_silhouette: little body :boy: off the ground :beach_umbrella: . The bee :bee: , of course, flies :wind_blowing_face: anyway. Because bees :bee: don’t :x: care :no_good: what humans :couple: think is impossible :no_entry_sign: .” SEQ. 75 - “INTRO TO BARRY” INT. BENSON HOUSE - DAY ANGLE ON: Sneakers :athletic_shoe: on the ground :earth_americas: :beach_umbrella: . Camera :movie_camera: PANS UP :arrow_up: to reveal :hushed: BARRY BENSON’S BEDROOM :bed: ANGLE ON: Barry’s hand :hand_splayed: flipping :middle_finger: through different sweaters :shirt: in his closet:closed_umbrella: . BARRY Yellow :yellow_heart: black :black_heart: , yellow :yellow_heart: black :black_heart: yellow :yellow_heart: black :black_heart: yellow :yellow_heart: black :black_heart: yellow :yellow_heart: black :black_heart:, yellow :yellow_heart: black :black_heart: ...oohh, black :black_heart: and yellow :yellow_heart:... ANGLE ON: Barry wearing the sweater :shirt: he picked :thinking: , looking :eyes: in the mirror . BARRY (CONT’D) Yeah :white_check_mark: , let’s shake :handshake: it up :arrow_up_small: a little :white_small_square: . He picks :eye: the black :black_heart: and yellow :yellow_heart: one :one: . He then goes :walking: to the sink :potable_water: , takes the top :top: off :mobile_phone_off: a CONTAINER :wastebasket: OF HONEY :honey_pot: , and puts some honey :honey_pot: into his hair :haircut: . He squirts :sweat_drops: some in his mouth :lips: and gargles :anger_right: . Then he takes :head_bandage: the lid :level_slider: off the bottle :champagne: , and rolls :newspaper2: some on like deodorant :snowflake: . CUT :scissors: TO :two: : INT. BENSON HOUSE"

madzia_3="<@607262136623824897>"

madzia_4="eric has a gun. this is a threat"

madzia_5="<@607262136623824897> short ass mother fucker"

eva_1="<@757725466575503381>"

shadow_copy_pasta_1="I've come to make an announcement: Zohal Karim's a bitch-ass motherfucker. They pissed on my fucking wife. That's right. They took their hedgehog fuckin' quilly dick out and they pissed on my FUCKING wife, and they said their dick was THIS BIG, and I said that's disgusting. So I'm making a callout post on my Twitter.com. Zohal Karim, you got a small dick. It's the size of this walnut except WAY smaller. And guess what? Here's what my dong looks like. That's right, baby. Tall points, no quills, no pillows, look at that, it looks like two balls and a bong. They fucked my wife, so guess what, I'm gonna fuck the earth. That's right, this is what you get! My SUPER LASER PISS! Except I'm not gonna piss on the earth. I'm gonna go higher. I'm pissing on the MOOOON! How do you like that, OBAMA? I PISSED ON THE MOON, YOU IDIOT! You have twenty-three hours before the piss DROPLETS hit the fucking earth, now get out of my fucking sight before I piss on you too!"

#message list store MC hell

MC_hell_messages=[connor_1, connor_2, suket_2, suket_3, suket_4, h4ck3r_1, xi_1, alex_jones_1, eric_2, zohal_1, marine_1, madzia_2, madzia_3, madzia_4, madzia_5, eva_1, shadow_copy_pasta_1]


# Post the message to the Discord webhook at a random interval via random message selection

def verbal_abuse():     ##defining the process to loop the webhook
    
    while exitloop==False:      ##this can be used to temporarily stop the loop while it continues checking to see if it has been reactivated
            
        while loop == True:
                
            clock=random.randint(timer_min, timer_max) #chooses interval

                #chooses number for message to be chosen from

            message=random.choice(MC_hell_messages)

                    #sets data to the message to send to the webhook
                
            data = {
                    
                "content": message
                    
                }
                
            requests.post(discord_webhook_url_MC_hell, data=data)



            time.sleep(clock)



class Application(tk.Frame):

    def __init__(self, master=None):        ##standardly copied from documentation/previous project

        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        def shutdown():     ##a function that shuts down the thread by ending the loop completely
    
            exitloop=True
            loop=False
            print(str(exitloop) + " " + str(loop))
            print("shutdown complete")

        self.quit = tk.Button(self, width = 10, height = 1, text = "QUIT")  ##making the buttons
        self.quit["command"] = self.master.destroy
        self.quit.grid(row = 99, column =1)
        self.end = tk.Button(self, width = 10, height = 1, text = "shutdown")
        self.end["command"] = lambda i=i: shutdown()
        self.end.grid(row = 2, column = 1)

        self.timer_min_change = tk.Entry(self)      ##making entry fields to change interval
        self.timer_min_change.insert(10, "900")
        self.timer_min_change.grid(row = 1, column = 0)
        
        self.timer_max_change = tk.Entry(self)
        self.timer_max_change.insert(10, "1800")
        self.timer_max_change.grid(row = 1, column = 2)

        timer_min=self.timer_min_change.get()       ##changing the interval (hopefully)
        timer_max=self.timer_max_change.get()

abuse_thread = threading.Thread(target = verbal_abuse, daemon=True)     ##creates thread and starts it

abuse_thread.start()

root = tk.Tk()

app = Application(master=root)

app.master.title=("verbal abuse UI")
app.master.geometry("400x100")
app.mainloop()




