from flask import Flask, render_template, request, jsonify
from project_student.utils import Student_performance
import config

app = Flask(__name__)

#################################################################################################################
#################################### Home Page API ##############################################################
#################################################################################################################

@app.route('/')
def Performance_model():
    print('Welcome to Student Performance Model')
    return render_template('performance.html')

###################################################################################################################
########################################## Model API ##############################################################
###################################################################################################################

@app.route('/predict_score', methods=['POST', 'GET'])
def get_predicted_score1():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        
        try:
            Hours_Studied = float(data['Hours_Studied'])
            Previous_Scores = float(data['Previous_Scores'])
            Extracurricular_Activities = data['Extracurricular_Activities']
            Sleep_Hours = float(data['Sleep_Hours'])
            Sample_Question_Papers_Practiced = float(data['Sample_Question_Papers_Practiced'])

            Pred_Scores = Student_performance(Hours_Studied, Previous_Scores, Extracurricular_Activities, Sleep_Hours, Sample_Question_Papers_Practiced)
            predicted_score = Pred_Scores.get_Predicted_score()
            return jsonify({'The Predicted score is': round(predicted_score, 2)})

        except ValueError as e:
            return jsonify({'error': 'Invalid input: ' + str(e)})
        except Exception as e:
            return jsonify({'error': str(e)})

    else:
        print('We are in GET Method')
        data1 = request.args
        
        try:
            Hours_Studied = float(data1.get('Hours_Studied', 0))
            Previous_Scores = float(data1.get('Previous_Scores', 0))
            Extracurricular_Activities = data1.get('Extracurricular_Activities', '')
            Sleep_Hours = float(data1.get('Sleep_Hours', 0))
            Sample_Question_Papers_Practiced = float(data1.get('Sample_Question_Papers_Practiced', 0))

            Pred_Scores = Student_performance(Hours_Studied, Previous_Scores, Extracurricular_Activities, Sleep_Hours, Sample_Question_Papers_Practiced)
            predicted_score = Pred_Scores.get_predicted_score()
            return jsonify({'The Predicted score is': round(predicted_score, 2)})

        except ValueError as e:
            return jsonify({'error': 'Invalid input: ' + str(e)})
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT_NUMBER, debug=True)
