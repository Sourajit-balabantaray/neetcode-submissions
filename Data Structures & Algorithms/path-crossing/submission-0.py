class Solution:
    def isPathCrossing(self, path: str) -> bool:
        di={"N":(0,1),
           "S":(0,-1),
           "E":(+1,0),
           "W":(-1,0),}
        x=y=0
        seen={(0,0)}
        for i in path:
            x+=di[i][0]
            y+=di[i][1]
            if (x,y) in seen:
                return True
            seen.add((x,y))
        return False
        
        