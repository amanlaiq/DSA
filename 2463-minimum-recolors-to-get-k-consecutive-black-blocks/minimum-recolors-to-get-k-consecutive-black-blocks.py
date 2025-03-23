class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        block_queue = deque()
        num_white = 0

        for i in range(k):
            current_char = blocks[i]
            if current_char == "W":
                num_white += 1
            block_queue.append(current_char)

        num_recolor = num_white

        for i in range(k, len(blocks)):
            if block_queue.popleft() == "W":
                num_white -= 1
            
            current_char = blocks[i]
            if current_char == "W":
                num_white += 1
            block_queue.append(current_char)

            num_recolor = min(num_recolor, num_white)

        return num_recolor