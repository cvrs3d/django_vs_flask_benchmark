from locust import HttpUser, TaskSet, task, between
import os
import random


class UserBehavior(TaskSet):
    def on_start(self):
        self.order_urls = []
        with open("order_urls.txt", 'r') as file:
            self.order_urls = [line.strip('\n') for line in file]

    @task(1)
    def get_order(self):
        url = random.choice(self.order_urls)
        self.client.get(url)


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2)