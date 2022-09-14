"""
AML:
Continuous video recording using Mako U291 USB3.0
Video is saved in mp4 format.
Big part of the code is borrowed from their Examples directory and others
("https://github.com/morefigs/pymba" & https://github.com/alliedvision/VimbaPython
& https://gist.github.com/goksinan)
"""

import time
from pymba import Vimba, Frame
from typing import Optional
import cv2
import serial

value = 0


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


def display_frame(frame: Frame, delay: Optional[int] = 1) -> None:
    """
    Displays the acquired frame.
    :param frame: The frame object to display.
    :param delay: Display delay in milliseconds, use 0 for indefinite.
    """

    PIXEL_FORMATS_CONVERSIONS = {
        'BayerRG8': cv2.COLOR_BAYER_RG2RGB,
    }
    # get a copy of the frame data
    image = frame.buffer_data_numpy()
    # convert colour space if desired
    """try:
        image = cv2.cvtColor(image, PIXEL_FORMATS_CONVERSIONS[frame.pixel_format])
    except KeyError:
        pass
    """
    # write image to output file
    out.write(image)
    # display image
    cv2.imshow('Image', image)
    cv2.waitKey(delay)


with serial.Serial(port='COM4', baudrate=9600, timeout=.1) as arduino:
    while not (value == b'55'):
        num = input("Enter a number until you receive '55' (three tries for security): ")  # Taking input from user
        value = write_read(num)
        print(value)  # printing the value
        time.sleep(0.1)
    print("You have established connection")

with Vimba() as vimba:
        camera = vimba.camera(0)
        camera.open()
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'X264')
        out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640, 480))
        try:
            camera.arm('Continuous', display_frame)
            camera.start_frame_acquisition()
            x = input("Press 'Enter' to Stop Recording")

            if not x:
                print("Exiting the Program in a sec.")
                camera.stop_frame_acquisition()
                time.sleep(0.2)
                camera.disarm()
                camera.close()
                out.release()
                exit()

            time.sleep(0.1)
        finally:
            # stop frame acquisition
            # start_frame_acquisition can simply be called again if the camera is still armed
            camera.stop_frame_acquisition()
            time.sleep(0.2)
            if x:
                camera.disarm()
                camera.close()
                out.release()
