class Solution(object):
    def buildArray(self, target, n):
        commands = []
        stop_int = max(target)
        for i in range(1,n+1):
            commands.append("Push")
            if i not in target:
                commands.append("Pop")
            if i == stop_int:
                break
        return commands         
        