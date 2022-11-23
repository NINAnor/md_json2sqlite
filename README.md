# md_json2sqlite: Convert MegaDetector output to an SQLite database

This repository contains script for converting the `.json` file outputed by [MegaDetector](https://github.com/microsoft/CameraTraps) into an SQLite database.

## Run the script

Clone the repository and change directory:

```
git clone https://github.com/NINAnor/md_json2sqlite
cd md_json2sqlite
```

### Using Docker

First we build the docker image:

```
docker build -t md_json2sqlite -f Dockerfile .
```

Assuming `md_output.json` is located in the repository, we run the script:

```
docker run -v $PWD:/app md_json2sqlite \
    python src/md_json2sqlite.py \
    --result_file test_output.json
```

### Using poetry, without Docker

Install poetry and setup the virtual environment:

```
pip install poetry 
poetry install --no-root
```

Run the script:

```
poetry run python src/md_json2sqlite.py \
    --result_file test_output.json
```