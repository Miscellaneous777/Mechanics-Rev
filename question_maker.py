import math
from random import *

#Projectiles Class will generate all the questions for the program.
#Harder questions will use simpler questions to 

class Projectiles:
    def __init__(self):
        self.grav = 9.80665
    def simple_q(self):
        angle = randint(1,89)
        velocity = randint(5,50)

        u = velocity #Converting to mechanics terms for my own usability
        theta = math.radians(angle) #Math module needs it in radians :/

        # calculations

        timeTakenEnd = (2*u*math.sin(theta))/self.grav
        #Should calculate the time it takes for the projectile to complete the curve

        highPoint = ((u**2)*math.sin(theta)**2)/(2*self.grav)
        
        finalPoint = (u*math.cos(theta))*timeTakenEnd
        

        return angle,velocity,finalPoint,highPoint,timeTakenEnd

    def simple_q_teach(self,angle,velocity):
        
        u = velocity
        theta = math.radians(angle)

        # calculations

        timeTakenEnd = (2*u*math.sin(theta))/self.grav
        #Should calculate the time it takes for the projectile to complete the curve

        highPoint = ((u**2)*math.sin(theta)**2)/(2*self.grav)
        
        finalPoint = (u*math.cos(theta))*timeTakenEnd

        print(finalPoint,highPoint,timeTakenEnd)

        return finalPoint,highPoint,timeTakenEnd

    def medium_q(self):
        angle,velocity,finalPoint,highPoint,timeTakenEnd = self.simple_q()
        print(angle)
        print(finalPoint)

        #Generate
        
        obj_location = randint(0,int(finalPoint))
        print(obj_location)
        
    def hard_q(self):
        print("none")

class Kinematics:
    def __init__(self):
        self.grav = 9.81
    def simple_weight_q(self):

        weight = randint(1,50)
        s = ""
        u = 0
        v = ""
        a = self.grav * weight
        t = ""

        s_or_t_or_v = randint(0,2)

        if s_or_t_or_v == 0: # Generates question giving t
            t = randint(1,20)
            
            s = u*t + 0.5*a*t**2
            v = u + a*t
            
        elif s_or_t_or_v == 1: # Generates question giving s
            s = randint(1,50)
            
            t = math.sqrt((2*s)/a)
            v = u + a*t

        elif s_or_t_or_v == 2: # Generates question giving v
            v = randint(1,100)
            
            t = (v-u)/a
            s = u*t + 0.5*a*t**2

        return s,u,v,a,t,weight,s_or_t_or_v
        


        

if __name__ == "__main__":
    bobby = Projectiles()
    print(bobby.simple_q())
