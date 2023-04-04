import json
from flask import jsonify

# the first year group for Ashesi University
FIRST_YEAR_GROUP = 2002

VOTERS_FILE = "./data/voters.txt"
ELECTIONS_FILE = "./data/elections.txt"


def valid_request_body(request):
    """ensures that the request body is valid (not empty)

    Args:
        request (tuple): the request being sent to the API

    Returns:
        JSON: a boolean of whether or not the request is valid
    """
    
    if not request.data:
        return False    
    return True


def read_from_file(filepath):
    """reads data from a file and return it

    Args:
        filepath (str): the file path

    Returns:
        str: a string representation of the data in the file
    """
    
    read_file = open(filepath, "r")
    data = read_file.read()
        
    return data


def write_to_file(filepath, data):
    """writes provided json data to specified file path

    Args:
        filepath (str): the file path
        data (json): a list of dict
    """
    
    write_file = open(filepath, "w")
    write_file.write(json.dumps(data, indent=4))
    write_file.close()
    
    
def valid_keys(voter_info, expected_keys):
    """validates a voter's information and returns result

    Args:
        voter_info (dict): JSON representation of a voter's information

    Returns:
        dict: a dictionary of boolean and or list of messages from validation
    """
    
    result = {"is_valid": False}            # result from validation
    result_message = []                     # message from validation
    num_correct_keys = 0                    # variable to keep track of the number of matching keys
    data_keys = voter_info.keys()
    
    for key in expected_keys:
        if key in data_keys:
            num_correct_keys += 1
        else:
            result_message.append(f"{key.capitalize()} is required")
    
    if num_correct_keys == len(expected_keys):
        result["is_valid"] = True
    else:
        result["message"] = result_message
    
    return result


def key_is_unique(key_list, dictionary_list, voter_info):
    """ensures that all values corresponding to unique keys in the provided 
    voter information is unique (does not already exist in voters file)

    Args:
        key_list (list): list of unique keys
        dictionary_list (list of dict): a list of voter information (dict)
        voter_info (dict): a dictionary containing voter information

    Returns:
        result: a dictionary containing the result from unique test
    """
    
    result = dict()
    for key in key_list:
        key_values = [record[key] for record in dictionary_list]
        
        if voter_info[key] in key_values:
            result[key] = key + " already exists!"
    
    return result


def valid_student_id(student_id):
    """ensures that a given student_id is valid
    - a student ID is valid if it's eight characters long and numeric

    Args:
        student_id (str): a student's ID

    Returns:
        dict: a dictionary containing user_id (the first four values of a student id)
        and year_group (the year group of the student)
    """
    
    # ensure that the student id is of length 8
    if(len(student_id)) != 8:
        return False
    
    # ensure that the student id is numeric
    if not student_id.isnumeric():
        return False
    
    user_id = student_id[:4]
    year_group = student_id[4:]
    
    return {"user_id": user_id, "year_group": year_group} 


def valid_voter_info(request, unique_keys):
    """ensures that a voter request data is valid
    i.e. contains all necessary keys, contains unique values for
    unique keys, student_id, firstname, lastname and email are syntactically valid

    Args:
        request (tuple): request from client
        unique_keys (list): a list of keys that should be unique

    Returns:
        dict: dictionary containing the status of the validation 
        and a JSON representation of the voter's info from the request or
        appropriate message if an exception occurred
    """
    
    # ensure that the voter_info is not empty
    if not valid_request_body(request):
        return jsonify({"message": "Voter information missing!"}), 400
    
    # get request data
    voter_info = json.loads(request.data)
    
    # ensure that the data contains all expected fields
    # if validation fails, return appropriate message
    # expected keys
    VOTERS_KEYS = [
            "student_id", "firstname", "lastname", "email"
        ]
    
    validate_data = valid_keys(voter_info, VOTERS_KEYS)
    if validate_data["is_valid"] == False:
        return jsonify(validate_data["message"]), 400
    
    # ensure that the student_id is synctactically correct since
    # the system assumes a certain format for later computation
    student_id_is_valid = valid_student_id(voter_info["student_id"])
    if not student_id_is_valid:
        return jsonify({"message": "Student ID is not valid."}), 400
    elif int(student_id_is_valid["year_group"]) < FIRST_YEAR_GROUP:
        return jsonify({"message": "Student year group is invalid."})
    
    # ensure that the email is a valid ashesi email
    if not voter_info["email"].endswith("@ashesi.edu.gh"):
        return jsonify({"message": "Email must be a valid Ashesi email address."}), 400
    
    # ensure that firstname and lastname is valid (is a string)
    if not str(voter_info["firstname"]).isalpha() or not str(voter_info["lastname"]).isalpha():
        return jsonify({"message": "Firstname or Lastname must be a string."}), 400
    
    # reading existing data into a list
    data = read_from_file(VOTERS_FILE)
    
    # if no voter has been registered, skip unique test
    if not data:
        return {"data": voter_info}
    
    # ensure keys are unique
    # if unique contraints fails, return appropriate response
    data_list = json.loads(data)
    ununique_result = key_is_unique(unique_keys, data_list, voter_info)
    if len(ununique_result) > 0:
        return jsonify(ununique_result), 400
    
    return {"data": voter_info}


def get_voters(id_list):
    
    result_list = list()
    return_data = dict()
    # read voters database
    data = read_from_file(VOTERS_FILE)
    
    if not data:
        return {"message": "No voter has been registered!"}
    
    voters_data = json.loads(data)
    for voter in voters_data:
        if voter["student_id"] in id_list and bool(voter["is_registered"]) == True:
            result_list.append(voter)
            if len(result_list) == len(id_list):
                return return_data

    return False
