def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort(reverse=True) 
    print (ranked)   
    player_ranked = [] 
    rank = 0
    for score in player:
        #rank = 1
        for j in ranked:
            if score >= j:
                player_ranked.append(rank)
                break
            elif score < j and rank == len(ranked):
                player_ranked.append(rank+1)
                break
            rank += 1
    return player_ranked



ranked = [100, 100, 50, 40, 40, 20, 10] # 80 90 100
player = [5, 25, 50, 120] 

print (climbingLeaderboard(ranked, player)) 