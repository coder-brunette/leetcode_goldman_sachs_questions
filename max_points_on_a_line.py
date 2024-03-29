
# def maxPoints(points):
#     if len(points) < 3:
#         return len(points)
#     max_points = 0
#     for i in range(len(points)):
#         slopes = {}
#         vertical = 0
#         duplicate = 0
#         current_max = 1
#         for j in range(i+1, len(points)):
#             x1, y1 = points[i]
#             x2, y2 = points[j]
#             if x1 == x2:
#                 if y1 == y2:
#                     duplicate += 1
#                 else:
#                     vertical += 1
#             else:
#                 slope = (y2 - y1) / (x2 - x1)
#                 slopes[slope] = slopes.get(slope, 1) + 1
#                 current_max = max(current_max, slopes[slope])
        
#         max_points = max(max_points, current_max + duplicate + 1, vertical + duplicate + 1)
#     return max_points

# print(maxPoints([[4, 5], [4, -1], [4, 0]]))
# print(maxPoints([[1,1],[2,2],[3,3]]))


def maxPoints(points):
    n=len(points)
    d={}
    for i in range(n):
        x,y=points[i][0],points[i][1]
        for j in range(i+1,n):
            x1=x-points[j][0]
            y1=y-points[j][1]
            b=x1*y-y1*x
            d[(y1,x1,b)]=0
    for i in range(n):
        x,y=points[i][0],points[i][1]
        for j in d:
            if j[1]*y==j[0]*x+j[2]:
                    d[j]+=1
    m=1
    for x in d:
        m=max(m,d[x])
    return m

print(maxPoints([[1,1],[2,2],[3,3]]))