import csv
import ipaddress


def format(jsonArray):
    return ""

#getDetails from the csv file load by serialnumber
def getDetailBySerialNumber(serialNumber, jsonArray):

    result = []
    for s in jsonArray:
        if s['serial'] == serialNumber:
            #strip the hostname
            s["hostname"] = s["hostname"].strip()
            result.append(s)
            break

    return result

#validates ip address
def isIPv4(ip_Address):
    try:
        ip = ipaddress.ip_address(ip_Address)
        return True
    except ValueError:
        return False

#conver csv to json 
def convertToJson(csvFilePath):

    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

        return jsonArray
