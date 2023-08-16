from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(2, 4)

    @task
    def attempt(self):
        # self.client.get("/predict?sepallength=6.3&sepalwidth=2.5&petallength=4.9&petalwidth=1.5")
        # local
        # self.client.get("http://127.0.0.1:8000/predict?sequallength=3.0&sequalwidth=2.0&petallength=1.0&petalwidth=9.0")

        # On AWS
        # self.client.get('http://3.70.97.156/predict?sequallength=3.0&sequalwidth=2.0')


        # Relative 
        self.client.get('/predict?sequallength=3.0&sequalwidth=2.0')
