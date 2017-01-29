from flask import Flask, jsonify, request,render_template,json #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

#homepage
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!',
                    'GET':'http://127.0.0.1:8080/lang',
                    'POST':'http://127.0.0.1:8080/add',
                    'PUT':'http://127.0.0.1:8080/update',
                    'DELETE':'http://127.0.0.1:8080/remove'})

#show all languages available
@app.route('/lang/', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

#show particular language name
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    for language in languages:
        if language['name'] == name:
            langs = language
    return jsonify({'language': langs})


# @app.route('/setapi', methods=['GET'])
# def setData():
#     return render_template('sentapi.html')

#adding data via POST
@app.route('/add', methods=['POST'])
def addOne():
    # jsondata = request.form['jsondata']
    # data = json.loads(jsondata)
    # language = data[0]
    app.logger.debug(jsonify(request.get_json(force=True)))
    if request.json:
        mydata = request.json
        print(mydata)
        languages.append(mydata)
    return jsonify({'languages' : languages})

#updating data via PUT
@app.route('/update/<string:name>', methods=['PUT'])
def updateOne(name):
    app.logger.debug(jsonify(request.get_json(force=True)))
    for language in languages:
        if language['name'] == name:
            langs = language
    try:
        langs['name'] = request.json['name']
    except Exception as e:
        return "ERORR " + str(e)
    return jsonify({'language': langs})

#deleting data via DELETE
@app.route('/remove/<string:name>', methods=['DELETE'])

def deleteOne(name):
    app.logger.debug(jsonify(request.get_json(force=True)))
    for language in languages:
        if language['name'] == name:
            langs = language
    try:
        languages.remove(langs)
    except Exception as e:
        return "ERORR " + str(e)
    return jsonify({'language': languages})

@app.errorhandler(404)
@app.errorhandler(405)
def not_found(error):
    return jsonify({'message' : 'ERROR!',
                    'GET':{'url':'http://127.0.0.1:8080/lang'},
                    'POST':{'url':'http://127.0.0.1:8080/add','method':'PUT','postParameters':'{"name":"NEW"}'},
                    'PUT':{'url':'http://127.0.0.1:8080/update/NEW','method':'PUT','postParameters':''},
                    'DELETE':{'url':'http://127.0.0.1:8080/remove/Python','method':'DELETE','postParameters':''}})

if __name__ == '__main__':
    app.run(debug=True, port=8080) #run app on port 8080 in debug mode