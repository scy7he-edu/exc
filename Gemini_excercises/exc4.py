#Тз от gemini: Проект: "Ledger of Truth" (Простой Блокчейн)
#Твоя задача — написать программу, которая имитирует цепочку блоков. 
#Каждый блок должен быть связан с предыдущим через его хеш. 
#Если изменить данные в старом блоке, вся цепочка после него должна стать невалидной.

from hashlib import sha256
from datetime import datetime as dt
from dataclasses import dataclass, field

@dataclass
class Block:
    index: int = field(init = False)
    timestamp: float = field(init = False)
    data: str
    previous_hash: str
    hash: str = field(init = False)
    nonce: int

    _index_counter: int = 0

    def __post_init__(self):
        Block._index_counter += 1
        self.index = Block._index_counter
        self.timestamp = self._generate_timestamp()
        self.hash = self.get_hash()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.get_hash()
    
    def _generate_timestamp(self):
        return dt.now().timestamp()
    
    def get_hash(self):
        sha = sha256()
        payload = f'{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}'
        sha.update(payload.encode('utf-8'))
        return sha.hexdigest()
    
    def __str__(self):
        return f'id: {self.index}, timestamp: {self.timestamp}, hash: "{self.hash}", prev. hash: "{self.previous_hash}", data: {self.data}'
    
class Blockchain:
    difficulty: int = 4

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        gen = Block('Genesis Block', '0', 0)
        self.chain.append(gen)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.get_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True

blc = Blockchain()

print("Майнинг блока 1.")
blc.add_block(Block('User1 -> User2: 10 BTC', '', 0))
print("Майнинг блока 2.")
blc.add_block(Block('User2 -> User3: 5 BTC', '', 0))
print("Майнинг блока 3.")
blc.add_block(Block('User3 -> User4: 2 BTC', '', 0))

for block in blc.chain:
    print(block)

print(f"Цепочка валидна: {blc.is_chain_valid()}")

print('---------------------------------------------')
blc.chain[1].data='Hacked'
print('      ---blc.chain[1].data changed---')
print(f'Цепочка валидна: {blc.is_chain_valid()}')