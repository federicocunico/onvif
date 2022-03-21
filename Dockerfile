FROM python:3.7

RUN pip install onvif_zeep

WORKDIR /onvif

RUN mkdir onvif_data && \
    mkdir onvif_data/onvif_specs && \
    git clone https://github.com/onvif/specs onvif_data/onvif_specs/specs && \
    cd onvif_data/onvif_specs/specs && \
    git checkout tags/21.12

RUN cp onvif_data/onvif_specs/specs/wsdl/ver10/device/wsdl/devicemgmt.wsdl onvif_data/onvif_specs/specs/wsdl/devicemgmt.wsdl && \
    cp -r onvif_data/onvif_specs/specs/wsdl/ver10 onvif_data/ver10 && \
    cp onvif_data/onvif_specs/specs/wsdl/ver10/media/wsdl/media.wsdl onvif_data/onvif_specs/specs/wsdl/media.wsdl && \
    cp onvif_data/onvif_specs/specs/wsdl/ver20/ptz/wsdl/ptz.wsdl onvif_data/onvif_specs/specs/wsdl/ptz.wsdl

COPY camera_control.py /onvif/camera_control.py
