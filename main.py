from modules.utils import extract_calibration_value

with open('./files/day-1/input.txt') as calibration_document:
    calibrations = calibration_document.read().splitlines()

print(sum([extract_calibration_value(calibration) for calibration in calibrations]))