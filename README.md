# ONVIF control with python

## Requirements:

### Python requirements
From https://github.com/FalkTannhaeuser/python-onvif-zeep install with:

```
pip install onvif_zeep
```

### ONVIF specification files requirements
Then download the WSDL data from: https://github.com/onvif/specs and put it in a folder with this nesting (double nesting required for bug in onvif_zeep):

```
ROOT
    onvif_data
        onvif_specs
            specs      (<git-repo>)
```

```
mkdir onvif_data
mkdir onvif_data/onvif_specs
git clone https://github.com/onvif/specs onvif_data/onvif_specs/specs
cd onvif_data/onvif_specs/specs
git checkout tags/21.12
```

Then copy the files:

```
cp onvif_data/onvif_specs/specs/wsdl/ver10/device/wsdl/devicemgmt.wsdl onvif_data/onvif_specs/specs/wsdl/devicemgmt.wsdl
cp -r onvif_data/onvif_specs/specs/wsdl/ver10 onvif_data/ver10
cp onvif_data/onvif_specs/specs/wsdl/ver10/media/wsdl/media.wsdl onvif_data/onvif_specs/specs/wsdl/media.wsdl
cp onvif_data/onvif_specs/specs/wsdl/ver20/ptz/wsdl/ptz.wsdl onvif_data/onvif_specs/specs/wsdl/ptz.wsdl
```


