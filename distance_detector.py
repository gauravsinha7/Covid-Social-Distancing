from image_processing import social_distancing_config as config
from image_processing.detection import detect_people
from scipy.spatial import distance as dist
import numpy as np
import argparse
import imutils
import cv2
import os
