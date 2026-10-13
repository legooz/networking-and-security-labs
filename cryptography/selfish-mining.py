# Recovered student coursework; see README.md and PROVENANCE.json for attribution and status.
import random


state = 0
total_transitions = 20000
for alpha in [0.1, 0.2, 0.3, 0.4]:
    print(f"alpha = {alpha}")
    
    for gamma in [0.0, 0.5, 1.0]:
        total_selfish_revenue = 0
        total_honest_revenue = 0
        
        for _ in range(1,total_transitions):
            randint = random.random()
            honestminerportion = random.random()
            #state 0 
            if (state == 0):
                #print("state 0")
                if(alpha >= randint): # 0 - 0.1
                    state = 1
                    total_selfish_revenue += 0
                elif(alpha < randint): # 0.1 - 1
                    state = 0
                    total_honest_revenue += 1
            #state 1 or greater
            elif (state >= 1):
                #print("state: ", state)
                if(state == 1 and alpha < randint):
                    state = -1
                    total_honest_revenue += 0
                elif(state == 2 and alpha < randint):
                    state = 0
                    total_honest_revenue += 0
                elif(state == 1 and alpha >= randint):
                    state = 2
                    total_selfish_revenue += 2
                elif(alpha >= randint):
                    state += 1
                    total_selfish_revenue += 1
                elif(alpha < randint):
                    state -= 1
                    total_honest_revenue += 0
            #state 0'
            elif(state == -1):
                #print("state 0'")
                if(alpha >= randint):
                    state = 0
                    total_selfish_revenue += 2
                elif(alpha < randint and gamma < honestminerportion):
                    state = 0
                    total_honest_revenue += 2
                elif(alpha < randint and gamma >= honestminerportion):
                    state = 0
                    total_honest_revenue += 1
                    total_selfish_revenue += 1


                
        
        relative_revenue = total_selfish_revenue / ( total_selfish_revenue + total_honest_revenue )

        print(f" gamma = {gamma}, Selfish Miner Relative Revenue = {relative_revenue}")
