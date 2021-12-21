import mediapipe as mp
import cv2
import math

from models import User

'''
왼쪽 팔각도 L_arm
오른쪽 팔각도 R_arm
왼쪽 겨드랑이 L_gyeo
오른쪽 겨드랑이 R_gyeo
왼쪽 골반 L_hip
오른쪽 골반 R_hip
왼쪽 무릎 L_knee
오른쪽 무릎 R_knee
'''

def getCal(L_arm, L_gyeo, L_hip, L_knee, R_arm, R_gyeo, R_hip, R_knee):
    usertable = User()
    usertable.score=0
    """
    #동작1-태권도
    if(L_arm >= 80 and L_arm <= 110):
        if(L_gyeo >= 40 and L_gyeo <= 60):
            if(L_hip >= 110 and L_hip <= 130):
                if(L_knee >= 95 and L_knee <= 125):
                    if(R_arm >= 170 and R_arm <= 190):
                        if(R_gyeo >= 20 and R_gyeo <= 25):
                            if(R_hip >= 125 and R_hip <= 145):
                                if(R_knee >= 165 and R_knee <= 190):
                                    usertable.score += 200
                                    print ("Taekwondo")

    #동작2-전사포즈
    if(L_arm >= 170 and L_arm <= 190):
        if(L_gyeo >=80 and L_gyeo <= 110):
            if(L_hip >= 80 and L_hip <= 110):
                if(L_knee >= 80 and L_knee <= 110):
                    if(R_arm >= 170 and R_arm <= 190):
                        if(R_gyeo >= 80 and R_gyeo <= 110):
                            if(R_hip >= 125 and R_hip <= 145):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 300
                                    print ("Warrior")

    #동작3-나무1(여자)
    if(L_arm >= 15 and L_arm <= 40):
        if(L_gyeo >= 95 and L_gyeo <= 110):
            if(L_hip >= 90 and L_hip <= 120):
                if(L_knee >= 30 and L_knee <= 45):
                    if(R_arm >= 15 and R_arm <= 40):
                        if(R_gyeo >= 95 and R_gyeo <= 110):
                            if(R_hip >= 170 and R_hip <= 190):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 200
                                    print ("Tree 1")

    #동작4-나무2(남자)
    if(L_arm >= 160 and L_arm <= 185):
        if(L_gyeo >= 170 and L_gyeo <= 190):
            if(L_hip >= 90 and L_hip <= 120):
                if(L_knee >= 30 and L_knee <= 45):
                    if(R_arm >= 160 and R_arm <= 185):
                        if(R_gyeo >= 170 and R_gyeo <= 190):
                            if(R_hip >= 170 and R_hip <= 190):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 100
                                    print ("Tree 2")

    #동작5-나무3(똥머리)
    if(L_arm >= 160 and L_arm <= 185):
        if(L_gyeo >= 150 and L_gyeo <= 170):
            if(L_hip >= 170 and L_hip <= 190):
                if(L_knee >= 170 and L_knee <= 190):
                    if(R_arm >= 170 and R_arm <= 190):
                        if(R_gyeo >= 45 and R_gyeo <= 70):
                            if(R_hip >= 85 and R_hip <= 115):
                                if(R_knee >= 30 and R_knee <= 45):
                                    usertable.score += 150
                                    print ("Tree 3")

    #동작6-십자가
    if(L_arm >= 170 and L_arm <= 190):
        if(L_gyeo >= 80 and L_gyeo <= 100):
            if(L_hip >= 170 and L_hip <= 190):
                if(L_knee >= 170 and L_knee <= 190):
                    if(R_arm >= 170 and R_arm <= 190):
                        if(R_gyeo >= 80 and R_gyeo <= 100):
                            if(R_hip >= 170 and R_hip <= 190):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 50
                                    print ("Cross")
    """

    #동작1 - 니가 사는 그집(your_home)
    if(L_arm >= 120 and L_arm <= 170):
        if(L_gyeo >= 160 and L_gyeo <= 180):
            if(L_hip >= 120 and L_hip <= 180):
                if(L_knee >= 155 and L_knee <= 180):
                    if(R_arm >= 120 and R_arm <= 170):
                        if(R_gyeo >= 160 and R_gyeo <= 180):
                            if(R_hip >= 80 and R_hip <= 130):
                                if(R_knee >= 75 and R_knee <= 110):
                                    usertable.score += 200
                                    print("Your Home")

    #동작2 - 전사 포즈(warrior)
    if(L_arm >= 155 and L_arm <= 180):
        if(L_gyeo >= 80 and L_gyeo <= 110):
            if(L_hip >= 90 and L_hip <= 140):
                if(L_knee >= 100 and L_knee <= 160):
                    if(R_arm >= 155 and R_arm <= 180):
                        if(R_gyeo >= 80 and R_gyeo <= 110):
                            if(R_hip >= 130 and R_hip <= 160):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 300
                                    print("Warrior")

    #동작3 - 서 (seo)
    if(L_arm >= 165 and L_arm <= 195):
        if(L_gyeo >= 65 and L_gyeo <= 100):
            if(L_hip >= 60 and L_hip <= 85):
                if(L_knee >= 165 and L_knee <= 195):
                    if(R_arm >= 165 and R_arm <= 195):
                        if(R_gyeo >= 100 and R_gyeo <= 140):
                            if(R_hip >= 140 and R_hip <= 180):
                                if(R_knee >= 165 and R_knee <= 195):
                                    usertable.score += 500
                                    print("Seo")

    #동작4 - Y
    if(L_arm >= 160 and L_arm <= 180):
        if(L_gyeo >= 150 and L_gyeo <= 170):
            if(L_hip >= 160 and L_hip <= 180):
                if(L_knee >= 160 and L_knee <= 180):
                    if(R_arm >= 160 and R_arm <= 180):
                        if(R_gyeo >= 150 and R_gyeo <= 170):
                            if(R_hip >= 160 and R_hip <= 180):
                                if(R_knee >= 160 and R_knee <= 180):
                                    usertable.score += 100
                                    print("Y")

    #동작5 - 가랑이 삼각형(triangle)
    if(L_arm >= 150 and L_arm <= 180):
        if(L_gyeo >= 100 and L_gyeo <= 125):
            if(L_hip >= 130 and L_hip <= 180):
                if(L_knee >= 120 and L_knee <= 180):
                    if(R_arm >= 150 and R_arm <= 180):
                        if(R_gyeo >= 90 and R_gyeo <= 130):
                            if(R_hip >= 120 and R_hip <= 160):
                                if(R_knee >= 70 and R_knee <= 100):
                                    usertable.score += 200
                                    print("Triangle")


