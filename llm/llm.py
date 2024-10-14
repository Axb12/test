class Model:

    def __init__(self, model_name):
        self.model_name = model_name

    def chat(self, query):
        # operate
        return "success"

model = Model(model_name="gpt-3.5-turbo")