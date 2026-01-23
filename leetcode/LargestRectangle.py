class Solution:
    def largestRectangleArea(self, heights):
        stack = [0,]  # will store indices
        max_area = 0
        heights.append(0)  # sentinel to flush out the stack at the end
        heights = [1,9,4,5,2,7]
        for i, h in enumerate(heights):
            # if current height is smaller than stack top -> pop
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                # width calculation
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