def calculateAngle(i, j, k):
    try:
        x1, y1 = results.pose_landmarks.landmark[mp_holistic.PoseLandmark(i).value].x, results.pose_landmarks.landmark[mp_holistic.PoseLandmark(i).value].y
        x2, y2 = results.pose_landmarks.landmark[mp_holistic.PoseLandmark(j).value].x, results.pose_landmarks.landmark[mp_holistic.PoseLandmark(j).value].y
        x3, y3 =results.pose_landmarks.landmark[mp_holistic.PoseLandmark(k).value].x, results.pose_landmarks.landmark[mp_holistic.PoseLandmark(k).value].y
    
        length_ij = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        length_jk = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        length_ki = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

        angle_cos2 = int(math.degrees(math.acos((length_ij ** 2 + length_jk ** 2 - length_ki ** 2) / (2 * length_ij * length_jk))))
        
        angle_atan = int(math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2)))

        return angle_cos2

    except:
        return 0


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)

with mp_holistic.Holistic() as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        # color 채널 변경
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # holistic 적용
        results = holistic.process(image)

        # imshow를 위해 채널 변경
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        # print(results.pose_landmarks.landmark[mp_holistic.PoseLandmark(15).value].x)  #19
        # print(results.pose_landmarks.landmark[mp_holistic.PoseLandmark(15).value].y)
        # def getCal():
        L_arm = calculateAngle(12, 14, 16) #L_arm
        L_gyeo = calculateAngle(14, 12, 24) #L_gyeo
        L_hip = calculateAngle(12, 24, 26) #L_hip
        L_knee = calculateAngle(24, 26, 28) #L_knee
        R_arm = calculateAngle(11, 13, 15) #R_arm
        R_gyeo = calculateAngle(13, 11, 23) #R_gyeo
        R_hip = calculateAngle(11, 23, 25) #R_hip
        R_knee = calculateAngle(23, 25, 27) #R_knee
        
        # print(f"""L_arm: {L_arm}, 
        # L_gyeo: {L_gyeo}, 
        # L_hip: {L_hip}, 
        # L_knee: {L_knee},
        # R_arm: {R_arm}, 
        # R_gyeo: {R_gyeo}, 
        # R_hip: {R_hip}, 
        # R_knee: {R_knee} """)

        getCal(L_arm, L_gyeo, L_hip, L_knee, R_arm, R_gyeo, R_hip, R_knee)

        cv2.imshow('Pose Landmark', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()