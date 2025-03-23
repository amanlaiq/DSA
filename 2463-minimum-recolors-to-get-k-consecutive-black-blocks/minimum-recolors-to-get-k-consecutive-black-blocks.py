class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        block_queue = deque()
        num_white = 0

        for i in range(k):
            if blocks[i] == "W":
                num_white += 1
            block_queue.append(blocks[i])

        num_recolor = num_white

        for i in range(k, len(blocks)):
            if block_queue.popleft() == "W":
                num_white -= 1
            if blocks[i] == "W":
                num_white += 1
            block_queue.append(blocks[i])

            num_recolor = min(num_recolor, num_white)

        return num_recolor