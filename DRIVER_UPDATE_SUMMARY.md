# Waveshare epd13in3E Driver Integration - Summary

## Date: 2026-02-18

## Changes Made

### 1. Driver Update
- **File**: `src/display/waveshare_epd/epd13in3E.py`
- **Action**: Replaced with official Waveshare driver
- **Backup**: `src/display/waveshare_epd/epd13in3E.py.backup`
- **Source**: https://github.com/waveshareteam/e-Paper/tree/master/E-paper_Separate_Program/13.3inch_e-Paper_E
- **Resolution**: 1200×1600 (portrait native), displays as 1600×1200 in horizontal orientation
- **Colors**: E6 full color palette (BLACK, WHITE, YELLOW, RED, BLUE, GREEN)

### 2. Configuration Verification
- **File**: `install/config_base/device.json`
- **Status**: ✓ Already configured correctly
  - `display_type`: "epd13in3E"
  - `orientation`: "horizontal"
- **No changes needed**

### 3. Hardware Configuration
- **File**: `src/display/waveshare_epd/epdconfig.py`
- **Status**: ✓ Keeping existing (V1.2, 2022-10-29)
- **Reason**: More recent than official version, includes multi-platform support
- **Features**: RaspberryPi, JetsonNano, SunriseX3 classes with dual CS pin support

### 4. Shared Object File
- **File**: `src/display/waveshare_epd/DEV_Config_64_b.so`
- **Status**: ✓ Current (202920 bytes, matches official version)
- **No update needed**

## Driver Verification

### File Structure ✓
- Header: References epd12in48 (incorrect but doesn't affect functionality)
- Resolution Constants: EPD_WIDTH=1200, EPD_HEIGHT=1600 ✓
- Color Palette: 6 colors defined ✓
- Dual CS Pins: EPD_CS_M_PIN, EPD_CS_S_PIN ✓

### Required Methods ✓
- `Init()` - Display initialization
- `display(image)` - Display image buffer
- `getbuffer(image)` - Convert PIL image to buffer
- `Clear(color)` - Clear display
- `sleep()` - Put display to sleep

### Integration Compatibility ✓
- WaveshareDisplay wrapper: Compatible (dynamic loading)
- Display method: Compatible (calls Init, Clear, getbuffer, display)
- Resolution auto-detection: Compatible (reads width/height from driver)

## Testing Checklist

### Pre-Deployment (macOS) ✓
- [x] Downloaded official epd13in3E.py driver
- [x] Verified driver header and constants
- [x] Confirmed all required methods exist
- [x] Verified dual CS pin support in epdconfig.py
- [x] Backed up original driver file
- [x] Device config has correct display_type

### On Raspberry Pi (To be tested)
- [ ] SPI enabled (check `/dev/spidev0.0` and `/dev/spidev0.1` exist)
- [ ] Python dependencies installed: `pip3 install gpiozero lgpio RPi.GPIO spidev`
- [ ] WaveshareDisplay loads driver successfully
- [ ] Display initializes without errors
- [ ] Clear() function works
- [ ] Test image displays correctly
- [ ] All 6 E6 colors render properly
- [ ] Sleep mode functions correctly

## Deployment Instructions

1. **Transfer updated files to Raspberry Pi:**
   ```bash
   scp src/display/waveshare_epd/epd13in3E.py pi@raspberrypi:~/InkyPi/src/display/waveshare_epd/
   ```

2. **Verify SPI is enabled:**
   ```bash
   ls /dev/spi*
   # Should show: /dev/spidev0.0  /dev/spidev0.1
   ```

3. **Install dependencies (if needed):**
   ```bash
   pip3 install gpiozero lgpio RPi.GPIO spidev
   ```

4. **Test the display:**
   ```bash
   cd ~/InkyPi
   python3 -m src.main
   ```

5. **Monitor for errors:**
   ```bash
   journalctl -u inkypi.service -f
   ```

## Rollback Procedure

If issues occur:
```bash
cd ~/InkyPi/src/display/waveshare_epd
mv epd13in3E.py epd13in3E.py.new
mv epd13in3E.py.backup epd13in3E.py
sudo systemctl restart inkypi
```

## Expected Behavior

- Display initializes on startup
- Images render at 1600×1200 resolution (horizontal orientation)
- All 6 E6 colors display correctly
- Display enters sleep mode between updates
- Clear() removes residual pixels before each refresh

## References

- [InkyPi Discussion #409](https://github.com/fatihak/InkyPi/discussions/409)
- [Waveshare 13.3" E6 Driver](https://github.com/waveshareteam/e-Paper/tree/master/E-paper_Separate_Program/13.3inch_e-Paper_E)
- [InkyPi Troubleshooting](https://github.com/fatihak/InkyPi/blob/main/docs/troubleshooting.md)
