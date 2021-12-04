#왼쪽 팔각도 L_arm
#오른쪽 팔각도 R_arm
#왼쪽 겨드랑이 L_gyeo
#오른쪽 겨드랑이 R_gyeo
#왼쪽 골반 L_hip
#오른쪽 골반 R_hip
#왼쪽 무릎 L_knee
#오른쪽 무릎 R_knee

from models.models import User

L_arm=0, R_arm=0, L_gyeo=0, R_gyeo=0
L_hip=0, R_hip=0, L_knee=0, R_knee=0

# 여기에다가 캠에서 받아온 각도 추출한 것 각도 저장하고 L_arm등에 받아오기

#동작1-태권도
if(L_arm >= 80 & L_arm <= 110):
    if(L_gyeo >= 40 & L_gyeo <= 60):
        if(L_hip >= 110 & L_hip <= 130):
            if(L_knee >= 95 & L_knee <= 125):
                if(R_arm >= 170 & R_arm <= 190):
                    if(R_gyeo >= 20 & R_gyeo <= 40):
                        if(R_hip >= 125 & R_hip <= 145):
                            if(R_knee >= 165 & R_knee <= 190):
                                usertable = User() 
                                usertable.score += 200
                                print ("Taekwondo")

#동작2-전사포즈
if(L_arm >= 170 & L_arm <= 190):
    if(L_gyeo >=80 & L_gyeo <= 110):
        if(L_hip >= 80 & L_hip <= 110):
            if(L_knee >= 80 & L_knee <= 110):
                if(R_arm >= 170 & R_arm <= 190):
                    if(R_gyeo >= 80 & R_gyeo <= 110):
                        if(R_hip >= 125 & R_hip <= 145):
                            if(R_knee >= 170 & R_knee <= 190):
                                usertable = User() 
                                usertable.score += 300
                                print ("Warrior")

#동작3-나무1(여자)
if(L_arm >= 15 & L_arm <= 40):
    if(L_gyeo >= 95 & L_gyeo <= 110):
        if(L_hip >= 90 & L_hip <= 120):
            if(L_knee >= 30 & L_knee <= 45):
                if(R_arm >= 15 & R_arm <= 40):
                    if(R_gyeo >= 95 & R_gyeo <= 110):
                        if(R_hip >= 170 & R_hip <= 190):
                            if(R_knee >= 170 & R_knee <= 190):
                                usertable = User() 
                                usertable.score += 200
                                print ("Tree 1")

#동작4-나무2(남자)
if(L_arm >= 160 & L_arm <= 185):
    if(L_gyeo >= 170 & L_gyeo <= 190):
        if(L_hip >= 90 & L_hip <= 120):
            if(L_knee >= 30 & L_knee <= 45):
                if(R_arm >= 160 & R_arm <= 185):
                    if(R_gyeo >= 170 & R_gyeo <= 190):
                        if(R_hip >= 170 & R_hip <= 190):
                            if(R_knee >= 170 & R_knee <= 190):
                                usertable = User() 
                                usertable.score += 100
                                print ("Tree 2")

#동작5-나무3(똥머리)
if(L_arm >= 160 & L_arm <= 185):
    if(L_gyeo >= 150 & L_gyeo <= 170):
        if(L_hip >= 170 & L_hip <= 190):
            if(L_knee >= 170 & L_knee <= 190):
                if(R_arm >= 170 & R_arm <= 190):
                    if(R_gyeo >= 45 & R_gyeo <= 70):
                        if(R_hip >= 85 & R_hip <= 115):
                            if(R_knee >= 30 & R_knee <= 45):
                                usertable = User() 
                                usertable.score += 150
                                print ("Tree 3")

#동작6-십자가
if(L_arm >= 170 & L_arm <= 190):
    if(L_gyeo >= 80 & L_gyeo <= 100):
        if(L_hip >= 170 & L_hip <= 190):
            if(L_knee >= 170 & L_knee <= 190):
                if(R_arm >= 170 & R_arm <= 190):
                    if(R_gyeo >= 80 & R_gyeo <= 100):
                        if(R_hip >= 170 & R_hip <= 190):
                            if(R_knee >= 170 & R_knee <= 190):
                                usertable = User() 
                                usertable.score += 50
                                print ("Cross")