import json
import pprint
import csv
import os

def main():
    yes = file_paths("/mnt/c/Users/Mike/Desktop/Parse/json_matches")
    jsonThing(yes)

def file_paths(dira):
    """
    gets all the json matches in the dira directory
    """
    print(dira)
    paths = []
    for root, _, file in os.walk(dira):
       for f in file:
        fullpath = os.path.join(root, f)
        paths.append(fullpath)

    return paths

def jsonThing(file):
    """
    extracts all of the relavent round information that I think is needed
    for at least something simple
    """
    rows_csv = []
    for i in file:
        print(i)
        with open(i, "r") as f:
            data = json.load(f)

            try:
                rounds = data.get("Rounds", [])

                for i in rounds:
                    ct_equip_val = i.get("CTEquipmentValue", 0)
                    t_equip_val = i.get("TEquipmentValue", 0)
                    type_buy_ct = i.get("TypeofBuyCT", "Unknown")
                    type_but_t = i.get("TypeofBuyT", "Unknown")
                    score_ct = i.get("ScoreCT", 0)
                    score_t = i.get("ScoreT", 0)
                    bomb_plant = i.get("BombPlanted", False)
                    round_end_reason = i.get("RoundEndedReason", "Unknown")

                    round_row = [round_end_reason, ct_equip_val, t_equip_val, type_buy_ct, type_but_t,score_ct, score_t, bomb_plant]

                    rows_csv.append(round_row)
            except Exception as e:
                pass
        print(len(rows_csv))

    write_csv(rows_csv)

def write_csv(rows):
    columns = ["round_end_reason", "ct_equip_val", "t_equip_val", "type_buy_ct", "type_buy_t", "score_ct", "score_t", "bomb_plant"]
    with open("rounds.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)
if __name__ == "__main__":
    main()