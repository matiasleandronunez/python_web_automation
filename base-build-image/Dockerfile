FROM python:3.8

RUN apt-get update && apt-get install -yq \
    xvfb \
    xsel

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# install firefox
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends firefox

# install geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz
RUN sh -c 'tar -x geckodriver -zf geckodriver-v0.29.1-linux64.tar.gz -O > /usr/bin/geckodriver'
RUN chmod +x /usr/bin/geckodriver
RUN export PATH=$PATH:/usr/bin/geckodriver/.
RUN rm geckodriver-v0.29.1-linux64.tar.gz

# set display port to avoid crash
ENV DISPLAY=:99

# xvfb - X server display
ADD xvfb-chromium /usr/bin/xvfb-chromium
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
    && chmod 777 /usr/bin/xvfb-chromium

# upgrade pip
RUN pip install --upgrade pip
