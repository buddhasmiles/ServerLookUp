from utils import *
from flask import Flask, jsonify, request, Response


app = Flask(__name__)

jsonArray = []

csvFilePath = r'newservers.csv'
jsonArray = convertToJson(csvFilePath)

# a simple page that says hello


@app.route('/')
def hello():
    return 'api working'


# get all servers from the csv
@app.route('/servers/all')
def getAll():
    if not jsonArray:
        return Response(f'Unable to read from CSV', status=1,)

    return jsonify(jsonArray)


@app.route('/servers/<string:serialNumber>', methods=['GET'])
def getDetails(serialNumber):

    result = []

    result = getDetailBySerialNumber(serialNumber, jsonArray)

  # if not matching record is found then return error
    if not result:
        return Response(f'SerialNumber {serialNumber} doesnt exits', status=1,)

  # if ip is not valid then return error
    if not isIPv4(result[0]["ip"]):
        return Response(f'Invalid Ip Address {result[0]["ip"]} for SerialNumber {serialNumber}', status=1,)

  # if gateway is not valid then return error
    if not isIPv4(result[0]["gateway"]):
        return Response(f'Invalid gateway Address {result[0]["gateway"]} for SerialNumber {serialNumber} ', status=1,)

    return jsonify(result)


if __name__ == "__main__":
    app.run()
