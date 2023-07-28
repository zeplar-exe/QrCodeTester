import os
import glob
import cv2
import pandas
import pathlib
import argparse

FAILED_READ_TEXT = "BLANK/FAILED"

parser = argparse.ArgumentParser()

check_type_group = parser.add_mutually_exclusive_group(required=True)
check_type_group.add_argument('-s', type=str, dest="check_single")
check_type_group.add_argument('-a', type=str, dest="check_all")

args = parser.parse_args()

def read_qr_code(file_name):
    img = cv2.imread(file_name)
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)

    if value == "": 
        return FAILED_READ_TEXT

    return value

if args.check_single != None:
    qr = read_qr_code(args.check_single)

    if qr == FAILED_READ_TEXT:
        print("Failure: QR could not be read or was blank.")
    else:
        print(f"Success: {qr}")
elif args.check_all != None:
    frame = pandas.DataFrame(columns=['File Name', 'QR Code'])

    success_count = 0
    total_count = 0

    for file_name in glob.iglob(f"{args.check_all}/**/*.png", recursive=True):
        qr = read_qr_code(file_name)
        row = {'File Name': file_name, 'QR Code': qr}
        
        frame = pandas.concat([frame, pandas.DataFrame([row])], ignore_index=True)

        if qr != FAILED_READ_TEXT:
            success_count += 1
        total_count += 1

    with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
        print(frame)

    print('------------------------------')
    print(f"{success_count / total_count * 100}% Success Rate out of {total_count} images.")
