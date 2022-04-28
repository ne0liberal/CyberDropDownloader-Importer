# CyberDropDownloader Importer

## importer_auto.py

imports everything i download with cyberdrop into my collections

really only works with the TB rips, but i guess other folders *could* work.

assumes your collections folders will have at least a shared string with the TB thread title

requires fuzzywuzzy to string match.

USE AT YOUR OWN RISK. NOTHING BROKE OR MOVED INCORRECTLY ON MY RUNS, BUT DON'T YELL AT ME IF SOMETHING GOES WRONG. IT SHOULD ASK YOU TO CONFIRM THE PATHS PRIOR TO ACTUALLY MOVING.

feel free to audit/improve the code


edit line #60 and #62 with your proper full paths

    cyberdrop_root = "path/to/CyberDropDownloader/Downloads/"
    collections_root = "path/to/collections/"
