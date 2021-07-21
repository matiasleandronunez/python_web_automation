FROM selenium/node-firefox-debug:3.141.59-20210105

LABEL authors=SeleniumHQ

USER root

#=========

# Firefox

#=========

ARG FIREFOX_VERSION=77.0b9

RUN apt-get update -qqy \

  && apt-get -qqy --no-install-recommends install firefox \

  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \

  && wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-US/firefox-$FIREFOX_VERSION.tar.bz2 \

  && apt-get -y purge firefox \

  && rm -rf /opt/firefox \

  && tar -C /opt -xjf /tmp/firefox.tar.bz2 \

  && rm /tmp/firefox.tar.bz2 \

  && mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \

  && ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox



USER 1200