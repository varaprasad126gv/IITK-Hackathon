class Agent:
    def __init__(self, name):
        self.name = name

    def respond(self, input_text):
        raise NotImplementedError("Each agent must implement respond()")