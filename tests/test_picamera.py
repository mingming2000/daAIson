from blindbee import BlindBeeCamera


if __name__ == "__main__":
    #run_quickstart()
    # $ export GOOGLE_APPLICATION_CREDENTIALS="/home/dspi/storage/dauntless-graph-393517-4fc404d248f0.json"

    cam = BlindBeeCamera()
    data, box, straight_qrcode = cam.testing()

