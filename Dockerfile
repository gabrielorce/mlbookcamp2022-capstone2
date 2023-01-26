FROM public.ecr.aws/lambda/python:3.9

RUN pip3 install --upgrade pip

RUN pip3 install keras_image_helper --no-cache-dir
RUN pip3 install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl?raw=true --no-cache-dir

COPY electronics-components-v2.tflite electronics-components-v2.tflite
COPY lambda_function.py lambda_function.py

CMD [ "lambda_function.lambda_handler" ]