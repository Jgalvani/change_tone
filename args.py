import argparse

# Command line options
parser = argparse.ArgumentParser(prog='change_tone', description='Create multiple tones for the same sound file')
parser.add_argument('-i', '--input', type=str, help='sound file')
parser.add_argument('-d', '--directory', type=str, help='sound file directory')
parser.add_argument('-o', '--output', type=str, required=True, help='destination folder')
parser.add_argument('-s', '--shift', type=int, required=False, default=5, help='maximum tone to perform the pitch shifting')
parser.add_argument('-m', '--minimum', type=int, required=False, default=2, help='minimum tone to perform the pitch shifting')
parser.add_argument('-g', '--gender', type=str, required=False, help='Gender of the new voice', choices=['male', 'female'])
parser.add_argument('-u', '--unique',  action='store_true', required=False, help='Only shift maximal and/or minimal tone')
parser.add_argument('-f', '--force',  action='store_true', required=False, help='Ignore range limitation')
args = parser.parse_args()