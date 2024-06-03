import pickle
import json
import config
import numpy as np

class Student_performance():
   def __init__(self,hours_studied,previous_score,extra_act,sleep_hours,sample_paper):
     self.hours_studied = hours_studied
     self.previous_score = previous_score
     self.extra_act = extra_act
     self.sleep_hours = sleep_hours
     self.sample_paper = sample_paper
    
   def load_model(self):
      with open(config.model_path,'rb') as f:
         self.model = pickle.load(f)

      with open(config.json_path,'r') as f:
         self.project_data = json.load(f)

   def get_predicted_score(self):
      self.load_model()  
        
      test_array = np.zeros(5)
      test_array[0]=self.hours_studied
      test_array[1]=self.previous_score
      test_array[2]=self.project_data['extra_act'][self.extra_act]
      test_array[3]=self.sleep_hours
      test_array[4]=self.sample_paper
      print('The Test Arrays',test_array)

      prediction = self.model.predict([test_array])[0]
      print(f'The Predicted Score of the Student is ',{round(prediction,2)})
      return prediction

if __name__ == '__main__':
 hours_studied = 8
 previous_score = 92
 extra_act = 'yes'
 sleep_hours	= 8
 sample_paper = 2
 Scores = Student_performance(hours_studied,previous_score,extra_act,sleep_hours,sample_paper)
 Scores.get_predicted_score()
