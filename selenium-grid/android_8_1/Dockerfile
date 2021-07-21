FROM budtmo/docker-android-x86-8.1

USER root

RUN wget -qP /tmp/ "https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip"

RUN unzip -o /tmp/chromedriver_linux64.zip -d /root/

RUN rm /tmp/chromedriver*

RUN adb reconnect