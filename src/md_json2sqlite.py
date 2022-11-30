import argparse
import json
import sqlite_utils
import tqdm

def main(json_file, output_sqlite, recreate):

    db = sqlite_utils.Database(output_sqlite, recreate=recreate)

    with open(json_file) as f:
        j = json.load(f)

    for entry in tqdm.tqdm(j['images']):
    
        file = entry['file']
    
        if 'failure' in entry:
            print(f"Skipping {entry}, failure: '{entry['failure']}'")
            continue
    
        detections = entry['detections']

        if len(detections) > 0:
            is_empty = False
        else:
            is_empty = True

        if is_empty:
            db['mdout'].insert_all([{
                "file": file,
                "category": 0,
                "conf": 0,
                "x_min": 0,
                "y_min": 0,
                "x_max": 0,
                "y_max": 0,
                "is_empty": is_empty
            }])

        else:
            for detection in detections:
                
                category = detection['category']
                conf = detection['conf']
                bbox = detection['bbox']

                db['mdout'].insert_all([{
                    "file": file,
                    "category": category,
                    "conf": conf,
                    "x_min": bbox[0],
                    "y_min": bbox[1],
                    "x_max": bbox[2],
                    "y_max": bbox[3],
                    "is_empty": is_empty
                }])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Convert MegaDetector json results into a SQLite database",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--result_file",
        help="MegaDetector output json file",
    )
    parser.add_argument(
        "--database_path",
        help="Path of the database to create or update",
        default="mddb.sqlite",
    )
    parser.add_argument(
        "--recreate",
        help="Recreate the database",
        type=bool,
        default=False
    )
    args = parser.parse_args()

    main(args.result_file, args.database_path, args.recreate)
