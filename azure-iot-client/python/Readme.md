# サンプルプログラムについて

本サンプルプログラムは、IoT Hubの公式ドキュメントに記載の方法で実装しています。
詳細は参考ドキュメントに記載のURLを参照してください。

## 実行方法

### 実行環境とライブラリ
* Python 2.7.x
* paho-mqtt

### プログラムの編集
以下の文字列を、利用環境に合わせて編集してください。


* `<REPLACE YOUR IOT HUB NAME>` : 利用するIoT Hub URI
* `<REPLACE YOUR DEVICE ID>` : IoT Hub に登録したデバイスID
* `<REPLACE IOT HUB SHARED CONNECT KEY>` : IoT Hub 共有アクセスキー
* `<REPLACE YOUR DEVICE KEY>` : デバイスキー



### プログラムの実行
1. `send_mqtt.py` と `local_root_ca.cer` をダウンロードします。
2. コンソールで `python send_mqtt.py` を実行します。


## 参考ドキュメント
[1] MQTTサポート
https://docs.microsoft.com/ja-jp/azure/iot-hub/iot-hub-mqtt-support

[2] IoT Hub へのアクセス制御
https://docs.microsoft.com/ja-jp/azure/iot-hub/iot-hub-devguide-security
