import asyncio
from collections import deque

class RenameQueue:
    def __init__(self):
        # A dictionary to store the queue for each user
        self.user_queues = {}

    def add_to_queue(self, user_id, task):
        # Initialize a queue for the user if not exists
        if user_id not in self.user_queues:
            self.user_queues[user_id] = deque()
        self.user_queues[user_id].append(task)

    async def process_queue(self, user_id):
        # Process the user's queue
        if user_id in self.user_queues and self.user_queues[user_id]:
            while self.user_queues[user_id]:
                task = self.user_queues[user_id].popleft()
                await task()
            del self.user_queues[user_id]  # Remove user from queue after processing

    def is_in_queue(self, user_id):
        # Check if the user has tasks in queue
        return user_id in self.user_queues and bool(self.user_queues[user_id])

rename_queue = RenameQueue()
