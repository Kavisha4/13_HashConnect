# from flask import Flask, request, jsonify
from compute import compute


# # app = Flask(__name__)

# # @app.route('/', methods=['GET', 'POST'])

# # def index():
# #     if request.method == 'POST':
# #         # Get the input values from the form
# #         input1 = request.form.get('input1')
# #         input2 = request.form.get('input2')
# #         input3 = request.form.get('input3')
# #         input4 = request.form.get('input4')
# #         input5 = request.form.get('input5')
        
# #         # Call the function that processes the input and returns a result
# #         result = process_input(input1, input2,input3,input4,input5)
        
# #         # Return the result as a string in the response body
# #         return str(result)


# app = Flask(__name__)


 
# @app.route('/submit-form', methods=['POST'])
# def submit_form():
#     name = request.form['name']
#     email = request.form['email']

#     # Process the data as needed...

#     return 'Data received!'

# if __name__ == '__main__':

    
#     # If the request is a GET request, return the index.html template
#    # return app.send_static_file('Home.html')



# # def process_input(input1, input2,input3,input4,input5):
# #     # Call the compute function to compute the output
# #     output = compute(str(input1), str(input2),str(input3),str(input4),str(input5))
# #     return output


# # if __name__ == '__main__':
# #     app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['hashtag']
    caption = request.form['message']
    # profession = request.form['profession']

    hash1 = request.form['hash1']
    hash2 = request.form['hash2']
    hash3 = request.form['hash3']
    hash4 = request.form['hash4']
    hash5 = request.form['hash5']

    return str(compute(hash1,hash2,hash3,hash4,hash5))

    # process the form data here
    # return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)