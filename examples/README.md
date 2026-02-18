# InkyPi Display Test Examples

This directory contains test scripts for verifying your e-Paper display is working correctly.

## Test Scripts

### epd_13in3E_test.py
Test script for the **13.3" e-Paper HAT+ (E)** display.

This script tests:
- Display initialization
- Color rendering (Black, White, Yellow, Red, Blue, Green)
- Text drawing
- Shape drawing
- Display clearing

## Running the Tests

### Prerequisites

Make sure you have the required Python packages installed:

```bash
sudo apt-get install python3-pip python3-pil python3-numpy
sudo pip3 install RPi.GPIO spidev
```

### Run the 13.3" e-Paper (E) Test

```bash
cd /Users/barpiglyansky/dev/Playground/InkyPi/examples
sudo python3 epd_13in3E_test.py
```

**Note:** You need to run with `sudo` because the script requires GPIO access.

## What to Expect

When the test runs successfully:
1. The display will initialize and clear (show white)
2. You'll see colored rectangles and text demonstrating all available colors
3. A second test will show "InkyPi Display Test" and "Display is working!"
4. The display will clear again
5. The display goes to sleep mode

The entire test takes about 15-20 seconds to complete.

## Troubleshooting

### Display Not Responding
- Check that SPI is enabled: `sudo raspi-config` → Interface Options → SPI → Enable
- Verify all ribbon cable connections are secure
- Make sure you're running with `sudo`

### Import Errors
- Make sure all dependencies are installed
- Check that the `epd13in3E.py` driver exists in `src/display/waveshare_epd/`

### Display Shows Garbled Output
- Run the test again - sometimes the first initialization after a long power-off needs a second run
- Try power cycling the display

## Additional Resources

- Original Waveshare examples from `/tmp/e-Paper` (if still available)
- Waveshare Wiki: https://www.waveshare.com/wiki/13.3inch_e-Paper_HAT-E
- Test images are available in the `pic/` directory
