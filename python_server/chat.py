
def process_request(msg, model):
    if model == "GPT-3.5Turbo":
        return msg.upper()
    else:
        return msg.capitalize()