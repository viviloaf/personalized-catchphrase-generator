from aitextgen import aitextgen
import numpy as np

class Gpt2Generator():
    
    def __init__(self):
        ai = aitextgen(model="models/my_fb_trained_model/pytorch_model.bin", config="models/my_fb_trained_model/config.json")
        self.ai = ai

    def twitter_respond(self, passing_input, temperature):
        '''
        Args:
        
        '''

        def generate_response(passing_input):
            ai_output = self.ai.generate(prompt=passing_input,
                    temperature=temperature,
                    max_length=1024,
                    return_as_list=True)
            return ai_output
            
        ai_output = generate_response(passing_input)
        
        if ai_output[0] == passing_input or ai_output[0].split(passing_input) != ' \\n':
            new_passing_input = np.random.choice(passing_input.split())
            new_passing_output = generate_response(new_passing_input)
            
            return passing_input, new_passing_output[0]

        else:
            return passing_input, ai_output.split(passing_input)