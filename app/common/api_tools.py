from flask import jsonify, make_response, request


def params(*keys):
    args = []
    for key in keys:
        args.append(request.args[key])
    return args


def render_ok(data={}):
    return make_response(jsonify(data), 200)


def render_err(error_msg=""):
    return make_response(jsonify({"error_msg": error_msg}), 400)