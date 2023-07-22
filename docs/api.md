# Text to Speech

## A gulidline for installation
Try [this](https://cloud.google.com/sdk/docs/install-sdk?hl=ko#deb)

##  Debbuging: duplicated error
  ```
  $ cd /etc/apt/sources.list.d
  ```

  ```
  $ sudo rm google-cloud-sdk.list
  ```

## Setting API key (.json)
  ```
  $ export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
  # ex) $ export GOOGLE_APPLICATION_CREDENTIALS="/Users/../Desktop/BEAM_CODE/Key.json"
  ```

  ([ref](https://ninano1109.tistory.com/186))
