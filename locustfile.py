from locust import HttpLocust, TaskSet, task


class BlogView(TaskSet):
    def on_start(self):
        self.client.get("/")

    @task
    def view_blog(self):
        self.client.get("/")


class WebVisitor(HttpLocust):
    task_set = BlogView
    min_wait = 5000
    max_wait = 9000
