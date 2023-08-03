from flask import Flask, request, jsonify
import json
import multiprocessing as mp
import logging

from blindbee import service
from state import State
from text_color import TextColor


logging.basicConfig(
    format='[%(asctime)s : %(name)s ] %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S',
    level=logging.INFO,
)

to_service_queue = mp.Queue(maxsize=1)
to_flask_queue = mp.Queue(maxsize=1)
app = Flask(__name__)
state = State()

logging.info(
    TextColor.blue_bright(f"{state} ID: {id(state)}")
)

@app.route('/send/<qr_name>')
def receive_json(qr_name):
    logging.info(TextColor.yellow_bright(f"{qr_name}"))

    try:
        to_service_queue.put(qr_name)
        logging.info(f"{to_service_queue.qsize()}")
        _msg = to_flask_queue.get()
        logging.info(f"{to_flask_queue.qsize()}")
        logging.info( TextColor.yellow_bright(_msg) )
        return "Success"
        # if state.is_detecting:
        #     queue.put(qr_name)
        #     return "Success"
        # else:
        #     logging.info(
        #         TextColor.blue_bright(f"{state} ID: {id(state)}")
        #     )
        #     return f"It is not Correct! state[{state}, {id(state)}]"
    except Exception as e:
        return str(e)


def running_server():
    global app
    app.run(host='192.168.137.87', port=5000)


if __name__ == "__main__":  
    # instantiating
    procs = [
        mp.Process(
            target=running_server, 
            daemon=True),
        mp.Process(
            target=service.running_service, 
            args=(to_service_queue, to_flask_queue, state,), 
            daemon=True)
    ]

    for p in procs:
        p.start()

    # complete the processes
    for p in procs:
        p.join()

