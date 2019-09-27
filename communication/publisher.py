"""
created on thrusday September 26 2019

@author: William Begin <william.begin2@uqac.ca>
    M. Sc. (C) Sciences cliniques et biomediacles, UQAC
    Office: H2-1180

project: V.A.A.L.E.R.I.E. <vaalerie.uqac@gmail.com>
"""

from outputdevices import display, guidance

from outputdevices.guidance import Guidance
from outputdevices.display import Display


class Publisher:

    guidance = Guidance(11, 33, 32, 50)
    display = Display()

    def general_publish(self, steering_input):
        self.guidance.control_steering(steering_input)
        self.guidance.brake_is_on(True)
        self.display.emotion_factor = 0
        # Publishing values to Bluetooth
