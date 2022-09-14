Adaptation from Pymba to control recording system through Serial Port.

## Installation

### Installing Vimba SDK

For Windows:
* [Download](https://www.alliedvision.com/en/products/software.html) and launch the Vimba SDK installer:
 
### Installing Pymba

    pip install pymba
    
### Testing installation 

    from pymba import Vimba, __version__
    print(__version__)
    print(Vimba.version())
