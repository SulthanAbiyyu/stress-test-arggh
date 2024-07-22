from locust import HttpUser, TaskSet, task, between

class MyTaskSet(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    @task
    def items(self):
        self.client.get("/items/1?q=test")

class MyUser(HttpUser):
    tasks = [MyTaskSet]
    wait_time = between(1, 5)
