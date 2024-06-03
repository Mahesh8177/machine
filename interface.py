from flask import Flask, render_template, request, jsonify
from project_student.utils import Student_performance
import config

app = Flask(__name__)

#################################################################################################################
#################################### Home Page API ##############################################################
#################################################################################################################

@app.route('/')
def Performance_model():
    print('Welcome to Student Performnace Model')
    return render_template('performance.html')

###################################################################################################################
########################################## Model API ##############################################################
###################################################################################################################

@app.route('/predict_score', methods = ['POST','GET'])
def get_predicted_score():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        hours_studied = float(data['hours_studied'])
        previous_score = float(data['previous_score'])
        extra_act = data['extra_act']
        sleep_hours = float(data['sleep_hours'])
        sample_paper = float(data['sample_paper'])

        Scores = Student_performance(hours_studied,previous_score,extra_act,sleep_hours,sample_paper)
        pred_Scores = Scores.get_predicted_score()
        return jsonify({'The Predicted score is ',round(pred_Scores,2)})
    else:
        print('We are in GET Method')
        data1 = request.args
        hours_studied = float(data1.get('hours_studied'))
        previous_score = float(data1.get('previous_score'))
        extra_act = data1.get('extra_act')
        sleep_hours= float(data1.get('sleep_hours'))
        sample_paper= float(data1.get('sample_paper'))

        Scores1 = Student_performance(hours_studied,previous_score,extra_act,sleep_hours,sample_paper)
        pred_Scores = Scores1.get_predicted_score()
        return jsonify({'The Predicted score is': round(pred_Scores, 2)})
        print(data1)
    
if __name__=='__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug=True)
    