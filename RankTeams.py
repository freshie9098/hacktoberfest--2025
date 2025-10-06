class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # Create array as : "A" : (0:0),(1:0)....and so on.
        di = {}
        for vote in votes:
            for i in range(len(vote)):
                ch = vote[i]
                if di.get(ch,0)==0:
                    di[ch] = [0]*(len(vote))
                di[ch][i]+=1
        
        # sort the team based on the ASC order
        # Keep negative parts as first so that its sorted better. 
        teams_sorted = sorted(
            di.items(), 
            key = lambda x: ([-v for v in x[1]], x[0])
        )
        res = []
        for team in teams_sorted:
            res.append(team[0])
        return ''.join(res)
