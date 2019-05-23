import zipfile
import argparse

parser = argparse.ArgumentParser("file input")
parser.add_argument("--file", help="Enter file name")
args = parser.parse_args()

if not args.file:
    print("Please enter file")
else:
    file_name = args.file
    output_directory = "test_zip"
    zip_file = zipfile.ZipFile(file_name, "r")
    zip_file.extractall(output_directory)
    zip_file.close()
    print("zip file has been extracted successfully! you can find it in ", args.file[:-4])
