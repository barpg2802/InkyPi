#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

# Add the src directory to the path so we can import the waveshare_epd module
projectdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(projectdir, 'src', 'display'))

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')

import logging
from waveshare_epd import epd13in3E
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd13in3E Demo - 13.3inch e-Paper HAT+ (E)")
    epd = epd13in3E.EPD()

    logging.info("Init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(2)

    # Load font (use a fallback if Font.ttc is not available)
    try:
        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
        font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    except:
        logging.warning("Font.ttc not found, using default font")
        font24 = ImageFont.load_default()
        font18 = ImageFont.load_default()
        font35 = ImageFont.load_default()

    # Drawing test - 13.3" e-Paper (E) supports color
    logging.info("1. Drawing test with colors...")
    Himage = Image.new('RGB', (epd.width, epd.height), epd.WHITE)
    draw = ImageDraw.Draw(Himage)

    # Draw text in different colors
    draw.text((10, 0), 'hello world', font=font24, fill=epd.BLACK)
    draw.text((10, 30), '13.3inch e-Paper HAT+ (E)', font=font24, fill=epd.RED)
    draw.text((10, 60), 'Color Display Test', font=font24, fill=epd.BLUE)

    # Draw shapes in different colors
    draw.rectangle((20, 100, 120, 200), outline=epd.BLACK, width=2)
    draw.rectangle((140, 100, 240, 200), fill=epd.YELLOW)
    draw.rectangle((260, 100, 360, 200), fill=epd.RED)
    draw.rectangle((380, 100, 480, 200), fill=epd.BLUE)
    draw.rectangle((500, 100, 600, 200), fill=epd.GREEN)

    # Draw color labels
    draw.text((30, 210), 'BLACK', font=font18, fill=epd.BLACK)
    draw.text((150, 210), 'YELLOW', font=font18, fill=epd.BLACK)
    draw.text((270, 210), 'RED', font=font18, fill=epd.BLACK)
    draw.text((390, 210), 'BLUE', font=font18, fill=epd.BLACK)
    draw.text((510, 210), 'GREEN', font=font18, fill=epd.BLACK)

    epd.display(epd.getbuffer(Himage))
    logging.info("Display updated, waiting 5 seconds...")
    time.sleep(5)

    logging.info("2. Simple text test...")
    Himage = Image.new('RGB', (epd.width, epd.height), epd.WHITE)
    draw = ImageDraw.Draw(Himage)
    draw.text((400, 700), 'InkyPi Display Test', font=font35, fill=epd.BLACK)
    draw.text((450, 750), 'Display is working!', font=font24, fill=epd.GREEN)
    epd.display(epd.getbuffer(Himage))
    time.sleep(5)

    logging.info("3. Clearing display...")
    epd.Clear()

    logging.info("Going to sleep...")
    epd.sleep()

    logging.info("Test completed successfully!")

except IOError as e:
    logging.error(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd13in3E.epdconfig.module_exit(cleanup=True)
    exit()

except Exception as e:
    logging.error("An error occurred:")
    logging.error(traceback.format_exc())
    epd13in3E.epdconfig.module_exit(cleanup=True)
    exit()
