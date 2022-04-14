from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.uix.camera import camera
from kivy.lang import Builder
from kivy.core.window import Windows
import numpy as np
import cv2
import jnius as autoclass
from android.permissions import request_permissions, Permissions

Camerax = autoclass('android.hardware.Camera')
CameraInfo=autoclass('android.hardware.Camera$CameraInfo')

Builder.load_file("camera.kv")
class AndroidCamera(Camera):
    face_cascade =