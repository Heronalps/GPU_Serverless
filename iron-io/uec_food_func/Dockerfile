FROM izone/pycuda

RUN apt-get update \
    && apt-get install -y git \
    && git clone \
    https://github.com/Heronalps/img-filters.git

WORKDIR /root/img-filters
COPY ./UECFOOD100/ /root/img-filters/UECFOOD100/
RUN pip install Pillow && cp -r ./UECFOOD100/ ./UECFOOD100_filter/

COPY ./func.py /root/img-filters/func.py

ENTRYPOINT [ "python3", "func.py" ]