# CSV to DC/XML

This tool converts a CSV to a Dublin Core XML file. It is created to help the archivists of a.o. Oudenburg to create XML according to [this metadata scheme](https://github.com/PACKED-vzw/demo-oudenburg/wiki/Beschrijven-van-stuk-en-collectie).

## Requirements

* Python 3
* CSV according to [this schemes](https://github.com/PACKED-vzw/demo-oudenburg/wiki/Beschrijven-van-stuk-en-collectie)

## Usage

```bash
python3 convert-csv.py $filename.csv
```

Change `$filename` into the path of your csv file, e.g. for converting the CSV file `my.csv`, use following command: `python3 convert-csv.py my.csv`

You can also specify the output folder for your XML-files by using the `-d` or `--dest` option

```bash
python3 convert-csv.py -d $destination $filename.csv
```

The `$destination` argument is optional, e.g. for storing the XML-files in the Desktop folder, use: `python3 -d /Users/nastasia/Desktop my.csv`
