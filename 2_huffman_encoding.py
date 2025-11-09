import heapq

# Creating Huffman tree node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq      # Frequency of symbol
        self.symbol = symbol  # Symbol name (character)
        self.left = left      # Node left of current node
        self.right = right    # Node right of current node
        self.huff = ''        # Tree direction (0/1)

    def __lt__(self, nxt):
        return self.freq < nxt.freq


# Function to print Huffman codes
def print_nodes(node, val=''):
    new_val = val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    # If leaf node
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")


# Main function
if __name__ == "__main__":
    print("----- Huffman Coding -----")

    # Take number of symbols
    n = int(input("Enter the number of characters: "))

    chars = []
    freq = []

    # Taking input from user
    for i in range(n):
        ch = input(f"Enter character {i+1}: ")
        f = int(input(f"Enter frequency of '{ch}': "))
        chars.append(ch)
        freq.append(f)

    # Creating a list of nodes
    nodes = []
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freq[i], chars[i]))

    # Combine nodes until one remains
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    print("\nHuffman Codes for each character:")
    print("--------------------------------")
    print_nodes(nodes[0])

# ouput:
#----- Huffman Coding -----
#Enter the number of characters: 4
#Enter character 1: m
#Enter frequency of 'm': 1
#Enter character 2: p
#Enter frequency of 'p': 2
#Enter character 3: s
#Enter frequency of 's': 4
#Enter character 4: i
#Enter frequency of 'i': 4
#
#Huffman Codes for each character:
#--------------------------------
#i -> 0
#m -> 100
#p -> 101
#s -> 11