FROM izone/pycuda

RUN apt-get update \
    && apt-get install -y git \
    && git clone \
    https://github.com/Heronalps/img-filters.git

WORKDIR /root/img-filters
COPY ./UECFOOD100/ /root/img-filters/UECFOOD100/
COPY ./func.py /root/img-filters/func.py
RUN pip install Pillow && mkdir ./UECFOOD100_filter

ENTRYPOINT [ "python3", "func.py" ]