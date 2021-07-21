FROM base-build-image

# create folder to copy code
RUN mkdir /code

# project scope
WORKDIR /code

#copy testing code
COPY ./src_code .

# install requirements
RUN pip install -r requirements.txt