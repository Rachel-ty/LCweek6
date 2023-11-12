class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cnt=0
        q=deque()
        indegree={}
        pre={}
        vis=set()
        for a,b in prerequisites:
            if a not in indegree:
                indegree[a]=1
            else:
                indegree[a]+=1
            if b not in pre:
                pre[b]=[]
            pre[b].append(a)
        for i in range(numCourses):
            if i not in indegree:
                vis.add(i)
                q.append(i)
                cnt+=1
        while q:
            cur=q.popleft()
            if cur in pre:
                for i in pre[cur]:
                    indegree[i]-=1
            for key,value in indegree.items():
                if value==0 and key not in vis:
                    vis.add(key)
                    q.append(key)
                    cnt+=1
        return cnt==numCourses