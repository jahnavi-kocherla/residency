import time

class Block:
    def __init__(self, number, data, prev_number):
        self.number = number
        self.data = data
        self.prev_number = prev_number
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def display(self):
        print(f"Block Number: {self.number}")
        print(f"Data: {self.data}")
        print(f"Previous Block Number: {self.prev_number}")
        print(f"Timestamp: {self.timestamp}")
        print("-" * 30)

class SimpleBlockchain:
    def __init__(self):
        self.chain = []

    def create_block(self, data):
        number = len(self.chain) + 1
        prev_number = self.chain[-1].number if self.chain else None
        block = Block(number, data, prev_number)
        self.chain.append(block)
        print(f"\n✅ Block {number} created successfully.\n")

    def display_block(self, number):
        if 1 <= number <= len(self.chain):
            self.chain[number - 1].display()
        else:
            print("\n❌ Block not found.\n")

    def display_all_blocks(self):
        if not self.chain:
            print("\n⛔ No blocks in the blockchain yet.\n")
        else:
            print("\n🔗 Showing all blocks:\n")
            for block in self.chain:
                block.display()

def main():
    blockchain = SimpleBlockchain()
    print("🔷 Welcome to the Simplified Virtual Blockchain!\n")

    # Pre-fill 10 blocks with default data
    for i in range(1, 11):
        blockchain.create_block(f"Auto-filled data for block {i}")

    while True:
        print("Menu:")
        print("1. Create a new block")
        print("2. View a block by number")
        print("3. View all blocks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            data = input("Enter data for the new block: ").strip()
            if data:
                blockchain.create_block(data)
            else:
                print("\n⚠️ Data cannot be empty.\n")

        elif choice == '2':
            try:
                num = int(input("Enter block number to view: ").strip())
                blockchain.display_block(num)
            except ValueError:
                print("\n❗ Please enter a valid number.\n")

        elif choice == '3':
            blockchain.display_all_blocks()

        elif choice == '4':
            print("\n👋 Exiting program. Goodbye!\n")
            break

        else:
            print("\n❗ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
