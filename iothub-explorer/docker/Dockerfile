# Created On: 2018-06-22
# iot-explorer runtim
FROM microsoft/azure-cli:2.0.24

RUN apk add --update nodejs
RUN npm install -g iothub-explorer
RUN az extension add --name azure-cli-iot-ext
