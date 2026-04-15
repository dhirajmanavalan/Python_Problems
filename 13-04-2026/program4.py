'Largest Rectangle in Histogram'
heights = [2,1,5,6,2,3]

stack = []
max_area = 0

for i in range(len(heights) + 1):
    while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
        h = heights[stack.pop()]
        w = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, h * w)

    stack.append(i)

print("Max area:", max_area)